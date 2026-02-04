"""
Script para adicionar link do GitHub às redes sociais
"""

import sys
from pathlib import Path

# Adicionar diretório raiz ao path
sys.path.insert(0, str(Path(__file__).parent))

import database as db

def adicionar_github():
    """Adiciona link do GitHub se não existir"""
    
    # Buscar currículo
    curriculum = db.get_curriculum()
    
    if not curriculum:
        print("❌ Currículo não encontrado!")
        return
    
    # Buscar links existentes
    links = db.get_links_sociais(curriculum['id'])
    
    # Verificar se GitHub já existe
    github_existe = any(link['plataforma'].lower() == 'github' for link in links)
    
    if github_existe:
        print("ℹ️ GitHub já está cadastrado!")
        print("\nLinks atuais:")
        for link in links:
            print(f"  - {link['plataforma']}: {link['url']}")
        
        # Perguntar se deseja atualizar
        resposta = input("\nDeseja atualizar a URL do GitHub? (s/n): ")
        if resposta.lower() == 's':
            nova_url = input("Digite a nova URL do GitHub: ")
            for link in links:
                if link['plataforma'].lower() == 'github':
                    db.update_link_social(link['id'], nova_url)
                    print(f"✅ GitHub atualizado: {nova_url}")
                    break
    else:
        # Adicionar GitHub
        url_github = input("Digite a URL do seu GitHub (ex: https://github.com/usuario): ")
        
        if url_github:
            db.add_link_social(curriculum['id'], 'GitHub', url_github)
            print(f"✅ GitHub adicionado com sucesso: {url_github}")
        else:
            print("❌ URL vazia! GitHub não foi adicionado.")
    
    # Mostrar todos os links
    print("\n📊 Links Sociais Cadastrados:")
    links_atualizados = db.get_links_sociais(curriculum['id'])
    for link in links_atualizados:
        print(f"  - {link['plataforma']}: {link['url']}")

if __name__ == "__main__":
    print("=" * 60)
    print("ADICIONAR GITHUB AO PORTFÓLIO")
    print("=" * 60 + "\n")
    
    try:
        adicionar_github()
    except Exception as e:
        print(f"\n❌ Erro: {e}")
        import traceback
        traceback.print_exc()
