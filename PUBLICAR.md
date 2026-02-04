# 🎯 Início Rápido - Publicar Portfólio no GitHub e Online

**Tempo total: ~10 minutos**

---

## ⚡ Opção 1: Script Automático (MAIS RÁPIDO)

```powershell
# Execute o script assistente
.\publicar.ps1
```

Escolha a opção desejada do menu interativo.

---

## ✍️ Opção 2: Manual em 3 Passos

### 1️⃣ GitHub (5 min)

```bash
# Inicializar Git
git init
git add .
git commit -m "Initial commit - Portfólio Profissional"

# Criar repositório no GitHub: https://github.com/new
# Nome: portfolio-profissional | Público: ✅ | README: ❌

# Conectar e enviar (ALTERE SEU_USUARIO)
git remote add origin https://github.com/SEU_USUARIO/portfolio-profissional.git
git branch -M main
git push -u origin main
```

### 2️⃣ Streamlit Cloud (2 min)

1. https://streamlit.io/cloud
2. "Continue with GitHub"
3. "New app" → Selecione seu repositório
4. Repository: `portfolio-profissional` | Branch: `main` | File: `app.py`
5. "Deploy!"

### 3️⃣ Pronto! ✅

Seu portfólio estará em:
```
https://SEU_USUARIO-portfolio-profissional.streamlit.app
```

---

## 📚 Documentação Completa

| Arquivo | Descrição |
|---------|-----------|
| [PUBLICACAO_RAPIDA.md](PUBLICACAO_RAPIDA.md) | Guia visual rápido ⭐ |
| [GUIA_PUBLICACAO.md](GUIA_PUBLICACAO.md) | Todas as opções detalhadas |
| [COMANDOS_GIT.md](COMANDOS_GIT.md) | Comandos prontos para copiar |
| [COMPARACAO_HOSPEDAGEM.md](COMPARACAO_HOSPEDAGEM.md) | Comparar plataformas |

---

## 🔄 Atualizar Depois

```bash
git add .
git commit -m "Atualização"
git push
```

O Streamlit Cloud atualiza automaticamente! ✨

---

**💡 Dica**: Comece pelo [PUBLICACAO_RAPIDA.md](PUBLICACAO_RAPIDA.md)
