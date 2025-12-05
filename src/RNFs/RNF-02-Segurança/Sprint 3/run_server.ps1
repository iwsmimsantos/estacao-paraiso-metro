# Script para executar o servidor RNF-02 Segurança
$ErrorActionPreference = "Stop"

# Define codificação UTF-8
$env:PYTHONIOENCODING = "utf-8"
[Console]::OutputEncoding = [System.Text.Encoding]::UTF8

# Navega para o diretório do script
$scriptPath = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $scriptPath

Write-Host "===============================================================" -ForegroundColor Cyan
Write-Host "  RNF-02 Seguranca - Middleware de Controle de Acesso" -ForegroundColor Cyan
Write-Host "  Sistema de Simulacao - Companhia do Metro" -ForegroundColor Cyan
Write-Host "===============================================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "Iniciando servidor..." -ForegroundColor Yellow
Write-Host ""
Write-Host "Acesse a documentacao interativa em:" -ForegroundColor Green
Write-Host "  - Swagger UI: http://localhost:8000/docs" -ForegroundColor Green
Write-Host "  - ReDoc: http://localhost:8000/redoc" -ForegroundColor Green
Write-Host ""
Write-Host "Cenarios disponiveis em: http://localhost:8000/scenarios" -ForegroundColor Green
Write-Host ""

# Executa o servidor
python main.py


