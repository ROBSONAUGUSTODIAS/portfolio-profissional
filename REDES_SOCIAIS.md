# 🔗 Guia de Redes Sociais

Este documento explica como funcionam os links de redes sociais na página inicial do portfólio.

## 📋 Funcionalidades

A seção "Conecte-se" na página inicial agora apresenta:

- **Ícones clicáveis**: Cada rede social é exibida como um ícone circular colorido
- **Design responsivo**: Os ícones se adaptam a diferentes tamanhos de tela
- **Efeito hover**: Animação suave ao passar o mouse sobre os ícones
- **Cores personalizadas**: Cada plataforma tem sua cor oficial
- **Labels descritivos**: Nome da plataforma abaixo de cada ícone

## 🎨 Plataformas Suportadas

As seguintes plataformas têm ícones e cores pré-configurados:

| Plataforma | Ícone | Cor | Nome no Banco |
|------------|-------|-----|---------------|
| LinkedIn | 💼 | #0A66C2 | linkedin |
| GitHub | 💻 | #181717 | github |
| Portfólio | 🌐 | #FF6B6B | portfolio ou portfólio |
| Email | 📧 | #EA4335 | email |
| Twitter | 🐦 | #1DA1F2 | twitter |
| Instagram | 📷 | #E4405F | instagram |
| YouTube | 🎥 | #FF0000 | youtube |
| Facebook | 👥 | #1877F2 | facebook |
| WhatsApp | 💬 | #25D366 | whatsapp |
| Telegram | ✈️ | #0088cc | telegram |
| Website | 🌍 | #4CAF50 | website ou site |

## 📝 Como Adicionar Links Sociais

### Via Painel de Administração

1. Acesse **⚙️ Administração** no menu lateral
2. Role até a seção **"Gerenciar Links Sociais"**
3. Preencha:
   - **Plataforma**: Nome da rede social (use os nomes da tabela acima)
   - **URL**: Link completo para seu perfil
4. Clique em **"Adicionar Link Social"**

### Via Código Python

```python
from database import Database

db = Database("data/portfolio.db")

# Adicionar LinkedIn
db.add_link_social(curriculum_id, "LinkedIn", "https://linkedin.com/in/seuperfil")

# Adicionar GitHub
db.add_link_social(curriculum_id, "GitHub", "https://github.com/seuusuario")

# Adicionar Email
db.add_link_social(curriculum_id, "Email", "seu.email@exemplo.com")

# Adicionar Portfólio
db.add_link_social(curriculum_id, "Portfolio", "https://seusite.com")
```

## 🔧 Personalização

### Adicionar Nova Plataforma

Para adicionar suporte a uma nova plataforma, edite o arquivo `app.py`:

```python
platform_icons = {
    # ... plataformas existentes ...
    'nova_plataforma': {
        'icon': '🆕',           # Emoji do ícone
        'color': '#FF00FF',     # Cor em hexadecimal
        'name': 'Nova Plataforma'  # Nome de exibição
    },
}
```

### Modificar Estilo dos Ícones

Os estilos CSS estão definidos no arquivo `app.py`. Você pode ajustar:

- **Tamanho**: Altere `width` e `height` em `.social-icon`
- **Espaçamento**: Modifique `gap` em `.social-links`
- **Efeitos hover**: Ajuste `transform` e `box-shadow` em `.social-icon:hover`

## 💡 Dicas

1. **Use nomes em minúsculas**: O sistema converte automaticamente para minúsculas
2. **Email automático**: Se o nome da plataforma for "email", o link automaticamente adiciona `mailto:`
3. **URLs completas**: Sempre use o URL completo (com https://)
4. **Múltiplos perfis**: Você pode adicionar múltiplos links da mesma plataforma (exemplo: 2 emails)

## 🎯 Exemplos de URLs

```
LinkedIn:   https://linkedin.com/in/seuperfil
GitHub:     https://github.com/seuusuario
Portfolio:  https://seusite.com.br
Email:      seu.email@gmail.com
Instagram:  https://instagram.com/seuusuario
YouTube:    https://youtube.com/@seucanal
WhatsApp:   https://wa.me/5511999999999
```

## 🐛 Solução de Problemas

### Ícone não aparece

- Verifique se o nome da plataforma está correto
- Plataformas não reconhecidas usam o ícone padrão 🔗

### Link não funciona

- Verifique se a URL está completa (com https://)
- Para email, pode usar apenas o endereço (sem mailto:)

### Cores diferentes

- Cada plataforma tem sua cor oficial
- Para personalizar, edite o dicionário `platform_icons` em `app.py`

---

**Desenvolvido com ❤️ para um portfólio profissional interativo!**
