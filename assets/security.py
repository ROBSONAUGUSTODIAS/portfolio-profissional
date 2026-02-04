"""
Módulo de segurança aprimorado para o portfólio
Implementa validações, hashing de senhas e proteções
"""

import hashlib
import secrets
import re
import os
from pathlib import Path
from typing import Tuple, Optional
import time


class SecurityManager:
    """Gerencia aspectos de segurança da aplicação"""
    
    # Configurações de sessão
    SESSION_TIMEOUT = 1800  # 30 minutos em segundos
    MAX_LOGIN_ATTEMPTS = 5
    LOGIN_COOLDOWN = 300  # 5 minutos
    
    # Configurações de upload
    MAX_FILE_SIZE = 5 * 1024 * 1024  # 5MB
    ALLOWED_IMAGE_TYPES = ['image/png', 'image/jpeg', 'image/jpg', 'image/gif']
    ALLOWED_DOC_TYPES = ['application/pdf']
    
    @staticmethod
    def hash_password(password: str, salt: bytes = None) -> Tuple[bytes, bytes]:
        """
        Cria hash seguro da senha usando PBKDF2
        
        Args:
            password: Senha em texto plano
            salt: Salt opcional (gerado se não fornecido)
        
        Returns:
            Tupla (hash, salt)
        """
        if salt is None:
            salt = secrets.token_bytes(32)
        
        # PBKDF2 com 100.000 iterações
        key = hashlib.pbkdf2_hmac(
            'sha256',
            password.encode('utf-8'),
            salt,
            100000
        )
        return key, salt
    
    @staticmethod
    def verify_password(password: str, stored_hash: bytes, salt: bytes) -> bool:
        """
        Verifica se a senha corresponde ao hash armazenado
        
        Args:
            password: Senha em texto plano
            stored_hash: Hash armazenado
            salt: Salt usado no hash
        
        Returns:
            True se a senha estiver correta
        """
        key, _ = SecurityManager.hash_password(password, salt)
        return secrets.compare_digest(key, stored_hash)
    
    @staticmethod
    def validate_email(email: str) -> bool:
        """
        Valida formato de email
        
        Args:
            email: Email para validar
        
        Returns:
            True se o email for válido
        """
        if not email or len(email) > 320:
            return False
        
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(pattern, email) is not None
    
    @staticmethod
    def sanitize_input(text: str, max_length: int = 1000) -> str:
        """
        Sanitiza input removendo conteúdo potencialmente perigoso
        
        Args:
            text: Texto para sanitizar
            max_length: Tamanho máximo permitido
        
        Returns:
            Texto sanitizado
        """
        if not text:
            return ""
        
        # Remover tags HTML/Script
        text = re.sub(r'<[^>]+>', '', text)
        
        # Remover caracteres de controle
        text = ''.join(char for char in text if ord(char) >= 32 or char in '\n\r\t')
        
        # Limitar tamanho
        return text[:max_length].strip()
    
    @staticmethod
    def validate_file_size(file_size: int) -> Tuple[bool, str]:
        """
        Valida tamanho do arquivo
        
        Args:
            file_size: Tamanho do arquivo em bytes
        
        Returns:
            Tupla (válido, mensagem)
        """
        if file_size > SecurityManager.MAX_FILE_SIZE:
            max_mb = SecurityManager.MAX_FILE_SIZE / (1024 * 1024)
            return False, f"Arquivo muito grande. Máximo: {max_mb}MB"
        
        if file_size == 0:
            return False, "Arquivo vazio"
        
        return True, "OK"
    
    @staticmethod
    def validate_file_extension(filename: str, allowed_extensions: list) -> Tuple[bool, str]:
        """
        Valida extensão do arquivo
        
        Args:
            filename: Nome do arquivo
            allowed_extensions: Lista de extensões permitidas
        
        Returns:
            Tupla (válido, mensagem)
        """
        ext = Path(filename).suffix.lower()
        
        if not ext:
            return False, "Arquivo sem extensão"
        
        if ext[1:] not in allowed_extensions:
            return False, f"Extensão {ext} não permitida. Permitidas: {', '.join(allowed_extensions)}"
        
        return True, "OK"
    
    @staticmethod
    def generate_safe_filename(original_filename: str) -> str:
        """
        Gera nome de arquivo seguro
        
        Args:
            original_filename: Nome original do arquivo
        
        Returns:
            Nome de arquivo seguro
        """
        # Obter extensão
        ext = Path(original_filename).suffix.lower()
        
        # Gerar nome único
        unique_id = secrets.token_hex(16)
        
        return f"{unique_id}{ext}"
    
    @staticmethod
    def check_session_timeout(last_activity: float) -> bool:
        """
        Verifica se a sessão expirou
        
        Args:
            last_activity: Timestamp da última atividade
        
        Returns:
            True se a sessão expirou
        """
        current_time = time.time()
        return (current_time - last_activity) > SecurityManager.SESSION_TIMEOUT
    
    @staticmethod
    def validate_phone(phone: str) -> bool:
        """
        Valida formato de telefone brasileiro
        
        Args:
            phone: Telefone para validar
        
        Returns:
            True se o telefone for válido
        """
        if not phone:
            return True  # Telefone é opcional
        
        # Remove caracteres não numéricos
        phone_digits = re.sub(r'\D', '', phone)
        
        # Valida tamanho (10 ou 11 dígitos)
        return len(phone_digits) in [10, 11]
    
    @staticmethod
    def validate_url(url: str) -> bool:
        """
        Valida formato de URL
        
        Args:
            url: URL para validar
        
        Returns:
            True se a URL for válida
        """
        if not url:
            return True  # URL é opcional
        
        pattern = r'^https?://[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}(/.*)?$'
        return re.match(pattern, url) is not None
    
    @staticmethod
    def create_secure_session_token() -> str:
        """
        Cria token seguro para sessão
        
        Returns:
            Token hexadecimal de 32 bytes
        """
        return secrets.token_urlsafe(32)


class RateLimiter:
    """Implementa rate limiting para prevenir brute force"""
    
    def __init__(self):
        self.attempts = {}
        self.blocked_until = {}
    
    def check_rate_limit(self, identifier: str) -> Tuple[bool, Optional[str]]:
        """
        Verifica se o identificador excedeu o limite de tentativas
        
        Args:
            identifier: Identificador único (ex: username, IP)
        
        Returns:
            Tupla (permitido, mensagem_erro)
        """
        current_time = time.time()
        
        # Verificar se está bloqueado
        if identifier in self.blocked_until:
            if current_time < self.blocked_until[identifier]:
                remaining = int(self.blocked_until[identifier] - current_time)
                return False, f"Muitas tentativas. Tente novamente em {remaining}s"
            else:
                # Desbloquear
                del self.blocked_until[identifier]
                if identifier in self.attempts:
                    del self.attempts[identifier]
        
        return True, None
    
    def record_attempt(self, identifier: str, success: bool):
        """
        Registra uma tentativa de login
        
        Args:
            identifier: Identificador único
            success: Se a tentativa foi bem-sucedida
        """
        current_time = time.time()
        
        if success:
            # Limpar tentativas em caso de sucesso
            if identifier in self.attempts:
                del self.attempts[identifier]
            return
        
        # Registrar tentativa falha
        if identifier not in self.attempts:
            self.attempts[identifier] = []
        
        self.attempts[identifier].append(current_time)
        
        # Remover tentativas antigas (mais de 5 minutos)
        self.attempts[identifier] = [
            t for t in self.attempts[identifier] 
            if current_time - t < SecurityManager.LOGIN_COOLDOWN
        ]
        
        # Verificar se excedeu o limite
        if len(self.attempts[identifier]) >= SecurityManager.MAX_LOGIN_ATTEMPTS:
            self.blocked_until[identifier] = current_time + SecurityManager.LOGIN_COOLDOWN


# Singleton do rate limiter
_rate_limiter = RateLimiter()

def get_rate_limiter() -> RateLimiter:
    """Retorna instância do rate limiter"""
    return _rate_limiter
