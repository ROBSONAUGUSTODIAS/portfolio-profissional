"""
Configurações de autenticação para o painel administrativo
Agora com hash de senha seguro
"""

import os
import base64
from dotenv import load_dotenv
from pathlib import Path

# Carregar variáveis de ambiente
load_dotenv()

# Importar SecurityManager
import sys
sys.path.insert(0, str(Path(__file__).parent.parent))
from assets.security import SecurityManager

# Credenciais do .env
ADMIN_USERNAME = os.getenv('ADMIN_USERNAME', 'admin')
ADMIN_PASSWORD_HASH = os.getenv('ADMIN_PASSWORD_HASH')
ADMIN_PASSWORD_SALT = os.getenv('ADMIN_PASSWORD_SALT')

def verify_credentials(username: str, password: str) -> bool:
    """
    Verifica se as credenciais estão corretas usando hash seguro
    
    Args:
        username: Nome de usuário
        password: Senha em texto plano
    
    Returns:
        True se as credenciais forem válidas, False caso contrário
    """
    # Verificar username
    if username != ADMIN_USERNAME:
        return False
    
    # Verificar se hash está configurado
    if not ADMIN_PASSWORD_HASH or not ADMIN_PASSWORD_SALT:
        print("⚠️ ERRO: Variáveis de ambiente não configuradas!")
        print("Execute: python scripts/generate_password_hash.py")
        print("E configure o arquivo .env com ADMIN_PASSWORD_HASH e ADMIN_PASSWORD_SALT")
        return False
    
    try:
        # Decodificar hash e salt do base64
        stored_hash = base64.b64decode(ADMIN_PASSWORD_HASH)
        salt = base64.b64decode(ADMIN_PASSWORD_SALT)
        
        # Verificar senha com hash
        return SecurityManager.verify_password(password, stored_hash, salt)
    except Exception as e:
        # Em caso de erro, logar e retornar False
        print(f"❌ Erro ao verificar credenciais: {e}")
        print("Verifique se as variáveis ADMIN_PASSWORD_HASH e ADMIN_PASSWORD_SALT estão corretas no .env")
        return False
