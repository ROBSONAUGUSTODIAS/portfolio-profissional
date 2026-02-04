# 📚 EXEMPLOS DE USO

## 🎯 Exemplo Completo: Criar um Portfólio do Zero

### Passo 1: Executar a Aplicação
```bash
cd d:\PROTOTIPO\PORTIFOLIO
.\.venv\Scripts\Activate
streamlit run app.py
```

### Passo 2: Criar Perfil
1. Vá para **⚙️ Administração** → **👤 Perfil**
2. Clique em **➕ Criar Perfil**
3. Preencha:
   - Nome: `Maria Silva`
   - Email: `maria@email.com`
   - Profissão: `Desenvolvedora Full Stack`
   - Telefone: `+55 (11) 9xxxx-xxxx`
4. Clique em **Criar Perfil**

### Passo 3: Adicionar Experiência
1. Vá para **⚙️ Administração** → **💼 Experiência**
2. Preencha:
   - Título: `Senior Python Developer`
   - Empresa: `Tech Company XYZ`
   - Descrição: `Desenvolvimento de aplicações web com Django...`
   - Data Início: `2020-01-15`
   - Data Fim: `2024-01-20`
3. Clique em **➕ Adicionar Experiência**

### Passo 4: Adicionar Educação
1. Vá para **⚙️ Administração** → **🎓 Educação**
2. Preencha:
   - Título: `Bacharelado em Ciência da Computação`
   - Instituição: `Universidade Federal`
   - Data Início: `2016-02-01`
   - Data Conclusão: `2020-06-30`
3. Clique em **➕ Adicionar Educação**

### Passo 5: Adicionar Certificado (Com Slider!)
1. Vá para **⚙️ Administração** → **🏆 Certificados**
2. Preencha:
   - Título: `Python Advanced Certification`
   - Emissor: `Udemy`
   - Data de Obtenção: `2023-05-15`
   - Descrição: `Certificado avançado de Python...`
   - URL: `https://udemy.com/verify/XXXX`
3. **Upload do Certificado**: Selecione uma imagem ou PDF
4. Clique em **➕ Adicionar Certificado**
5. Vá para **🏆 Certificados** e use o **slider** para navegar!

### Passo 6: Adicionar Habilidades
1. Vá para **⚙️ Administração** → **⭐ Habilidades**
2. Adicione várias habilidades:
   - Categoria: `Programação`
   - Nome: `Python`
   - Nível: `5 ⭐⭐⭐⭐⭐`
3. Repita para outras habilidades

### Passo 7: Conectar Redes Sociais
1. Vá para **⚙️ Administração** → **🔗 Redes Sociais**
2. Adicione links:
   - Plataforma: `LinkedIn`
   - URL: `https://linkedin.com/in/mariasilva`
3. Repita para GitHub, Portfolio, etc.

---

## 💻 Exemplos de Código Direto no Python

### Usar Database Sem Streamlit
```python
from database import Database

# Criar/conectar banco
db = Database("data/portfolio.db")

# Criar currículo
curriculum_id = db.create_curriculum(
    nome="João Silva",
    email="joao@email.com",
    profissao="Desenvolvedor",
    telefone="+55 11 9xxxx-xxxx"
)

# Adicionar experiência
db.add_experiencia(
    curriculum_id=curriculum_id,
    titulo="Senior Developer",
    empresa="Tech Corp",
    descricao="Desenvolveu aplicações em Python",
    data_inicio="2020-01-15",
    data_fim="2023-12-31"
)

# Recuperar dados
curriculum = db.get_curriculum()
print(f"Nome: {curriculum['nome']}")
print(f"Profissão: {curriculum['profissao']}")

experiencias = db.get_experiencias(curriculum_id)
for exp in experiencias:
    print(f"- {exp['titulo']} em {exp['empresa']}")

# Fechar banco
db.close()
```

### Upload de Certificado Programaticamente
```python
from database import Database
from assets.utils import FileManager
from pathlib import Path

db = Database()
curriculum = db.get_curriculum()

# Simular upload de arquivo
class FakeUpload:
    def __init__(self, path):
        self.name = Path(path).name
        self.type = "image/png"
        
    def getbuffer(self):
        with open(path, "rb") as f:
            return f.read()

# Salvar arquivo
fake_file = FakeUpload("meu_certificado.png")
file_path = FileManager.save_upload_file(
    fake_file, 
    "data/certificados"
)

# Adicionar ao banco
cert_id = db.add_certificado(
    curriculum_id=curriculum['id'],
    titulo="AWS Certification",
    arquivo_path=file_path,
    issuer="Amazon Web Services",
    data_obtencao="2023-06-15",
    url_certificado="https://aws.amazon.com/verify"
)

print(f"Certificado criado com ID: {cert_id}")
db.close()
```

---

## 🎨 Exemplos de Customização

### Alterar Cores do Tema
```python
# Em assets/config.py

COLORS = {
    "primary": "#FF6B6B",      # Vermelho
    "secondary": "#4ECDC4",    # Teal
    "success": "#95E1D3",      # Mint
    "danger": "#FF6B9D",       # Rosa
    "warning": "#FFA502",      # Laranja
    "info": "#38ADA9",         # Azul marinho
    "light": "#F7F7F7",        # Cinza claro
    "dark": "#1A1A1A"          # Preto
}

# Em app.py, alterar as cores do CSS
st.markdown(f"""
<style>
.metric-card {{
    background: linear-gradient(135deg, {COLORS['primary']} 0%, {COLORS['secondary']} 100%);
}}
</style>
""", unsafe_allow_html=True)
```

### Adicionar Mais Categorias de Habilidades
```python
# Em app.py, na tab5 (tab com habilidades)

categorias_customizadas = [
    "Programação",
    "Frameworks",
    "Banco de Dados",
    "DevOps",
    "Cloud (AWS/Azure/GCP)",
    "Soft Skills",
    "Ferramentas",
    "Linguagens",
    "Design",
    "Gestão"
]

categoria = st.selectbox("Categoria", categorias_customizadas)
```

### Customizar Texto da Home Page
```python
# Em app.py, função show_home()

st.markdown(f"""
## 👋 Bem-vindo ao meu portfólio!

Sou **{curriculum['nome']}** - **{curriculum['profissao']}**

**Bio:**
{curriculum['sobre']}

### Confira meus projetos e experiências! 🚀
""")
```

---

## 📊 Exemplos com Dados Reais

### Banco de Dados Pré-carregado
```python
# init_sample_data.py (já fornecido)
python init_sample_data.py
```

Cria automaticamente:
- 1 Currículo (João Silva)
- 2 Experiências profissionais
- 2 Formações educacionais
- 14 Habilidades técnicas
- 3 Links de redes sociais

### Gerar Relatório em Markdown
```python
from database import Database

def generate_markdown_report():
    db = Database()
    curriculum = db.get_curriculum()
    
    with open("curriculo_export.md", "w", encoding="utf-8") as f:
        f.write(f"# {curriculum['nome']}\n\n")
        f.write(f"**{curriculum['profissao']}**\n\n")
        f.write(f"📧 {curriculum['email']}\n")
        f.write(f"📱 {curriculum['telefone']}\n\n")
        
        f.write("## Sobre\n\n")
        f.write(f"{curriculum['sobre']}\n\n")
        
        experiencias = db.get_experiencias(curriculum['id'])
        if experiencias:
            f.write("## Experiência\n\n")
            for exp in experiencias:
                f.write(f"### {exp['titulo']} - {exp['empresa']}\n")
                f.write(f"{exp['descricao']}\n\n")
    
    db.close()
    print("✅ Relatório gerado em curriculo_export.md")

generate_markdown_report()
```

---

## 🔧 Exemplos Avançados

### Busca e Filtro de Certificados
```python
# Adicionar em app.py

def search_certificados(curriculum_id, termo_busca):
    db = Database()
    certificados = db.get_certificados(curriculum_id)
    
    filtered = [
        cert for cert in certificados
        if termo_busca.lower() in cert['titulo'].lower() or
           termo_busca.lower() in cert['issuer'].lower()
    ]
    
    return filtered

# Usar em show_certificados()
search_termo = st.text_input("🔍 Buscar certificado...")
if search_termo:
    certificados = search_certificados(curriculum_id, search_termo)
```

### Exportar para PDF
```python
# Instalar: pip install reportlab

from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def export_curriculum_to_pdf(curriculum_id):
    db = Database()
    curriculum = db.get_curriculum()
    
    pdf = canvas.Canvas("curriculo.pdf", pagesize=letter)
    pdf.setTitle(f"Currículo - {curriculum['nome']}")
    
    # Adicionar conteúdo
    pdf.setFont("Helvetica-Bold", 20)
    pdf.drawString(50, 750, curriculum['nome'])
    
    pdf.setFont("Helvetica", 12)
    pdf.drawString(50, 730, curriculum['profissao'])
    pdf.drawString(50, 710, f"Email: {curriculum['email']}")
    
    # Mais conteúdo...
    pdf.save()
    db.close()
```

### Analytics Simples
```python
from datetime import datetime

def log_visit(page_name):
    timestamp = datetime.now().isoformat()
    with open("logs/visits.log", "a") as f:
        f.write(f"{timestamp} - {page_name}\n")

def get_visit_stats():
    stats = {}
    with open("logs/visits.log", "r") as f:
        for line in f:
            page = line.split(" - ")[1].strip()
            stats[page] = stats.get(page, 0) + 1
    return stats

# Usar em show_admin()
visits = get_visit_stats()
st.metric("Total de Visitas", sum(visits.values()))
for page, count in visits.items():
    st.metric(f"Visitas: {page}", count)
```

---

## 🚀 Próximos Passos

1. **Personalizar cores e temas** → Editar `assets/config.py`
2. **Adicionar mais campos** → Estender `database.py` e `app.py`
3. **Implementar autenticação** → Instalar `streamlit-authenticator`
4. **Deploy** → Fazer push para GitHub e conectar Streamlit Cloud
5. **Monitorar** → Adicionar analytics e logs

---

**Todos os exemplos são baseados no código real da aplicação!**
