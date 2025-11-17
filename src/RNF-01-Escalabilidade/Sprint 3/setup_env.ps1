# Script para configurar e ativar o ambiente virtual no Windows
# Uso: .\setup_env.ps1

Write-Host "==================================" -ForegroundColor Cyan
Write-Host "  Setup Ambiente Virtual - Sprint 3" -ForegroundColor Cyan
Write-Host "==================================" -ForegroundColor Cyan
Write-Host ""

$PROJECT_ROOT = $PSScriptRoot

# Verifica se o ambiente virtual já existe
if (Test-Path "$PROJECT_ROOT\venv") {
    Write-Host "Ambiente virtual encontrado." -ForegroundColor Green
} else {
    Write-Host "Criando ambiente virtual..." -ForegroundColor Yellow
    python -m venv "$PROJECT_ROOT\venv"
    
    if ($LASTEXITCODE -eq 0) {
        Write-Host "Ambiente virtual criado com sucesso!" -ForegroundColor Green
    } else {
        Write-Host "Erro ao criar ambiente virtual." -ForegroundColor Red
        exit 1
    }
}

Write-Host ""
Write-Host "Ativando ambiente virtual..." -ForegroundColor Yellow

# Ativa o ambiente virtual
& "$PROJECT_ROOT\venv\Scripts\Activate.ps1"

if ($LASTEXITCODE -eq 0 -or $env:VIRTUAL_ENV) {
    Write-Host "Ambiente virtual ativado!" -ForegroundColor Green
    Write-Host ""
    Write-Host "Versão do Python:" -ForegroundColor Cyan
    python --version
    Write-Host ""
    
    # Verifica se as dependências estão instaladas
    Write-Host "Verificando dependências..." -ForegroundColor Yellow
    $installed = pip list --format=freeze
    
    if ($installed -match "fastapi") {
        Write-Host "Dependências já instaladas." -ForegroundColor Green
    } else {
        Write-Host "Instalando dependências..." -ForegroundColor Yellow
        pip install -r "$PROJECT_ROOT\requirements.txt"
        
        if ($LASTEXITCODE -eq 0) {
            Write-Host "Dependências instaladas com sucesso!" -ForegroundColor Green
        } else {
            Write-Host "Erro ao instalar dependências." -ForegroundColor Red
        }
    }
} else {
    Write-Host "Erro ao ativar ambiente virtual." -ForegroundColor Red
    Write-Host ""
    Write-Host "Tente ativar manualmente:" -ForegroundColor Yellow
    Write-Host "  venv\Scripts\Activate.ps1" -ForegroundColor White
    exit 1
}

Write-Host ""
Write-Host "==================================" -ForegroundColor Cyan
Write-Host "  Ambiente Pronto!" -ForegroundColor Green
Write-Host "==================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "Para executar os mocks:" -ForegroundColor Cyan
Write-Host "  python -m uvicorn src.mocks.ingestor_mock:app --host 0.0.0.0 --port 8001" -ForegroundColor White
Write-Host ""
Write-Host "Para executar testes:" -ForegroundColor Cyan
Write-Host "  pytest tests/unit/ -v" -ForegroundColor White
Write-Host ""
