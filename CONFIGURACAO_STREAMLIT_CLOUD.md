# 🚀 Guia de Configuração - Streamlit Cloud

## 📋 Visão Geral

Este guia mostra como configurar as credenciais de administração no Streamlit Cloud usando **Secrets**.

---

## 🔐 Passo 1: Obter as Credenciais

Você já tem as credenciais configuradas localmente no arquivo `.env`:

```toml
ADMIN_USERNAME = "admin"
ADMIN_PASSWORD_HASH = "D+oJUIx4ygUbSk8cgp+dtAEwAlujCt8AngcH2GvcNyk="
ADMIN_PASSWORD_SALT = "DO+axrlYzmj+3A6F09/JaI2K9qK3FvdzEN/jIw9lEyg="
```

### Opção 1: Usar os Valores Atuais

Use os valores do seu arquivo `.env` (recomendado para manter a mesma senha).

### Opção 2: Gerar Novas Credenciais

Se preferir uma senha diferente para produção:

```powershell
# Ativar ambiente virtual
.venv\Scripts\Activate.ps1

# Gerar novo hash
python scripts/generate_password_hash.py
```

---

## ☁️ Passo 2: Configurar no Streamlit Cloud

### 1. Acessar o Painel

1. Acesse: https://share.streamlit.io/
2. Faça login com sua conta
3. Encontre o app **"portfolio-profissional"**

### 2. Abrir Configurações de Secrets

1. Clique nos **três pontos (⋮)** ao lado do app
2. Selecione **"Settings"** (⚙️)
3. Na barra lateral, clique em **"Secrets"**

### 3. Adicionar as Credenciais

Cole o seguinte conteúdo na caixa de texto:

```toml
# Autenticação do Painel Admin
ADMIN_USERNAME = "admin"
ADMIN_PASSWORD_HASH = "D+oJUIx4ygUbSk8cgp+dtAEwAlujCt8AngcH2GvcNyk="
ADMIN_PASSWORD_SALT = "DO+axrlYzmj+3A6F09/JaI2K9qK3FvdzEN/jIw9lEyg="

# Configurações da Aplicação
DB_PATH = "data/portfolio.db"
MAX_FILE_SIZE_MB = 5
UPLOAD_DIR = "data/uploads"
SESSION_TIMEOUT_MINUTES = 30
MAX_LOGIN_ATTEMPTS = 5
DEBUG = false
```

### 4. Salvar

1. Clique em **"Save"**
2. O app será **redesployado automaticamente**
3. Aguarde 1-2 minutos

---

## ✅ Passo 3: Testar o Login

### 1. Acessar o Site

https://portfolio-profissional-robsonaugustodias.streamlit.app/

### 2. Ir ao Painel Admin

1. No menu lateral, clique em **"🔧 Painel Admin"**
2. Faça login com:
   - **Usuário:** `admin`
   - **Senha:** (a senha que você definiu ao gerar o hash)

### 3. Verificar Funcionamento

Se o login funcionar, a configuração está correta! ✅

---

## 🔧 Como Funciona

### Desenvolvimento Local (seu computador)

```
app.py → auth_config.py → .env (arquivo local)
```

A aplicação lê do arquivo `.env`.

### Produção (Streamlit Cloud)

```
app.py → auth_config.py → st.secrets (configurado no painel)
```

A aplicação lê dos **Secrets** configurados no Streamlit Cloud.

### Prioridade de Leitura

O código `auth_config.py` foi atualizado para:

1. **Primeiro:** Tentar ler de `st.secrets` (Streamlit Cloud)
2. **Fallback:** Ler de `.env` (desenvolvimento local)

Isso permite que a **mesma aplicação funcione em ambos os ambientes!**

---

## 🔄 Alterar Senha no Futuro

### No Streamlit Cloud

1. Gere novo hash: `python scripts/generate_password_hash.py`
2. Acesse: https://share.streamlit.io/ > Settings > Secrets
3. Atualize os valores de `ADMIN_PASSWORD_HASH` e `ADMIN_PASSWORD_SALT`
4. Clique em **"Save"**
5. App redesploya automaticamente

### Local

1. Gere novo hash: `python scripts/generate_password_hash.py`
2. Atualize o arquivo `.env`
3. Reinicie a aplicação

---

## 🆘 Solução de Problemas

### Erro: "Credenciais não configuradas"

**Sintoma:** Ao tentar fazer login, aparece erro de credenciais não configuradas.

**Solução:**
1. Verifique se salvou os Secrets no Streamlit Cloud
2. Aguarde 1-2 minutos após salvar (redeploy)
3. Force reboot: Settings > ⋮ > Reboot app

### Erro: "Senha incorreta"

**Sintoma:** Login falha mesmo com senha correta.

**Possíveis causas:**
1. Hash copiado incorretamente (verifique espaços/quebras de linha)
2. Senha gerada é diferente da que você está usando
3. Valores do .env e Streamlit Cloud estão diferentes

**Solução:**
1. Gere um novo hash de senha
2. Atualize tanto .env (local) quanto Secrets (cloud)
3. Use a mesma senha em ambos

### App não atualiza após mudar Secrets

**Solução:**
1. Settings > ⋮ > Reboot app
2. Aguarde 1-2 minutos
3. Limpe cache do navegador (Ctrl + F5)

---

## 📊 Checklist de Configuração

- [ ] Acesso ao Streamlit Cloud (https://share.streamlit.io/)
- [ ] App "portfolio-profissional" encontrado
- [ ] Secrets configurados (copiados do .env ou gerados novos)
- [ ] Secrets salvos
- [ ] Aguardado redeploy (1-2 minutos)
- [ ] Login testado no site
- [ ] Login funcionando ✅

---

## 🔒 Segurança

### ✅ O que está Seguro

- ✅ Secrets **NÃO aparecem no código-fonte**
- ✅ Secrets **NÃO estão no repositório Git**
- ✅ Secrets são **criptografados** no Streamlit Cloud
- ✅ Apenas você (dono do app) pode ver/editar Secrets

### ⚠️ Boas Práticas

1. **Nunca commite** `secrets.toml` no Git
2. **Sempre use** `secrets.toml.example` (template vazio)
3. **Use senhas diferentes** para local e produção (opcional)
4. **Troque a senha** periodicamente
5. **Não compartilhe** os valores dos Secrets

---

## 📚 Referências

- [Documentação Streamlit Secrets](https://docs.streamlit.io/streamlit-community-cloud/deploy-your-app/secrets-management)
- [Streamlit Cloud](https://share.streamlit.io/)
- Arquivo local: `.streamlit/secrets.toml.example`

---

## ✅ Resumo Rápido

```bash
# 1. Obter credenciais do .env ou gerar novas
cat .env

# 2. Acessar Streamlit Cloud
https://share.streamlit.io/

# 3. Settings > Secrets > Colar valores > Save

# 4. Aguardar redeploy (1-2 min)

# 5. Testar login
https://portfolio-profissional-robsonaugustodias.streamlit.app/
```

**🎉 Pronto! Seu app está configurado e seguro!**
