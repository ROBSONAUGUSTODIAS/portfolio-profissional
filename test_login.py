"""
Script para testar login e gerar credenciais válidas
"""

from assets.auth_config import verify_credentials, ADMIN_USERNAME, ADMIN_PASSWORD_HASH, ADMIN_PASSWORD_SALT

print("=" * 60)
print("🔐 TESTE DE CREDENCIAIS")
print("=" * 60)

# Verificar se as variáveis estão carregadas
print(f"\nUsuário configurado: {ADMIN_USERNAME}")
print(f"Hash configurado: {'Sim' if ADMIN_PASSWORD_HASH else 'NÃO'}")
print(f"Salt configurado: {'Sim' if ADMIN_PASSWORD_SALT else 'NÃO'}")

# Testar senhas
senhas_teste = [
    "EngenheiroDev0ps@#",     # Correta
    "EngenehiroDev0ps@#",     # Erro de digitação (que o usuário mencionou)
    "engenheiroDev0ps@#",     # Minúscula
]

print("\n" + "=" * 60)
print("TESTANDO SENHAS:")
print("=" * 60)

for senha in senhas_teste:
    resultado = verify_credentials("admin", senha)
    status = "✅ CORRETA" if resultado else "❌ INCORRETA"
    print(f"{status} - '{senha}'")

print("\n" + "=" * 60)
print("INFORMAÇÕES:")
print("=" * 60)
print("• Usuário: admin")
print("• Senha correta: EngenheiroDev0ps@#")
print("")
print("⚠️  ATENÇÃO: Verifique se digitou corretamente:")
print("   - Eng'e'nheiro (com 'e', não 'ene')")
print("   - Dev'0'ps (zero, não letra O)")
print("   - @ # (caracteres especiais)")
print("=" * 60)
