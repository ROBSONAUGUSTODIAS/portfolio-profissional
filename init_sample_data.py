"""
Script para inicializar o banco de dados com dados de exemplo
Útil para testes e demonstração da aplicação
"""

from database import Database
from datetime import datetime, timedelta

def init_sample_data():
    """Inicializa o banco com dados de exemplo"""
    
    db = Database("data/portfolio.db")
    
    # Verificar se já existe currículo
    curriculum = db.get_curriculum()
    if curriculum:
        print(f"✅ Banco de dados já contém dados de {curriculum['nome']}")
        return
    
    print("📝 Inicializando banco de dados com dados de exemplo...")
    
    # Criar currículo
    curriculum_id = db.create_curriculum(
        nome="João Silva",
        email="joao.silva@email.com",
        profissao="Desenvolvedor Python Full Stack",
        telefone="+55 (11) 9xxxx-xxxx",
        sobre="Desenvolvedor apaixonado por Python com 5+ anos de experiência em web development."
    )
    
    db.update_curriculum(
        curriculum_id,
        resumo="""
        Sou um desenvolvedor Python full stack com forte experiência em Streamlit, Django e FastAPI.
        Tenho paixão por criar aplicações escaláveis e interfaces intuitivas. 
        Sempre buscando aprender novas tecnologias e melhores práticas de desenvolvimento.
        """
    )
    
    print(f"✅ Currículo criado com ID: {curriculum_id}")
    
    # Adicionar experiências
    db.add_experiencia(
        curriculum_id,
        titulo="Senior Developer Python",
        empresa="Tech Solutions Ltda",
        descricao="Responsável pelo desenvolvimento de aplicações web usando Python/Django, implementação de APIs REST e otimização de performance.",
        data_inicio="2021-01-15",
        data_fim="2024-01-20"
    )
    
    db.add_experiencia(
        curriculum_id,
        titulo="Desenvolvedor Python",
        empresa="Digital Innovations Inc",
        descricao="Desenvolvimento de scripts de automação, criação de dashboards com Streamlit e manutenção de aplicações legadas.",
        data_inicio="2019-06-01",
        data_fim="2020-12-31"
    )
    
    print("✅ Experiências adicionadas")
    
    # Adicionar educação
    db.add_educacao(
        curriculum_id,
        titulo="Bacharelado em Ciência da Computação",
        instituicao="Universidade Federal",
        data_inicio="2016-02-01",
        data_conclusao="2020-06-30",
        descricao="Formação completa em computação com ênfase em desenvolvimento de software e banco de dados."
    )
    
    db.add_educacao(
        curriculum_id,
        titulo="Certificação Advanced Python Developer",
        instituicao="Platforma Online de Cursos",
        data_conclusao="2023-03-15",
        descricao="Curso avançado cobrindo decorators, generators, async/await e design patterns."
    )
    
    print("✅ Educação adicionada")
    
    # Adicionar habilidades
    habilidades_tecnicas = [
        ("Programação", "Python", 5),
        ("Programação", "JavaScript", 4),
        ("Programação", "SQL", 5),
        ("Frameworks", "Django", 5),
        ("Frameworks", "FastAPI", 4),
        ("Frameworks", "Streamlit", 5),
        ("Banco de Dados", "PostgreSQL", 5),
        ("Banco de Dados", "SQLite", 5),
        ("Banco de Dados", "MongoDB", 3),
        ("DevOps", "Docker", 4),
        ("DevOps", "Git", 5),
        ("Soft Skills", "Comunicação", 4),
        ("Soft Skills", "Liderança", 3),
        ("Soft Skills", "Trabalho em Equipe", 5),
    ]
    
    for categoria, habilidade, nivel in habilidades_tecnicas:
        db.add_habilidade(curriculum_id, categoria, habilidade, nivel)
    
    print("✅ Habilidades adicionadas")
    
    # Adicionar links sociais
    db.add_link_social(curriculum_id, "LinkedIn", "https://linkedin.com/in/joaosilva")
    db.add_link_social(curriculum_id, "GitHub", "https://github.com/joaosilva")
    db.add_link_social(curriculum_id, "Portfolio", "https://joaosilva.com")
    
    print("✅ Links sociais adicionados")
    
    print("\n✨ Banco de dados inicializado com sucesso!")
    print("📊 Resumo dos dados carregados:")
    print(f"  • Currículo: João Silva (ID: {curriculum_id})")
    print(f"  • Experiências: 2")
    print(f"  • Educações: 2")
    print(f"  • Habilidades: {len(habilidades_tecnicas)}")
    print(f"  • Links Sociais: 3")
    print("\n⚠️  Nota: Certificados não foram adicionados (exigem upload de arquivos)")
    print("💡 Para adicionar certificados, use a seção de Administração na aplicação")
    
    db.close()

if __name__ == "__main__":
    init_sample_data()
