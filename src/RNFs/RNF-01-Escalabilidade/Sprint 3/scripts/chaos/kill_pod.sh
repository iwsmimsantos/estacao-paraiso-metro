#!/bin/bash

# Script para simular falha de pod em Kubernetes
# Uso: ./kill_pod.sh <namespace> <pod-name>

set -e

NAMESPACE=${1:-default}
POD_NAME=$2

if [ -z "$POD_NAME" ]; then
    echo "Uso: $0 <namespace> <pod-name>"
    echo "Exemplo: $0 escalabilidade ingestor-pod-abc123"
    exit 1
fi

echo "=== Chaos Engineering: Matando pod ==="
echo "Namespace: $NAMESPACE"
echo "Pod: $POD_NAME"
echo ""

# Verifica se o pod existe
if ! kubectl get pod "$POD_NAME" -n "$NAMESPACE" &> /dev/null; then
    echo "Erro: Pod $POD_NAME não encontrado no namespace $NAMESPACE"
    exit 1
fi

# Mata o pod
echo "Executando: kubectl delete pod $POD_NAME -n $NAMESPACE"
kubectl delete pod "$POD_NAME" -n "$NAMESPACE"

echo ""
echo "Pod deletado. Monitorando recriação..."
echo ""

# Monitora a recriação do pod
for i in {1..30}; do
    sleep 2
    
    NEW_PODS=$(kubectl get pods -n "$NAMESPACE" | grep "${POD_NAME%%-*}" | grep -v Terminating || true)
    
    if [ -n "$NEW_PODS" ]; then
        echo "Novo pod detectado:"
        echo "$NEW_PODS"
        break
    fi
    
    echo "Aguardando recriação do pod... ($i/30)"
done

echo ""
echo "=== Teste de chaos concluído ==="
