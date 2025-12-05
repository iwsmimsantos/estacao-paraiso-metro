#!/bin/bash

# Script para parar/iniciar um serviço mock
# Uso: ./stop_service.sh <service-name> <action>

set -e

SERVICE_NAME=$1
ACTION=${2:-stop}

if [ -z "$SERVICE_NAME" ]; then
    echo "Uso: $0 <service-name> <action>"
    echo "Services disponíveis: ingestor, orchestrator, sharepoint, audit, iam"
    echo "Actions: stop, start, restart"
    exit 1
fi

# Mapeamento de serviços para portas
declare -A SERVICE_PORTS=(
    ["ingestor"]=8001
    ["orchestrator"]=8002
    ["sharepoint"]=8003
    ["audit"]=8004
    ["iam"]=8005
)

PORT=${SERVICE_PORTS[$SERVICE_NAME]}

if [ -z "$PORT" ]; then
    echo "Erro: Serviço $SERVICE_NAME não reconhecido"
    exit 1
fi

echo "=== Chaos Engineering: Gerenciando serviço ==="
echo "Serviço: $SERVICE_NAME"
echo "Porta: $PORT"
echo "Ação: $ACTION"
echo ""

case $ACTION in
    stop)
        echo "Parando serviço..."
        # Encontra e mata o processo na porta
        PID=$(lsof -ti:$PORT || true)
        if [ -n "$PID" ]; then
            kill -9 $PID
            echo "Serviço parado (PID: $PID)"
        else
            echo "Nenhum processo encontrado na porta $PORT"
        fi
        ;;
    
    start)
        echo "Iniciando serviço..."
        # Verifica se já está rodando
        if lsof -ti:$PORT > /dev/null 2>&1; then
            echo "Serviço já está rodando na porta $PORT"
            exit 1
        fi
        
        # Inicia o serviço em background
        cd "$(dirname "$0")/../../src/mocks"
        uvicorn "${SERVICE_NAME}_mock:app" --host 0.0.0.0 --port $PORT &
        echo "Serviço iniciado na porta $PORT"
        ;;
    
    restart)
        echo "Reiniciando serviço..."
        $0 $SERVICE_NAME stop
        sleep 2
        $0 $SERVICE_NAME start
        ;;
    
    *)
        echo "Ação inválida: $ACTION"
        echo "Actions válidas: stop, start, restart"
        exit 1
        ;;
esac

echo ""
echo "=== Operação concluída ==="
