"""
Script para atualizar o link do LinkedIn
"""

from database import Database

def atualizar_linkedin():
    """Atualiza o link do LinkedIn para o URL correto"""
    
    db = Database("data/portfolio.db")
    
    # Buscar currículo
    curriculum = db.get_curriculum()
    if not curriculum:
        print("❌ Nenhum currículo encontrado!")
        return
    
    print(f"✅ Currículo encontrado: {curriculum['nome']}\n")
    
    # Buscar links sociais
    links = db.get_links_sociais(curriculum['id'])
    
    # Encontrar o LinkedIn
    linkedin_link = None
    for link in links:
        if link['plataforma'].lower() == 'linkedin':
            linkedin_link = link
            break
    
    if linkedin_link:
        print(f"📋 Link atual do LinkedIn:")
        print(f"   ID: {linkedin_link['id']}")
        print(f"   URL: {linkedin_link['url']}")
        print()
        
        # Novo URL
        novo_url = "https://www.linkedin.com/in/robsonaugustodias/"
        
        # Atualizar
        if db.update_link_social(linkedin_link['id'], novo_url):
            print(f"✅ Link do LinkedIn atualizado com sucesso!")
            print(f"   Novo URL: {novo_url}")
        else:
            print("❌ Erro ao atualizar o link")
    else:
        print("⚠️ Link do LinkedIn não encontrado")
        print("   Adicionando novo link...")
        
        novo_url = "https://www.linkedin.com/in/robsonaugustodias/"
        link_id = db.add_link_social(curriculum['id'], "LinkedIn", novo_url)
        print(f"✅ Link do LinkedIn adicionado!")
        print(f"   ID: {link_id}")
        print(f"   URL: {novo_url}")
    
    db.close()
    print("\n✨ Operação concluída!")

if __name__ == "__main__":
    atualizar_linkedin()
