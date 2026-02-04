# 🚀 Guia Completo de Publicação

Este guia detalha o processo completo para publicar seu portfólio online usando GitHub e Streamlit Cloud.

## 📋 Índice

1. [Preparação do Projeto](#1-preparação-do-projeto)
2. [Publicação no GitHub](#2-publicação-no-github)
3. [Deploy no Streamlit Cloud](#3-deploy-no-streamlit-cloud)
4. [Configurações Finais](#4-configurações-finais)
5. [Opções Alternativas](#5-opções-alternativas)

---

## 1. Preparação do Projeto

### 1.1. Verificar Arquivos Essenciais

Certifique-se de que os seguintes arquivos existam:

- ✅ `requirements.txt` - Dependências do projeto
- ✅ `.gitignore` - Arquivos a serem ignorados
- ✅ `app.py` - Aplicação principal
- ✅ `README.md` - Documentação do projeto

### 1.2. Criar/Atualizar .gitkeep nas Pastas de Dados

```bash
# Criar arquivos .gitkeep para manter estrutura de pastas vazias
New-Item -Path "data/curriculo/.gitkeep" -ItemType File -Force
New-Item -Path "data/certificados/.gitkeep" -ItemType File -Force
```

### 1.3. Criar Arquivo de Secrets (Opcional)

Se você usar variáveis de ambiente, crie um arquivo `.streamlit/secrets.toml.example`:

```toml
# Exemplo de configuração de secrets
# Copie este arquivo para secrets.toml e preencha com seus valores

[passwords]
admin = "sua_senha_aqui"
```

---

## 2. Publicação no GitHub

### 2.1. Instalar Git (se ainda não tiver)

Baixe e instale: https://git-scm.com/download/win

### 2.2. Configurar Git (primeira vez)

```bash
git config --global user.name "Seu Nome"
git config --global user.email "seu.email@example.com"
```

### 2.3. Inicializar Repositório Local

Abra o PowerShell na pasta do projeto:

```powershell
cd D:\PROTOTIPO\PORTIFOLIO
git init
```

### 2.4. Adicionar Arquivos ao Staging

```bash
git add .
```

### 2.5. Fazer o Primeiro Commit

```bash
git commit -m "Initial commit - Portfólio Profissional"
```

### 2.6. Criar Repositório no GitHub

1. Acesse https://github.com
2. Faça login na sua conta
3. Clique no botão **"+"** (canto superior direito) → **"New repository"**
4. Preencha:
   - **Repository name**: `portfolio-profissional` (ou nome de sua preferência)
   - **Description**: "Portfólio profissional interativo desenvolvido com Streamlit"
   - **Visibilidade**: **Public** (necessário para Streamlit Cloud gratuito)
   - **NÃO** marque "Initialize with README" (já temos nosso README)
5. Clique em **"Create repository"**

### 2.7. Conectar Repositório Local ao GitHub

Copie os comandos que o GitHub mostra (algo como):

```bash
git remote add origin https://github.com/SEU_USUARIO/portfolio-profissional.git
git branch -M main
git push -u origin main
```

**Nota**: Substitua `SEU_USUARIO` pelo seu nome de usuário do GitHub.

### 2.8. Verificar Publicação

Acesse seu repositório no GitHub e verifique se todos os arquivos foram enviados.

---

## 3. Deploy no Streamlit Cloud

### 3.1. Criar Conta no Streamlit Cloud

1. Acesse: https://streamlit.io/cloud
2. Clique em **"Sign up"**
3. **Escolha**: "Continue with GitHub"
4. Autorize o Streamlit Cloud a acessar seus repositórios

### 3.2. Criar Nova Aplicação

1. No dashboard do Streamlit Cloud, clique em **"New app"**
2. Preencha os campos:
   - **Repository**: Selecione `SEU_USUARIO/portfolio-profissional`
   - **Branch**: `main`
   - **Main file path**: `app.py`
3. Clique em **"Advanced settings"** (opcional)

### 3.3. Configurar Secrets (se necessário)

Se você usa senhas ou variáveis de ambiente:

1. Em "Advanced settings", vá para **"Secrets"**
2. Adicione suas configurações no formato TOML:

```toml
[passwords]
admin = "sua_senha_segura_aqui"
```

3. Clique em **"Save"**

### 3.4. Deploy

1. Clique em **"Deploy!"**
2. Aguarde alguns minutos (geralmente 2-5 minutos)
3. Sua aplicação estará disponível em: `https://SEU_USUARIO-portfolio-profissional.streamlit.app`

---

## 4. Configurações Finais

### 4.1. Personalizar URL (Opcional)

Você pode personalizar a URL da aplicação nas configurações do Streamlit Cloud.

### 4.2. Configurar Domínio Próprio (Opcional - Plano Pago)

No plano pago do Streamlit Cloud, você pode usar seu próprio domínio.

### 4.3. Monitorar Logs

Acesse os logs em tempo real no dashboard do Streamlit Cloud para diagnosticar problemas.

### 4.4. Atualizar Aplicação

Sempre que fizer mudanças no código:

```bash
git add .
git commit -m "Descrição das alterações"
git push
```

O Streamlit Cloud detectará as mudanças e fará o redeploy automaticamente!

---

## 5. Opções Alternativas

### 5.1. Streamlit Cloud (✅ RECOMENDADO)

**Prós:**
- ✅ 100% Gratuito
- ✅ Integração direta com GitHub
- ✅ Deploy automático
- ✅ SSL/HTTPS incluso
- ✅ Sem configuração de servidor
- ✅ Ideal para apps Streamlit

**Contras:**
- ❌ Recursos limitados (1 GB RAM no plano gratuito)
- ❌ Requer repositório público
- ❌ Pode dormir após inatividade

**Melhor para**: Portfólios e apps Streamlit

---

### 5.2. Render

**Site**: https://render.com

**Prós:**
- ✅ Gratuito (plano free)
- ✅ Suporta múltiplas linguagens
- ✅ SSL automático

**Contras:**
- ❌ Pode ser mais lento que Streamlit Cloud
- ❌ Dorme após 15 min de inatividade no plano free

**Configuração**:
1. Crie uma conta no Render
2. Conecte seu repositório GitHub
3. Configure:
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `streamlit run app.py --server.port $PORT --server.address 0.0.0.0`

---

### 5.3. Heroku

**Site**: https://heroku.com

**Prós:**
- ✅ Plataforma madura
- ✅ Fácil integração com GitHub

**Contras:**
- ❌ Não tem mais plano gratuito (desde 2022)
- ❌ Mínimo $5/mês

---

### 5.4. Google Cloud Run

**Site**: https://cloud.google.com/run

**Prós:**
- ✅ Escalável
- ✅ Pay-per-use
- ✅ Créditos gratuitos iniciais

**Contras:**
- ❌ Mais complexo de configurar
- ❌ Requer Dockerfile

---

### 5.5. Azure App Service

**Site**: https://azure.microsoft.com

**Prós:**
- ✅ Integração com Microsoft
- ✅ Escalável
- ✅ Créditos gratuitos (estudantes)

**Contras:**
- ❌ Mais caro que outras opções
- ❌ Configuração mais complexa

---

## 🎯 Recomendação Final

**Para seu portfólio, recomendo fortemente o Streamlit Cloud:**

1. ✅ **Gratuito** e otimizado para Streamlit
2. ✅ **Simples** - apenas 3 cliques após subir no GitHub
3. ✅ **Automático** - redeploy a cada push
4. ✅ **Confiável** - mantido pela equipe do Streamlit
5. ✅ **Profissional** - URL personalizada e SSL incluso

---

## 📝 Checklist Final

Antes de publicar, verifique:

- [ ] Todos os arquivos commitados no Git
- [ ] `.gitignore` configurado corretamente
- [ ] `requirements.txt` atualizado
- [ ] README.md informativo
- [ ] Repositório criado no GitHub (público)
- [ ] Código enviado para GitHub (`git push`)
- [ ] Conta criada no Streamlit Cloud
- [ ] App configurado e deployado
- [ ] Aplicação funcionando na URL pública
- [ ] Secrets configurados (se necessário)

---

## 🆘 Problemas Comuns

### Erro: "Module not found"
- Verifique se a biblioteca está em `requirements.txt`
- Use versões específicas (ex: `streamlit==1.40.0`)

### Aplicação não inicia
- Verifique os logs no Streamlit Cloud
- Confirme que `app.py` está na raiz do repositório

### Erro de memória
- Otimize seu código
- Considere upgrade para plano pago
- Use cache do Streamlit (`@st.cache_data`)

### Push rejeitado no GitHub
- Faça `git pull` antes de `git push`
- Resolva conflitos se houver

---

## 🎉 Próximos Passos

Após publicar:

1. 📱 Teste em diferentes dispositivos
2. 🔗 Compartilhe o link em seu LinkedIn
3. 📊 Monitore acessos via Streamlit Cloud analytics
4. 🚀 Continue melhorando e fazendo updates
5. ⭐ Adicione o link do GitHub em seu currículo

---

**Boa sorte com a publicação! 🚀**
