# 🔒 RELATÓRIO DE SEGURANÇA - Portfólio Profissional

## 📋 Análise Completa de Segurança

Data: 04/02/2026
Aplicação: Portfólio Profissional (Streamlit)

---

## ⚠️ VULNERABILIDADES CRÍTICAS ENCONTRADAS

### 1. 🔴 CRÍTICO - Senhas em Texto Claro
**Arquivo:** `assets/auth_config.py` e `ACESSO_ADMIN.txt`

**Problema:**
```python
ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "EngenheiroDev0ps@#"  # ❌ SENHA EXPOSTA NO CÓDIGO
```

**Riscos:**
- Senha armazenada em texto plano no código-fonte
- Senha visível em repositório Git
- Sem hash/criptografia
- Credenciais diferentes no arquivo TXT vs código

**Impacto:** CRÍTICO
**Prioridade:** URGENTE

---

### 2. 🔴 CRÍTICO - SQL Injection (Baixo Risco Controlado)
**Arquivo:** `database.py`

**Status:** ✅ BOM - Usando Prepared Statements
```python
cursor.execute("""
    INSERT INTO habilidades (curriculum_id, categoria, nome_habilidade, nivel)
    VALUES (?, ?, ?, ?)
""", (curriculum_id, categoria, nome_habilidade, nivel))
```

**Observação:** O código está usando `?` placeholders corretamente, protegido contra SQL injection.

---

### 3. 🟡 MÉDIO - Upload de Arquivos Sem Validação Completa
**Arquivo:** `app.py` (linhas 473, 601, 664)

**Problema:**
```python
arquivo = st.file_uploader("Upload do Certificado", 
    type=['png', 'jpg', 'jpeg', 'pdf', 'gif'])
```

**Riscos:**
- Sem validação de tamanho de arquivo
- Sem verificação de conteúdo real (magic bytes)
- Possível upload de arquivos maliciosos disfarçados
- Sem limite de armazenamento

**Impacto:** MÉDIO

---

### 4. 🟡 MÉDIO - Session Management Fraco
**Arquivo:** `app.py`

**Problema:**
```python
if "current_user" not in st.session_state:
    st.session_state.current_user = None
```

**Riscos:**
- Sem timeout de sessão
- Sem proteção contra session fixation
- Sem logout adequado
- Sessão não expira após inatividade

**Impacto:** MÉDIO

---

### 5. 🟡 MÉDIO - Ausência de Validação de Inputs
**Arquivo:** `app.py`

**Problema:**
```python
nome = st.text_input("Nome", value=curriculum['nome'])
email = st.text_input("Email", value=curriculum['email'])
# Sem validação de formato de email
# Sem sanitização de inputs
```

**Riscos:**
- XSS (Cross-Site Scripting) potencial
- Inputs malformados no banco
- Sem validação de formato de email
- Sem limite de caracteres

**Impacto:** MÉDIO

---

### 6. 🟢 BAIXO - Conexão SQLite com Thread Safety Desabilitado
**Arquivo:** `database.py`

**Problema:**
```python
self.conn = sqlite3.connect(self.db_path, check_same_thread=False)
```

**Riscos:**
- Possível race condition em ambiente multi-thread
- Corrupção de dados em concorrência alta
- Necessário para Streamlit, mas arriscado

**Impacto:** BAIXO (aceitável para Streamlit)

---

### 7. 🟢 BAIXO - Falta de Rate Limiting
**Arquivo:** Todo o sistema

**Problema:**
- Sem limite de requisições
- Sem proteção contra brute force
- Sem CAPTCHA no login

**Riscos:**
- Ataque de força bruta no admin
- DoS (Denial of Service)

**Impacto:** BAIXO (aplicação local/desenvolvimento)

---

### 8. 🟡 MÉDIO - Logs e Informações Sensíveis
**Arquivo:** Vários

**Problema:**
- Possível exposição de dados sensíveis em logs
- Mensagens de erro muito detalhadas
- Stack traces visíveis ao usuário

**Riscos:**
- Information disclosure
- Facilita reconhecimento do sistema

**Impacto:** MÉDIO

---

### 9. 🟢 BAIXO - Ausência de HTTPS
**Observação:** Streamlit em desenvolvimento

**Problema:**
- Aplicação roda em HTTP (localhost:8501)
- Dados trafegam sem criptografia

**Riscos:**
- Man-in-the-middle
- Sniffing de credenciais

**Impacto:** BAIXO (apenas se em produção)

---

### 10. 🟡 MÉDIO - Dependências Desatualizadas (Potencial)
**Arquivo:** `requirements.txt`

**Problema:**
```
streamlit==1.40.0
pillow==10.0.0
reportlab==4.0.9
```

**Riscos:**
- Versões específicas podem ter vulnerabilidades conhecidas
- Sem verificação de CVEs

**Impacto:** MÉDIO

---

## ✅ PONTOS POSITIVOS DE SEGURANÇA

1. ✅ **Prepared Statements** - Proteção contra SQL Injection
2. ✅ **Validação de tipos de arquivo** - Upload apenas de extensões permitidas
3. ✅ **Soft Delete** - Links sociais usam ativo=0 ao invés de DELETE
4. ✅ **Separação de configurações** - Config em arquivo separado
5. ✅ **Uso de forms** - Previne envio acidental de dados

---

## 🛠️ RECOMENDAÇÕES DE CORREÇÃO

### URGENTES (Implementar Imediatamente)

#### 1. Hash de Senhas
```python
import hashlib
import secrets

def hash_password(password: str, salt: bytes = None) -> tuple:
    if salt is None:
        salt = secrets.token_bytes(32)
    key = hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 100000)
    return key, salt

def verify_password(password: str, stored_hash: bytes, salt: bytes) -> bool:
    key, _ = hash_password(password, salt)
    return key == stored_hash
```

#### 2. Variáveis de Ambiente
```python
import os
from dotenv import load_dotenv

load_dotenv()
ADMIN_USERNAME = os.getenv('ADMIN_USERNAME')
ADMIN_PASSWORD_HASH = os.getenv('ADMIN_PASSWORD_HASH')
```

#### 3. Validação de Uploads
```python
import magic

def validate_file(file):
    # Verificar tamanho (max 5MB)
    if file.size > 5 * 1024 * 1024:
        return False, "Arquivo muito grande"
    
    # Verificar tipo real do arquivo
    mime = magic.from_buffer(file.read(1024), mime=True)
    file.seek(0)
    
    allowed_types = ['image/png', 'image/jpeg', 'application/pdf']
    if mime not in allowed_types:
        return False, "Tipo de arquivo inválido"
    
    return True, "OK"
```

#### 4. Validação de Inputs
```python
import re

def validate_email(email: str) -> bool:
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def sanitize_input(text: str, max_length: int = 255) -> str:
    # Remover tags HTML
    text = re.sub(r'<[^>]+>', '', text)
    # Limitar tamanho
    return text[:max_length].strip()
```

#### 5. Session Timeout
```python
import time

if "last_activity" not in st.session_state:
    st.session_state.last_activity = time.time()

# Verificar timeout (30 minutos)
if time.time() - st.session_state.last_activity > 1800:
    st.session_state.current_user = None
    st.warning("Sessão expirada. Faça login novamente.")
else:
    st.session_state.last_activity = time.time()
```

---

### IMPORTANTES (Implementar em Breve)

1. **Rate Limiting para Login**
2. **Logging seguro** (sem dados sensíveis)
3. **CSRF Protection** (se expor publicamente)
4. **Backup automático do banco de dados**
5. **Auditoria de ações administrativas**

---

### OPCIONAIS (Para Produção)

1. **HTTPS com certificado SSL**
2. **WAF (Web Application Firewall)**
3. **2FA (Two-Factor Authentication)**
4. **Monitoramento de segurança**
5. **Testes de penetração**

---

## 📊 SCORE DE SEGURANÇA

| Categoria | Score | Status |
|-----------|-------|--------|
| Autenticação | 3/10 | 🔴 Crítico |
| Autorização | 5/10 | 🟡 Médio |
| Validação de Dados | 4/10 | 🟡 Médio |
| Armazenamento | 6/10 | 🟡 Médio |
| Criptografia | 2/10 | 🔴 Crítico |
| Upload de Arquivos | 5/10 | 🟡 Médio |
| Session Management | 4/10 | 🟡 Médio |
| Logging | 5/10 | 🟡 Médio |

**SCORE GERAL: 4.25/10** 🟡

---

## 🎯 PLANO DE AÇÃO

### Semana 1
- [ ] Implementar hash de senhas
- [ ] Mover credenciais para .env
- [ ] Adicionar validação de email
- [ ] Implementar timeout de sessão

### Semana 2
- [ ] Validação completa de uploads
- [ ] Limite de tamanho de arquivos
- [ ] Sanitização de todos os inputs
- [ ] Rate limiting no login

### Semana 3
- [ ] Logging seguro
- [ ] Backup automático
- [ ] Auditoria de ações
- [ ] Testes de segurança

---

## 📝 CONCLUSÃO

A aplicação possui **vulnerabilidades críticas** que devem ser corrigidas antes de ir para produção, especialmente:

1. **Senhas em texto claro** - CRÍTICO
2. **Falta de validação de uploads** - MÉDIO
3. **Ausência de timeout de sessão** - MÉDIO

Para ambiente de **desenvolvimento local**, o nível atual é aceitável, mas **NÃO RECOMENDADO para produção** sem as correções sugeridas.

---

**Próximos Passos:** Implementar as correções urgentes listadas acima.
