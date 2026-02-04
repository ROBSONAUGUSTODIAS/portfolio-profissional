"""Script para verificar e adicionar GitHub"""
from database import Database

db = Database("data/portfolio.db")
curriculum = db.get_curriculum()
links = db.get_links_sociais(curriculum['id'])

print("Links cadastrados:")
for link in links:
    print(f"  {link['plataforma']}: {link['url']}")

github_existe = any('github' in link['plataforma'].lower() for link in links)

if not github_existe:
    print("\n✅ Adicionando GitHub...")
    db.add_link_social(curriculum['id'], 'GitHub', 'https://github.com/1201133')
    print("GitHub adicionado com sucesso!")
else:
    print("\nℹ️ GitHub já está cadastrado!")
