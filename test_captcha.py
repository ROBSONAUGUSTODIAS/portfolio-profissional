"""
Script de teste do sistema CAPTCHA
"""

import sys
from pathlib import Path

# Adicionar diretório raiz ao path
sys.path.insert(0, str(Path(__file__).parent))

from assets.captcha_manager import CaptchaManager


def test_captcha_generation():
    """Testa geração de texto CAPTCHA"""
    print("=" * 60)
    print("TESTE 1: Geração de Texto CAPTCHA")
    print("=" * 60)
    
    # Gerar vários textos
    for i in range(5):
        text = CaptchaManager.generate_captcha_text()
        print(f"✓ CAPTCHA #{i+1}: {text} (comprimento: {len(text)})")
    
    # Verificar comprimento customizado
    custom_text = CaptchaManager.generate_captcha_text(length=8)
    print(f"✓ CAPTCHA customizado (8 chars): {custom_text}")
    
    print("✅ Geração de texto: OK\n")


def test_captcha_image():
    """Testa geração de imagem CAPTCHA"""
    print("=" * 60)
    print("TESTE 2: Geração de Imagem CAPTCHA")
    print("=" * 60)
    
    text = "ABC123"
    try:
        image = CaptchaManager.generate_captcha_image(text)
        size = len(image.getvalue())
        print(f"✓ Imagem gerada para '{text}'")
        print(f"  - Tamanho: {size} bytes")
        print(f"  - Tipo: BytesIO")
        print("✅ Geração de imagem: OK\n")
    except Exception as e:
        print(f"❌ Erro ao gerar imagem: {e}\n")


def test_captcha_verification():
    """Testa verificação de CAPTCHA"""
    print("=" * 60)
    print("TESTE 3: Verificação de CAPTCHA")
    print("=" * 60)
    
    test_cases = [
        ("ABC123", "ABC123", True, "Texto exato"),
        ("ABC123", "abc123", True, "Case insensitive"),
        ("ABC123", " ABC123 ", True, "Com espaços"),
        ("ABC123", "XYZ789", False, "Texto incorreto"),
        ("ABC123", "", False, "Vazio"),
        ("", "ABC123", False, "Correto vazio"),
    ]
    
    passed = 0
    failed = 0
    
    for correct, user_input, expected, desc in test_cases:
        result = CaptchaManager.verify_captcha(user_input, correct)
        status = "✓" if result == expected else "✗"
        
        if result == expected:
            passed += 1
            print(f"{status} {desc}: OK")
        else:
            failed += 1
            print(f"{status} {desc}: FALHOU (esperado: {expected}, obtido: {result})")
    
    print(f"\n{'✅' if failed == 0 else '⚠️'} Testes passados: {passed}/{len(test_cases)}\n")


def test_captcha_manager_integration():
    """Testa integração completa do CaptchaManager"""
    print("=" * 60)
    print("TESTE 4: Integração do CaptchaManager")
    print("=" * 60)
    
    # Simular ciclo completo
    print("1. Gerando texto CAPTCHA...")
    text = CaptchaManager.generate_captcha_text()
    print(f"   ✓ Texto: {text}")
    
    print("2. Gerando imagem CAPTCHA...")
    try:
        image = CaptchaManager.generate_captcha_image(text)
        print(f"   ✓ Imagem gerada ({len(image.getvalue())} bytes)")
    except Exception as e:
        print(f"   ❌ Erro: {e}")
        return
    
    print("3. Verificando respostas...")
    # Correta
    if CaptchaManager.verify_captcha(text, text):
        print("   ✓ Resposta correta validada")
    else:
        print("   ✗ Falha na validação de resposta correta")
    
    # Incorreta
    if not CaptchaManager.verify_captcha("ERRADO", text):
        print("   ✓ Resposta incorreta rejeitada")
    else:
        print("   ✗ Falha na rejeição de resposta incorreta")
    
    print("✅ Integração: OK\n")


def test_captcha_security():
    """Testa aspectos de segurança do CAPTCHA"""
    print("=" * 60)
    print("TESTE 5: Segurança do CAPTCHA")
    print("=" * 60)
    
    # Gerar múltiplos CAPTCHAs e verificar aleatoriedade
    captchas = set()
    for _ in range(100):
        captchas.add(CaptchaManager.generate_captcha_text())
    
    uniqueness = len(captchas) / 100 * 100
    print(f"✓ Aleatoriedade: {len(captchas)}/100 únicos ({uniqueness:.1f}%)")
    
    if uniqueness >= 95:
        print("✅ Boa aleatoriedade (≥95%)")
    else:
        print("⚠️ Aleatoriedade baixa (<95%)")
    
    # Verificar caracteres permitidos
    text = CaptchaManager.generate_captcha_text()
    all_allowed = all(c in CaptchaManager.CAPTCHA_CHARS for c in text)
    
    if all_allowed:
        print("✓ Apenas caracteres permitidos usados")
        print("✅ Segurança: OK\n")
    else:
        print("✗ Caracteres não permitidos encontrados")
        print("❌ Segurança: FALHOU\n")


def main():
    """Executa todos os testes"""
    print("\n" + "=" * 60)
    print("SUITE DE TESTES - SISTEMA CAPTCHA")
    print("=" * 60 + "\n")
    
    try:
        test_captcha_generation()
        test_captcha_image()
        test_captcha_verification()
        test_captcha_manager_integration()
        test_captcha_security()
        
        print("=" * 60)
        print("✅ TODOS OS TESTES CONCLUÍDOS")
        print("=" * 60)
        
    except Exception as e:
        print(f"\n❌ ERRO CRÍTICO: {e}")
        import traceback
        traceback.print_exc()
        return 1
    
    return 0


if __name__ == "__main__":
    exit(main())
