"""
Arquivo de configurações da aplicação Streamlit
"""

import streamlit as st
from pathlib import Path

# Configurações gerais
APP_TITLE = "Meu Portfólio Profissional"
APP_DESCRIPTION = "Portal para visualizar currículo, certificados e experiências profissionais"

# Caminhos
DATA_DIR = Path("data")
CURRICULO_DIR = DATA_DIR / "curriculo"
CERTIFICADOS_DIR = DATA_DIR / "certificados"
DB_PATH = DATA_DIR / "portfolio.db"

# Criar diretórios se não existirem
DATA_DIR.mkdir(exist_ok=True)
CURRICULO_DIR.mkdir(exist_ok=True)
CERTIFICADOS_DIR.mkdir(exist_ok=True)

# Configurações de upload
MAX_FILE_SIZE = 50 * 1024 * 1024  # 50 MB
ALLOWED_FILE_TYPES = {
    "certificados": ["png", "jpg", "jpeg", "pdf", "gif"],
    "curriculo": ["pdf", "doc", "docx"]
}

# Temas e cores - Cada tema com cor específica
COLORS = {
    "certificado": "#9b59b6",  # Roxo - Certificado genérico
    "certificação": "#e74c3c",  # Vermelho - Certificação profissional
    "diploma": "#27ae60",       # Verde escuro - Diploma acadêmico
    "curso": "#3498db",         # Azul - Cursos de formação
    "extensão": "#f39c12"       # Laranja - Cursos de extensão
}

# Configurar página Streamlit
def configure_page():
    st.set_page_config(
        page_title=APP_TITLE,
        page_icon="👨‍💼",
        layout="wide",
        initial_sidebar_state="expanded",
        menu_items={
            "About": "Portfólio Profissional criado com Streamlit e SQLite"
        }
    )
    
    # CSS customizado
    st.markdown("""
    <style>
    :root {
        --primary-color: #0066cc;
        --secondary-color: #00d4ff;
        --success-color: #00cc44;
        --danger-color: #ff3333;
    }
    
    .main {
        padding: 2rem;
    }
    
    .metric-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 1.5rem;
        border-radius: 10px;
        color: white;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    
    .certificado-card {
        border: 1px solid #e0e0e0;
        border-radius: 8px;
        padding: 1rem;
        margin: 0.5rem 0;
        transition: all 0.3s ease;
    }
    
    .certificado-card:hover {
        box-shadow: 0 4px 12px rgba(0,0,0,0.15);
        border-color: #0066cc;
    }
    
    .skill-badge {
        display: inline-block;
        background: #e3f2fd;
        color: #0066cc;
        padding: 0.5rem 1rem;
        border-radius: 20px;
        margin: 0.25rem;
        font-size: 0.9rem;
    }
    </style>
    """, unsafe_allow_html=True)
