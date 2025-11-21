#!/bin/bash

# Script principal para executar todos os testes
# Uso: ./run_tests.sh [unit|integration|locust|all]

set -e

TEST_TYPE=${1:-all}
PROJECT_ROOT="$(cd "$(dirname "$0")/.." && pwd)"

echo "==================================="
echo "  Executando Testes - Sprint 3"
echo "==================================="
echo "Tipo de teste: $TEST_TYPE"
echo "Diretório: $PROJECT_ROOT"
echo ""

# Ativa ambiente virtual se existir
if [ -d "$PROJECT_ROOT/venv" ]; then
    echo "Ativando ambiente virtual..."
    source "$PROJECT_ROOT/venv/bin/activate"
fi

# Função para executar testes unitários
run_unit_tests() {
    echo ""
    echo ">>> Executando Testes Unitários <<<"
    echo ""
    
    cd "$PROJECT_ROOT"
    pytest tests/unit/ -v --tb=short --color=yes
    
    echo ""
    echo "✓ Testes unitários concluídos"
}

# Função para executar testes de integração
run_integration_tests() {
    echo ""
    echo ">>> Executando Testes de Integração <<<"
    echo ""
    
    cd "$PROJECT_ROOT"
    pytest tests/integration/ -v --tb=short --color=yes
    
    echo ""
    echo "✓ Testes de integração concluídos"
}

# Função para executar testes de carga com Locust
run_locust_tests() {
    echo ""
    echo ">>> Executando Testes de Carga (Locust) <<<"
    echo ""
    echo "Nota: Testes Locust devem ser executados manualmente"
    echo ""
    echo "Para executar um teste de carga específico:"
    echo "  locust -f tests/locust/locustfile_ingestor.py --host=http://localhost:8001"
    echo ""
    echo "Ou execute todos os serviços e use a interface web:"
    echo "  locust -f tests/locust/locustfile_ingestor.py --web-port=8089"
    echo ""
}

# Função para gerar relatório de cobertura
generate_coverage() {
    echo ""
    echo ">>> Gerando Relatório de Cobertura <<<"
    echo ""
    
    cd "$PROJECT_ROOT"
    pytest tests/ --cov=src --cov-report=html --cov-report=term
    
    echo ""
    echo "Relatório HTML gerado em: htmlcov/index.html"
    echo ""
}

# Executa testes baseado no tipo
case $TEST_TYPE in
    unit)
        run_unit_tests
        ;;
    
    integration)
        run_integration_tests
        ;;
    
    locust)
        run_locust_tests
        ;;
    
    coverage)
        generate_coverage
        ;;
    
    all)
        run_unit_tests
        run_integration_tests
        generate_coverage
        run_locust_tests
        ;;
    
    *)
        echo "Tipo de teste inválido: $TEST_TYPE"
        echo ""
        echo "Uso: $0 [unit|integration|locust|coverage|all]"
        echo ""
        echo "Opções:"
        echo "  unit        - Executa apenas testes unitários"
        echo "  integration - Executa apenas testes de integração"
        echo "  locust      - Mostra instruções para testes de carga"
        echo "  coverage    - Gera relatório de cobertura"
        echo "  all         - Executa todos os testes (padrão)"
        exit 1
        ;;
esac

echo ""
echo "==================================="
echo "  Testes Concluídos com Sucesso!"
echo "==================================="
