"""
Teste rápido de integração do CAPTCHA com Streamlit
"""

import streamlit as st
import sys
from pathlib import Path

# Adicionar diretório raiz ao path
sys.path.insert(0, str(Path(__file__).parent))

from assets.captcha_manager import CaptchaManager

st.set_page_config(page_title="Teste CAPTCHA", page_icon="🤖")

st.title("🤖 Teste de CAPTCHA")
st.markdown("---")

st.markdown("### Demonstração do Sistema CAPTCHA")

# Exibir CAPTCHA
st.markdown("#### CAPTCHA Gerado:")
captcha_text, user_input = CaptchaManager.show_captcha()

if st.button("Verificar Código", type="primary"):
    if user_input:
        if CaptchaManager.verify_captcha(user_input, captcha_text):
            st.success("✅ Código correto!")
            st.balloons()
        else:
            st.error("❌ Código incorreto! Tente novamente.")
            CaptchaManager.refresh_captcha()
            st.rerun()
    else:
        st.warning("⚠️ Por favor, digite o código!")

st.markdown("---")
st.markdown("### Informações Técnicas")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Comprimento", "5 caracteres")

with col2:
    st.metric("Caracteres", "A-Z, 0-9")

with col3:
    st.metric("Combinações", "60M+")

st.markdown("---")
st.info("💡 Este é um teste do módulo CAPTCHA integrado ao portfólio.")
st.caption("🔒 O CAPTCHA protege o login administrativo contra bots e ataques automatizados.")
