"""
Configurações de autenticação para o painel administrativo
Suporta .env (local) e Streamlit Secrets (cloud)
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

# Tentar importar streamlit (pode não estar disponível em todos os contextos)
try:
    import streamlit as st
    HAS_STREAMLIT = True
except ImportError:
    HAS_STREAMLIT = False

def get_config(key: str, default=None):
    """
    Obtém configuração de múltiplas fontes (prioridade):
    1. Streamlit Secrets (para Streamlit Cloud)
    2. Variáveis de ambiente .env (para desenvolvimento local)
    3. Valor padrão
    """
    # Tentar Streamlit Secrets primeiro (produção)
    if HAS_STREAMLIT:
        try:
            if key in st.secrets:
                return st.secrets[key]
        except:
            pass
    
    # Fallback para .env (desenvolvimento local)
    return os.getenv(key, default)

# Credenciais - suporta .env e st.secrets
ADMIN_USERNAME = get_config('ADMIN_USERNAME', 'admin')
ADMIN_PASSWORD_HASH = get_config('ADMIN_PASSWORD_HASH')
ADMIN_PASSWORD_SALT = get_config('ADMIN_PASSWORD_SALT')

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
        print("⚠️ ERRO: Credenciais não configuradas!")
        if HAS_STREAMLIT:
            print("Configure em: Streamlit Cloud > Settings > Secrets")
            print("Use o template em: .streamlit/secrets.toml.example")
        else:
            print("Execute: python scripts/generate_password_hash.py")
            print("E configure o arquivo .env")
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
