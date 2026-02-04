"""
Script para gerar hash de senha seguro
Execute: python scripts/generate_password_hash.py
"""

import sys
import os
from pathlib import Path

# Adicionar pasta raiz ao path
sys.path.insert(0, str(Path(__file__).parent.parent))

from assets.security import SecurityManager
import base64


def main():
    print("=" * 60)
    print("🔒 GERADOR DE HASH DE SENHA SEGURO")
    print("=" * 60)
    print()
    
    # Solicitar senha
    password = input("Digite a senha que deseja usar: ")
    
    if len(password) < 8:
        print("❌ ERRO: A senha deve ter pelo menos 8 caracteres!")
        return
    
    # Verificar força da senha
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in "!@#$%^&*()_+-=[]{}|;:,.<>?" for c in password)
    
    strength = sum([has_upper, has_lower, has_digit, has_special])
    
    print()
    print("📊 Força da senha:")
    if strength < 2:
        print("   🔴 FRACA - Adicione letras maiúsculas, números e símbolos")
    elif strength < 3:
        print("   🟡 MÉDIA - Recomendado adicionar mais variedade")
    elif strength < 4:
        print("   🟢 BOA - Senha aceitável")
    else:
        print("   ✅ FORTE - Excelente!")
    
    print()
    confirmar = input("Continuar com esta senha? (s/n): ")
    
    if confirmar.lower() != 's':
        print("Operação cancelada.")
        return
    
    # Gerar hash
    print()
    print("⏳ Gerando hash seguro...")
    hash_value, salt = SecurityManager.hash_password(password)
    
    # Converter para base64 para armazenamento
    hash_b64 = base64.b64encode(hash_value).decode('utf-8')
    salt_b64 = base64.b64encode(salt).decode('utf-8')
    
    print()
    print("=" * 60)
    print("✅ HASH GERADO COM SUCESSO!")
    print("=" * 60)
    print()
    print("Adicione as seguintes linhas no arquivo .env:")
    print()
    print(f"ADMIN_PASSWORD_HASH={hash_b64}")
    print(f"ADMIN_PASSWORD_SALT={salt_b64}")
    print()
    print("=" * 60)
    print()
    print("⚠️  IMPORTANTE:")
    print("   1. Copie os valores acima para o arquivo .env")
    print("   2. Nunca compartilhe estes valores")
    print("   3. Não commite o arquivo .env no Git")
    print("   4. Adicione .env ao .gitignore")
    print()
    
    # Testar hash
    print("🧪 Testando hash...")
    if SecurityManager.verify_password(password, hash_value, salt):
        print("✅ Verificação bem-sucedida!")
    else:
        print("❌ Erro na verificação!")


if __name__ == "__main__":
    main()
