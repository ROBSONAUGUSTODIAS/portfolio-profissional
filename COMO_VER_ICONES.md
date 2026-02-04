# 🎯 GUIA RÁPIDO - Visualizar Ícones de Redes Sociais

## ⚡ Início Rápido (5 minutos)

### 1️⃣ Executar a Aplicação

```bash
# Abrir PowerShell na pasta do projeto
cd D:\PROTOTIPO\PORTIFOLIO

# Ativar ambiente virtual
.venv\Scripts\Activate.ps1

# Executar aplicação
streamlit run app.py
```

### 2️⃣ Visualizar os Ícones

1. Abra o navegador em: **http://localhost:8501**
2. Clique em **🏠 Início** no menu lateral
3. Role a página até encontrar: **🔗 Conecte-se**
4. Você verá 3 ícones circulares coloridos:
   - 💼 **LinkedIn** (azul)
   - 🌐 **Portfólio** (vermelho)
   - 📧 **Email** (vermelho Gmail)

### 3️⃣ Testar Interatividade

- **Passe o mouse** sobre os ícones → Efeito de elevação
- **Clique** em qualquer ícone → Abre o link
- **Email** → Abre cliente de email automaticamente

---

## ➕ Adicionar Mais Redes Sociais

### Via Interface (Recomendado)

1. No menu lateral, clique em **⚙️ Administração**
2. Role até **"Adicionar Link de Rede Social"**
3. Selecione uma plataforma (ex: **Instagram**)
4. Cole a URL: `https://instagram.com/seu_usuario`
5. Clique em **➕ Adicionar Link**
6. Volte para **🏠 Início** para ver o novo ícone

### Plataformas Disponíveis

```
💼 LinkedIn     💻 GitHub       🌐 Portfolio
📧 Email        📷 Instagram    🐦 Twitter
👥 Facebook     🎥 YouTube      💬 WhatsApp
✈️ Telegram     🌍 Website      🔗 Outro
```

---

## 🎨 Resultado Esperado

```
┌──────────────────────────────────────┐
│  🔗 Conecte-se                       │
│                                      │
│   ┌─────┐  ┌─────┐  ┌─────┐        │
│   │ 💼  │  │ 💻  │  │ 🌐  │        │
│   └─────┘  └─────┘  └─────┘        │
│  LinkedIn  GitHub  Portfólio        │
└──────────────────────────────────────┘
```

**Características:**
- ✅ Ícones circulares com cores das marcas
- ✅ Animação suave ao passar o mouse
- ✅ Clicáveis e abrem em nova aba
- ✅ Responsivo para mobile

---

## 🗑️ Remover Links

1. Vá para **⚙️ Administração**
2. Veja a seção **"Links Cadastrados"**
3. Clique no botão **🗑️** ao lado do link
4. Link removido instantaneamente

---

## 📊 Verificar Status

Execute o script de teste:

```bash
python test_redes_sociais.py
```

Saída esperada:
```
✅ Conectado ao banco: data/portfolio.db
✅ Currículo encontrado: Robson Augusto Dias
📋 Links Sociais Cadastrados:
1. LinkedIn        → https://...
2. Portfólio       → https://...
3. Email           → mailto:...
```

---

## 🐛 Problemas Comuns

### Ícones não aparecem?
- Verifique se há links cadastrados
- Vá para Administração e adicione pelo menos 1 link

### Cores diferentes?
- Cada plataforma tem sua cor oficial
- LinkedIn = Azul (#0A66C2)
- GitHub = Preto (#181717)
- Portfolio = Vermelho (#FF6B6B)

### Link não funciona?
- Certifique-se de usar URL completa: `https://...`
- Email pode ser apenas: `seu@email.com`

---

## 📚 Documentação Completa

- **REDES_SOCIAIS.md** → Guia completo
- **MELHORIAS_REDES_SOCIAIS.md** → Detalhes técnicos
- **IMPLEMENTACAO_ICONES.md** → Resumo da implementação

---

## ✨ Pronto!

Agora você tem uma seção de redes sociais profissional e interativa no seu portfólio! 🎉

**Tempo estimado:** 5 minutos
**Dificuldade:** ⭐ Fácil
**Status:** ✅ Funcionando
