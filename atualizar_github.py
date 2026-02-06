"""
Script para atualizar o endereço do GitHub no banco de dados
"""
from database import Database

def atualizar_github():
    """Atualiza ou adiciona o link do GitHub"""
    db = Database("data/portfolio.db")
    
    curriculum = db.get_curriculum()
    if not curriculum:
        print("❌ Nenhum currículo encontrado!")
        return
    
    links = db.get_links_sociais(curriculum['id'])
    
    # Verificar se GitHub já existe
    github_link = None
    for link in links:
        if link['plataforma'].lower() == 'github':
            github_link = link
            break
    
    novo_url = "https://github.com/ROBSONAUGUSTODIAS"
    
    if github_link:
        # Atualizar GitHub existente
        print(f"📝 GitHub atual: {github_link['url']}")
        print(f"🔄 Atualizando para: {novo_url}")
        
        cursor = db.conn.cursor()
        cursor.execute("""
            UPDATE links_sociais 
            SET url = ? 
            WHERE id = ?
        """, (novo_url, github_link['id']))
        db.conn.commit()
        
        print("✅ GitHub atualizado com sucesso!")
    else:
        # Adicionar novo link do GitHub
        print("➕ Adicionando link do GitHub...")
        db.add_link_social(curriculum['id'], 'GitHub', novo_url)
        print(f"✅ GitHub adicionado: {novo_url}")
    
    # Mostrar todos os links atuais
    print("\n📋 Links sociais atuais:")
    links_atualizados = db.get_links_sociais(curriculum['id'])
    for link in links_atualizados:
        print(f"  • {link['plataforma']}: {link['url']}")
    
    db.close()

if __name__ == "__main__":
    atualizar_github()
