# 👨‍💼 Portfólio Profissional com Streamlit

Um portal completo e profissional para apresentar seu currículo, certificados e experiências, com suporte a slider de imagens e banco de dados SQLite.

## 🚀 Recursos Principais

- **📄 Currículo Digital**: Apresente suas informações profissionais de forma organizada
- **🏆 Slider de Certificados**: Navegue por seus certificados com um slider interativo
- **💼 Experiências Profissionais**: Liste sua trajetória de carreira
- **🎓 Educação e Cursos**: Mostre sua formação acadêmica
- **⭐ Habilidades**: Categorize suas competências técnicas e soft skills
- **🔗 Redes Sociais**: Vincule seus perfis em redes sociais
- **🗄️ Banco de Dados SQLite**: Armazenamento seguro e escalável
- **⚙️ Painel Administrativo**: Gerenciador completo para atualizar conteúdos

## 📋 Estrutura do Projeto

```
PORTIFOLIO/
├── app.py                    # Aplicação principal Streamlit
├── database.py               # Camada de banco de dados
├── requirements.txt          # Dependências do projeto
├── README.md                 # Este arquivo
├── assets/
│   ├── config.py            # Configurações e tema
│   └── utils.py             # Funções utilitárias
├── data/
│   ├── portfolio.db         # Banco de dados SQLite (gerado automaticamente)
│   ├── curriculo/           # Armazena arquivos de currículo
│   └── certificados/        # Armazena imagens/PDFs dos certificados
└── pages/                   # (Estrutura para futuras sub-páginas)
```

## 🛠️ Instalação

### Pré-requisitos
- Python 3.8 ou superior
- pip (gerenciador de pacotes Python)

### Passos de Instalação

1. **Clone ou navegue até a pasta do projeto:**
```bash
cd PORTIFOLIO
```

2. **Crie um ambiente virtual (recomendado):**
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

3. **Instale as dependências:**
```bash
pip install -r requirements.txt
```

## 🚀 Como Executar

1. **Inicie a aplicação Streamlit:**
```bash
streamlit run app.py
```

2. **Acesse no navegador:**
A aplicação será aberta automaticamente em `http://localhost:8501`

## 📖 Guia de Uso

### 1. Configurar Perfil (Primeira Vez)
- Clique em "⚙️ Administração" no menu lateral
- Vá para a aba "👤 Perfil"
- Preencha suas informações pessoais
- Clique em "➕ Criar Perfil"

### 2. Adicionar Conteúdo

#### Experiência Profissional
1. Na aba "💼 Experiência"
2. Preencha o formulário com suas experiências
3. Clique em "➕ Adicionar Experiência"

#### Educação e Cursos
1. Na aba "🎓 Educação"
2. Adicione seus cursos e formações
3. Clique em "➕ Adicionar Educação"

#### Certificados (Com Slider)
1. Na aba "🏆 Certificados"
2. Faça upload de imagens ou PDFs
3. Preencha informações do certificado
4. Clique em "➕ Adicionar Certificado"

#### Habilidades
1. Na aba "⭐ Habilidades"
2. Selecione categoria e adicione habilidade
3. Defina o nível de proficiência (1-5 estrelas)

#### Redes Sociais
1. Na aba "🔗 Redes Sociais"
2. Selecione a plataforma
3. Cole o URL do seu perfil

### 3. Visualizar Portfólio

#### 🏠 Página Inicial
- Resumo com estatísticas
- Visão geral das informações

#### 📄 Página Currículo
- Apresentação completa formatada
- Todas as experiências, educação e habilidades
- Download do arquivo PDF

#### 🏆 Página Certificados
- **Slider Interativo**: Navegue pelos certificados
- Visualização de imagens ou PDFs
- Informações detalhadas de cada certificado
- Link para verificação online

## 🗄️ Banco de Dados

### Tabelas Principais

- **curriculum**: Dados pessoais e profissionais
- **experiencia**: Histórico profissional
- **educacao**: Formação acadêmica
- **certificados**: Certificados e cursos
- **habilidades**: Competências técnicas e soft skills
- **links_sociais**: Redes sociais e contatos

## 🎨 Personalização

### Cores e Temas
Edite `assets/config.py` para alterar cores:

```python
COLORS = {
    "primary": "#0066cc",
    "secondary": "#00d4ff",
    # ... mais cores
}
```

### CSS Customizado
Adicione CSS customizado em `assets/config.py` na função `configure_page()`

## 📤 Publicação Online

### 🚀 Guia Rápido (Recomendado: Streamlit Cloud)

**Veja o guia completo**: [PUBLICACAO_RAPIDA.md](PUBLICACAO_RAPIDA.md)

**Processo em 3 passos:**

1. **GitHub** (5 min):
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git remote add origin https://github.com/SEU_USUARIO/portfolio.git
   git push -u origin main
   ```

2. **Streamlit Cloud** (2 min):
   - Acesse: https://streamlit.io/cloud
   - Login com GitHub
   - New app → Selecione seu repositório
   - Deploy!

3. **Pronto!** Seu portfólio estará online em minutos.

### 📚 Documentação Completa

- 📖 [Guia Completo de Publicação](GUIA_PUBLICACAO.md) - Todas as opções detalhadas
- ⚡ [Publicação Rápida](PUBLICACAO_RAPIDA.md) - Processo simplificado
- 🤖 Execute `.\publicar.ps1` - Script assistente automático

### Outras Opções de Hospedagem

- **Streamlit Cloud** ⭐ (Grátis, recomendado)
- Render (Grátis com limitações)
- Heroku (Pago, a partir de $5/mês)
- Google Cloud Run
- Azure App Service

## 🐛 Troubleshooting

### Erro: "ModuleNotFoundError"
**Solução**: Instale as dependências novamente
```bash
pip install -r requirements.txt
```

### Erro: Banco de dados não encontrado
**Solução**: A pasta `data/` será criada automaticamente na primeira execução

### Certificados não aparecem no slider
**Solução**: Verifique se os arquivos estão em `data/certificados/`

## 🔐 Segurança

- Não compartilhe arquivos `.db` publicamente
- Use variáveis de ambiente para dados sensíveis
- Valide uploads de arquivo
- Considere adicionar autenticação para o painel admin

## 📚 Tecnologias Utilizadas

| Tecnologia | Versão | Propósito |
|---|---|---|
| Python | 3.8+ | Linguagem |
| Streamlit | 1.40.0 | Framework Web |
| SQLite | 3.x | Banco de Dados |
| Pillow | 10.0.0 | Processamento de Imagens |

## 🤝 Contribuições

Sinta-se livre para fazer fork e enviar pull requests!

## 📄 Licença

Este projeto está sob licença MIT.

## ✨ Autor

Desenvolvido como solução de portfólio profissional.

---

**Desenvolvido com ❤️ usando Python e Streamlit**

Para mais informações sobre Streamlit, visite: [streamlit.io](https://streamlit.io)
