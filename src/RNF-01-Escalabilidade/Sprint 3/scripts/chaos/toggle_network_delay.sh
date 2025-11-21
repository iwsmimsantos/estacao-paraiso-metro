#!/bin/bash

# Script para adicionar/remover latência de rede usando tc (traffic control)
# Uso: ./toggle_network_delay.sh <action> <delay-ms> <interface>

set -e

ACTION=${1:-add}
DELAY=${2:-100}
INTERFACE=${3:-eth0}

echo "=== Chaos Engineering: Controle de Latência de Rede ==="
echo "Ação: $ACTION"
echo "Delay: ${DELAY}ms"
echo "Interface: $INTERFACE"
echo ""

# Verifica se tc está instalado
if ! command -v tc &> /dev/null; then
    echo "Erro: 'tc' (traffic control) não está instalado"
    echo "Instale com: apt-get install iproute2"
    exit 1
fi

# Verifica permissões de root
if [ "$EUID" -ne 0 ]; then
    echo "Este script requer permissões de root"
    echo "Execute com: sudo $0 $@"
    exit 1
fi

case $ACTION in
    add|enable)
        echo "Adicionando latência de ${DELAY}ms..."
        
        # Remove regras existentes (se houver)
        tc qdisc del dev $INTERFACE root 2> /dev/null || true
        
        # Adiciona delay
        tc qdisc add dev $INTERFACE root netem delay ${DELAY}ms
        
        echo "Latência adicionada com sucesso"
        echo ""
        echo "Para testar: ping -c 5 8.8.8.8"
        ;;
    
    remove|disable)
        echo "Removendo latência..."
        
        # Remove todas as regras de traffic control
        tc qdisc del dev $INTERFACE root 2> /dev/null || true
        
        echo "Latência removida"
        ;;
    
    status)
        echo "Status atual do traffic control:"
        tc qdisc show dev $INTERFACE
        ;;
    
    *)
        echo "Ação inválida: $ACTION"
        echo "Actions válidas: add, remove, status"
        exit 1
        ;;
esac

echo ""
echo "=== Operação concluída ==="
