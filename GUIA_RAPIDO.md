## 🚀 GUIA DE INÍCIO RÁPIDO

### ⚙️ Configuração (Primeira Vez)

1. **Abra o PowerShell/Terminal** na pasta do projeto

2. **Ative o ambiente virtual:**
   ```powershell
   .\.venv\Scripts\Activate
   ```

3. **Instale as dependências (se não estiver instalado):**
   ```bash
   pip install -r requirements.txt
   ```

4. **Inicialize o banco com dados de exemplo (Opcional):**
   ```bash
   python init_sample_data.py
   ```
   Isso criará um currículo de exemplo com dados de teste.

5. **Inicie a aplicação:**
   ```bash
   streamlit run app.py
   ```

6. **Acesse no navegador:**
   A aplicação abrirá automaticamente em `http://localhost:8501`

---

### 📝 Fluxo de Uso

#### Se você **NÃO** iniciou com dados de exemplo:

1. Vá para **⚙️ Administração** → **👤 Perfil**
2. Clique em **➕ Criar Perfil**
3. Preencha seus dados pessoais
4. Use as outras abas para adicionar conteúdo

#### Se você **JÁ** iniciou com dados de exemplo:

1. A página inicial mostrará um portfólio de exemplo
2. Vá para **⚙️ Administração** para editar/adicionar conteúdo
3. Veja o resultado em **🏠 Início**, **📄 Currículo** e **🏆 Certificados**

---

### 🎯 Principais Funcionalidades

| Página | O que faz |
|--------|----------|
| **🏠 Início** | Resumo do portfólio com estatísticas |
| **📄 Currículo** | Visualização formatada de todas suas informações |
| **🏆 Certificados** | Slider interativo para navegar certificados |
| **⚙️ Administração** | Painel para criar e editar todo conteúdo |

---

### 📊 Estrutura de Banco de Dados

```
curriculum
├── experiencia (💼 Histórico profissional)
├── educacao (🎓 Formação acadêmica)
├── certificados (🏆 Com slider interativo)
├── habilidades (⭐ Categorias de skills)
└── links_sociais (🔗 Redes sociais)
```

---

### 💾 Arquivos Gerados Automaticamente

```
data/
├── portfolio.db        ← Banco de dados SQLite
├── curriculo/          ← Armazena arquivos PDF
└── certificados/       ← Armazena imagens/PDFs
```

---

### 🆘 Dúvidas Comuns

**P: Onde vão meus certificados?**  
R: Em `data/certificados/` e também no banco de dados

**P: Como remover dados de exemplo?**  
R: Delete `data/portfolio.db` e reinicie a app

**P: Posso mudar cores e temas?**  
R: Sim, edite `assets/config.py`

**P: Como compartilhar meu portfólio?**  
R: Deploy no Streamlit Cloud (veja README.md)

---

### 📞 Próximos Passos

1. ✅ Configurar seu perfil básico
2. ✅ Adicionar sua experiência profissional
3. ✅ Inserir sua educação e certificados
4. ✅ Listar suas habilidades
5. ✅ Vincular suas redes sociais
6. ✅ (Opcional) Deploy na nuvem

**Pronto para começar? Execute `streamlit run app.py` ! 🚀**
