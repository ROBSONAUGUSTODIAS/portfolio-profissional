"""
Script de teste de segurança - Valida todas as implementações
"""

import sys
from pathlib import Path

# Adicionar raiz ao path
sys.path.insert(0, str(Path(__file__).parent.parent))

def test_password_hash():
    """Testa hash de senha"""
    print("\n📋 Teste 1: Hash de Senha")
    print("-" * 60)
    
    from assets.security import SecurityManager
    
    password = "EngenheiroDev0ps@#"
    hash_value, salt = SecurityManager.hash_password(password)
    
    print(f"✅ Hash gerado: {len(hash_value)} bytes")
    print(f"✅ Salt gerado: {len(salt)} bytes")
    
    # Verificar
    if SecurityManager.verify_password(password, hash_value, salt):
        print("✅ Verificação de senha: OK")
    else:
        print("❌ Verificação de senha: FALHOU")
        return False
    
    # Testar senha errada
    if not SecurityManager.verify_password("senha_errada", hash_value, salt):
        print("✅ Rejeição de senha incorreta: OK")
    else:
        print("❌ Rejeição de senha incorreta: FALHOU")
        return False
    
    return True

def test_rate_limiter():
    """Testa rate limiter"""
    print("\n📋 Teste 2: Rate Limiting")
    print("-" * 60)
    
    from assets.security import RateLimiter
    
    limiter = RateLimiter()
    user = "test_user"
    
    # Testar 5 tentativas
    for i in range(5):
        limiter.record_attempt(user, False)
        print(f"   Tentativa {i+1} registrada")
    
    # 6ª tentativa deve ser bloqueada
    allowed, msg = limiter.check_rate_limit(user)
    if not allowed:
        print(f"✅ Bloqueio após 5 tentativas: OK")
        print(f"   Mensagem: {msg}")
    else:
        print("❌ Rate limiting: FALHOU")
        return False
    
    return True

def test_validations():
    """Testa validações"""
    print("\n📋 Teste 3: Validações")
    print("-" * 60)
    
    from assets.security import SecurityManager
    
    # Email
    valid_emails = ["test@test.com", "user@example.com.br"]
    invalid_emails = ["invalid", "@test.com", "test@"]
    
    for email in valid_emails:
        if SecurityManager.validate_email(email):
            print(f"✅ Email válido aceito: {email}")
        else:
            print(f"❌ Email válido rejeitado: {email}")
            return False
    
    for email in invalid_emails:
        if not SecurityManager.validate_email(email):
            print(f"✅ Email inválido rejeitado: {email}")
        else:
            print(f"❌ Email inválido aceito: {email}")
            return False
    
    # Sanitização
    dangerous = "<script>alert('xss')</script>Hello"
    safe = SecurityManager.sanitize_input(dangerous)
    if "<script>" not in safe and "Hello" in safe:
        print(f"✅ Sanitização remove scripts: OK")
    else:
        print(f"❌ Sanitização: FALHOU")
        return False
    
    # URL
    if SecurityManager.validate_url("https://exemplo.com"):
        print("✅ URL válida aceita: OK")
    else:
        print("❌ Validação de URL: FALHOU")
        return False
    
    # Telefone
    if SecurityManager.validate_phone("(11) 99999-9999"):
        print("✅ Telefone válido aceito: OK")
    else:
        print("❌ Validação de telefone: FALHOU")
        return False
    
    return True

def test_file_validation():
    """Testa validação de arquivos"""
    print("\n📋 Teste 4: Validação de Arquivos")
    print("-" * 60)
    
    from assets.security import SecurityManager
    
    # Tamanho
    valid_size, msg = SecurityManager.validate_file_size(1024 * 1024)  # 1MB
    if valid_size:
        print("✅ Arquivo 1MB aceito: OK")
    else:
        print(f"❌ Validação de tamanho: FALHOU - {msg}")
        return False
    
    valid_size, msg = SecurityManager.validate_file_size(10 * 1024 * 1024)  # 10MB
    if not valid_size:
        print("✅ Arquivo 10MB rejeitado: OK")
    else:
        print("❌ Validação de tamanho: FALHOU")
        return False
    
    # Extensão
    valid_ext, msg = SecurityManager.validate_file_extension("test.pdf", ['pdf', 'png'])
    if valid_ext:
        print("✅ Extensão PDF aceita: OK")
    else:
        print(f"❌ Validação de extensão: FALHOU - {msg}")
        return False
    
    valid_ext, msg = SecurityManager.validate_file_extension("test.exe", ['pdf', 'png'])
    if not valid_ext:
        print("✅ Extensão EXE rejeitada: OK")
    else:
        print("❌ Validação de extensão: FALHOU")
        return False
    
    # Nome seguro
    safe_name = SecurityManager.generate_safe_filename("../../etc/passwd.txt")
    if ".." not in safe_name and safe_name.endswith(".txt"):
        print("✅ Nome seguro gerado: OK")
        print(f"   Nome: {safe_name}")
    else:
        print("❌ Geração de nome seguro: FALHOU")
        return False
    
    return True

def test_auth_config():
    """Testa configuração de autenticação"""
    print("\n📋 Teste 5: Autenticação")
    print("-" * 60)
    
    try:
        from assets.auth_config import verify_credentials
        
        # Testar credenciais corretas
        if verify_credentials("admin", "EngenheiroDev0ps@#"):
            print("✅ Login com credenciais corretas: OK")
        else:
            print("❌ Login com credenciais corretas: FALHOU")
            return False
        
        # Testar credenciais incorretas
        if not verify_credentials("admin", "senha_errada"):
            print("✅ Rejeição de senha incorreta: OK")
        else:
            print("❌ Rejeição de senha incorreta: FALHOU")
            return False
        
        if not verify_credentials("usuario_errado", "EngenheiroDev0ps@#"):
            print("✅ Rejeição de usuário incorreto: OK")
        else:
            print("❌ Rejeição de usuário incorreto: FALHOU")
            return False
        
        return True
    except Exception as e:
        print(f"❌ Erro ao testar autenticação: {e}")
        return False

def test_env_config():
    """Testa configuração de variáveis de ambiente"""
    print("\n📋 Teste 6: Variáveis de Ambiente")
    print("-" * 60)
    
    import os
    from dotenv import load_dotenv
    
    load_dotenv()
    
    required_vars = [
        'ADMIN_USERNAME',
        'ADMIN_PASSWORD_HASH',
        'ADMIN_PASSWORD_SALT'
    ]
    
    all_present = True
    for var in required_vars:
        value = os.getenv(var)
        if value:
            print(f"✅ {var}: Configurado")
        else:
            print(f"❌ {var}: NÃO configurado")
            all_present = False
    
    return all_present

def main():
    """Executa todos os testes"""
    print("=" * 60)
    print("🔒 TESTE DE SEGURANÇA - PORTFÓLIO PROFISSIONAL")
    print("=" * 60)
    
    tests = [
        ("Hash de Senha", test_password_hash),
        ("Rate Limiting", test_rate_limiter),
        ("Validações", test_validations),
        ("Validação de Arquivos", test_file_validation),
        ("Autenticação", test_auth_config),
        ("Variáveis de Ambiente", test_env_config),
    ]
    
    results = []
    
    for name, test_func in tests:
        try:
            result = test_func()
            results.append((name, result))
        except Exception as e:
            print(f"\n❌ Erro ao executar teste '{name}': {e}")
            results.append((name, False))
    
    # Sumário
    print("\n" + "=" * 60)
    print("📊 SUMÁRIO DOS TESTES")
    print("=" * 60)
    
    passed = sum(1 for _, result in results if result)
    total = len(results)
    
    for name, result in results:
        status = "✅ PASSOU" if result else "❌ FALHOU"
        print(f"{status} - {name}")
    
    print("=" * 60)
    print(f"\n🎯 Resultado: {passed}/{total} testes passaram")
    
    if passed == total:
        print("✅ TODOS OS TESTES PASSARAM!")
        print("🔒 Segurança implementada com sucesso!")
        return 0
    else:
        print("⚠️ ALGUNS TESTES FALHARAM")
        print("Revise as implementações acima")
        return 1

if __name__ == "__main__":
    exit(main())
