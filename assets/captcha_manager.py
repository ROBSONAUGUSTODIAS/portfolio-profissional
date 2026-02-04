"""
Módulo de CAPTCHA para proteção contra bots
Gera imagens CAPTCHA para validação no login
"""

from captcha.image import ImageCaptcha
from io import BytesIO
import random
import string
import streamlit as st


class CaptchaManager:
    """Gerenciador de CAPTCHA para proteção de login"""
    
    # Configurações do CAPTCHA
    CAPTCHA_LENGTH = 5
    CAPTCHA_CHARS = string.ascii_uppercase + string.digits
    CAPTCHA_WIDTH = 280
    CAPTCHA_HEIGHT = 90
    
    @staticmethod
    def generate_captcha_text(length: int = None) -> str:
        """
        Gera texto aleatório para CAPTCHA
        
        Args:
            length: Tamanho do texto (padrão: CAPTCHA_LENGTH)
        
        Returns:
            String aleatória com letras maiúsculas e números
        """
        if length is None:
            length = CaptchaManager.CAPTCHA_LENGTH
        
        return ''.join(random.choices(CaptchaManager.CAPTCHA_CHARS, k=length))
    
    @staticmethod
    def generate_captcha_image(text: str) -> BytesIO:
        """
        Gera imagem CAPTCHA a partir do texto
        
        Args:
            text: Texto para incluir no CAPTCHA
        
        Returns:
            BytesIO com a imagem PNG do CAPTCHA
        """
        # Criar gerador de imagem
        image_captcha = ImageCaptcha(
            width=CaptchaManager.CAPTCHA_WIDTH,
            height=CaptchaManager.CAPTCHA_HEIGHT,
            fonts=None  # Usa fontes padrão
        )
        
        # Gerar imagem
        image_data = image_captcha.generate(text)
        
        # Converter para BytesIO
        image_bytes = BytesIO()
        image_bytes.write(image_data.getvalue())
        image_bytes.seek(0)
        
        return image_bytes
    
    @staticmethod
    def verify_captcha(user_input: str, correct_text: str) -> bool:
        """
        Verifica se o CAPTCHA foi resolvido corretamente
        
        Args:
            user_input: Texto digitado pelo usuário
            correct_text: Texto correto do CAPTCHA
        
        Returns:
            True se correto, False caso contrário
        """
        if not user_input or not correct_text:
            return False
        
        # Comparação case-insensitive
        return user_input.upper().strip() == correct_text.upper().strip()
    
    @staticmethod
    def initialize_captcha_session():
        """
        Inicializa ou regenera o CAPTCHA na sessão do Streamlit
        """
        # Gerar novo texto
        captcha_text = CaptchaManager.generate_captcha_text()
        
        # Armazenar na sessão
        st.session_state.captcha_text = captcha_text
        st.session_state.captcha_attempts = 0
        st.session_state.captcha_verified = False
    
    @staticmethod
    def refresh_captcha():
        """
        Atualiza o CAPTCHA com um novo código
        """
        CaptchaManager.initialize_captcha_session()
    
    @staticmethod
    def show_captcha():
        """
        Exibe o CAPTCHA na interface Streamlit
        
        Returns:
            Tuple (captcha_text, user_input) - Texto correto e input do usuário
        """
        # Inicializar se necessário
        if "captcha_text" not in st.session_state:
            CaptchaManager.initialize_captcha_session()
        
        # Gerar imagem
        captcha_image = CaptchaManager.generate_captcha_image(
            st.session_state.captcha_text
        )
        
        # Exibir na interface
        col1, col2 = st.columns([3, 1])
        
        with col1:
            st.image(
                captcha_image, 
                caption="Digite o código acima",
                use_container_width=True
            )
        
        with col2:
            if st.button("🔄", help="Gerar novo código", key="refresh_captcha"):
                CaptchaManager.refresh_captcha()
                st.rerun()
        
        # Campo de input
        user_input = st.text_input(
            "🔐 Código de Verificação",
            placeholder="Digite o código",
            max_chars=CaptchaManager.CAPTCHA_LENGTH,
            key="captcha_input"
        )
        
        return st.session_state.captcha_text, user_input
    
    @staticmethod
    def validate_and_record_attempt(user_input: str, correct_text: str) -> tuple:
        """
        Valida o CAPTCHA e registra tentativa
        
        Args:
            user_input: Input do usuário
            correct_text: Texto correto
        
        Returns:
            Tuple (is_valid, message)
        """
        if "captcha_attempts" not in st.session_state:
            st.session_state.captcha_attempts = 0
        
        # Incrementar tentativas
        st.session_state.captcha_attempts += 1
        
        # Verificar
        is_valid = CaptchaManager.verify_captcha(user_input, correct_text)
        
        if is_valid:
            st.session_state.captcha_verified = True
            return True, "✅ Código verificado com sucesso!"
        else:
            # Limitar tentativas
            if st.session_state.captcha_attempts >= 3:
                CaptchaManager.refresh_captcha()
                return False, "❌ Código incorreto. Novo código gerado."
            else:
                return False, f"❌ Código incorreto. Tentativa {st.session_state.captcha_attempts}/3"
    
    @staticmethod
    def is_captcha_verified() -> bool:
        """
        Verifica se o CAPTCHA foi validado
        
        Returns:
            True se verificado, False caso contrário
        """
        return st.session_state.get("captcha_verified", False)
    
    @staticmethod
    def reset_captcha():
        """
        Reseta o estado do CAPTCHA
        """
        if "captcha_text" in st.session_state:
            del st.session_state.captcha_text
        if "captcha_attempts" in st.session_state:
            del st.session_state.captcha_attempts
        if "captcha_verified" in st.session_state:
            del st.session_state.captcha_verified
        if "captcha_input" in st.session_state:
            del st.session_state.captcha_input
