# Script de Publicacao do Portfolio
# Este script facilita o processo de publicacao no GitHub

Write-Host "ASSISTENTE DE PUBLICACAO - PORTFOLIO PROFISSIONAL" -ForegroundColor Cyan
Write-Host "============================================================" -ForegroundColor Cyan
Write-Host ""

# Verificar se Git esta instalado
try {
    $gitVersion = git --version
    Write-Host "[OK] Git encontrado: $gitVersion" -ForegroundColor Green
} catch {
    Write-Host "[ERRO] Git nao encontrado!" -ForegroundColor Red
    Write-Host "       Baixe e instale: https://git-scm.com/download/win" -ForegroundColor Yellow
    exit
}

Write-Host ""

# Menu de Opcoes
Write-Host "ESCOLHA UMA OPCAO:" -ForegroundColor Yellow
Write-Host "1. Configurar Git (primeira vez)"
Write-Host "2. Inicializar repositorio local"
Write-Host "3. Fazer commit das alteracoes"
Write-Host "4. Conectar ao GitHub e publicar"
Write-Host "5. Atualizar codigo (push)"
Write-Host "6. Ver status do Git"
Write-Host "7. Criar arquivos .gitkeep"
Write-Host "8. Ver guia completo"
Write-Host "0. Sair"
Write-Host ""

$opcao = Read-Host "Digite o numero da opcao"

switch ($opcao) {
    "1" {
        Write-Host "`nCONFIGURAR GIT" -ForegroundColor Cyan
        $nome = Read-Host "Digite seu nome"
        $email = Read-Host "Digite seu email"
        
        git config --global user.name "$nome"
        git config --global user.email "$email"
        
        Write-Host "[OK] Git configurado com sucesso!" -ForegroundColor Green
        Write-Host "     Nome: $nome" -ForegroundColor Gray
        Write-Host "     Email: $email" -ForegroundColor Gray
    }
    
    "2" {
        Write-Host "`nINICIALIZAR REPOSITORIO" -ForegroundColor Cyan
        
        if (Test-Path ".git") {
            Write-Host "[INFO] Repositorio Git ja existe!" -ForegroundColor Yellow
        } else {
            git init
            Write-Host "[OK] Repositorio inicializado!" -ForegroundColor Green
        }
        
        Write-Host "`nAdicionando arquivos..." -ForegroundColor Gray
        git add .
        
        Write-Host "`nFazendo commit inicial..." -ForegroundColor Gray
        git commit -m "Initial commit - Portfolio Profissional"
        
        Write-Host "[OK] Commit realizado!" -ForegroundColor Green
    }
    
    "3" {
        Write-Host "`nFAZER COMMIT" -ForegroundColor Cyan
        
        git status
        Write-Host ""
        
        $continuar = Read-Host "Deseja continuar com o commit? (s/n)"
        
        if ($continuar -eq "s") {
            git add .
            $mensagem = Read-Host "Digite a mensagem do commit"
            git commit -m "$mensagem"
            Write-Host "[OK] Commit realizado!" -ForegroundColor Green
        }
    }
    
    "4" {
        Write-Host "`nCONECTAR AO GITHUB" -ForegroundColor Cyan
        Write-Host ""
        Write-Host "PASSOS:" -ForegroundColor Yellow
        Write-Host "1. Acesse: https://github.com/new"
        Write-Host "2. Crie um repositorio PUBLICO"
        Write-Host "3. NAO inicialize com README"
        Write-Host "4. Copie a URL do repositorio criado"
        Write-Host ""
        
        $url = Read-Host "Digite a URL do repositorio (ex: https://github.com/usuario/portfolio)"
        
        Write-Host "`nConectando ao GitHub..." -ForegroundColor Gray
        git remote add origin $url
        git branch -M main
        
        Write-Host "`nEnviando codigo..." -ForegroundColor Gray
        git push -u origin main
        
        Write-Host "[OK] Codigo publicado no GitHub!" -ForegroundColor Green
        Write-Host "     Acesse: $url" -ForegroundColor Gray
    }
    
    "5" {
        Write-Host "`nATUALIZAR CODIGO" -ForegroundColor Cyan
        
        git status
        Write-Host ""
        
        git add .
        $mensagem = Read-Host "Mensagem do commit"
        git commit -m "$mensagem"
        git push
        
        Write-Host "[OK] Codigo atualizado no GitHub!" -ForegroundColor Green
    }
    
    "6" {
        Write-Host "`nSTATUS DO GIT" -ForegroundColor Cyan
        Write-Host ""
        git status
        Write-Host ""
        git remote -v
    }
    
    "7" {
        Write-Host "`nCRIAR .GITKEEP" -ForegroundColor Cyan
        
        New-Item -Path "data/curriculo/.gitkeep" -ItemType File -Force | Out-Null
        New-Item -Path "data/certificados/.gitkeep" -ItemType File -Force | Out-Null
        
        Write-Host "[OK] Arquivos .gitkeep criados!" -ForegroundColor Green
        Write-Host "     data/curriculo/.gitkeep" -ForegroundColor Gray
        Write-Host "     data/certificados/.gitkeep" -ForegroundColor Gray
    }
    
    "8" {
        Write-Host "`nABRINDO GUIA COMPLETO..." -ForegroundColor Cyan
        Start-Process "GUIA_PUBLICACAO.md"
    }
    
    "0" {
        Write-Host "`nAte logo!" -ForegroundColor Cyan
        exit
    }
    
    default {
        Write-Host "`n[ERRO] Opcao invalida!" -ForegroundColor Red
    }
}

Write-Host ""
Write-Host "============================================================" -ForegroundColor Cyan
Write-Host "Dica: Execute este script novamente para outras opcoes" -ForegroundColor Gray
Write-Host "Veja o guia completo em: GUIA_PUBLICACAO.md" -ForegroundColor Gray
Write-Host ""
