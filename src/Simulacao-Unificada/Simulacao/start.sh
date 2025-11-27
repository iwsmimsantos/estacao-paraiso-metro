#!/bin/bash

# Script de inicialização rápida das APIs mockadas
# Uso: ./start.sh

echo "======================================"
echo "APIs Mockadas - Microsoft 365 & Miro"
echo "======================================"
echo ""

# Verifica se Python está instalado
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 não encontrado. Por favor, instale Python 3.11 ou superior."
    exit 1
fi

echo "✓ Python encontrado: $(python3 --version)"
echo ""

# Verifica se o ambiente virtual existe
if [ ! -d "venv" ]; then
    echo "📦 Criando ambiente virtual..."
    python3 -m venv venv
    if [ $? -ne 0 ]; then
        echo "❌ Erro ao criar ambiente virtual."
        echo "   Tente instalar: sudo pacman -S python-pip (Arch Linux)"
        exit 1
    fi
    echo "✓ Ambiente virtual criado"
    echo ""
fi

# Ativa o ambiente virtual
echo "🔧 Ativando ambiente virtual..."
source venv/bin/activate

# Verifica se pip existe no venv, se não, instala
if [ ! -f "venv/bin/pip" ] && [ ! -f "venv/bin/pip3" ]; then
    echo "📥 Instalando pip no ambiente virtual..."
    python3 -m ensurepip --upgrade 2>/dev/null || {
        echo "⚠️  Tentando método alternativo..."
        # Baixa get-pip.py se curl estiver disponível
        if command -v curl &> /dev/null; then
            curl -sS https://bootstrap.pypa.io/get-pip.py -o /tmp/get-pip-temp.py && \
            python3 /tmp/get-pip-temp.py && \
            rm /tmp/get-pip-temp.py
        fi
    }
fi

# Verifica se as dependências estão instaladas
echo "📦 Verificando dependências..."
if ! python3 -c "import fastapi" 2>/dev/null; then
    echo "⚠️  FastAPI não encontrado. Instalando dependências..."
    
    # Tenta com pip, pip3 ou python -m pip
    if command -v pip &> /dev/null; then
        pip install -r requirements.txt
    elif command -v pip3 &> /dev/null; then
        pip3 install -r requirements.txt
    else
        python3 -m pip install -r requirements.txt
    fi
    
    echo ""
fi

echo "✓ Dependências verificadas"
echo ""

# Inicia o servidor
echo "🚀 Iniciando servidor na porta 8000..."
echo ""
echo "📚 Documentação disponível em:"
echo "   - Swagger UI: http://localhost:8000/docs"
echo "   - ReDoc:      http://localhost:8000/redoc"
echo "   - OpenAPI:    http://localhost:8000/openapi.json"
echo "   - Health:     http://localhost:8000/health"
echo ""
echo "Pressione Ctrl+C para parar o servidor"
echo "======================================"
echo ""

python3 main.py
