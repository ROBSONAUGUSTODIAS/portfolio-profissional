# 🔧 TROUBLESHOOTING & DICAS AVANÇADAS

## ❌ Problemas Comuns e Soluções

### 1. "ModuleNotFoundError: No module named 'streamlit'"

**Causa:** Dependências não instaladas

**Solução:**
```bash
pip install -r requirements.txt
```

---

### 2. Erro ao acessar localhost:8501

**Causa:** Porta já em uso ou Streamlit não iniciou

**Solução:**
```bash
# Usar porta diferente
streamlit run app.py --server.port 8502

# Ou matar processo na porta 8501 (Windows)
netstat -ano | findstr :8501
taskkill /PID <PID> /F
```

---

### 3. Certificados não aparecem no slider

**Causa:** 
- Arquivo não existe
- Path incorreto salvo no BD
- Tipo de arquivo não permitido

**Solução:**
```bash
# Verificar conteúdo de data/certificados/
dir data\certificados\

# Tipos permitidos: .png, .jpg, .jpeg, .pdf, .gif
```

---

### 4. "database.db is locked"

**Causa:** Múltiplas conexões simultâneas

**Solução:**
```python
# Close database antes de usar novamente
if "db" in st.session_state:
    st.session_state.db.close()
    del st.session_state["db"]

# Ou: Usar WAL mode (já implementado)
```

---

### 5. Aplicação muito lenta

**Causa:** 
- Muitos certificados
- Session state bloated
- Queries ineficientes

**Solução:**
```python
# Limpar cache periodicamente
st.cache_data.clear()

# Usar st.session_state para persistência
# Limite queries com LIMIT e OFFSET
```

---

### 6. Upload de arquivo falha silenciosamente

**Causa:** 
- Arquivo muito grande
- Sem permissão de escrita
- Path inválido

**Solução:**
```python
# Aumentar limite de upload (em app.py)
st.file_uploader(..., key="cert_upload")

# Verificar permissões de diretório
# Usar try-except no FileManager
```

---

## 🚀 Dicas de Performance

### Otimizar Queries
```python
# ❌ Ruim: Sem limite
SELECT * FROM certificados

# ✅ Bom: Com paginação
SELECT * FROM certificados LIMIT 50 OFFSET 0
```

### Cache de Dados
```python
# ✅ Adicionar caching
@st.cache_data(ttl=3600)  # Cache por 1 hora
def get_certificados_cached(curriculum_id):
    return db.get_certificados(curriculum_id)
```

### Lazy Loading
```python
# ✅ Slider já implementa lazy loading
# Só carrega certificado quando selecionado
current_cert = certificados[slider_value]
```

---

## 🔐 Segurança Avançada

### Autenticação (Adicionar)
```python
# Instalar: pip install streamlit-authenticator
import streamlit_authenticator as stauth

# Implementar no início de app.py
authenticated = authenticator.login()
if not authenticated:
    st.stop()
```

### Validação de Upload
```python
# Melhorar validação
ALLOWED_EXTENSIONS = {'pdf', 'png', 'jpg', 'jpeg'}
ALLOWED_MIMETYPES = {'image/png', 'image/jpeg', 'application/pdf'}
MAX_FILE_SIZE = 5 * 1024 * 1024  # 5MB

if uploaded_file.size > MAX_FILE_SIZE:
    st.error(f"Arquivo muito grande (máx: 5MB)")
```

### Sanitização de Path
```python
# Evitar path traversal
from pathlib import Path
safe_path = (Path("data") / filename).resolve()
if not str(safe_path).startswith(str(Path("data").resolve())):
    raise ValueError("Path inválido")
```

---

## 📊 Monitoramento e Logging

### Adicionar Logs
```python
# Criar logging.py
import logging

logger = logging.getLogger(__name__)
logger.info(f"Certificado {cert_id} visualizado")
logger.error(f"Falha ao carregar {file_path}")
```

### Health Check
```python
@st.cache_resource
def check_database_health():
    try:
        db = Database()
        curriculum = db.get_curriculum()
        db.close()
        return True
    except Exception as e:
        logger.error(f"Database error: {e}")
        return False
```

---

## 🔄 Backup e Recuperação

### Backup Manual
```bash
# Windows
copy data\portfolio.db data\portfolio_backup_$(date).db

# Linux/Mac
cp data/portfolio.db data/portfolio_backup_$(date +%Y%m%d_%H%M%S).db
```

### Backup Automático
```python
# Adicionar em init do app
def auto_backup_database():
    if not os.path.exists("data/backups"):
        os.makedirs("data/backups")
    
    shutil.copy(
        "data/portfolio.db",
        f"data/backups/portfolio_backup_{datetime.now().timestamp()}.db"
    )
```

### Restaurar Backup
```bash
# Substituir arquivo atual
copy data\portfolio_backup_TIMESTAMP.db data\portfolio.db
```

---

## 🎨 Customização Avançada

### Mudar Tema Completo
```python
# Em assets/config.py

st.markdown("""
<style>
:root {
    --primary: #FF6B6B;
    --secondary: #4ECDC4;
}

.stApp {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
}
</style>
""", unsafe_allow_html=True)
```

### Adicionar Favicon Customizado
```python
# Em .streamlit/config.toml
[browser]
faviconUrl = "https://seu-url/favicon.ico"
```

### Multi-página Avançada
```python
# Usar st.navigation() (Streamlit 1.38+)
pages = {
    "Home": "pages/home.py",
    "Currículo": "pages/curriculum.py",
    "Certificados": "pages/certificados.py",
}
```

---

## 🧪 Testes Básicos

### Teste de Conexão ao Banco
```python
# test_database.py
from database import Database

def test_database_creation():
    db = Database("test.db")
    curriculum_id = db.create_curriculum(
        "Test", "test@test.com", "Developer"
    )
    assert curriculum_id > 0
    db.close()
```

### Teste de Upload
```python
# test_utils.py
from assets.utils import FileManager

def test_file_size():
    size = FileManager.get_file_size("data/portfolio.db")
    assert size > 0
```

---

## 📱 Deploy na Nuvem

### Streamlit Cloud (Recomendado)
```bash
# 1. Push para GitHub
git init
git add .
git commit -m "Initial commit"
git push origin main

# 2. Ir em https://share.streamlit.io
# 3. Conectar repositório GitHub
# 4. Deploy automático
```

### Heroku
```bash
# 1. Criar Procfile
echo "web: streamlit run app.py --logger.level=error" > Procfile

# 2. Deploy
heroku login
heroku create seu-app-name
git push heroku main
```

### Docker
```dockerfile
FROM python:3.11-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .

CMD ["streamlit", "run", "app.py"]
```

```bash
# Build e run
docker build -t portifolio .
docker run -p 8501:8501 portifolio
```

---

## 🔄 Migração de Dados

### Exportar para JSON
```python
import json

def export_to_json(curriculum_id):
    db = Database()
    curriculum = dict(db.get_curriculum())
    experiencias = [dict(e) for e in db.get_experiencias(curriculum_id)]
    
    with open("export.json", "w") as f:
        json.dump({
            "curriculum": curriculum,
            "experiencias": experiencias
        }, f, indent=2, default=str)
```

### Migrar para PostgreSQL
```python
# Usar SQLAlchemy para abstração
from sqlalchemy import create_engine

engine = create_engine('postgresql://user:pass@localhost/portfolio')
# Migrar com Alembic
```

---

## 📞 Suporte

### Documentação
- [Streamlit Docs](https://docs.streamlit.io)
- [SQLite Docs](https://www.sqlite.org)
- [Python Docs](https://docs.python.org)

### Comunidade
- Streamlit Discord: https://discord.gg/streamlit
- Stack Overflow: tag `streamlit`
- GitHub Issues: https://github.com/streamlit/streamlit/issues

---

## ✅ Checklist Pré-Deploy

- [ ] Testar localmente
- [ ] Remover dados de teste (ou deixar)
- [ ] Verificar links das redes sociais
- [ ] Testar upload de certificados
- [ ] Verificar responsividade mobile
- [ ] Adicionar autenticação (se necessário)
- [ ] Configurar backups automáticos
- [ ] Testar em diferentes navegadores
- [ ] Documentar credenciais (se houver)
- [ ] Deploy em staging primeiro

---

**Problema não encontrado? Verifique logs em `.streamlit/` e console**
