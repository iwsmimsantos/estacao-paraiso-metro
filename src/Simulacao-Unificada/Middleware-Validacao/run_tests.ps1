# Script para executar testes do Middleware de Validação
# Executa todos os testes com relatório de cobertura

Write-Host "=====================================" -ForegroundColor Cyan
Write-Host "Executando Testes Unitários" -ForegroundColor Cyan
Write-Host "Middleware de Validação - Metrô SP" -ForegroundColor Cyan
Write-Host "=====================================" -ForegroundColor Cyan
Write-Host ""

# Verifica se pytest está instalado
if (-not (Get-Command pytest -ErrorAction SilentlyContinue)) {
    Write-Host "❌ pytest não encontrado. Instalando dependências..." -ForegroundColor Red
    pip install -r requirements.txt
    Write-Host ""
}

# Limpa cache anterior
Write-Host "🧹 Limpando cache de testes..." -ForegroundColor Yellow
if (Test-Path ".pytest_cache") {
    Remove-Item -Recurse -Force ".pytest_cache"
}
if (Test-Path "htmlcov") {
    Remove-Item -Recurse -Force "htmlcov"
}
if (Test-Path ".coverage") {
    Remove-Item -Force ".coverage"
}
Write-Host "✅ Cache limpo" -ForegroundColor Green
Write-Host ""

# Menu de opções
Write-Host "Selecione o tipo de teste:" -ForegroundColor Yellow
Write-Host "1. Todos os testes (45 testes)" -ForegroundColor White
Write-Host "2. RNF-01: Segurança (12 testes)" -ForegroundColor White
Write-Host "3. RNF-02: Escalabilidade (15 testes)" -ForegroundColor White
Write-Host "4. RNF-03: Rastreabilidade (18 testes)" -ForegroundColor White
Write-Host "5. Testes rápidos (excluir lentos)" -ForegroundColor White
Write-Host "6. Testes com coverage detalhado" -ForegroundColor White
Write-Host ""

$choice = Read-Host "Digite sua escolha (1-6)"

switch ($choice) {
    "1" {
        Write-Host ""
        Write-Host "🚀 Executando TODOS os testes..." -ForegroundColor Cyan
        pytest -v --cov=src --cov-report=html --cov-report=term-missing
    }
    "2" {
        Write-Host ""
        Write-Host "🔒 Executando testes RNF-01 (Segurança)..." -ForegroundColor Cyan
        pytest tests/unit/test_rnf01_seguranca.py -v --cov=src --cov-report=term-missing
    }
    "3" {
        Write-Host ""
        Write-Host "📈 Executando testes RNF-02 (Escalabilidade)..." -ForegroundColor Cyan
        pytest tests/unit/test_rnf02_escalabilidade.py -v --cov=src --cov-report=term-missing
    }
    "4" {
        Write-Host ""
        Write-Host "🔍 Executando testes RNF-03 (Rastreabilidade)..." -ForegroundColor Cyan
        pytest tests/unit/test_rnf03_rastreabilidade.py -v --cov=src --cov-report=term-missing
    }
    "5" {
        Write-Host ""
        Write-Host "⚡ Executando testes rápidos..." -ForegroundColor Cyan
        pytest -v -m "not slow" --cov=src --cov-report=term-missing
    }
    "6" {
        Write-Host ""
        Write-Host "📊 Executando com relatório HTML completo..." -ForegroundColor Cyan
        pytest -v --cov=src --cov-report=html --cov-report=term-missing
        
        Write-Host ""
        Write-Host "✅ Relatório gerado em: htmlcov/index.html" -ForegroundColor Green
        
        $openReport = Read-Host "Deseja abrir o relatório no navegador? (s/n)"
        if ($openReport -eq "s") {
            Start-Process "htmlcov/index.html"
        }
    }
    default {
        Write-Host ""
        Write-Host "❌ Opção inválida. Executando todos os testes..." -ForegroundColor Red
        pytest -v --cov=src --cov-report=html --cov-report=term-missing
    }
}

Write-Host ""
Write-Host "=====================================" -ForegroundColor Cyan
Write-Host "✅ Execução concluída!" -ForegroundColor Green
Write-Host "=====================================" -ForegroundColor Cyan
