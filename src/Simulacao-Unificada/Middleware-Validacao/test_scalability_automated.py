"""
Script de Teste Automatizado para Validação de Conformidade de Escalabilidade
Valida os requisitos de Escalabilidade (RNF-01) das APIs Unificadas

APENAS 3 CENÁRIOS DE TESTE:

1. CRÍTICO - RNF-01 Escalabilidade: 
   Validação de Métricas de Performance - Validar se meta.performance está 
   presente e contém: processing_time_ms, items_in_response.

2. ALTO - RNF-01 Escalabilidade:
   Validação de Limites de Latência - Validar se processing_time_ms está 
   dentro dos limites aceitáveis (< 1000ms para operações normais).

3. ALTO - RNF-01 Escalabilidade:
   Validação de Throughput - Validar se items_in_response está dentro dos 
   limites esperados e o sistema retorna dados consistentemente.
"""

import csv
import json
import time
import uuid
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, List, Optional
import requests


# Configurações
API_BASE_URL = "http://localhost:8000"
CSV_OUTPUT_PATH = Path(__file__).parent / "test_scalability_results.csv"

# Endpoints a testar - Testa um endpoint representativo de cada serviço Microsoft
ENDPOINTS_TO_TEST = [
    {"service": "sharepoint", "endpoint": "/sharepoint/sites", "method": "GET"},
    {"service": "miro", "endpoint": "/miro/boards", "method": "GET"},
    {"service": "copilot", "endpoint": "/copilot/sessions", "method": "GET"},
    {"service": "office", "endpoint": "/office/documents", "method": "GET"},
    {"service": "sentinel", "endpoint": "/sentinel/incidents", "method": "GET"},
]

# Limites de performance para validação (baseado em requisitos de escalabilidade)
MAX_LATENCY_MS = 1000  # Latência máxima aceitável para operações normais
MIN_ITEMS_EXPECTED = 1  # Mínimo de itens esperados em resposta
MAX_ITEMS_PER_PAGE = 100  # Máximo de itens por página


class ScalabilityTestResult:
    """Resultado de um teste de conformidade de escalabilidade"""
    
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


def test_performance_metrics(endpoint: str, service: str) -> ScalabilityTestResult:
    """
    CRÍTICO: Validação de Métricas de Performance
    Valida se meta.performance contém processing_time_ms e items_in_response
    """
    start_time = time.time()
    timestamp_utc = datetime.now(timezone.utc).isoformat()
    
    try:
        # Faz requisição ao endpoint
        response = requests.get(
            f"{API_BASE_URL}{endpoint}",
            timeout=10
        )
        
        execution_time = (time.time() - start_time) * 1000
        
        if response.status_code != 200:
            return ScalabilityTestResult(
                timestamp_utc=timestamp_utc,
                service_tested=service,
                endpoint_tested=endpoint,
                test_scenario="Validação de Métricas de Performance",
                status="FAILED",
                severity="CRÍTICO",
                details=f"Endpoint retornou status {response.status_code} ao invés de 200 OK",
                execution_time_ms=execution_time
            )
        
        # Valida estrutura da resposta
        try:
            data = response.json()
        except json.JSONDecodeError:
            return ScalabilityTestResult(
                timestamp_utc=timestamp_utc,
                service_tested=service,
                endpoint_tested=endpoint,
                test_scenario="Validação de Métricas de Performance",
                status="FAILED",
                severity="CRÍTICO",
                details="Resposta não é um JSON válido",
                execution_time_ms=execution_time
            )
        
        # Valida presença de meta
        if "meta" not in data:
            return ScalabilityTestResult(
                timestamp_utc=timestamp_utc,
                service_tested=service,
                endpoint_tested=endpoint,
                test_scenario="Validação de Métricas de Performance",
                status="FAILED",
                severity="CRÍTICO",
                details="Campo 'meta' não encontrado na resposta",
                execution_time_ms=execution_time
            )
        
        meta = data["meta"]
        
        # Valida presença de performance
        if "performance" not in meta:
            return ScalabilityTestResult(
                timestamp_utc=timestamp_utc,
                service_tested=service,
                endpoint_tested=endpoint,
                test_scenario="Validação de Métricas de Performance",
                status="FAILED",
                severity="CRÍTICO",
                details="Campo 'meta.performance' não encontrado na resposta",
                execution_time_ms=execution_time
            )
        
        performance = meta["performance"]
        missing_fields = []
        
        # Valida campos críticos de performance
        if "processing_time_ms" not in performance:
            missing_fields.append("processing_time_ms")
        if "items_in_response" not in performance:
            missing_fields.append("items_in_response")
        
        if missing_fields:
            return ScalabilityTestResult(
                timestamp_utc=timestamp_utc,
                service_tested=service,
                endpoint_tested=endpoint,
                test_scenario="Validação de Métricas de Performance",
                status="FAILED",
                severity="CRÍTICO",
                details=f"Campos faltando em performance: {', '.join(missing_fields)}",
                execution_time_ms=execution_time
            )
        
        # Valida tipos de dados
        try:
            processing_time = int(performance["processing_time_ms"])
            items_count = int(performance["items_in_response"])
        except (ValueError, TypeError):
            return ScalabilityTestResult(
                timestamp_utc=timestamp_utc,
                service_tested=service,
                endpoint_tested=endpoint,
                test_scenario="Validação de Métricas de Performance",
                status="FAILED",
                severity="CRÍTICO",
                details="Campos de performance não são numéricos válidos",
                execution_time_ms=execution_time
            )
        
        return ScalabilityTestResult(
            timestamp_utc=timestamp_utc,
            service_tested=service,
            endpoint_tested=endpoint,
            test_scenario="Validação de Métricas de Performance",
            status="PASSED",
            severity="CRÍTICO",
            details=f"Métricas válidas: processing_time={processing_time}ms, items={items_count}",
            execution_time_ms=execution_time
        )
    
    except requests.exceptions.RequestException as e:
        execution_time = (time.time() - start_time) * 1000
        return ScalabilityTestResult(
            timestamp_utc=timestamp_utc,
            service_tested=service,
            endpoint_tested=endpoint,
            test_scenario="Validação de Métricas de Performance",
            status="FAILED",
            severity="CRÍTICO",
            details=f"Erro na requisição: {str(e)}",
            execution_time_ms=execution_time
        )


def test_latency_limits(endpoint: str, service: str) -> ScalabilityTestResult:
    """
    ALTO: Validação de Limites de Latência
    Valida se processing_time_ms está dentro dos limites aceitáveis
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
            return ScalabilityTestResult(
                timestamp_utc=timestamp_utc,
                service_tested=service,
                endpoint_tested=endpoint,
                test_scenario="Validação de Limites de Latência",
                status="FAILED",
                severity="ALTO",
                details=f"Endpoint retornou status {response.status_code} ao invés de 200 OK",
                execution_time_ms=execution_time
            )
        
        try:
            data = response.json()
        except json.JSONDecodeError:
            return ScalabilityTestResult(
                timestamp_utc=timestamp_utc,
                service_tested=service,
                endpoint_tested=endpoint,
                test_scenario="Validação de Limites de Latência",
                status="FAILED",
                severity="ALTO",
                details="Resposta não é um JSON válido",
                execution_time_ms=execution_time
            )
        
        # Valida presença das métricas de performance
        if "meta" not in data or "performance" not in data["meta"]:
            return ScalabilityTestResult(
                timestamp_utc=timestamp_utc,
                service_tested=service,
                endpoint_tested=endpoint,
                test_scenario="Validação de Limites de Latência",
                status="FAILED",
                severity="ALTO",
                details="Métricas de performance não encontradas na resposta",
                execution_time_ms=execution_time
            )
        
        performance = data["meta"]["performance"]
        
        if "processing_time_ms" not in performance:
            return ScalabilityTestResult(
                timestamp_utc=timestamp_utc,
                service_tested=service,
                endpoint_tested=endpoint,
                test_scenario="Validação de Limites de Latência",
                status="FAILED",
                severity="ALTO",
                details="Campo 'processing_time_ms' não encontrado",
                execution_time_ms=execution_time
            )
        
        try:
            processing_time = int(performance["processing_time_ms"])
        except (ValueError, TypeError):
            return ScalabilityTestResult(
                timestamp_utc=timestamp_utc,
                service_tested=service,
                endpoint_tested=endpoint,
                test_scenario="Validação de Limites de Latência",
                status="FAILED",
                severity="ALTO",
                details="processing_time_ms não é um valor numérico válido",
                execution_time_ms=execution_time
            )
        
        # Valida se está dentro do limite aceitável
        if processing_time > MAX_LATENCY_MS:
            return ScalabilityTestResult(
                timestamp_utc=timestamp_utc,
                service_tested=service,
                endpoint_tested=endpoint,
                test_scenario="Validação de Limites de Latência",
                status="FAILED",
                severity="ALTO",
                details=f"Latência excede limite: {processing_time}ms > {MAX_LATENCY_MS}ms",
                execution_time_ms=execution_time
            )
        
        return ScalabilityTestResult(
            timestamp_utc=timestamp_utc,
            service_tested=service,
            endpoint_tested=endpoint,
            test_scenario="Validação de Limites de Latência",
            status="PASSED",
            severity="ALTO",
            details=f"Latência dentro do limite: {processing_time}ms ≤ {MAX_LATENCY_MS}ms",
            execution_time_ms=execution_time
        )
    
    except requests.exceptions.RequestException as e:
        execution_time = (time.time() - start_time) * 1000
        return ScalabilityTestResult(
            timestamp_utc=timestamp_utc,
            service_tested=service,
            endpoint_tested=endpoint,
            test_scenario="Validação de Limites de Latência",
            status="FAILED",
            severity="ALTO",
            details=f"Erro na requisição: {str(e)}",
            execution_time_ms=execution_time
        )


def test_throughput_consistency(endpoint: str, service: str) -> ScalabilityTestResult:
    """
    ALTO: Validação de Throughput
    Valida se items_in_response está dentro dos limites esperados
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
            return ScalabilityTestResult(
                timestamp_utc=timestamp_utc,
                service_tested=service,
                endpoint_tested=endpoint,
                test_scenario="Validação de Throughput",
                status="FAILED",
                severity="ALTO",
                details=f"Endpoint retornou status {response.status_code} ao invés de 200 OK",
                execution_time_ms=execution_time
            )
        
        try:
            data = response.json()
        except json.JSONDecodeError:
            return ScalabilityTestResult(
                timestamp_utc=timestamp_utc,
                service_tested=service,
                endpoint_tested=endpoint,
                test_scenario="Validação de Throughput",
                status="FAILED",
                severity="ALTO",
                details="Resposta não é um JSON válido",
                execution_time_ms=execution_time
            )
        
        # Valida presença das métricas
        if "meta" not in data or "performance" not in data["meta"]:
            return ScalabilityTestResult(
                timestamp_utc=timestamp_utc,
                service_tested=service,
                endpoint_tested=endpoint,
                test_scenario="Validação de Throughput",
                status="FAILED",
                severity="ALTO",
                details="Métricas de performance não encontradas na resposta",
                execution_time_ms=execution_time
            )
        
        performance = data["meta"]["performance"]
        
        if "items_in_response" not in performance:
            return ScalabilityTestResult(
                timestamp_utc=timestamp_utc,
                service_tested=service,
                endpoint_tested=endpoint,
                test_scenario="Validação de Throughput",
                status="FAILED",
                severity="ALTO",
                details="Campo 'items_in_response' não encontrado",
                execution_time_ms=execution_time
            )
        
        try:
            items_count = int(performance["items_in_response"])
        except (ValueError, TypeError):
            return ScalabilityTestResult(
                timestamp_utc=timestamp_utc,
                service_tested=service,
                endpoint_tested=endpoint,
                test_scenario="Validação de Throughput",
                status="FAILED",
                severity="ALTO",
                details="items_in_response não é um valor numérico válido",
                execution_time_ms=execution_time
            )
        
        # Valida se está dentro dos limites esperados
        if items_count < MIN_ITEMS_EXPECTED:
            return ScalabilityTestResult(
                timestamp_utc=timestamp_utc,
                service_tested=service,
                endpoint_tested=endpoint,
                test_scenario="Validação de Throughput",
                status="FAILED",
                severity="ALTO",
                details=f"Número de itens abaixo do mínimo: {items_count} < {MIN_ITEMS_EXPECTED}",
                execution_time_ms=execution_time
            )
        
        if items_count > MAX_ITEMS_PER_PAGE:
            return ScalabilityTestResult(
                timestamp_utc=timestamp_utc,
                service_tested=service,
                endpoint_tested=endpoint,
                test_scenario="Validação de Throughput",
                status="FAILED",
                severity="ALTO",
                details=f"Número de itens excede máximo: {items_count} > {MAX_ITEMS_PER_PAGE}",
                execution_time_ms=execution_time
            )
        
        # Valida consistência com campo data (se disponível)
        validation_details = f"Throughput adequado: {items_count} itens"
        
        if "data" in data and isinstance(data["data"], list):
            actual_items = len(data["data"])
            if actual_items != items_count:
                return ScalabilityTestResult(
                    timestamp_utc=timestamp_utc,
                    service_tested=service,
                    endpoint_tested=endpoint,
                    test_scenario="Validação de Throughput",
                    status="FAILED",
                    severity="ALTO",
                    details=f"Inconsistência: items_in_response={items_count} mas data contém {actual_items} itens",
                    execution_time_ms=execution_time
                )
            validation_details += f" (consistente com array data)"
        
        return ScalabilityTestResult(
            timestamp_utc=timestamp_utc,
            service_tested=service,
            endpoint_tested=endpoint,
            test_scenario="Validação de Throughput",
            status="PASSED",
            severity="ALTO",
            details=validation_details,
            execution_time_ms=execution_time
        )
    
    except requests.exceptions.RequestException as e:
        execution_time = (time.time() - start_time) * 1000
        return ScalabilityTestResult(
            timestamp_utc=timestamp_utc,
            service_tested=service,
            endpoint_tested=endpoint,
            test_scenario="Validação de Throughput",
            status="FAILED",
            severity="ALTO",
            details=f"Erro na requisição: {str(e)}",
            execution_time_ms=execution_time
        )


def run_all_tests() -> List[ScalabilityTestResult]:
    """Executa todos os testes em todos os endpoints"""
    results = []
    
    print("\n" + "="*80)
    print("EXECUTANDO TESTES AUTOMATIZADOS DE ESCALABILIDADE")
    print("="*80)
    print(f"\nTotal de endpoints: {len(ENDPOINTS_TO_TEST)}")
    print(f"Total de cenários: 3")
    print(f"Total de testes: {len(ENDPOINTS_TO_TEST) * 3}")
    print("\n" + "-"*80 + "\n")
    
    for endpoint_info in ENDPOINTS_TO_TEST:
        service = endpoint_info["service"]
        endpoint = endpoint_info["endpoint"]
        
        print(f"Testando {service.upper()}: {endpoint}")
        
        # Teste 1: Validação de Métricas de Performance (CRÍTICO)
        result1 = test_performance_metrics(endpoint, service)
        results.append(result1)
        print(f"  ✓ Métricas de Performance: {result1.status}")
        
        # Teste 2: Validação de Limites de Latência (ALTO)
        result2 = test_latency_limits(endpoint, service)
        results.append(result2)
        print(f"  ✓ Limites de Latência: {result2.status}")
        
        # Teste 3: Validação de Throughput (ALTO)
        result3 = test_throughput_consistency(endpoint, service)
        results.append(result3)
        print(f"  ✓ Throughput: {result3.status}")
        
        print()
    
    return results


def save_results_to_csv(results: List[ScalabilityTestResult]) -> None:
    """Salva resultados em arquivo CSV com encoding UTF-8"""
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
    
    # Salva arquivo principal
    with open(CSV_OUTPUT_PATH, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for result in results:
            writer.writerow(result.to_csv_row())
    
    print(f"\n✓ Resultados salvos em: {CSV_OUTPUT_PATH}")
    
    # Salva cópia com timestamp no histórico
    history_dir = CSV_OUTPUT_PATH.parent / "test_scalability_results_history"
    history_dir.mkdir(exist_ok=True)
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    history_file = history_dir / f"test_scalability_results_{timestamp}.csv"
    
    with open(history_file, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for result in results:
            writer.writerow(result.to_csv_row())
    
    print(f"✓ Cópia histórica salva em: {history_file}")


def save_execution_metadata(results: List[ScalabilityTestResult], started_at: datetime, finished_at: datetime) -> None:
    """Salva metadados da execução em JSON"""
    meta_path = CSV_OUTPUT_PATH.parent / "test_scalability_results_meta.json"
    
    duration = (finished_at - started_at).total_seconds()
    
    total = len(results)
    passed = sum(1 for r in results if r.status == "PASSED")
    failed = sum(1 for r in results if r.status == "FAILED")
    critical_failed = sum(1 for r in results if r.status == "FAILED" and r.severity == "CRÍTICO")
    
    metadata = {
        "started_at_utc": started_at.isoformat(),
        "finished_at_utc": finished_at.isoformat(),
        "duration_seconds": round(duration, 2),
        "total_tests": total,
        "passed": passed,
        "failed": failed,
        "critical_failed": critical_failed,
        "pass_rate": round(passed / total * 100, 1) if total > 0 else 0
    }
    
    with open(meta_path, 'w', encoding='utf-8') as f:
        json.dump(metadata, f, indent=2, ensure_ascii=False)
    
    print(f"✓ Metadados salvos em: {meta_path}")


def print_summary(results: List[ScalabilityTestResult]) -> None:
    """Imprime resumo dos resultados"""
    total = len(results)
    passed = sum(1 for r in results if r.status == "PASSED")
    failed = sum(1 for r in results if r.status == "FAILED")
    critical_failed = sum(1 for r in results if r.status == "FAILED" and r.severity == "CRÍTICO")
    
    print("\n" + "="*80)
    print("RESUMO DA EXECUÇÃO")
    print("="*80)
    print(f"\nTotal de testes: {total}")
    print(f"✓ Aprovados: {passed} ({passed/total*100:.1f}%)")
    print(f"✗ Falharam: {failed} ({failed/total*100:.1f}%)")
    print(f"⚠ Falhas críticas: {critical_failed}")
    print("\n" + "="*80 + "\n")


def main():
    """Função principal"""
    # Configura encoding UTF-8 para saída no Windows
    import sys
    import io
    if sys.platform == 'win32':
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
        sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')
    
    print("\n🚀 Iniciando testes automatizados de conformidade de escalabilidade...")
    
    started_at = datetime.now(timezone.utc)
    
    try:
        results = run_all_tests()
        
        finished_at = datetime.now(timezone.utc)
        
        save_results_to_csv(results)
        save_execution_metadata(results, started_at, finished_at)
        print_summary(results)
        
        print("✅ Testes concluídos com sucesso!\n")
        
    except Exception as e:
        print(f"\n❌ Erro durante execução dos testes: {str(e)}\n")
        raise


if __name__ == "__main__":
    main()
