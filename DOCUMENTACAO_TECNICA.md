# 📋 DOCUMENTAÇÃO TÉCNICA - PORTFÓLIO PROFISSIONAL

## 🏗️ Arquitetura do Projeto

```
┌─────────────────────────────────────┐
│   Interface Streamlit (app.py)      │
│   - Páginas: Home, CV, Cert, Admin  │
│   - Sliders, Forms, Cards           │
└──────────────┬──────────────────────┘
               │
┌──────────────▼──────────────────────┐
│   Camada de Banco de Dados          │
│   (database.py)                     │
│   - CRUD Operations                 │
│   - Queries otimizadas              │
└──────────────┬──────────────────────┘
               │
┌──────────────▼──────────────────────┐
│   SQLite Database (portfolio.db)    │
│   - 6 Tabelas relacionadas          │
│   - Integridade referencial         │
└─────────────────────────────────────┘
```

---

## 📁 Arquivos e Suas Responsabilidades

### Core Application
| Arquivo | Descrição | Linhas |
|---------|-----------|--------|
| **app.py** | Aplicação principal Streamlit com todas as páginas | ~600 |
| **database.py** | Classe Database com todos CRUD operations | ~350 |

### Configuração
| Arquivo | Descrição | Linhas |
|---------|-----------|--------|
| **assets/config.py** | Configurações, cores, CSS customizado | ~70 |
| **assets/utils.py** | Funções utilitárias (upload, formatação) | ~80 |
| **.streamlit/config.toml** | Configurações do Streamlit (tema, etc) | ~15 |

### Inicialização
| Arquivo | Descrição | Linhas |
|---------|-----------|--------|
| **init_sample_data.py** | Script para popular banco com dados de teste | ~120 |
| **requirements.txt** | Dependências Python | ~2 |

### Documentação
| Arquivo | Descrição |
|---------|-----------|
| **README.md** | Documentação completa e guia de uso |
| **GUIA_RAPIDO.md** | Quick start guide |
| **DOCUMENTACAO_TECNICA.md** | Este arquivo |

### Diretórios
| Diretório | Propósito |
|-----------|----------|
| **data/** | Armazena BD e uploads |
| **data/certificados/** | Imagens e PDFs dos certificados |
| **data/curriculo/** | Arquivo PDF do currículo |
| **.streamlit/** | Configurações do Streamlit |
| **pages/** | (Estrutura para sub-páginas futuras) |

---

## 🗄️ Schema do Banco de Dados

### Tabela: curriculum
```sql
CREATE TABLE curriculum (
    id INTEGER PRIMARY KEY,
    nome TEXT NOT NULL,
    email TEXT NOT NULL,
    telefone TEXT,
    profissao TEXT NOT NULL,
    sobre TEXT,
    resumo TEXT,
    arquivo_path TEXT,
    data_criacao TIMESTAMP,
    data_atualizacao TIMESTAMP
)
```

### Tabela: experiencia
```sql
CREATE TABLE experiencia (
    id INTEGER PRIMARY KEY,
    curriculum_id INTEGER FOREIGN KEY,
    titulo TEXT NOT NULL,
    empresa TEXT NOT NULL,
    descricao TEXT,
    data_inicio DATE,
    data_fim DATE,
    ativo BOOLEAN DEFAULT 1
)
```

### Tabela: educacao
```sql
CREATE TABLE educacao (
    id INTEGER PRIMARY KEY,
    curriculum_id INTEGER FOREIGN KEY,
    titulo TEXT NOT NULL,
    instituicao TEXT NOT NULL,
    data_inicio DATE,
    data_conclusao DATE,
    descricao TEXT
)
```

### Tabela: certificados ⭐
```sql
CREATE TABLE certificados (
    id INTEGER PRIMARY KEY,
    curriculum_id INTEGER FOREIGN KEY,
    titulo TEXT NOT NULL,
    issuer TEXT,
    data_obtencao DATE,
    validade_fim DATE,
    arquivo_path TEXT NOT NULL,
    tipo_arquivo TEXT,
    descricao TEXT,
    url_certificado TEXT
)
```

### Tabela: habilidades
```sql
CREATE TABLE habilidades (
    id INTEGER PRIMARY KEY,
    curriculum_id INTEGER FOREIGN KEY,
    categoria TEXT NOT NULL,
    nome_habilidade TEXT NOT NULL,
    nivel INTEGER (1-5)
)
```

### Tabela: links_sociais
```sql
CREATE TABLE links_sociais (
    id INTEGER PRIMARY KEY,
    curriculum_id INTEGER FOREIGN KEY,
    plataforma TEXT NOT NULL,
    url TEXT NOT NULL,
    ativo BOOLEAN DEFAULT 1
)
```

---

## 🔄 Fluxo de Dados

```
User Interface (Streamlit)
         │
         ├─ Input: Forms (texto, upload, datas)
         │
         ▼
   Session State (Streamlit)
         │
         ├─ Armazena instância do Database
         │
         ▼
   Database Class (database.py)
         │
         ├─ Valida dados
         ├─ Executa queries SQL
         │
         ▼
   SQLite Database
         │
         ├─ Persiste dados
         ├─ Garante integridade
         │
         ▼
   File System
         │
         ├─ Armazena certificados
         ├─ Armazena currículo
```

---

## 🎨 Componentes Streamlit Utilizados

### Widgets
```python
# Navegação
st.radio()          # Menu principal
st.tabs()           # Abas de administração

# Entrada de dados
st.text_input()     # Nome, email, etc
st.text_area()      # Bio, descrições
st.date_input()     # Datas
st.file_uploader()  # Certificados e CV

# Seleção
st.selectbox()      # Categorias

# Controles
st.slider()         # Slider de certificados ⭐
st.button()         # Ações

# Feedback
st.success()        # Mensagens de sucesso
st.error()          # Erros
st.warning()        # Avisos
st.info()           # Informações

# Layout
st.columns()        # Grid system
st.expander()       # Conteúdo expansível
st.markdown()       # Texto formatado
st.metric()         # Estatísticas
```

### Funcionalidades Avançadas
```python
st.session_state    # Persistência entre reruns
st.form()           # Formulários com submit
st.image()          # Exibir imagens
st.download_button()# Download de arquivos
st.markdown()       # HTML customizado com CSS
```

---

## 🔐 Segurança

### Implementado
- ✅ Validação de tipos de arquivo
- ✅ Sanitização de paths
- ✅ Proteção contra SQL Injection (prepared statements)
- ✅ Isolamento de dados por currículo

### Recomendações para Produção
- 🔒 Adicionar autenticação (Streamlit Auth ou similar)
- 🔒 Usar environment variables para dados sensíveis
- 🔒 Implementar rate limiting
- 🔒 Usar HTTPS
- 🔒 Backup automático do banco
- 🔒 Validação mais rigorosa de uploads

---

## 📊 Performance

### Otimizações Implementadas
- ✅ Queries com LIMIT para paginação
- ✅ Índices automáticos em PKs e FKs
- ✅ Session state para evitar reconexões
- ✅ Lazy loading de certificados com slider

### Escalabilidade
- SQLite: Até ~100k registros (suficiente para 1 pessoa)
- Para múltiplos usuários → migrar para PostgreSQL
- Cache Streamlit nativo para static content

---

## 🚀 Recursos Especiais

### Slider de Certificados ⭐
```python
slider_value = st.slider(...)  # Indice
current_cert = certificados[slider_value]  # Item selecionado
# Display dinâmico baseado em tipo de arquivo
```

### Upload Seguro
```python
class FileManager:
    - Cria timestamp único
    - Organiza em diretórios
    - Rastreia path no BD
    - Permite deleção com limpeza
```

### Banco Robusto
```python
class Database:
    - Context manager (__enter__/__exit__)
    - Validação de entrada
    - Transações automáticas
    - Recuperação de erros
```

---

## 📦 Dependências

```
streamlit==1.40.0       # Framework web
  └─ altair
  └─ pandas
  └─ pyarrow
  └─ plotly (opcional)

pillow==10.0.0         # Processamento de imagens
  └─ scipy (opcional)

sqlite3                # Incluído no Python
```

**Tamanho total**: ~150MB (com venv)

---

## 🔧 Extensões Possíveis

### Features Futuras
- [ ] Autenticação de múltiplos usuários
- [ ] Integração com LinkedIn
- [ ] Template de currículo em PDF
- [ ] Análise de visitas com analytics
- [ ] Dark mode
- [ ] Internacionalização (i18n)
- [ ] Busca full-text
- [ ] Versioning de currículo

### Integrações
- [ ] GitHub API (buscar repositórios)
- [ ] Cloudinary (upload de imagens)
- [ ] SendGrid (notificações por email)
- [ ] Google Analytics
- [ ] Stripe (para versão premium)

---

## 📈 Métricas do Projeto

| Métrica | Valor |
|---------|-------|
| Linhas de Código | ~1500 |
| Arquivos Python | 5 |
| Tabelas BD | 6 |
| Páginas Streamlit | 4 |
| Funcionalidades | 20+ |
| Tempo Desenvolvimento | ~4-5 horas |

---

## 🧪 Testes Recomendados

```python
# Testes unitários
test_database.py
test_utils.py

# Testes de integração
test_streamlit_pages.py

# Testes de carga
benchmark_slider.py
```

---

## 📝 Convenções de Código

### Nomenclatura
```python
# Classes: PascalCase
class Database:
    pass

# Funções/métodos: snake_case
def get_curriculum():
    pass

# Constantes: UPPER_SNAKE_CASE
MAX_FILE_SIZE = 50 * 1024 * 1024

# Private: _leading_underscore
def _validate_email():
    pass
```

### Docstrings
```python
def add_certificado(self, curriculum_id: int, titulo: str) -> int:
    """
    Adiciona um novo certificado
    
    Args:
        curriculum_id: ID do currículo
        titulo: Título do certificado
    
    Returns:
        ID do certificado criado
    """
```

---

## 🤝 Padrões de Design

### Padrão: Singleton (Session State)
```python
if "db" not in st.session_state:
    st.session_state.db = Database()
```

### Padrão: Context Manager
```python
with Database() as db:
    certificados = db.get_certificados(1)
```

### Padrão: Factory (File Manager)
```python
file_path = FileManager.save_upload_file(uploaded_file, dest)
```

---

## 📚 Referências

- [Streamlit Docs](https://docs.streamlit.io)
- [SQLite Tutorial](https://www.sqlite.org/docs.html)
- [Python Best Practices](https://pep8.org)
- [Streamlit Cloud Deploy](https://share.streamlit.io)

---

**Desenvolvido com ❤️ seguindo as melhores práticas de engenharia de software**
