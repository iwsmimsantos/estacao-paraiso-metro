# Script de inicialização rápida das APIs mockadas (Windows)
# Uso: .\start.ps1

Write-Host "======================================"
Write-Host "APIs Mockadas - Microsoft 365 & Miro"
Write-Host "======================================"
Write-Host ""

# Verifica se Python está instalado
try {
    $pythonVersion = python --version 2>&1
    Write-Host "✓ Python encontrado: $pythonVersion"
    Write-Host ""
} catch {
    Write-Host "❌ Python não encontrado. Por favor, instale Python 3.11 ou superior."
    exit 1
}

# Verifica se as dependências estão instaladas
Write-Host "📦 Verificando dependências..."
$fastapi = python -c "import fastapi" 2>&1
if ($LASTEXITCODE -ne 0) {
    Write-Host "⚠️  FastAPI não encontrado. Instalando dependências..."
    pip install -r requirements.txt
    Write-Host ""
}

Write-Host "✓ Dependências verificadas"
Write-Host ""

# Inicia o servidor
Write-Host "🚀 Iniciando servidor na porta 8000..."
Write-Host ""
Write-Host "📚 Documentação disponível em:"
Write-Host "   - Swagger UI: http://localhost:8000/docs"
Write-Host "   - ReDoc:      http://localhost:8000/redoc"
Write-Host "   - OpenAPI:    http://localhost:8000/openapi.json"
Write-Host "   - Health:     http://localhost:8000/health"
Write-Host ""
Write-Host "Pressione Ctrl+C para parar o servidor"
Write-Host "======================================"
Write-Host ""

python main.py

