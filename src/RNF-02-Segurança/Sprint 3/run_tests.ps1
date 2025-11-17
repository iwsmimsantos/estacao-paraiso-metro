# Script para executar os testes RNF-02 Segurança
$ErrorActionPreference = "Stop"

# Define codificação UTF-8
$env:PYTHONIOENCODING = "utf-8"
[Console]::OutputEncoding = [System.Text.Encoding]::UTF8

# Navega para o diretório do script
$scriptPath = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $scriptPath

Write-Host "===============================================================" -ForegroundColor Cyan
Write-Host "  Executando Testes RNF-02 Seguranca" -ForegroundColor Cyan
Write-Host "===============================================================" -ForegroundColor Cyan
Write-Host ""

# Executa os testes
python tests/test_scenarios.py


