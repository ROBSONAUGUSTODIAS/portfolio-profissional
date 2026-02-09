# Script de Limpeza e Segurança do Repositório
# Execute: .\limpar_seguranca.ps1

Write-Host "🔒 SCRIPT DE CORREÇÃO DE SEGURANÇA" -ForegroundColor Cyan
Write-Host "=" * 60 -ForegroundColor Cyan
Write-Host ""

# Verificar se estamos no diretório correto
if (-not (Test-Path "app.py")) {
    Write-Host "❌ Erro: Execute este script na raiz do projeto!" -ForegroundColor Red
    exit 1
}

Write-Host "📋 VERIFICAÇÃO INICIAL" -ForegroundColor Yellow
Write-Host "-" * 60

# 1. Verificar Git
Write-Host "Verificando Git..." -ForegroundColor White
$gitStatus = git status 2>&1
if ($LASTEXITCODE -ne 0) {
    Write-Host "❌ Repositório Git não inicializado" -ForegroundColor Red
} else {
    Write-Host "✅ Git inicializado" -ForegroundColor Green
}

# 2. Verificar arquivos sensíveis rastreados
Write-Host "`nVerificando arquivos sensíveis no Git..." -ForegroundColor White
$sensitiveFiles = @(
    "ACESSO_ADMIN.txt",
    "data/portfolio.db",
    ".env"
)

$foundSensitive = $false
foreach ($file in $sensitiveFiles) {
    $tracked = git ls-files $file 2>$null
    if ($tracked) {
        Write-Host "⚠️  ENCONTRADO: $file (rastreado pelo Git)" -ForegroundColor Red
        $foundSensitive = $true
    }
}

if (-not $foundSensitive) {
    Write-Host "✅ Nenhum arquivo sensível rastreado" -ForegroundColor Green
}

# 3. Verificar .gitignore
Write-Host "`nVerificando .gitignore..." -ForegroundColor White
if (Test-Path ".gitignore") {
    $gitignoreContent = Get-Content ".gitignore" -Raw
    $requiredPatterns = @("ACESSO_ADMIN.txt", ".env", "*.db")
    $allPresent = $true
    
    foreach ($pattern in $requiredPatterns) {
        if ($gitignoreContent -notmatch [regex]::Escape($pattern)) {
            Write-Host "⚠️  Faltando no .gitignore: $pattern" -ForegroundColor Yellow
            $allPresent = $false
        }
    }
    
    if ($allPresent) {
        Write-Host "✅ .gitignore configurado corretamente" -ForegroundColor Green
    }
} else {
    Write-Host "❌ .gitignore não encontrado!" -ForegroundColor Red
}

# 4. Verificar .env
Write-Host "`nVerificando configuração .env..." -ForegroundColor White
if (Test-Path ".env") {
    $envContent = Get-Content ".env" -Raw
    if ($envContent -match "ADMIN_PASSWORD_HASH" -and $envContent -match "ADMIN_PASSWORD_SALT") {
        Write-Host "✅ Arquivo .env configurado" -ForegroundColor Green
    } else {
        Write-Host "⚠️  .env existe mas não tem hash de senha configurado" -ForegroundColor Yellow
    }
} else {
    Write-Host "⚠️  Arquivo .env não encontrado" -ForegroundColor Yellow
    Write-Host "   Execute: python scripts/generate_password_hash.py" -ForegroundColor Cyan
}

Write-Host ""
Write-Host "=" * 60 -ForegroundColor Cyan
Write-Host ""

# Menu de opções
Write-Host "🛠️  OPÇÕES DE CORREÇÃO:" -ForegroundColor Yellow
Write-Host ""
Write-Host "1. Remover arquivos sensíveis do Git (staged/working)" -ForegroundColor White
Write-Host "2. Limpar histórico Git (PERIGOSO - cria backup)" -ForegroundColor White
Write-Host "3. Gerar configuração .env" -ForegroundColor White
Write-Host "4. Verificar o que será commitado" -ForegroundColor White
Write-Host "5. Executar testes de segurança" -ForegroundColor White
Write-Host "0. Sair" -ForegroundColor White
Write-Host ""

$choice = Read-Host "Escolha uma opção"

switch ($choice) {
    "1" {
        Write-Host "`n🗑️  REMOVENDO ARQUIVOS SENSÍVEIS DO GIT" -ForegroundColor Yellow
        
        # Remover do staging e working tree (não do histórico)
        git rm --cached ACESSO_ADMIN.txt 2>$null
        git rm --cached data/portfolio.db 2>$null
        git rm --cached .env 2>$null
        
        Write-Host "✅ Arquivos removidos do Git (mas mantidos localmente)" -ForegroundColor Green
        Write-Host "⚠️  Isso não remove do histórico! Use opção 2 para isso." -ForegroundColor Yellow
        Write-Host ""
        Write-Host "Próximos passos:" -ForegroundColor Cyan
        Write-Host "1. git add .gitignore" -ForegroundColor White
        Write-Host "2. git commit -m 'fix: Adicionar arquivos sensíveis ao .gitignore'" -ForegroundColor White
        Write-Host "3. git push" -ForegroundColor White
    }
    
    "2" {
        Write-Host "`n⚠️  LIMPEZA DO HISTÓRICO GIT" -ForegroundColor Red
        Write-Host "=" * 60 -ForegroundColor Red
        Write-Host "ATENÇÃO: Esta operação é IRREVERSÍVEL!" -ForegroundColor Red
        Write-Host "Um backup será criado em: ../PORTIFOLIO_BACKUP" -ForegroundColor Yellow
        Write-Host ""
        
        $confirm = Read-Host "Deseja continuar? (digite 'SIM' para confirmar)"
        
        if ($confirm -eq "SIM") {
            Write-Host "`nCriando backup..." -ForegroundColor Yellow
            
            # Criar backup
            $backupPath = "../PORTIFOLIO_BACKUP_$(Get-Date -Format 'yyyyMMdd_HHmmss')"
            Copy-Item -Path "." -Destination $backupPath -Recurse -Force
            Write-Host "✅ Backup criado em: $backupPath" -ForegroundColor Green
            
            Write-Host "`nLimpando histórico..." -ForegroundColor Yellow
            
            # Limpar ACESSO_ADMIN.txt do histórico
            git filter-branch --force --index-filter "git rm --cached --ignore-unmatch ACESSO_ADMIN.txt" --prune-empty --tag-name-filter cat -- --all
            
            # Limpar portfolio.db do histórico
            git filter-branch --force --index-filter "git rm --cached --ignore-unmatch data/portfolio.db" --prune-empty --tag-name-filter cat -- --all
            
            # Limpar .env do histórico
            git filter-branch --force --index-filter "git rm --cached --ignore-unmatch .env" --prune-empty --tag-name-filter cat -- --all
            
            # Limpar referências
            Remove-Item -Recurse -Force .git/refs/original/ -ErrorAction SilentlyContinue
            git reflog expire --expire=now --all
            git gc --prune=now --aggressive
            
            Write-Host "✅ Histórico limpo!" -ForegroundColor Green
            Write-Host ""
            Write-Host "⚠️  Para aplicar no GitHub, execute:" -ForegroundColor Yellow
            Write-Host "git push origin --force --all" -ForegroundColor White
            Write-Host "git push origin --force --tags" -ForegroundColor White
        } else {
            Write-Host "Operação cancelada." -ForegroundColor Yellow
        }
    }
    
    "3" {
        Write-Host "`n🔑 GERANDO CONFIGURAÇÃO .env" -ForegroundColor Yellow
        
        if (Test-Path ".env") {
            $overwrite = Read-Host "Arquivo .env já existe. Sobrescrever? (s/N)"
            if ($overwrite -ne "s") {
                Write-Host "Operação cancelada." -ForegroundColor Yellow
                exit 0
            }
        }
        
        Write-Host "`nExecute o gerador de hash de senha:" -ForegroundColor Cyan
        Write-Host "python scripts/generate_password_hash.py" -ForegroundColor White
        Write-Host ""
        Write-Host "Depois copie os valores gerados para o arquivo .env" -ForegroundColor Cyan
        
        # Criar .env do template
        if (Test-Path ".env.example") {
            Copy-Item ".env.example" ".env"
            Write-Host "✅ Arquivo .env criado do template" -ForegroundColor Green
        }
    }
    
    "4" {
        Write-Host "`n📋 VERIFICANDO ARQUIVOS PARA COMMIT" -ForegroundColor Yellow
        Write-Host ""
        
        # Listar arquivos staged
        Write-Host "Arquivos staged:" -ForegroundColor Cyan
        git diff --cached --name-only
        Write-Host ""
        
        # Procurar por padrões suspeitos
        Write-Host "Verificando padrões suspeitos..." -ForegroundColor Cyan
        
        $patterns = @(
            "password\s*=\s*['\"]",
            "secret\s*=\s*['\"]",
            "token\s*=\s*['\"]",
            "api_key\s*=\s*['\"]"
        )
        
        $stagedFiles = git diff --cached --name-only
        $foundIssues = $false
        
        foreach ($file in $stagedFiles) {
            if (Test-Path $file) {
                $content = Get-Content $file -Raw -ErrorAction SilentlyContinue
                foreach ($pattern in $patterns) {
                    if ($content -match $pattern) {
                        Write-Host "⚠️  Possível credencial em: $file" -ForegroundColor Red
                        $foundIssues = $true
                    }
                }
            }
        }
        
        if (-not $foundIssues) {
            Write-Host "✅ Nenhum padrão suspeito encontrado" -ForegroundColor Green
        }
    }
    
    "5" {
        Write-Host "`n🧪 EXECUTANDO TESTES DE SEGURANÇA" -ForegroundColor Yellow
        Write-Host ""
        
        python test_seguranca.py
    }
    
    "0" {
        Write-Host "Saindo..." -ForegroundColor Yellow
    }
    
    default {
        Write-Host "Opção inválida!" -ForegroundColor Red
    }
}

Write-Host ""
Write-Host "📚 Para mais informações, consulte: CORRECAO_SEGURANCA.md" -ForegroundColor Cyan
Write-Host ""
