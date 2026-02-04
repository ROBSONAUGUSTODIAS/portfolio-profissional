# 🔐 Guia de Autenticação - Painel Administrativo

## ✨ Segurança Implementada

O painel de **Administração** agora está protegido com autenticação obrigatória. Apenas usuários com credenciais válidas podem acessar e modificar os dados do portfólio.

## 🔑 Credenciais Padrão

### Usuário Padrão (ALTERE IMEDIATAMENTE)
- **👤 Usuário:** `admin`
- **🔑 Senha:** `admin123`

⚠️ **IMPORTANTE:** Altere essas credenciais imediatamente após a primeira execução para não deixar seu portfólio desprotegido!

## 🔄 Como Alterar as Credenciais

1. **Abra o arquivo** `assets/auth_config.py`

2. **Localize essas linhas:**
```python
ADMIN_USERNAME = "**********"
ADMIN_PASSWORD = "**********"
```

3. **Modifique com suas novas credenciais:**
```python
ADMIN_USERNAME = "seu_usuario_aqui"
ADMIN_PASSWORD = "sua_senha_aqui"
```

4. **Salve o arquivo**

5. **Reinicie a aplicação Streamlit**

## 📝 Acesso ao Painel

### Processo de Login

1. Na barra lateral, clique em **"⚙️ Administração"**
2. A tela de login será exibida
3. Digite seu **usuário** e **senha**
4. Clique em **"🔓 Entrar"**

### Se as Credenciais Estiverem Erradas
- Você verá uma mensagem: **"❌ Usuário ou senha inválidos!"**
- Tente novamente com as credenciais corretas

## 🚪 Como Fazer Logout

1. No painel administrativo, clique no botão **"🚪 Sair"** no canto superior direito
2. Você será desconectado automaticamente
3. Para acessar novamente, faça login

## 🛡️ Dicas de Segurança

✅ **Faça:**
- Altere a senha padrão imediatamente
- Use uma senha forte (combine letras, números e caracteres especiais)
- Não compartilhe suas credenciais
- Use diferentes senhas para diferentes aplicações

❌ **Não Faça:**
- Não deixe a senha padrão em produção
- Não compartilhe o código com as credenciais visíveis
- Não reutilize a mesma senha em múltiplos portfólios

## 💾 Armazenamento de Credenciais

As credenciais são armazenadas no arquivo `assets/auth_config.py`. 

⚠️ **Nota:** Se você for fazer deploy do projeto no GitHub, considere:
- Usar variáveis de ambiente em vez de hardcoded
- Adicionar `auth_config.py` ao `.gitignore` antes de fazer push

## 🔄 Recuperação de Acesso

Se você esquecer sua senha:
1. Abra o arquivo `assets/auth_config.py` em seu editor
2. Altere a senha para uma nova
3. Reinicie a aplicação

## 🎯 Funcionalidades Protegidas

As seguintes seções agora requerem autenticação:

- 👤 **Perfil** - Editar dados pessoais
- 💼 **Experiência** - Adicionar/gerenciar experiências
- 🎓 **Educação** - Adicionar/gerenciar cursos
- 🏆 **Certificados** - Upload e gerenciamento de certificados
- ⭐ **Habilidades** - Adicionar/gerenciar habilidades
- 🔗 **Redes Sociais** - Gerenciar links sociais

---

**Sistema de segurança implementado com ❤️ para proteger seu portfólio profissional**
