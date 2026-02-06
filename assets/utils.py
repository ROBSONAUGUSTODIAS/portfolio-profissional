"""
Utilitários gerais da aplicação
"""

import os
import shutil
from pathlib import Path
from datetime import datetime
from io import BytesIO
from reportlab.lib.pagesizes import letter, A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib.colors import HexColor, black, grey
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, Image
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT, TA_JUSTIFY
import streamlit as st


class FileManager:
    """Gerenciador de arquivos para upload e armazenamento com validações de segurança"""
    
    @staticmethod
    def save_upload_file(uploaded_file, destination_dir: str) -> str:
        """
        Salva um arquivo fazer upload em um diretório específico com validações
        Retorna o caminho do arquivo salvo
        """
        if uploaded_file is None:
            return None
        
        # Importar SecurityManager
        from assets.security import SecurityManager
        
        # Validar tamanho do arquivo
        valid_size, size_msg = SecurityManager.validate_file_size(uploaded_file.size)
        if not valid_size:
            raise ValueError(size_msg)
        
        # Validar extensão
        allowed_extensions = ['pdf', 'png', 'jpg', 'jpeg', 'gif']
        valid_ext, ext_msg = SecurityManager.validate_file_extension(
            uploaded_file.name, 
            allowed_extensions
        )
        if not valid_ext:
            raise ValueError(ext_msg)
        
        destination_path = Path(destination_dir)
        destination_path.mkdir(parents=True, exist_ok=True)
        
        # Gerar nome seguro para arquivo
        safe_filename = SecurityManager.generate_safe_filename(uploaded_file.name)
        file_path = destination_path / safe_filename
        
        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        
        # Retornar caminho com barras normais para compatibilidade Windows/Linux
        return str(file_path).replace('\\', '/')
    
    @staticmethod
    def delete_file(file_path: str) -> bool:
        """Delete um arquivo"""
        try:
            if os.path.exists(file_path):
                os.remove(file_path)
                return True
        except Exception as e:
            print(f"Erro ao deletar arquivo: {e}")
        return False
    
    @staticmethod
    def file_exists(file_path: str) -> bool:
        """Verifica se um arquivo existe"""
        return os.path.exists(file_path)
    
    @staticmethod
    def get_file_size(file_path: str) -> int:
        """Retorna o tamanho do arquivo em bytes"""
        try:
            return os.path.getsize(file_path)
        except OSError:
            return 0


class DateFormatter:
    """Formatador de datas"""
    
    @staticmethod
    def format_date(date_string: str, format_type: str = "br") -> str:
        """
        Formata uma data
        format_type: 'br' (DD/MM/YYYY) ou 'en' (YYYY-MM-DD)
        """
        if not date_string:
            return ""
        
        try:
            date_obj = datetime.strptime(date_string, "%Y-%m-%d")
            if format_type == "br":
                return date_obj.strftime("%d/%m/%Y")
            else:
                return date_obj.strftime("%Y-%m-%d")
        except:
            return date_string
    
    @staticmethod
    def format_date_range(start_date: str, end_date: str = None) -> str:
        """Formata um intervalo de datas"""
        start = DateFormatter.format_date(start_date, "br")
        if end_date:
            end = DateFormatter.format_date(end_date, "br")
            return f"{start} - {end}"
        else:
            return f"{start} - Presente"


class PDFGenerator:
    """Gerador de currículo em PDF"""
    
    @staticmethod
    def generate_curriculum_pdf(curriculum, experiencias, educacao, habilidades, links_sociais) -> bytes:
        """
        Gera um PDF do currículo com os dados fornecidos
        Retorna os bytes do PDF
        """
        # Criar um BytesIO para armazenar o PDF em memória
        pdf_buffer = BytesIO()
        
        # Criar o documento
        doc = SimpleDocTemplate(
            pdf_buffer,
            pagesize=A4,
            rightMargin=0.5*inch,
            leftMargin=0.5*inch,
            topMargin=0.5*inch,
            bottomMargin=0.5*inch
        )
        
        # Container para os elementos do PDF
        elements = []
        
        # Estilos
        styles = getSampleStyleSheet()
        
        # Estilos customizados
        titulo_style = ParagraphStyle(
            'Titulo',
            parent=styles['Heading1'],
            fontSize=24,
            textColor=HexColor('#0066cc'),
            spaceAfter=6,
            alignment=TA_CENTER,
            fontName='Helvetica-Bold'
        )
        
        profissao_style = ParagraphStyle(
            'Profissao',
            parent=styles['Normal'],
            fontSize=14,
            textColor=HexColor('#666666'),
            spaceAfter=12,
            alignment=TA_CENTER,
            fontName='Helvetica'
        )
        
        secao_style = ParagraphStyle(
            'Secao',
            parent=styles['Heading2'],
            fontSize=12,
            textColor=HexColor('#0066cc'),
            spaceAfter=10,
            spaceBefore=10,
            fontName='Helvetica-Bold',
            borderPadding=5
        )
        
        normal_style = ParagraphStyle(
            'Normal_Custom',
            parent=styles['Normal'],
            fontSize=10,
            spaceAfter=4,
            alignment=TA_JUSTIFY
        )
        
        # Título e profissão
        elements.append(Paragraph(curriculum['nome'], titulo_style))
        elements.append(Paragraph(curriculum['profissao'], profissao_style))
        
        # Informações de contato
        contato_info = []
        if curriculum['email']:
            contato_info.append(f"📧 {curriculum['email']}")
        if curriculum['telefone']:
            contato_info.append(f"📱 {curriculum['telefone']}")
        
        if contato_info:
            elements.append(Paragraph(" | ".join(contato_info), ParagraphStyle(
                'Contato',
                parent=styles['Normal'],
                fontSize=9,
                alignment=TA_CENTER,
                spaceAfter=12,
                textColor=grey
            )))
        
        # Redes sociais
        if links_sociais:
            redes = [f"{link['plataforma']}" for link in links_sociais]
            elements.append(Paragraph("Redes Sociais: " + " | ".join(redes), ParagraphStyle(
                'Redes',
                parent=styles['Normal'],
                fontSize=9,
                alignment=TA_CENTER,
                spaceAfter=12,
                textColor=grey
            )))
        
        elements.append(Spacer(1, 0.15*inch))
        
        # Sobre
        if curriculum['sobre']:
            elements.append(Paragraph("SOBRE", secao_style))
            elements.append(Paragraph(curriculum['sobre'], normal_style))
            elements.append(Spacer(1, 0.1*inch))
        
        # Resumo
        if curriculum['resumo']:
            elements.append(Paragraph("RESUMO PROFISSIONAL", secao_style))
            elements.append(Paragraph(curriculum['resumo'], normal_style))
            elements.append(Spacer(1, 0.1*inch))
        
        # Experiência Profissional
        if experiencias:
            elements.append(Paragraph("EXPERIÊNCIA PROFISSIONAL", secao_style))
            for exp in experiencias:
                # Título e empresa
                titulo_exp = f"<b>{exp['titulo']}</b> - {exp['empresa']}"
                elements.append(Paragraph(titulo_exp, normal_style))
                
                # Datas
                data_fim = exp['data_fim'] if exp['data_fim'] else "Presente"
                data_str = f"{DateFormatter.format_date(exp['data_inicio'], 'br')} - {DateFormatter.format_date(data_fim, 'br') if exp['data_fim'] else 'Presente'}"
                elements.append(Paragraph(f"<i>{data_str}</i>", ParagraphStyle(
                    'Data',
                    parent=styles['Normal'],
                    fontSize=9,
                    textColor=grey,
                    spaceAfter=4
                )))
                
                # Descrição
                if exp['descricao']:
                    elements.append(Paragraph(exp['descricao'], normal_style))
                
                elements.append(Spacer(1, 0.08*inch))
            
            elements.append(Spacer(1, 0.1*inch))
        
        # Educação
        if educacao:
            elements.append(Paragraph("EDUCAÇÃO E CURSOS", secao_style))
            for edu in educacao:
                # Título e instituição
                titulo_edu = f"<b>{edu['titulo']}</b> - {edu['instituicao']}"
                elements.append(Paragraph(titulo_edu, normal_style))
                
                # Data
                if edu['data_conclusao']:
                    data_str = DateFormatter.format_date(edu['data_conclusao'], 'br')
                    elements.append(Paragraph(f"<i>Conclusão: {data_str}</i>", ParagraphStyle(
                        'Data',
                        parent=styles['Normal'],
                        fontSize=9,
                        textColor=grey,
                        spaceAfter=4
                    )))
                
                # Descrição
                if edu['descricao']:
                    elements.append(Paragraph(edu['descricao'], normal_style))
                
                elements.append(Spacer(1, 0.08*inch))
            
            elements.append(Spacer(1, 0.1*inch))
        
        # Habilidades
        if habilidades:
            elements.append(Paragraph("HABILIDADES", secao_style))
            
            # Agrupar por categoria
            categorias = {}
            for hab in habilidades:
                cat = hab['categoria']
                if cat not in categorias:
                    categorias[cat] = []
                categorias[cat].append(hab)
            
            for categoria, habs in categorias.items():
                hab_names = ", ".join([h['nome_habilidade'] for h in habs])
                elements.append(Paragraph(f"<b>{categoria}:</b> {hab_names}", normal_style))
            
            elements.append(Spacer(1, 0.1*inch))
        
        # Footer com data
        elements.append(Spacer(1, 0.2*inch))
        data_geracao = datetime.now().strftime("%d/%m/%Y")
        elements.append(Paragraph(
            f"<i>Currículo gerado em {data_geracao}</i>",
            ParagraphStyle(
                'Footer',
                parent=styles['Normal'],
                fontSize=8,
                alignment=TA_CENTER,
                textColor=grey
            )
        ))
        
        # Build PDF
        doc.build(elements)
        
        # Retornar os bytes do PDF
        pdf_buffer.seek(0)
        return pdf_buffer.getvalue()


class AuthManager:
    """Gerenciador de autenticação para o painel administrativo com segurança aprimorada"""
    
    @staticmethod
    def check_session_timeout():
        """Verifica e aplica timeout de sessão"""
        if "admin_authenticated" in st.session_state and st.session_state.admin_authenticated:
            if "last_activity" in st.session_state:
                from assets.security import SecurityManager
                import time
                
                if SecurityManager.check_session_timeout(st.session_state.last_activity):
                    st.session_state.admin_authenticated = False
                    st.session_state.last_activity = None
                    st.warning("⏱️ Sessão expirada por inatividade (30 minutos). Faça login novamente.")
                    return False
                else:
                    # Atualizar última atividade
                    st.session_state.last_activity = time.time()
            else:
                # Inicializar timestamp
                import time
                st.session_state.last_activity = time.time()
        
        return True
    
    @staticmethod
    def show_login_form() -> bool:
        """
        Exibe o formulário de login com rate limiting
        Retorna True se autenticado, False caso contrário
        """
        from assets.security import get_rate_limiter
        # CAPTCHA desabilitado para compatibilidade com Streamlit Cloud
        # from assets.captcha_manager import CaptchaManager
        import time
        
        # Criar container centralizado
        st.markdown("---")
        col1, col2, col3 = st.columns([1, 2, 1])
        
        with col2:
            st.markdown("# 🔐 Acesso Restrito")
            st.markdown("Área de Administração - Autenticação Obrigatória")
            st.markdown("---")
            
            # CAPTCHA desabilitado
            # if "captcha_text" not in st.session_state:
            #     CaptchaManager.initialize_captcha_session()
            
            # CAPTCHA desabilitado
            # st.markdown("### 🤖 Verificação Anti-Bot")
            # captcha_text, captcha_input = CaptchaManager.show_captcha()
            
            # st.markdown("---")
            
            with st.form("login_form"):
                username = st.text_input(
                    "👤 Usuário",
                    placeholder="Digite seu usuário"
                )
                password = st.text_input(
                    "🔑 Senha",
                    type="password",
                    placeholder="Digite sua senha"
                )
                
                col1, col2 = st.columns([1, 1])
                
                with col1:
                    if st.form_submit_button("🔓 Entrar", use_container_width=True):
                        # CAPTCHA desabilitado para compatibilidade
                        # if not captcha_input or not CaptchaManager.verify_captcha(captcha_input, captcha_text):
                        #     st.error("❌ Código de verificação incorreto!")
                        #     CaptchaManager.refresh_captcha()
                        #     st.rerun()
                        #     return False
                        
                        # Obter rate limiter
                        rate_limiter = get_rate_limiter()
                        
                        # Verificar rate limit
                        allowed, error_msg = rate_limiter.check_rate_limit(username)
                        
                        if not allowed:
                            st.error(f"❌ {error_msg}")
                            # CaptchaManager.refresh_captcha()
                            st.rerun()
                            return False
                        
                        # Verificar credenciais
                        from auth_config import verify_credentials
                        
                        if verify_credentials(username, password):
                            # Login bem-sucedido
                            st.session_state.admin_authenticated = True
                            st.session_state.last_activity = time.time()
                            rate_limiter.record_attempt(username, True)
                            # CaptchaManager.reset_captcha()
                            st.success("✅ Autenticado com sucesso!")
                            st.rerun()
                        else:
                            # Login falhou
                            rate_limiter.record_attempt(username, False)
                            st.error("❌ Usuário ou senha inválidos!")
                            st.session_state.admin_authenticated = False
                            # CaptchaManager.refresh_captcha()
                            st.rerun()
                            return False
                
                with col2:
                    if st.form_submit_button("❌ Cancelar", use_container_width=True):
                        st.info("Acesso cancelado.")
                        # CaptchaManager.reset_captcha()
                        return False
            
            st.markdown("---")
            st.info("💡 Use as credenciais fornecidas para acessar a área administrativa.")
            st.caption("🔒 Proteção: Rate Limiting (máx. 5 tentativas/5 min) + Session Timeout (30 min)")
        
        return False
    
    @staticmethod
    def check_admin_access() -> bool:
        """
        Verifica se o usuário tem acesso ao painel administrativo
        Retorna True se autenticado, False caso contrário
        """
        if "admin_authenticated" not in st.session_state:
            st.session_state.admin_authenticated = False
        
        # Verificar timeout de sessão
        if st.session_state.admin_authenticated:
            if not AuthManager.check_session_timeout():
                return False
        
        return st.session_state.admin_authenticated
    
    @staticmethod
    def logout():
        """Faz logout do usuário administrador"""
        st.session_state.admin_authenticated = False
        st.session_state.last_activity = None
        st.success("✅ Logout realizado com sucesso!")
    
    @staticmethod
    def show_admin_header():
        """Exibe header com informações do usuário autenticado e botão de logout"""
        col1, col2 = st.columns([4, 1])
        
        with col1:
            st.markdown("### 🔐 Painel Administrativo")
            # Mostrar tempo restante da sessão
            if "last_activity" in st.session_state:
                import time
                from assets.security import SecurityManager
                elapsed = time.time() - st.session_state.last_activity
                remaining = SecurityManager.SESSION_TIMEOUT - elapsed
                minutes = int(remaining / 60)
                st.caption(f"⏱️ Sessão expira em {minutes} minutos")
        
        with col2:
            if st.button("🚪 Sair", key="logout_btn"):
                AuthManager.logout()
                st.rerun()
