"""
Script de Teste Automatizado para Validação de Conformidade
Valida os requisitos de Segurança e Rastreabilidade das APIs Unificadas

APENAS 3 CENÁRIOS DE TESTE:

1. CRÍTICO - RNF-03 Rastreabilidade: 
   Validação de Correlação - Enviar UUID no header x-correlation-id e validar 
   se o mesmo valor é retornado no campo correlation_id do corpo da resposta.

2. ALTO - RNF-02 Segurança:
   Presença do Contexto de Segurança - Validar se meta.security_context está 
   presente e contém: user_id, tenant_id, mfa_enabled.

3. ALTO - RNF-03 Rastreabilidade:
   Presença do Contexto de Rastreabilidade - Validar se meta.traceability está 
   presente e contém: trace_id, span_id, ingested_at_utc (formato ISO 8601).
"""

import csv
import json
import time
import uuid
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, List, Optional
import requests
from dateutil import parser as date_parser


# Configurações
API_BASE_URL = "http://localhost:8000"
CSV_OUTPUT_PATH = Path(__file__).parent / "test_results.csv"

# Endpoints a testar - Apenas o necessário para validar os 3 cenários
# Testa um endpoint representativo de cada serviço Microsoft
ENDPOINTS_TO_TEST = [
    {"service": "sharepoint", "endpoint": "/sharepoint/sites", "method": "GET"},
    {"service": "miro", "endpoint": "/miro/boards", "method": "GET"},
    {"service": "copilot", "endpoint": "/copilot/sessions", "method": "GET"},
    {"service": "office", "endpoint": "/office/documents", "method": "GET"},
    {"service": "sentinel", "endpoint": "/sentinel/incidents", "method": "GET"},
]


class ComplianceTestResult:
    """Resultado de um teste de conformidade"""
    
    def __init__(
        self,
        timestamp_utc: str,
        service_tested: str,
        endpoint_tested: str,
        test_scenario: str,
        status: str,
        severity: str,
        details: str,
        execution_time_ms: float
    ):
        self.timestamp_utc = timestamp_utc
        self.service_tested = service_tested
        self.endpoint_tested = endpoint_tested
        self.test_scenario = test_scenario
        self.status = status
        self.severity = severity
        self.details = details
        self.execution_time_ms = execution_time_ms
    
    def to_csv_row(self) -> Dict[str, str]:
        """Converte para dicionário compatível com CSV"""
        return {
            "timestamp_utc": self.timestamp_utc,
            "service_tested": self.service_tested,
            "endpoint_tested": self.endpoint_tested,
            "test_scenario": self.test_scenario,
            "status": self.status,
            "severity": self.severity,
            "details": self.details,
            "execution_time_ms": f"{self.execution_time_ms:.2f}"
        }


def test_correlation_id(endpoint: str, service: str) -> ComplianceTestResult:
    """
    CRÍTICO: Validação de Correlação
    Envia UUID no header x-correlation-id e valida se retorna no corpo
    """
    start_time = time.time()
    timestamp_utc = datetime.now(timezone.utc).isoformat()
    
    # Gera UUID dinâmico
    correlation_id = str(uuid.uuid4())
    
    try:
        # Faz requisição com correlation_id no header
        response = requests.get(
            f"{API_BASE_URL}{endpoint}",
            headers={"x-correlation-id": correlation_id},
            timeout=10
        )
        
        execution_time = (time.time() - start_time) * 1000
        
        if response.status_code != 200:
            return ComplianceTestResult(
                timestamp_utc=timestamp_utc,
                service_tested=service,
                endpoint_tested=endpoint,
                test_scenario="Validação de Correlação",
                status="FAILED",
                severity="CRÍTICO",
                details=f"Endpoint retornou status {response.status_code} ao invés de 200 OK",
                execution_time_ms=execution_time
            )
        
        # Valida estrutura da resposta
        try:
            data = response.json()
        except json.JSONDecodeError:
            return ComplianceTestResult(
                timestamp_utc=timestamp_utc,
                service_tested=service,
                endpoint_tested=endpoint,
                test_scenario="Validação de Correlação",
                status="FAILED",
                severity="CRÍTICO",
                details="Resposta não é um JSON válido",
                execution_time_ms=execution_time
            )
        
        # Valida presença de correlation_id
        if "correlation_id" not in data:
            return ComplianceTestResult(
                timestamp_utc=timestamp_utc,
                service_tested=service,
                endpoint_tested=endpoint,
                test_scenario="Validação de Correlação",
                status="FAILED",
                severity="CRÍTICO",
                details="Campo 'correlation_id' não encontrado na resposta",
                execution_time_ms=execution_time
            )
        
        # Valida se o correlation_id retornado é o mesmo enviado
        returned_correlation_id = data["correlation_id"]
        if returned_correlation_id != correlation_id:
            return ComplianceTestResult(
                timestamp_utc=timestamp_utc,
                service_tested=service,
                endpoint_tested=endpoint,
                test_scenario="Validação de Correlação",
                status="FAILED",
                severity="CRÍTICO",
                details=f"Correlation ID não corresponde. Enviado: {correlation_id}, Retornado: {returned_correlation_id}",
                execution_time_ms=execution_time
            )
        
        return ComplianceTestResult(
            timestamp_utc=timestamp_utc,
            service_tested=service,
            endpoint_tested=endpoint,
            test_scenario="Validação de Correlação",
            status="PASSED",
            severity="CRÍTICO",
            details=f"Correlation ID validado com sucesso: {correlation_id}",
            execution_time_ms=execution_time
        )
    
    except requests.exceptions.RequestException as e:
        execution_time = (time.time() - start_time) * 1000
        return ComplianceTestResult(
            timestamp_utc=timestamp_utc,
            service_tested=service,
            endpoint_tested=endpoint,
            test_scenario="Validação de Correlação",
            status="FAILED",
            severity="CRÍTICO",
            details=f"Erro na requisição: {str(e)}",
            execution_time_ms=execution_time
        )


def test_security_context(endpoint: str, service: str) -> ComplianceTestResult:
    """
    ALTO: Presença do Contexto de Segurança
    Valida se meta.security_context contém user_id, tenant_id e mfa_enabled
    """
    start_time = time.time()
    timestamp_utc = datetime.now(timezone.utc).isoformat()
    
    try:
        response = requests.get(
            f"{API_BASE_URL}{endpoint}",
            timeout=10
        )
        
        execution_time = (time.time() - start_time) * 1000
        
        if response.status_code != 200:
            return ComplianceTestResult(
                timestamp_utc=timestamp_utc,
                service_tested=service,
                endpoint_tested=endpoint,
                test_scenario="Presença do Contexto de Segurança",
                status="FAILED",
                severity="ALTO",
                details=f"Endpoint retornou status {response.status_code} ao invés de 200 OK",
                execution_time_ms=execution_time
            )
        
        try:
            data = response.json()
        except json.JSONDecodeError:
            return ComplianceTestResult(
                timestamp_utc=timestamp_utc,
                service_tested=service,
                endpoint_tested=endpoint,
                test_scenario="Presença do Contexto de Segurança",
                status="FAILED",
                severity="ALTO",
                details="Resposta não é um JSON válido",
                execution_time_ms=execution_time
            )
        
        # Valida presença de meta
        if "meta" not in data:
            return ComplianceTestResult(
                timestamp_utc=timestamp_utc,
                service_tested=service,
                endpoint_tested=endpoint,
                test_scenario="Presença do Contexto de Segurança",
                status="FAILED",
                severity="ALTO",
                details="Campo 'meta' não encontrado na resposta",
                execution_time_ms=execution_time
            )
        
        meta = data["meta"]
        
        # Valida presença de security_context
        if "security_context" not in meta:
            return ComplianceTestResult(
                timestamp_utc=timestamp_utc,
                service_tested=service,
                endpoint_tested=endpoint,
                test_scenario="Presença do Contexto de Segurança",
                status="FAILED",
                severity="ALTO",
                details="Campo 'meta.security_context' não encontrado na resposta",
                execution_time_ms=execution_time
            )
        
        security_context = meta["security_context"]
        missing_fields = []
        
        # Valida campos críticos
        if "user_id" not in security_context:
            missing_fields.append("user_id")
        if "tenant_id" not in security_context:
            missing_fields.append("tenant_id")
        if "mfa_enabled" not in security_context:
            missing_fields.append("mfa_enabled")
        
        if missing_fields:
            return ComplianceTestResult(
                timestamp_utc=timestamp_utc,
                service_tested=service,
                endpoint_tested=endpoint,
                test_scenario="Presença do Contexto de Segurança",
                status="FAILED",
                severity="ALTO",
                details=f"Campos faltando em security_context: {', '.join(missing_fields)}",
                execution_time_ms=execution_time
            )
        
        return ComplianceTestResult(
            timestamp_utc=timestamp_utc,
            service_tested=service,
            endpoint_tested=endpoint,
            test_scenario="Presença do Contexto de Segurança",
            status="PASSED",
            severity="ALTO",
            details=f"Security context válido: user_id={security_context.get('user_id')}, tenant_id={security_context.get('tenant_id')}, mfa_enabled={security_context.get('mfa_enabled')}",
            execution_time_ms=execution_time
        )
    
    except requests.exceptions.RequestException as e:
        execution_time = (time.time() - start_time) * 1000
        return ComplianceTestResult(
            timestamp_utc=timestamp_utc,
            service_tested=service,
            endpoint_tested=endpoint,
            test_scenario="Presença do Contexto de Segurança",
            status="FAILED",
            severity="ALTO",
            details=f"Erro na requisição: {str(e)}",
            execution_time_ms=execution_time
        )


def test_traceability_context(endpoint: str, service: str) -> ComplianceTestResult:
    """
    ALTO: Presença do Contexto de Rastreabilidade
    Valida se meta.traceability contém trace_id, span_id e ingested_at_utc (ISO 8601)
    """
    start_time = time.time()
    timestamp_utc = datetime.now(timezone.utc).isoformat()
    
    try:
        response = requests.get(
            f"{API_BASE_URL}{endpoint}",
            timeout=10
        )
        
        execution_time = (time.time() - start_time) * 1000
        
        if response.status_code != 200:
            return ComplianceTestResult(
                timestamp_utc=timestamp_utc,
                service_tested=service,
                endpoint_tested=endpoint,
                test_scenario="Presença do Contexto de Rastreabilidade",
                status="FAILED",
                severity="ALTO",
                details=f"Endpoint retornou status {response.status_code} ao invés de 200 OK",
                execution_time_ms=execution_time
            )
        
        try:
            data = response.json()
        except json.JSONDecodeError:
            return ComplianceTestResult(
                timestamp_utc=timestamp_utc,
                service_tested=service,
                endpoint_tested=endpoint,
                test_scenario="Presença do Contexto de Rastreabilidade",
                status="FAILED",
                severity="ALTO",
                details="Resposta não é um JSON válido",
                execution_time_ms=execution_time
            )
        
        # Valida presença de meta
        if "meta" not in data:
            return ComplianceTestResult(
                timestamp_utc=timestamp_utc,
                service_tested=service,
                endpoint_tested=endpoint,
                test_scenario="Presença do Contexto de Rastreabilidade",
                status="FAILED",
                severity="ALTO",
                details="Campo 'meta' não encontrado na resposta",
                execution_time_ms=execution_time
            )
        
        meta = data["meta"]
        
        # Valida presença de traceability
        if "traceability" not in meta:
            return ComplianceTestResult(
                timestamp_utc=timestamp_utc,
                service_tested=service,
                endpoint_tested=endpoint,
                test_scenario="Presença do Contexto de Rastreabilidade",
                status="FAILED",
                severity="ALTO",
                details="Campo 'meta.traceability' não encontrado na resposta",
                execution_time_ms=execution_time
            )
        
        traceability = meta["traceability"]
        missing_fields = []
        
        # Valida campos críticos
        if "trace_id" not in traceability:
            missing_fields.append("trace_id")
        if "span_id" not in traceability:
            missing_fields.append("span_id")
        if "ingested_at_utc" not in traceability:
            missing_fields.append("ingested_at_utc")
        
        if missing_fields:
            return ComplianceTestResult(
                timestamp_utc=timestamp_utc,
                service_tested=service,
                endpoint_tested=endpoint,
                test_scenario="Presença do Contexto de Rastreabilidade",
                status="FAILED",
                severity="ALTO",
                details=f"Campos faltando em traceability: {', '.join(missing_fields)}",
                execution_time_ms=execution_time
            )
        
        # Valida formato ISO 8601 de ingested_at_utc
        ingested_at = traceability.get("ingested_at_utc")
        if ingested_at:
            try:
                date_parser.isoparse(ingested_at)
            except (ValueError, TypeError):
                return ComplianceTestResult(
                    timestamp_utc=timestamp_utc,
                    service_tested=service,
                    endpoint_tested=endpoint,
                    test_scenario="Presença do Contexto de Rastreabilidade",
                    status="FAILED",
                    severity="ALTO",
                    details=f"Campo 'ingested_at_utc' não está em formato ISO 8601: {ingested_at}",
                    execution_time_ms=execution_time
                )
        
        return ComplianceTestResult(
            timestamp_utc=timestamp_utc,
            service_tested=service,
            endpoint_tested=endpoint,
            test_scenario="Presença do Contexto de Rastreabilidade",
            status="PASSED",
            severity="ALTO",
            details=f"Traceability context válido: trace_id={traceability.get('trace_id')[:16]}..., span_id={traceability.get('span_id')[:16]}..., ingested_at_utc={ingested_at}",
            execution_time_ms=execution_time
        )
    
    except requests.exceptions.RequestException as e:
        execution_time = (time.time() - start_time) * 1000
        return ComplianceTestResult(
            timestamp_utc=timestamp_utc,
            service_tested=service,
            endpoint_tested=endpoint,
            test_scenario="Presença do Contexto de Rastreabilidade",
            status="FAILED",
            severity="ALTO",
            details=f"Erro na requisição: {str(e)}",
            execution_time_ms=execution_time
        )


def run_all_tests() -> List[ComplianceTestResult]:
    """Executa todos os testes de conformidade"""
    results = []
    
    print("=" * 80)
    print("TESTE AUTOMATIZADO DE CONFORMIDADE - APIs Unificadas")
    print("=" * 80)
    print(f"API Base URL: {API_BASE_URL}")
    print(f"Total de endpoints: {len(ENDPOINTS_TO_TEST)}")
    print(f"Total de testes por endpoint: 3")
    print(f"Total de testes: {len(ENDPOINTS_TO_TEST) * 3}")
    print("=" * 80)
    print()
    
    for endpoint_config in ENDPOINTS_TO_TEST:
        service = endpoint_config["service"]
        endpoint = endpoint_config["endpoint"]
        
        print(f"Testando: {service} - {endpoint}")
        
        # Teste 1: Correlation ID (CRÍTICO)
        result1 = test_correlation_id(endpoint, service)
        results.append(result1)
        print(f"  [{'✓' if result1.status == 'PASSED' else '✗'}] {result1.test_scenario}: {result1.status}")
        
        # Teste 2: Security Context (ALTO)
        result2 = test_security_context(endpoint, service)
        results.append(result2)
        print(f"  [{'✓' if result2.status == 'PASSED' else '✗'}] {result2.test_scenario}: {result2.status}")
        
        # Teste 3: Traceability Context (ALTO)
        result3 = test_traceability_context(endpoint, service)
        results.append(result3)
        print(f"  [{'✓' if result3.status == 'PASSED' else '✗'}] {result3.test_scenario}: {result3.status}")
        
        print()
    
    return results


def save_results_to_csv(results: List[ComplianceTestResult]):
    """Salva resultados no CSV padronizado"""
    csv_path = CSV_OUTPUT_PATH
    
    # Cria diretório se não existir
    csv_path.parent.mkdir(parents=True, exist_ok=True)
    
    # Cabeçalho do CSV
    fieldnames = [
        "timestamp_utc",
        "service_tested",
        "endpoint_tested",
        "test_scenario",
        "status",
        "severity",
        "details",
        "execution_time_ms"
    ]
    
    # Escreve CSV
    with open(csv_path, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        
        for result in results:
            writer.writerow(result.to_csv_row())
    
    print("=" * 80)
    print(f"Resultados salvos em: {csv_path}")
    print(f"Total de testes: {len(results)}")
    
    # Estatísticas
    passed = sum(1 for r in results if r.status == "PASSED")
    failed = sum(1 for r in results if r.status == "FAILED")
    critical_failed = sum(1 for r in results if r.status == "FAILED" and r.severity == "CRÍTICO")
    
    print(f"Passou: {passed} ({passed/len(results)*100:.1f}%)")
    print(f"Falhou: {failed} ({failed/len(results)*100:.1f}%)")
    print(f"Falhas CRÍTICAS: {critical_failed}")
    print("=" * 80)


def main():
    """Função principal"""
    try:
        # Verifica se API está acessível
        response = requests.get(f"{API_BASE_URL}/health", timeout=5)
        if response.status_code != 200:
            print(f"⚠️  Aviso: API retornou status {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"⚠️  Aviso: Não foi possível conectar à API em {API_BASE_URL}")
        print(f"   Erro: {str(e)}")
        print("   Continuando mesmo assim...")
        print()
    
    # Executa testes
    results = run_all_tests()
    
    # Salva resultados
    save_results_to_csv(results)
    
    return results


if __name__ == "__main__":
    main()

