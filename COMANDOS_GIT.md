# 📋 COMANDOS PRONTOS PARA COPIAR E COLAR

Este arquivo contém todos os comandos necessários para publicar seu portfólio.
Copie e cole no terminal conforme necessário.

---

## 🔧 CONFIGURAÇÃO INICIAL DO GIT

```bash
# Configure seu nome e email (ALTERE OS VALORES)
git config --global user.name "Seu Nome Aqui"
git config --global user.email "seu.email@exemplo.com"

# Verificar configuração
git config --list
```

---

## 📦 PRIMEIRA PUBLICAÇÃO NO GITHUB

### Passo 1: Inicializar Git Local

```bash
# Inicializar repositório
git init

# Adicionar todos os arquivos
git add .

# Fazer primeiro commit
git commit -m "Initial commit - Portfólio Profissional"
```

### Passo 2: Criar Repositório no GitHub

1. Acesse: https://github.com/new
2. Nome do repositório: `portfolio-profissional`
3. Visibilidade: **Public** (obrigatório para Streamlit Cloud gratuito)
4. **NÃO** marque "Initialize with README"
5. Clique em "Create repository"

### Passo 3: Conectar e Enviar

```bash
# ALTERE "SEU_USUARIO" pelo seu nome de usuário do GitHub
git remote add origin https://github.com/SEU_USUARIO/portfolio-profissional.git

# Definir branch principal
git branch -M main

# Enviar código
git push -u origin main
```

---

## 🔄 ATUALIZAR CÓDIGO (APÓS MUDANÇAS)

```bash
# Ver o que mudou
git status

# Adicionar mudanças
git add .

# Fazer commit (ALTERE A MENSAGEM)
git commit -m "Atualização do portfólio - descrição das mudanças"

# Enviar para GitHub
git push
```

---

## 🚀 DEPLOY NO STREAMLIT CLOUD

**NÃO HÁ COMANDOS** - É via interface web:

1. Acesse: https://streamlit.io/cloud
2. Clique em "Continue with GitHub"
3. Autorize o Streamlit Cloud
4. Clique em "New app"
5. Configure:
   - **Repository**: SEU_USUARIO/portfolio-profissional
   - **Branch**: main
   - **Main file path**: app.py
6. Clique em "Deploy!"
7. Aguarde 2-5 minutos

**Sua URL será**: `https://SEU_USUARIO-portfolio-profissional.streamlit.app`

---

## 🔐 CONFIGURAR SECRETS (SE NECESSÁRIO)

No Streamlit Cloud (interface web):

1. Vá para "Settings" → "Secrets"
2. Cole o conteúdo:

```toml
[passwords]
admin = "SUA_SENHA_SEGURA_AQUI"
```

3. Clique em "Save"

---

## 🛠️ COMANDOS ÚTEIS DO GIT

```bash
# Ver status atual
git status

# Ver histórico de commits
git log --oneline

# Ver repositórios remotos
git remote -v

# Baixar mudanças do GitHub (se houver)
git pull

# Desfazer mudanças locais (CUIDADO!)
git checkout -- .

# Ver diferenças
git diff

# Ver branches
git branch -a

# Criar nova branch
git checkout -b nome-da-branch
```

---

## 🗑️ RECOMEÇAR DO ZERO (SE NECESSÁRIO)

```bash
# CUIDADO: Isso apaga todo o histórico Git local

# Remover pasta .git
Remove-Item -Path .git -Recurse -Force

# Recomeçar
git init
git add .
git commit -m "Initial commit - Portfólio Profissional"
```

---

## 📱 ATUALIZAÇÃO AUTOMÁTICA

Após configurar tudo, suas atualizações serão automáticas:

```bash
# Faça mudanças no código...

# Envie para GitHub
git add .
git commit -m "Descrição da mudança"
git push

# O Streamlit Cloud atualiza automaticamente! ✨
```

---

## 🆘 RESOLVER PROBLEMAS COMUNS

### Erro: "Permission denied (publickey)"

```bash
# Use HTTPS em vez de SSH
git remote set-url origin https://github.com/SEU_USUARIO/portfolio-profissional.git
```

### Erro: "Updates were rejected"

```bash
# Baixe mudanças remotas primeiro
git pull --rebase origin main

# Depois envie
git push
```

### Erro: "fatal: not a git repository"

```bash
# Você não está em um repositório Git
# Volte para a pasta do projeto
cd D:\PROTOTIPO\PORTIFOLIO

# Ou inicialize um novo repositório
git init
```

### Desfazer último commit (mas manter mudanças)

```bash
git reset --soft HEAD~1
```

### Desfazer último commit (e descartar mudanças)

```bash
git reset --hard HEAD~1
```

---

## 📋 CHECKLIST PRÉ-PUBLICAÇÃO

Antes de fazer push, verifique:

```bash
# ✅ Git configurado?
git config --list

# ✅ Todos arquivos adicionados?
git status

# ✅ .gitignore funcionando?
cat .gitignore

# ✅ Requirements atualizado?
cat requirements.txt

# ✅ README preenchido?
cat README.md
```

---

## 🎯 SEQUÊNCIA COMPLETA (COPY/PASTE)

Se você está começando do zero, copie e execute TUDO:

```bash
# 1. Configure Git (ALTERE OS VALORES)
git config --global user.name "Seu Nome"
git config --global user.email "seu@email.com"

# 2. Inicialize repositório local
git init
git add .
git commit -m "Initial commit - Portfólio Profissional"

# 3. Crie repositório no GitHub (manual - veja instruções acima)

# 4. Conecte e envie (ALTERE SEU_USUARIO)
git remote add origin https://github.com/SEU_USUARIO/portfolio-profissional.git
git branch -M main
git push -u origin main

# 5. Deploy no Streamlit Cloud (manual - interface web)
```

---

## 💡 DICAS IMPORTANTES

1. **Sempre use mensagens descritivas** nos commits
2. **Teste localmente** antes de fazer push
3. **Não commite senhas** ou dados sensíveis
4. **Faça commits frequentes** (mas significativos)
5. **Use .gitignore** para excluir arquivos desnecessários

---

## 🎓 APRENDER MAIS

- Git: https://git-scm.com/doc
- GitHub: https://docs.github.com/pt
- Streamlit Cloud: https://docs.streamlit.io/streamlit-cloud

---

**Criado em**: Fevereiro 2025
**Para**: Publicação do Portfólio Profissional
