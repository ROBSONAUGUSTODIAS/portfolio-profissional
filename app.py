"""
Aplicação Principal - Portfólio Profissional com Streamlit
"""

import streamlit as st
from pathlib import Path
import sys
import datetime

# Adicionar pasta de assets ao path
sys.path.insert(0, str(Path(__file__).parent / "assets"))

from config import configure_page, APP_TITLE, APP_DESCRIPTION, DB_PATH, COLORS
from utils import PDFGenerator, AuthManager
from assets.auth_config import verify_credentials

# Importar database da raiz
import database
from database import Database

# Configurar página
configure_page()

# Função para inicializar banco de dados com dados de exemplo
def initialize_database_if_empty():
    """Inicializa o banco de dados com dados de Robson se estiver vazio"""
    db = Database(str(DB_PATH))
    curriculum = db.get_curriculum()
    
    # Se não houver currículo, criar dados
    if not curriculum:
        try:
            from init_robson_data import init_robson_data
            init_robson_data()
        except Exception as e:
            # Se falhar, tentar dados de exemplo
            try:
                from init_sample_data import init_sample_data
                init_sample_data()
            except:
                pass

# Inicializar banco de dados
initialize_database_if_empty()

# Inicializar session state
if "db" not in st.session_state:
    st.session_state.db = Database(str(DB_PATH))

if "current_user" not in st.session_state:
    st.session_state.current_user = None

def main():
    """Função principal da aplicação"""
    
    # Sidebar com navegação
    with st.sidebar:
        st.title("📋 Portfólio")
        st.markdown("---")
        
        # Verificar se tem currículo criado
        db = st.session_state.db
        curriculum = db.get_curriculum()
        
        if curriculum:
            st.markdown(f"### 👤 {curriculum['nome']}")
            st.markdown(f"**{curriculum['profissao']}**")
            st.markdown("---")
        
        # Menu de navegação
        page = st.radio(
            "Navegação",
            ["🏠 Início", "📄 Currículo", "🏆 Certificados", "⚙️ Administração"],
            label_visibility="collapsed"
        )
        
        st.markdown("---")
        st.markdown("**Desenvolvido com:**  \n🐍 Python • 🌀 Streamlit • 🗄️ SQLite")
    
    # Roteamento de páginas
    if page == "🏠 Início":
        show_home()
    elif page == "📄 Currículo":
        show_curriculum()
    elif page == "🏆 Certificados":
        show_certificados()
    elif page == "⚙️ Administração":
        show_admin()

def show_home():
    """Página inicial"""
    st.title(f"🎯 {APP_TITLE}")
    st.markdown(APP_DESCRIPTION)
    st.markdown("---")
    
    db = st.session_state.db
    curriculum = db.get_curriculum()
    
    if curriculum:
        # Seção de boas-vindas
        col1, col2 = st.columns([2, 1])
        
        with col1:
            st.markdown(f"## Olá! Eu sou **{curriculum['nome']}**")
            st.markdown(f"### {curriculum['profissao']}")
            
            if curriculum['sobre']:
                st.markdown(f"**{curriculum['sobre'][:200]}...**" if len(curriculum['sobre']) > 200 else f"**{curriculum['sobre']}**")
            
            if curriculum['resumo']:
                with st.expander("📖 Sobre mim"):
                    st.markdown(curriculum['resumo'])
        
        st.markdown("---")
        
        # Cards de estatísticas
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            experiencias = db.get_experiencias(curriculum['id'])
            st.metric("📌 Experiências", len(experiencias))
        
        with col2:
            educacao = db.get_educacao(curriculum['id'])
            st.metric("🎓 Formações", len(educacao))
        
        with col3:
            certificados = db.get_certificados(curriculum['id'])
            st.metric("🏆 Certificados", len(certificados))
        
        with col4:
            habilidades = db.get_habilidades(curriculum['id'])
            st.metric("⭐ Habilidades", len(habilidades))
        
        st.markdown("---")
        
        # Redes Sociais
        links = db.get_links_sociais(curriculum['id'])
        if links:
            st.subheader("🔗 Conecte-se")
            
            # Mapeamento de plataformas para ícones e cores
            platform_icons = {
                'linkedin': {'icon': '💼', 'color': '#0A66C2', 'name': 'LinkedIn'},
                'github': {'icon': '💻', 'color': '#181717', 'name': 'GitHub'},
                'portfolio': {'icon': '🌐', 'color': '#FF6B6B', 'name': 'Portal Slider Antigo'},
                'portfólio': {'icon': '🌐', 'color': '#FF6B6B', 'name': 'Portal Slider Antigo'},
                'email': {'icon': '📧', 'color': '#EA4335', 'name': 'Email'},
                'twitter': {'icon': '🐦', 'color': '#1DA1F2', 'name': 'Twitter'},
                'instagram': {'icon': '📷', 'color': '#E4405F', 'name': 'Instagram'},
                'youtube': {'icon': '🎥', 'color': '#FF0000', 'name': 'YouTube'},
                'facebook': {'icon': '👥', 'color': '#1877F2', 'name': 'Facebook'},
                'whatsapp': {'icon': '💬', 'color': '#25D366', 'name': 'WhatsApp'},
                'telegram': {'icon': '✈️', 'color': '#0088cc', 'name': 'Telegram'},
                'website': {'icon': '🌍', 'color': '#4CAF50', 'name': 'Website'},
                'site': {'icon': '🌍', 'color': '#4CAF50', 'name': 'Site'},
            }
            
            # Usar abordagem nativa do Streamlit com colunas
            num_links = len(links)
            cols_per_row = min(6, num_links)  # Máximo 6 ícones por linha
            
            # Criar linhas de colunas conforme necessário
            for i in range(0, num_links, cols_per_row):
                chunk = links[i:i + cols_per_row]
                cols = st.columns(len(chunk))
                
                for col, link in zip(cols, chunk):
                    with col:
                        platform_key = link['plataforma'].lower()
                        platform_info = platform_icons.get(platform_key, {
                            'icon': '🔗', 
                            'color': '#666666', 
                            'name': link['plataforma']
                        })
                        
                        url = link['url']
                        # Adicionar mailto: se for email e não tiver
                        if platform_key == 'email' and '@' in url and not url.startswith('mailto:'):
                            url = f"mailto:{url}"
                        
                        # Criar botão personalizado com HTML
                        button_html = f'''
                        <div style="text-align: center; margin: 10px 0;">
                            <a href="{url}" target="_blank" style="text-decoration: none;">
                                <div style="
                                    display: inline-flex;
                                    align-items: center;
                                    justify-content: center;
                                    width: 70px;
                                    height: 70px;
                                    border-radius: 50%;
                                    background: linear-gradient(135deg, {platform_info['color']}, {platform_info['color']}dd);
                                    box-shadow: 0 4px 6px rgba(0,0,0,0.1);
                                    transition: all 0.3s ease;
                                    cursor: pointer;
                                    font-size: 32px;
                                " onmouseover="this.style.transform='translateY(-5px) scale(1.05)'; this.style.boxShadow='0 8px 15px rgba(0,0,0,0.2)';" 
                                   onmouseout="this.style.transform='translateY(0) scale(1)'; this.style.boxShadow='0 4px 6px rgba(0,0,0,0.1)';">
                                    {platform_info['icon']}
                                </div>
                            </a>
                            <div style="
                                margin-top: 8px;
                                font-size: 13px;
                                font-weight: 500;
                                color: #555;
                            ">{platform_info['name']}</div>
                        </div>
                        '''
                        st.markdown(button_html, unsafe_allow_html=True)
    
    else:
        st.info("⚠️ Nenhum currículo foi criado ainda. Acesse a seção de Administração para começar!")

def show_curriculum():
    """Página do currículo"""
    st.title("📄 Meu Currículo")
    
    db = st.session_state.db
    curriculum = db.get_curriculum()
    
    if not curriculum:
        st.warning("⚠️ Nenhum currículo cadastrado")
        return
    
    # Header do currículo
    st.markdown(f"# {curriculum['nome']}")
    st.markdown(f"### {curriculum['profissao']}")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown(f"📧 **Email:** {curriculum['email']}")
    if curriculum['telefone']:
        with col2:
            st.markdown(f"📱 **Telefone:** {curriculum['telefone']}")
    
    st.markdown("---")
    
    # Sobre
    if curriculum['sobre']:
        st.subheader("👤 Sobre")
        st.markdown(curriculum['sobre'])
        st.markdown("---")
    
    # Experiência Profissional
    experiencias = db.get_experiencias(curriculum['id'])
    if experiencias:
        st.subheader("💼 Experiência Profissional")
        for exp in experiencias:
            with st.expander(f"**{exp['titulo']}** - {exp['empresa']}"):
                if exp['descricao']:
                    st.markdown(exp['descricao'])
                col1, col2 = st.columns(2)
                with col1:
                    st.markdown(f"**Data Início:** {exp['data_inicio']}")
                with col2:
                    st.markdown(f"**Data Fim:** {exp['data_fim']}" if exp['data_fim'] else "**Presente**")
        st.markdown("---")
    
    # Educação
    educacao = db.get_educacao(curriculum['id'])
    if educacao:
        st.subheader("🎓 Educação e Cursos")
        for edu in educacao:
            with st.expander(f"**{edu['titulo']}** - {edu['instituicao']}"):
                if edu['descricao']:
                    st.markdown(edu['descricao'])
                st.markdown(f"**Conclusão:** {edu['data_conclusao']}" if edu['data_conclusao'] else "")
        st.markdown("---")
    
    # Habilidades
    habilidades = db.get_habilidades(curriculum['id'])
    if habilidades:
        st.subheader("⭐ Habilidades")
        
        # Agrupar por categoria
        categorias = {}
        for hab in habilidades:
            cat = hab['categoria']
            if cat not in categorias:
                categorias[cat] = []
            categorias[cat].append(hab)
        
        # Exibir cada categoria
        for categoria, habs in categorias.items():
            with st.expander(f"**{categoria}** ({len(habs)} habilidades)", expanded=True):
                # Organizar em colunas de 3
                num_cols = 3
                for i in range(0, len(habs), num_cols):
                    cols = st.columns(num_cols)
                    chunk = habs[i:i + num_cols]
                    
                    for col, hab in zip(cols, chunk):
                        with col:
                            # Nome da habilidade com estrelas
                            stars = "⭐" * hab['nivel']
                            st.markdown(f"**{hab['nome_habilidade']}**")
                            st.caption(f"{stars} ({hab['nivel']}/5)")
                            st.progress(hab['nivel'] / 5)
    
    # Seção de Download
    st.markdown("---")
    st.subheader("📥 Download do Currículo")
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Botão para gerar e baixar PDF dinâmico
        experiencias = db.get_experiencias(curriculum['id'])
        educacao = db.get_educacao(curriculum['id'])
        habilidades = db.get_habilidades(curriculum['id'])
        links_sociais = db.get_links_sociais(curriculum['id'])
        
        try:
            pdf_bytes = PDFGenerator.generate_curriculum_pdf(
                curriculum,
                experiencias,
                educacao,
                habilidades,
                links_sociais
            )
            
            st.download_button(
                label="📄 Baixar Currículo (PDF Gerado)",
                data=pdf_bytes,
                file_name=f"{curriculum['nome']}_curriculo.pdf",
                mime="application/pdf",
                key="download_pdf_generated"
            )
        except Exception as e:
            st.error(f"⚠️ Erro ao gerar PDF: {str(e)}")
    
    # Se houver arquivo enviado, mostrar opção de download também
    if curriculum['arquivo_path']:
        with col2:
            try:
                with open(curriculum['arquivo_path'], 'rb') as pdf_file:
                    st.download_button(
                        label="📄 Baixar Currículo (Arquivo Original)",
                        data=pdf_file,
                        file_name=f"{curriculum['nome']}_curriculo_original.pdf",
                        mime="application/pdf",
                        key="download_pdf_original"
                    )
            except FileNotFoundError:
                st.warning("⚠️ Arquivo original não encontrado")

def show_certificados():
    """Página de certificados com slider"""
    st.title("🏆 Meus Certificados")
    
    db = st.session_state.db
    curriculum = db.get_curriculum()
    
    if not curriculum:
        st.warning("⚠️ Nenhum currículo cadastrado")
        return
    
    certificados = db.get_certificados(curriculum['id'])
    
    # Verificação robusta para lista vazia
    if certificados is None or len(certificados) == 0:
        st.info("📌 Nenhum certificado cadastrado ainda.")
        return
    
    num_certs = len(certificados)
    
    # Guard duplo para garantir que não chegamos ao slider com dados inválidos
    if num_certs < 1:
        st.warning("⚠️ Erro ao carregar certificados")
        return
    
    st.markdown(f"**Total de Certificados:** {num_certs}")
    st.markdown("---")
    
    # Slider de certificados - apenas se houver mais de 1
    # Se o usuário clicou em 'Ver', usar essa seleção como valor inicial do slider
    selected = st.session_state.get('selected_cert', None)
    if num_certs > 1:
        default_idx = selected if (selected is not None and 0 <= selected < num_certs) else 0
        
        st.write("**Navegue pelos certificados:**")
        # Usar slider nativo do Streamlit
        slider_value = st.slider(
            label="",
            min_value=1,
            max_value=num_certs,
            value=default_idx + 1,
            step=1,
            key="cert_slider",
            label_visibility="collapsed"
        )
        # Ajustar para índice base 0 para acessar a lista
        slider_value = slider_value - 1
    else:
        slider_value = selected if (selected is not None and 0 <= selected < num_certs) else 0
        st.markdown("**Certificado 1 de 1**")

    # Limpar seleção após uso para evitar comportamento indesejado em próximas interações
    if 'selected_cert' in st.session_state:
        del st.session_state['selected_cert']

    current_cert = certificados[slider_value]
    
    # Exibir certificado atual
    col1, col2 = st.columns([2, 1])
    
    with col1:
        # Exibir imagem ou PDF - normalizar caminho para compatibilidade Windows/Linux
        if current_cert['arquivo_path']:
            # Normalizar caminho: substituir \ por / para compatibilidade
            arquivo_normalizado = current_cert['arquivo_path'].replace('\\', '/')
            
            if Path(arquivo_normalizado).exists():
                file_ext = Path(arquivo_normalizado).suffix.lower()
                
                if file_ext in ['.png', '.jpg', '.jpeg', '.gif']:
                    st.image(arquivo_normalizado, use_container_width=True)
                elif file_ext == '.pdf':
                    st.info("📄 Documento PDF - disponível para download")
            else:
                st.warning(f"⚠️ Arquivo não encontrado: {arquivo_normalizado}")
    
    with col2:
        tema = current_cert['tema'] if 'tema' in current_cert.keys() and current_cert['tema'] else 'certificado'
        color = COLORS.get(tema, COLORS['certificado'])
        st.markdown(f"<span style='background:{color};color:white;padding:4px 8px;border-radius:6px'>{tema.capitalize()}</span>", unsafe_allow_html=True)
        st.markdown(f"### {current_cert['titulo']}")
        st.markdown("---")
        
        if current_cert['issuer']:
            st.markdown(f"**Emissor:** {current_cert['issuer']}")
        
        if current_cert['data_obtencao']:
            st.markdown(f"**Data de Obtenção:** {current_cert['data_obtencao']}")
        
        if current_cert['validade_fim']:
            st.markdown(f"**Válido até:** {current_cert['validade_fim']}")
        
        if current_cert['descricao']:
            st.markdown(f"**Descrição:** {current_cert['descricao']}")
        
        if current_cert['url_certificado']:
            st.markdown(f"[🔗 Verificar Certificado]({current_cert['url_certificado']})")
    
    st.markdown("---")
    
    # Informações adicionais
    st.markdown(f"**Certificado {slider_value + 1} de {len(certificados)}**")
    
    # Exibir todos os certificados em cards
    st.markdown("### 📋 Todos os Certificados")
    
    for idx, cert in enumerate(certificados):
        tema = cert['tema'] if 'tema' in cert.keys() and cert['tema'] else 'certificado'
        color = COLORS.get(tema, COLORS['certificado'])
        issuer_html = f"<br><small>_Emissor: {cert['issuer']}_</small>" if cert['issuer'] else ""
        st.markdown(f"{idx + 1}. {cert['titulo']} <span style='background:{color};color:white;padding:2px 8px;border-radius:6px'>{tema.capitalize()}</span>{issuer_html}", unsafe_allow_html=True)

def show_admin():
    """Página de administração"""
    # Verificar autenticação
    if not AuthManager.check_admin_access():
        AuthManager.show_login_form()
        return
    
    # Se chegou aqui, está autenticado
    AuthManager.show_admin_header()
    
    st.title("⚙️ Painel Administrativo")
    
    db = st.session_state.db
    
    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
        "👤 Perfil",
        "💼 Experiência",
        "🎓 Educação",
        "🏆 Certificados",
        "⭐ Habilidades",
        "🔗 Redes Sociais"
    ])
    
    # Tab 1: Perfil
    with tab1:
        st.subheader("Informações Pessoais")
        curriculum = db.get_curriculum()
        
        if curriculum:
            st.info(f"✅ Currículo de {curriculum['nome']} carregado")
            
            with st.form("form_curriculum"):
                nome = st.text_input("Nome", value=curriculum['nome'])
                email = st.text_input("Email", value=curriculum['email'])
                profissao = st.text_input("Profissão", value=curriculum['profissao'])
                telefone = st.text_input("Telefone", value=curriculum['telefone'] or "")
                sobre = st.text_area("Sobre", value=curriculum['sobre'] or "", height=100)
                resumo = st.text_area("Resumo/Bio", value=curriculum['resumo'] or "", height=150)
                
                arquivo = st.file_uploader("Curriculum (PDF)", type=['pdf'])
                
                if st.form_submit_button("💾 Atualizar"):
                    db.update_curriculum(
                        curriculum['id'],
                        nome=nome,
                        email=email,
                        profissao=profissao,
                        telefone=telefone,
                        sobre=sobre,
                        resumo=resumo
                    )
                    st.success("✅ Perfil atualizado!")
        else:
            st.warning("⚠️ Criar novo perfil")
            with st.form("form_novo_curriculum"):
                nome = st.text_input("Nome")
                email = st.text_input("Email")
                profissao = st.text_input("Profissão")
                telefone = st.text_input("Telefone")
                
                if st.form_submit_button("➕ Criar Perfil"):
                    if nome and email and profissao:
                        curriculum_id = db.create_curriculum(
                            nome, email, profissao, telefone
                        )
                        st.success(f"✅ Perfil criado com ID: {curriculum_id}")
                        st.rerun()
    
    # Tab 2: Experiência
    with tab2:
        st.subheader("Gerenciar Experiência Profissional")
        curriculum = db.get_curriculum()
        
        if curriculum:
            with st.form("form_experiencia"):
                st.markdown("**Adicionar Experiência**")
                titulo = st.text_input("Título do Cargo")
                empresa = st.text_input("Empresa")
                descricao = st.text_area("Descrição", height=150)
                col1, col2 = st.columns(2)
                with col1:
                    data_inicio = st.date_input("Data Início")
                with col2:
                    data_fim = st.date_input("Data Fim")
                
                if st.form_submit_button("➕ Adicionar Experiência"):
                    db.add_experiencia(
                        curriculum['id'],
                        titulo,
                        empresa,
                        descricao,
                        str(data_inicio),
                        str(data_fim)
                    )
                    st.success("✅ Experiência adicionada!")
                    st.rerun()
            
            st.markdown("---")
            st.markdown("**Experiências Cadastradas**")
            experiencias = db.get_experiencias(curriculum['id'])
            if experiencias:
                for exp in experiencias:
                    st.markdown(f"• **{exp['titulo']}** - {exp['empresa']}")
            else:
                st.info("Nenhuma experiência cadastrada")
        else:
            st.warning("⚠️ Crie um perfil primeiro")
    
    # Tab 3: Educação
    with tab3:
        st.subheader("Gerenciar Educação e Cursos")
        curriculum = db.get_curriculum()
        
        if curriculum:
            with st.form("form_educacao"):
                st.markdown("**Adicionar Educação**")
                titulo = st.text_input("Título do Curso/Formação")
                instituicao = st.text_input("Instituição")
                descricao = st.text_area("Descrição", height=100)
                col1, col2 = st.columns(2)
                with col1:
                    data_inicio = st.date_input("Data Início")
                with col2:
                    data_conclusao = st.date_input("Data Conclusão")
                
                if st.form_submit_button("➕ Adicionar Educação"):
                    db.add_educacao(
                        curriculum['id'],
                        titulo,
                        instituicao,
                        str(data_conclusao),
                        descricao,
                        str(data_inicio)
                    )
                    st.success("✅ Educação adicionada!")
                    st.rerun()
            
            st.markdown("---")
            st.markdown("**Educações Cadastradas**")
            educacao = db.get_educacao(curriculum['id'])
            if educacao:
                for edu in educacao:
                    st.markdown(f"• **{edu['titulo']}** - {edu['instituicao']}")
            else:
                st.info("Nenhuma educação cadastrada")
        else:
            st.warning("⚠️ Crie um perfil primeiro")
    
    # Tab 4: Certificados
    with tab4:
        st.subheader("Gerenciar Certificados")
        curriculum = db.get_curriculum()
        
        if curriculum:
            with st.form("form_certificado"):
                st.markdown("**Adicionar Certificado**")
                
                # Campo 1: Título (obrigatório)
                titulo = st.text_input("Título do Certificado", placeholder="Ex: Python Advanced Certification")
                
                # Campo 2: Emissor (importante)
                issuer = st.text_input("Emissor/Instituição", placeholder="Ex: Udemy, Coursera, Google")
                
                # Campo 3: Tema/Categoria (organização)
                tema = st.selectbox("Tema do Certificado", options=["Certificado", "Certificação", "Diploma", "Curso", "Extensão"], index=0)
                
                # Campos 4 e 5: Datas (informações temporais agrupadas)
                col1, col2 = st.columns(2)
                with col1:
                    data_obtencao = st.date_input("Data de Obtenção", min_value=datetime.date(2000, 1, 1), max_value=datetime.date(2050, 12, 31))
                with col2:
                    data_validade = st.date_input("Data de Validade (opcional)", value=None, min_value=datetime.date(2000, 1, 1), max_value=datetime.date(2050, 12, 31))
                
                # Campo 6: Descrição (detalhes adicionais)
                descricao = st.text_area("Descrição", height=100, placeholder="Descreva o conteúdo e aprendizados do certificado...")
                
                # Campo 7: URL de Verificação (opcional)
                url_certificado = st.text_input("URL de Verificação (opcional)", placeholder="https://...")
                
                # Campo 8: Upload do Arquivo (por último)
                arquivo = st.file_uploader("Upload do Certificado (Imagem ou PDF)", type=['png', 'jpg', 'jpeg', 'pdf', 'gif'])
                
                if st.form_submit_button("➕ Adicionar Certificado", use_container_width=True):
                    # Validação completa dos campos obrigatórios
                    if not titulo or not titulo.strip():
                        st.session_state.cert_message = {"type": "error", "text": "⚠️ O título do certificado é obrigatório!"}
                        st.rerun()
                    elif not arquivo:
                        st.session_state.cert_message = {"type": "error", "text": "⚠️ Selecione um arquivo de certificado (imagem ou PDF)!"}
                        st.rerun()
                    else:
                        try:
                            from assets.utils import FileManager
                            file_path = FileManager.save_upload_file(arquivo, "data/certificados")
                            
                            certificado_id = db.add_certificado(
                                curriculum['id'],
                                titulo.strip(),
                                file_path,
                                issuer.strip() if issuer else "",
                                str(data_obtencao),
                                str(data_validade) if data_validade else "",
                                descricao.strip() if descricao else "",
                                url_certificado.strip() if url_certificado else "",
                                arquivo.type,
                                tema.lower()
                            )
                            
                            # Verificar se foi adicionado com sucesso
                            if certificado_id:
                                st.session_state.cert_message = {"type": "success", "text": f"✅ Certificado '{titulo}' adicionado com sucesso!"}
                            else:
                                st.session_state.cert_message = {"type": "error", "text": "❌ Falha ao adicionar certificado no banco de dados"}
                            st.rerun()
                        except Exception as e:
                            st.session_state.cert_message = {"type": "error", "text": f"❌ Erro ao adicionar certificado: {str(e)}"}
                            st.rerun()
            
            # Exibir mensagem de feedback abaixo do formulário
            if "cert_message" in st.session_state:
                if st.session_state.cert_message["type"] == "success":
                    st.success(st.session_state.cert_message["text"])
                elif st.session_state.cert_message["type"] == "error":
                    st.error(st.session_state.cert_message["text"])
                # Limpar mensagem após exibir
                del st.session_state.cert_message
            
            st.markdown("---")
            st.markdown("**Certificados Cadastrados**")
            certificados = db.get_certificados(curriculum['id'])
            
            # Verificação robusta
            if certificados is None:
                st.warning("⚠️ Erro ao buscar certificados no banco de dados")
                certificados = []
            
            # Mostrar total de certificados
            st.caption(f"📊 Total de certificados: {len(certificados)}")
            
            if len(certificados) > 0:
                # Enumerar certificados para mostrar ordem sequencial
                for index, cert in enumerate(certificados, start=1):
                    tema = cert['tema'] if 'tema' in cert.keys() and cert['tema'] else 'certificado'
                    color = COLORS.get(tema, COLORS['certificado'])
                    issuer_html = f" - _Emissor: {cert['issuer']}_" if cert['issuer'] else ""
                    
                    # Mostrar número sequencial junto com o nome
                    with st.expander(f"**#{index} - {cert['titulo']}** {issuer_html}"):
                        # Formulário de edição
                        with st.form(key=f"form_edit_{cert['id']}"):
                            st.markdown(f"<span style='background:{color};color:white;padding:4px 12px;border-radius:6px;display:inline-block;margin-bottom:10px'>{tema.capitalize()}</span>", unsafe_allow_html=True)
                            
                            edit_titulo = st.text_input("Título do Certificado", value=cert['titulo'])
                            edit_issuer = st.text_input("Emissor/Instituição", value=cert['issuer'] if cert['issuer'] else "")
                            edit_descricao = st.text_area("Descrição", value=cert['descricao'] if cert['descricao'] else "", height=100)
                            
                            col1, col2 = st.columns(2)
                            with col1:
                                edit_data_obtencao = st.date_input("Data de Obtenção", 
                                    value=datetime.datetime.strptime(cert['data_obtencao'], "%Y-%m-%d").date() if cert['data_obtencao'] else None,
                                    min_value=datetime.date(2000, 1, 1), 
                                    max_value=datetime.date(2050, 12, 31))
                            with col2:
                                edit_data_validade = st.date_input("Data de Validade (opcional)", 
                                    value=datetime.datetime.strptime(cert['validade_fim'], "%Y-%m-%d").date() if cert['validade_fim'] else None,
                                    min_value=datetime.date(2000, 1, 1), 
                                    max_value=datetime.date(2050, 12, 31))
                            
                            edit_url_certificado = st.text_input("URL de Verificação (opcional)", value=cert['url_certificado'] if cert['url_certificado'] else "")
                            
                            # Tema do certificado
                            temas_disponiveis = ["Certificado", "Certificação", "Diploma", "Curso", "Extensão"]
                            tema_index = temas_disponiveis.index(tema.capitalize()) if tema.capitalize() in temas_disponiveis else 0
                            edit_tema = st.selectbox("Tema do Certificado", options=temas_disponiveis, index=tema_index, key=f"tema_{cert['id']}")
                            
                            # Opção para trocar arquivo
                            edit_arquivo = st.file_uploader("Alterar Arquivo (Imagem ou PDF)", type=['png', 'jpg', 'jpeg', 'pdf', 'gif'], key=f"file_{cert['id']}")
                            
                            col_save, col_delete = st.columns(2)
                            with col_save:
                                if st.form_submit_button("💾 Salvar Alterações", use_container_width=True):
                                    file_path = cert['arquivo_path']
                                    file_type = cert['tipo_arquivo']
                                    
                                    # Se novo arquivo foi enviado, substituir
                                    if edit_arquivo:
                                        from assets.utils import FileManager
                                        # Deletar arquivo antigo
                                        FileManager.delete_file(cert['arquivo_path'])
                                        # Salvar novo arquivo
                                        file_path = FileManager.save_upload_file(edit_arquivo, "data/certificados")
                                        file_type = edit_arquivo.type
                                    
                                    # Atualizar certificado
                                    db.update_certificado(
                                        cert['id'],
                                        edit_titulo,
                                        file_path,
                                        edit_issuer,
                                        str(edit_data_obtencao) if edit_data_obtencao else "",
                                        str(edit_data_validade) if edit_data_validade else "",
                                        edit_descricao,
                                        edit_url_certificado,
                                        file_type,
                                        edit_tema.lower()
                                    )
                                    st.success("✅ Certificado atualizado!")
                                    st.rerun()
                            
                            with col_delete:
                                if st.form_submit_button("🗑️ Deletar", type="secondary", use_container_width=True):
                                    from assets.utils import FileManager
                                    FileManager.delete_file(cert['arquivo_path'])
                                    db.delete_certificado(cert['id'])
                                    st.success("✅ Certificado deletado!")
                                    st.rerun()
            else:
                st.info("Nenhum certificado cadastrado")
        else:
            st.warning("⚠️ Crie um perfil primeiro")
    
    # Tab 5: Habilidades
    with tab5:
        st.subheader("Gerenciar Habilidades")
        curriculum = db.get_curriculum()
        
        if curriculum:
            with st.form("form_habilidade"):
                st.markdown("**Adicionar Habilidade**")
                categoria = st.selectbox("Categoria", [
                    "Programação",
                    "Frameworks",
                    "Banco de Dados",
                    "DevOps",
                    "Soft Skills",
                    "Ferramentas",
                    "Outras"
                ])
                nome_habilidade = st.text_input("Nome da Habilidade")
                nivel = st.slider("Nível de Proficiência", 1, 5, 3)
                
                if st.form_submit_button("➕ Adicionar Habilidade"):
                    db.add_habilidade(
                        curriculum['id'],
                        categoria,
                        nome_habilidade,
                        nivel
                    )
                    st.success("✅ Habilidade adicionada!")
                    st.rerun()
            
            st.markdown("---")
            st.markdown("**Habilidades Cadastradas**")
            habilidades = db.get_habilidades(curriculum['id'])
            if habilidades:
                categorias = {}
                for hab in habilidades:
                    cat = hab['categoria']
                    if cat not in categorias:
                        categorias[cat] = []
                    categorias[cat].append(hab)
                
                for categoria, habs in categorias.items():
                    st.markdown(f"### {categoria}")
                    for hab in habs:
                        col1, col2 = st.columns([4, 1])
                        with col1:
                            st.markdown(f"**{hab['nome_habilidade']}** {'⭐' * hab['nivel']}")
                        with col2:
                            if st.button("🗑️", key=f"del_hab_{hab['id']}", help="Remover habilidade"):
                                if db.delete_habilidade(hab['id']):
                                    st.success("✅ Habilidade removida!")
                                    st.rerun()
                                else:
                                    st.error("❌ Erro ao remover habilidade")
                    st.markdown("---")
            else:
                st.info("📭 Nenhuma habilidade cadastrada")
        else:
            st.warning("⚠️ Crie um perfil primeiro")
    
    # Tab 6: Redes Sociais
    with tab6:
        st.subheader("Gerenciar Redes Sociais")
        curriculum = db.get_curriculum()
        
        if curriculum:
            with st.form("form_link_social"):
                st.markdown("**Adicionar Link de Rede Social**")
                
                col1, col2 = st.columns([1, 2])
                with col1:
                    plataforma = st.selectbox("Plataforma", [
                        "LinkedIn",
                        "GitHub",
                        "Portfolio",
                        "Email",
                        "Instagram",
                        "Twitter",
                        "Facebook",
                        "YouTube",
                        "WhatsApp",
                        "Telegram",
                        "Website",
                        "Outro"
                    ])
                
                with col2:
                    # Placeholder dinâmico baseado na plataforma
                    placeholders = {
                        "LinkedIn": "https://linkedin.com/in/seuperfil",
                        "GitHub": "https://github.com/seuusuario",
                        "Portfolio": "https://seusite.com",
                        "Email": "seu.email@exemplo.com",
                        "Instagram": "https://instagram.com/seuusuario",
                        "Twitter": "https://twitter.com/seuusuario",
                        "Facebook": "https://facebook.com/seuperfil",
                        "YouTube": "https://youtube.com/@seucanal",
                        "WhatsApp": "https://wa.me/5511999999999",
                        "Telegram": "https://t.me/seuusuario",
                        "Website": "https://seusite.com",
                        "Outro": "https://..."
                    }
                    url = st.text_input("URL Completa", placeholder=placeholders.get(plataforma, "https://..."))
                
                if st.form_submit_button("➕ Adicionar Link", use_container_width=True):
                    if url:
                        db.add_link_social(curriculum['id'], plataforma, url)
                        st.success(f"✅ Link do {plataforma} adicionado com sucesso!")
                        st.rerun()
                    else:
                        st.error("⚠️ Por favor, preencha a URL")
            
            st.markdown("---")
            st.markdown("**Links Cadastrados**")
            links = db.get_links_sociais(curriculum['id'])
            if links:
                # Exibir em cards
                for link in links:
                    col1, col2, col3 = st.columns([1, 3, 1])
                    with col1:
                        # Ícones para cada plataforma
                        icons = {
                            'linkedin': '💼', 'github': '💻', 'portfolio': '🌐',
                            'email': '📧', 'instagram': '📷', 'twitter': '🐦',
                            'facebook': '👥', 'youtube': '🎥', 'whatsapp': '💬',
                            'telegram': '✈️', 'website': '🌍', 'outro': '🔗',
                            'portfólio': '🌐', 'site': '🌍'
                        }
                        icon = icons.get(link['plataforma'].lower(), '🔗')
                        st.markdown(f"## {icon}")
                    with col2:
                        st.markdown(f"**{link['plataforma']}**")
                        st.markdown(f"[{link['url']}]({link['url']})")
                    with col3:
                        if st.button("🗑️", key=f"del_{link['id']}", help="Remover link"):
                            if db.delete_link_social(link['id']):
                                st.success("✅ Link removido!")
                                st.rerun()
                            else:
                                st.error("❌ Erro ao remover link")
                st.markdown("---")
            else:
                st.info("📭 Nenhum link cadastrado ainda")
        else:
            st.warning("⚠️ Crie um perfil primeiro")

if __name__ == "__main__":
    main()
