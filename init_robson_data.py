"""
Script para inicializar o banco de dados com informações de Robson Augusto Dias
"""

import os
from database import Database
from datetime import datetime

def init_robson_data():
    """Inicializa o banco com dados de Robson Augusto Dias"""
    
    # Remover banco anterior se existir
    db_path = "data/portfolio.db"
    if os.path.exists(db_path):
        os.remove(db_path)
        print(f"✅ Banco anterior removido")
    
    db = Database(db_path)
    
    print("📝 Inicializando banco de dados com dados de Robson Augusto Dias...")
    
    # Criar currículo
    curriculum_id = db.create_curriculum(
        nome="Robson Augusto Dias",
        email="robson.augusto.dias@hotmail.com",
        profissao="Engenheiro DevOps",
        telefone="(11) 96495-1379",
        sobre="Graduado em Análise e Desenvolvimento de Sistemas, MBA em Desenvolvimento de Aplicações .NET e pós-graduação em Governança de TI, Gerenciamento de Projetos e Arquitetura de Infraestrutura."
    )
    
    db.update_curriculum(
        curriculum_id,
        resumo="""
Engenheiro DevOps com 10+ anos de experiência em desenvolvimento e infraestrutura de software. 

Especializado em:
• Cloud (Azure e GCP)
• DevOps e CI/CD
• Infraestrutura como Código (IaC)
• Docker e Kubernetes
• Automação com Python e PowerShell
• Desenvolvimento .NET

Responsável por integrar equipes de desenvolvimento e operações, promovendo padronização de processos e entregas ágeis. Experiência em aplicação de metodologias ágeis (Scrum, Kanban) e ferramentas de produtividade.

Objetivo: Continuar evoluindo como Engenheiro DevOps em ambientes Cloud-native, contribuindo para a transformação digital e excelência técnica.
        """
    )
    
    print(f"✅ Currículo criado com ID: {curriculum_id}")
    
    # Adicionar experiências profissionais
    experiencias = [
        {
            "titulo": "Analista DevOps II – Engenharia Corporativa",
            "empresa": "TOTVS S/A",
            "descricao": """• Responsável pela documentação completa das etapas de desenvolvimento, utilizando ferramentas de versionamento
• Colaboração ativa com equipes de desenvolvimento na definição de soluções de negócio
• Garantia da qualidade do software por meio de processos estruturados e ferramentas de monitoramento
• Orientação e suporte técnico a desenvolvedores de menor senioridade
• Levantamento, análise e detalhamento de requisitos de baixa e média complexidade
• Desenvolvimento de soluções utilizando frameworks corporativos
• Criação e otimização de consultas SQL e desenvolvimento de APIs
• Geração de dashboards interativos para visibilidade e suporte à tomada de decisão""",
            "data_inicio": "2023-04-23",
            "data_fim": None
        },
        {
            "titulo": "Analista DevOps Pleno",
            "empresa": "Agência Molla",
            "descricao": """• Aplicação da cultura DevOps
• Azure como Cloud Platform
• Automatização de processos de testes unitários
• Monitoramento com App Insights
• PowerShell e Shell Scripts para otimização de processos CI/CD
• Modernização de processos DevOps para melhorar qualidade nas implantações""",
            "data_inicio": "2022-09-13",
            "data_fim": "2023-04-13"
        },
        {
            "titulo": "Analista DevOps Pleno",
            "empresa": "Koode Tecnologia",
            "descricao": """• Implantação da cultura DevOps
• Utilização do Azure como Cloud Platform
• Automação de processos CI/CD com PowerShell e Shell Scripts
• Modernização de processos DevOps
• Gerenciamento Office 365
• Desenvolvimento com .NET Framework 4.7, Entity Framework Core e ASP.NET MVC
• Utilização de Azure SQL Server""",
            "data_inicio": "2021-09-13",
            "data_fim": "2022-05-19"
        },
        {
            "titulo": "Analista Desenvolvedor Jr",
            "empresa": "Digisystem – Secretaria da Fazenda/SP",
            "descricao": """• Aplicação da cultura DevOps e uso de ferramentas como Azure DevOps
• Desenvolvimento e sustentação de sistemas
• Suporte a sistemas legados e desenvolvimento de novas soluções
• Tecnologias: .NET Framework 4.7, Entity Framework Core, ASP.NET MVC, VB6, WebForms, WCF, SQL Server""",
            "data_inicio": "2020-03-13",
            "data_fim": "2021-09-13"
        },
        {
            "titulo": "Analista Programador I",
            "empresa": "Valid Soluções S.A",
            "descricao": """• Atendimento de incidentes, análise e manipulação de dados
• Scripts, correções e melhorias em aplicações
• Consultas e atualizações em SQL Server
• Tecnologias: Java 8, Tortoise SVN, SQL Server 2014, MySQL""",
            "data_inicio": "2019-06-01",
            "data_fim": "2019-12-31"
        },
        {
            "titulo": "Técnico em Suporte I",
            "empresa": "Valid Soluções S.A",
            "descricao": """• Manutenção preventiva em sistemas de captura de identidade
• Abertura e atualização de chamados
• Monitoramento de logs e serviços em Windows Server
• Tecnologias: C#, SQL Server, Windows Server 2012""",
            "data_inicio": "2014-01-01",
            "data_fim": "2019-06-30"
        },
        {
            "titulo": "Analista de Suporte Técnico",
            "empresa": "Mister Print Papéis Especiais LTDA",
            "descricao": "Atendimento ao usuário, manutenção de computadores e configuração de ativos",
            "data_inicio": "2013-07-01",
            "data_fim": "2013-12-31"
        },
        {
            "titulo": "Analista de Suporte Técnico",
            "empresa": "Jaime Administração de Bens e Condomínios LTDA",
            "descricao": """• Gerenciamento de redes de computadores
• Manutenções preventivas em ativos
• Controle de acesso e gerenciamento de diretivas via Active Directory""",
            "data_inicio": "2012-01-01",
            "data_fim": "2012-11-30"
        }
    ]
    
    for exp in experiencias:
        db.add_experiencia(
            curriculum_id,
            exp["titulo"],
            exp["empresa"],
            exp["descricao"],
            exp["data_inicio"],
            exp["data_fim"]
        )
    
    print(f"✅ {len(experiencias)} experiências profissionais adicionadas")
    
    # Adicionar educação
    educacoes = [
        {
            "titulo": "Governança e Gestão da Tecnologia da Informação",
            "instituicao": "UNIBF",
            "data_inicio": "2021-01-01",
            "data_conclusao": "2023-12-31",
            "descricao": "Pós-graduação em Governança e Gestão da TI"
        },
        {
            "titulo": "Gerenciamento de Projetos em TI",
            "instituicao": "UNIBF",
            "data_inicio": "2020-01-01",
            "data_conclusao": "2022-12-31",
            "descricao": "Pós-graduação em Gerenciamento de Projetos em TI"
        },
        {
            "titulo": "Arquitetura e Gestão de Infraestrutura em TI",
            "instituicao": "UNIBF",
            "data_inicio": "2019-01-01",
            "data_conclusao": "2022-12-31",
            "descricao": "Pós-graduação em Arquitetura e Gestão de Infraestrutura em TI"
        },
        {
            "titulo": "MBA em Desenvolvimento de Aplicações .NET",
            "instituicao": "UNIBF",
            "data_inicio": "2018-01-01",
            "data_conclusao": "2018-12-31",
            "descricao": "MBA em Desenvolvimento de Aplicações .NET"
        },
        {
            "titulo": "Graduação em Análise e Desenvolvimento de Sistemas",
            "instituicao": "Faculdade Impacta Tecnologia (FIT)",
            "data_inicio": "2016-01-01",
            "data_conclusao": "2016-12-31",
            "descricao": "Bacharelado em Análise e Desenvolvimento de Sistemas"
        },
        {
            "titulo": "Técnico em Informática",
            "instituicao": "SENAC",
            "data_inicio": "2011-01-01",
            "data_conclusao": "2011-12-31",
            "descricao": "Curso Técnico em Informática"
        }
    ]
    
    for edu in educacoes:
        db.add_educacao(
            curriculum_id,
            edu["titulo"],
            edu["instituicao"],
            edu["data_conclusao"],
            edu["descricao"],
            edu["data_inicio"]
        )
    
    print(f"✅ {len(educacoes)} educações adicionadas")
    
    # Adicionar habilidades técnicas
    habilidades = [
        # Cloud & DevOps
        ("DevOps & Cloud", "Azure", 5),
        ("DevOps & Cloud", "Azure DevOps", 5),
        ("DevOps & Cloud", "GCP", 4),
        ("DevOps & Cloud", "CI/CD", 5),
        ("DevOps & Cloud", "Docker", 5),
        ("DevOps & Cloud", "Kubernetes (AKS)", 4),
        ("DevOps & Cloud", "GitHub Actions", 4),
        ("DevOps & Cloud", "Terraform", 4),
        
        # Linguagens de Programação
        ("Programação", "C#", 5),
        ("Programação", ".NET Framework", 5),
        ("Programação", ".NET Core", 5),
        ("Programação", "Python", 4),
        ("Programação", "PowerShell", 5),
        ("Programação", "Shell Script", 4),
        ("Programação", "SQL", 5),
        ("Programação", "VB.NET", 3),
        ("Programação", "Java", 3),
        
        # Web & Framework
        ("Web Framework", "ASP.NET MVC", 5),
        ("Web Framework", "ASP.NET Core", 4),
        ("Web Framework", "Entity Framework", 5),
        ("Web Framework", "Angular", 3),
        
        # Banco de Dados
        ("Banco de Dados", "SQL Server", 5),
        ("Banco de Dados", "Azure SQL", 5),
        ("Banco de Dados", "MySQL", 3),
        ("Banco de Dados", "BigQuery", 4),
        
        # Ferramentas & Plataformas
        ("Ferramentas", "Azure DevOps", 5),
        ("Ferramentas", "Git", 5),
        ("Ferramentas", "Jira", 4),
        ("Ferramentas", "SonarQube", 4),
        ("Ferramentas", "Active Directory", 4),
        ("Ferramentas", "Office 365", 4),
        ("Ferramentas", "Looker Studio", 4),
        
        # Monitoramento
        ("Monitoramento", "Application Insights", 4),
        ("Monitoramento", "WhatsUp Gold", 3),
        
        # IaC & Infraestrutura
        ("Infraestrutura", "Infraestrutura como Código", 4),
        ("Infraestrutura", "Windows Server", 4),
        ("Infraestrutura", "SSRS/Report Builder", 3),
        
        # Metodologias
        ("Metodologias", "Scrum", 5),
        ("Metodologias", "Kanban", 4),
        ("Metodologias", "ITIL v4", 4),
        
        # Soft Skills
        ("Soft Skills", "Liderança Técnica", 5),
        ("Soft Skills", "Mentoria", 4),
        ("Soft Skills", "Comunicação", 5),
        ("Soft Skills", "Trabalho em Equipe", 5),
        ("Soft Skills", "Resolução de Problemas", 5),
    ]
    
    for categoria, habilidade, nivel in habilidades:
        db.add_habilidade(curriculum_id, categoria, habilidade, nivel)
    
    print(f"✅ {len(habilidades)} habilidades adicionadas")
    
    # Adicionar certificações
    db.add_habilidade(curriculum_id, "Certificações", "Scrum Foundation Professional Certificate (SFPC)", 5)
    db.add_habilidade(curriculum_id, "Certificações", "Microsoft Azure Fundamentals (AZ-900)", 5)
    db.add_habilidade(curriculum_id, "Certificações", "Microsoft AI-102: Azure AI Solution", 4)
    db.add_habilidade(curriculum_id, "Certificações", "AWS Cloud Practitioner", 3)
    db.add_habilidade(curriculum_id, "Certificações", "ITIL v4", 4)
    
    print("✅ Certificações adicionadas")
    
    # Adicionar links sociais
    links = [
        ("LinkedIn", "https://www.linkedin.com/in/robson-augusto-dias/"),
        ("Portfólio", "https://prototiposlider.azurewebsites.net"),
        ("Email", "mailto:robson.augusto.dias@hotmail.com"),
    ]
    
    for plataforma, url in links:
        db.add_link_social(curriculum_id, plataforma, url)
    
    print(f"✅ {len(links)} links sociais adicionados")
    
    print("\n" + "="*70)
    print("✨ Banco de dados inicializado com sucesso!")
    print("="*70)
    print(f"📊 Resumo dos dados carregados:")
    print(f"  • Currículo: Robson Augusto Dias (ID: {curriculum_id})")
    print(f"  • Experiências: {len(experiencias)}")
    print(f"  • Educações: {len(educacoes)}")
    print(f"  • Habilidades: {len(habilidades)} + 5 certificações")
    print(f"  • Links Sociais: {len(links)}")
    print("="*70)
    print("\n🚀 Agora execute: streamlit run app.py")
    
    db.close()

if __name__ == "__main__":
    init_robson_data()
