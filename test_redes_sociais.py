"""
Script de teste para verificar a funcionalidade de redes sociais
"""

from database import Database
import os

def test_social_links():
    """Testa as funções de links sociais"""
    
    print("🔍 Testando funcionalidades de Redes Sociais\n")
    print("=" * 60)
    
    # Conectar ao banco
    db_path = "data/portfolio.db"
    if not os.path.exists(db_path):
        print("❌ Banco de dados não encontrado!")
        print(f"   Esperado em: {db_path}")
        return
    
    db = Database(db_path)
    print(f"✅ Conectado ao banco: {db_path}\n")
    
    # Verificar se existe um currículo
    curriculum = db.get_curriculum()
    if not curriculum:
        print("❌ Nenhum currículo encontrado!")
        print("   Execute 'python init_sample_data.py' primeiro")
        return
    
    print(f"✅ Currículo encontrado: {curriculum['nome']}")
    print(f"   ID: {curriculum['id']}\n")
    
    # Listar links sociais existentes
    links = db.get_links_sociais(curriculum['id'])
    print("📋 Links Sociais Cadastrados:")
    print("-" * 60)
    
    if links:
        for i, link in enumerate(links, 1):
            print(f"{i}. {link['plataforma']:15} → {link['url']}")
            print(f"   ID: {link['id']} | Ativo: {link['ativo']}")
    else:
        print("   (Nenhum link cadastrado)")
    
    print("\n" + "=" * 60)
    
    # Testar plataformas suportadas
    print("\n🎨 Plataformas Suportadas:")
    print("-" * 60)
    
    platforms = {
        'LinkedIn': {'icon': '💼', 'color': '#0A66C2'},
        'GitHub': {'icon': '💻', 'color': '#181717'},
        'Portfolio': {'icon': '🌐', 'color': '#FF6B6B'},
        'Email': {'icon': '📧', 'color': '#EA4335'},
        'Instagram': {'icon': '📷', 'color': '#E4405F'},
        'Twitter': {'icon': '🐦', 'color': '#1DA1F2'},
        'Facebook': {'icon': '👥', 'color': '#1877F2'},
        'YouTube': {'icon': '🎥', 'color': '#FF0000'},
        'WhatsApp': {'icon': '💬', 'color': '#25D366'},
        'Telegram': {'icon': '✈️', 'color': '#0088cc'},
        'Website': {'icon': '🌍', 'color': '#4CAF50'},
    }
    
    for name, info in platforms.items():
        print(f"{info['icon']} {name:15} {info['color']}")
    
    print("\n" + "=" * 60)
    print("\n✨ Teste concluído com sucesso!")
    print("\n💡 Dicas:")
    print("   • Execute 'streamlit run app.py' para ver os ícones")
    print("   • Acesse 'Administração' para gerenciar links")
    print("   • Veja 'REDES_SOCIAIS.md' para documentação completa")
    
    db.close()

if __name__ == "__main__":
    try:
        test_social_links()
    except Exception as e:
        print(f"\n❌ Erro durante o teste: {e}")
        import traceback
        traceback.print_exc()
