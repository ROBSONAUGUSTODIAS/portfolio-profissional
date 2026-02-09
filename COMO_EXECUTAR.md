# Como Executar a Aplicação

Este guia explica como executar o Portfólio Profissional desenvolvido com Streamlit.

## Pré-requisitos

- Python 3.8 ou superior instalado
- Ambiente virtual configurado (`.venv`)

## Passos para Executar

### 1. Ativar o Ambiente Virtual

No terminal PowerShell, execute:

```powershell
& D:/PROTOTIPO/PORTIFOLIO/.venv/Scripts/Activate.ps1
```

Ou simplesmente:

```powershell
.venv\Scripts\Activate.ps1
```

### 2. Executar a Aplicação

Com o ambiente virtual ativado, execute:

```powershell
streamlit run app.py
```

Ou usando o caminho completo do Python:

```powershell
D:/PROTOTIPO/PORTIFOLIO/.venv/Scripts/python.exe -m streamlit run app.py
```

### 3. Acessar a Aplicação

Após executar o comando, a aplicação estará disponível em:

- **Local URL**: http://localhost:8501
- **Network URL**: http://192.168.0.21:8501 (ou o IP da sua rede)

Abra o navegador e acesse o endereço local para visualizar o portfólio.

## Parar a Aplicação

Para parar a aplicação, pressione `Ctrl + C` no terminal.

## Solução de Problemas

### Erro ao ativar o ambiente virtual

Se houver erro de permissão ao executar scripts PowerShell:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### Porta 8501 já em uso

Se a porta padrão estiver ocupada, execute em outra porta:

```powershell
streamlit run app.py --server.port 8502
```

### Dependências não instaladas

Se faltar alguma biblioteca, instale as dependências:

```powershell
pip install -r requirements.txt
```

## Acesso Administrativo

Para acessar o painel de administração:

1. **Configure o arquivo `.env`** (se ainda não configurou):
   ```powershell
   # Gerar hash de senha
   python scripts/generate_password_hash.py
   
   # Copiar template
   Copy-Item .env.example .env
   
   # Editar .env e adicionar os valores gerados
   ```

2. Acesse a página "🔧 Painel Admin" no menu lateral

3. Use as credenciais configuradas no arquivo `.env`:
   - Usuário: valor de `ADMIN_USERNAME` (padrão: `admin`)
   - Senha: a senha que você definiu ao gerar o hash

> **⚠️ Segurança:** O arquivo `.env` contém credenciais e **NUNCA deve ser commitado** no Git. Ele já está no `.gitignore`.

---

**Dica**: Mantenha o terminal aberto enquanto estiver usando a aplicação!
