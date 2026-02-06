# 🚀 Guia Rápido de Publicação

**3 Passos Simples para seu Portfólio Online**

---

## ⚡ OPÇÃO MAIS RÁPIDA

### 1️⃣ Publicar no GitHub (5 minutos)

```powershell
# Execute o script assistente
.\publicar.ps1
```

**OU manualmente:**

```bash
# 1. Inicializar Git
git init
git add .
git commit -m "Initial commit - Portifólio Profissional"

# 2. Criar repositório no GitHub (https://github.com/new)
#    - Nome: portfolio-profissional
#    - Público: ✅
#    - README: ❌ (já temos)

# 3. Conectar e enviar
git remote add origin https://github.com/SEU_USUARIO/portfolio-profissional.git
git branch -M main
git push -u origin main
```

---

### 2️⃣ Deploy no Streamlit Cloud (2 minutos)

1. **Acesse**: https://streamlit.io/cloud
2. **Login**: "Continue with GitHub"
3. **Novo App**: Clique "New app"
4. **Configure**:
   - Repository: `SEU_USUARIO/portfolio-profissional`
   - Branch: `main`
   - Main file: `app.py`
5. **Deploy**: Clique "Deploy!"

---

### 3️⃣ Pronto! ✅

Seu portfólio estará online em:
```
https://SEU_USUARIO-portfolio-profissional.streamlit.app
```

---

## 📱 Atualizar Depois

Sempre que modificar o código:

```bash
git add .
git commit -m "Atualização do portfólio"
git push
```

✨ O Streamlit Cloud atualiza automaticamente!

---

## 🎯 Melhor Escolha: **STREAMLIT CLOUD**

### Por quê?

| Característica | Streamlit Cloud | Render | Heroku | Vercel |
|---------------|-----------------|--------|--------|--------|
| **Preço** | 🟢 Grátis | 🟢 Grátis* | 🔴 $5/mês | 🟡 Grátis* |
| **Facilidade** | 🟢 Muito fácil | 🟡 Médio | 🟡 Médio | 🔴 Difícil** |
| **Para Streamlit** | 🟢 Otimizado | 🟡 Funciona | 🟡 Funciona | 🔴 Não ideal** |
| **Auto-deploy** | 🟢 Sim | 🟢 Sim | 🟢 Sim | 🟢 Sim |
| **SSL/HTTPS** | 🟢 Incluso | 🟢 Incluso | 🟢 Incluso | 🟢 Incluso |
| **Uptime*** | 🟡 Dorme | 🟡 Dorme | 🟢 24/7 | 🟡 Dorme |

\* Plano gratuito com limitações  
\** Vercel é para Next.js/React, não ideal para Streamlit

---

## 🆘 Problemas Comuns

### "Git não é reconhecido"
```powershell
# Instale o Git
# Download: https://git-scm.com/download/win
# Reinicie o terminal após instalar
```

### "Permission denied (publickey)"
```powershell
# Use HTTPS em vez de SSH:
git remote set-url origin https://github.com/USUARIO/REPO.git
```

### "Port 8501 already in use" (no Streamlit Cloud)
- Não se preocupe, o Streamlit Cloud gerencia isso automaticamente

### App não carrega no Streamlit Cloud
1. Verifique os **logs** no dashboard
2. Confirme que `requirements.txt` está correto
3. Certifique-se que o repositório é **público**

---

## 📋 Checklist Pré-Publicação

- [ ] Git instalado
- [ ] Conta no GitHub criada
- [ ] `.gitignore` verificado
- [ ] `requirements.txt` atualizado
- [ ] Arquivos `.gitkeep` criados
- [ ] README.md preenchido
- [ ] Código testado localmente

---

## 🎓 Recursos Úteis

- 📖 [Guia Completo](GUIA_PUBLICACAO.md) - Todas as opções detalhadas
- 🤖 [Script Assistente](publicar.ps1) - Automatiza o processo
- 📺 [Streamlit Docs](https://docs.streamlit.io/streamlit-cloud)
- 💬 [GitHub Docs](https://docs.github.com/pt/get-started)

---

## ⏱️ Resumo do Tempo

| Etapa | Tempo Estimado |
|-------|----------------|
| Configurar Git (primeira vez) | 2 min |
| Criar repositório GitHub | 2 min |
| Push inicial | 1 min |
| Criar conta Streamlit Cloud | 2 min |
| Deploy | 3-5 min |
| **TOTAL** | **~12 minutos** |

---

**🎉 Boa sorte com a publicação!**

*Para dúvidas, consulte o [Guia Completo](GUIA_PUBLICACAO.md)*
