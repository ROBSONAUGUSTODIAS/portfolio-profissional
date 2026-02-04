"""
Script para criar dados de teste no banco de dados
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent / "assets"))

from database import Database

# Criar ou conectar ao banco
db = Database("data/portfolio.db")

# Verificar se já existe currículo
curriculum = db.get_curriculum()

if not curriculum:
    print("📝 Criando currículo de teste...")
    curriculum_id = db.create_curriculum(
        nome="João Silva",
        email="joao@email.com",
        profissao="Desenvolvedor Full Stack",
        telefone="11999999999"
    )
    print(f"✅ Currículo criado com ID: {curriculum_id}")
    curriculum = db.get_curriculum()
else:
    print(f"✅ Currículo existente: {curriculum['nome']}")
    curriculum_id = curriculum['id']

# Adicionar experiência se não existir
experiencias = db.get_experiencias(curriculum_id)
if not experiencias:
    print("📝 Adicionando experiências...")
    db.add_experiencia(
        curriculum_id,
        "Desenvolvedor Python",
        "Tech Company",
        "Desenvolvimento de aplicações web com Django e FastAPI",
        "2020-01-15",
        "2022-12-31"
    )
    db.add_experiencia(
        curriculum_id,
        "Desenvolvedor Full Stack",
        "StartUp Innovation",
        "Desenvolvimento de plataforma SaaS com React e Node.js",
        "2023-01-01",
        None
    )
    print("✅ Experiências adicionadas")

# Adicionar educação se não existir
educacao = db.get_educacao(curriculum_id)
if not educacao:
    print("📝 Adicionando educação...")
    db.add_educacao(
        curriculum_id,
        "Bacharel em Ciência da Computação",
        "Universidade Federal",
        "2022-12-15",
        "Formação completa em Ciência da Computação",
        "2018-02-01"
    )
    print("✅ Educação adicionada")

# Adicionar habilidades se não existir
habilidades = db.get_habilidades(curriculum_id)
if not habilidades:
    print("📝 Adicionando habilidades...")
    db.add_habilidade(curriculum_id, "Programação", "Python", 5)
    db.add_habilidade(curriculum_id, "Programação", "JavaScript", 4)
    db.add_habilidade(curriculum_id, "Frameworks", "Django", 5)
    db.add_habilidade(curriculum_id, "Frameworks", "React", 4)
    db.add_habilidade(curriculum_id, "Banco de Dados", "PostgreSQL", 4)
    db.add_habilidade(curriculum_id, "Soft Skills", "Comunicação", 4)
    print("✅ Habilidades adicionadas")

# Adicionar links sociais se não existir
links = db.get_links_sociais(curriculum_id)
if not links:
    print("📝 Adicionando links sociais...")
    db.add_link_social(curriculum_id, "LinkedIn", "https://linkedin.com/in/joaosilva")
    db.add_link_social(curriculum_id, "GitHub", "https://github.com/joaosilva")
    db.add_link_social(curriculum_id, "Portfolio", "https://joaosilva.dev")
    print("✅ Links sociais adicionados")

print("\n✅ Dados de teste criados com sucesso!")
print(f"📊 Currículo de: {curriculum['nome']}")
print(f"📌 Profissão: {curriculum['profissao']}")
