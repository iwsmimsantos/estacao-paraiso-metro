"""
Endpoints de Monitoramento e Logs

Rotas para consultar logs, incident queue e métricas do sistema.
"""
import csv
import json
import shutil
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from fastapi import APIRouter, Query, HTTPException
from typing import Optional, List, Dict, Any

from ..monitoring.logger import logger, EventType


router = APIRouter(prefix="/monitoring", tags=["Monitoramento"])


@router.get("/logs")
async def get_logs(
    limit: int = Query(50, ge=1, le=500, description="Número máximo de logs"),
    user_id: Optional[str] = Query(None, description="Filtrar por usuário"),
    event_type: Optional[str] = Query(None, description="Filtrar por tipo de evento"),
    status: Optional[str] = Query(None, description="Filtrar por status (success, failed, denied)")
):
    """
    Recupera logs de auditoria com filtros opcionais
    
    Retorna os logs mais recentes primeiro
    """
    logs = logger.get_logs(
        limit=limit,
        user_id=user_id,
        event_type=event_type,
        status=status
    )
    
    return {
        "total": len(logs),
        "limit": limit,
        "filters": {
            "user_id": user_id,
            "event_type": event_type,
            "status": status
        },
        "logs": logs
    }


@router.get("/logs/trace/{trace_id}")
async def get_log_by_trace(trace_id: str):
    """Busca log específico por trace_id"""
    log = logger.get_log_by_trace_id(trace_id)
    
    if not log:
        return {
            "found": False,
            "trace_id": trace_id,
            "message": "Log não encontrado"
        }
    
    return {
        "found": True,
        "log": log
    }


@router.get("/logs/correlation/{correlation_id}")
async def get_logs_by_correlation(correlation_id: str):
    """
    Busca todos os logs de uma mesma transação (correlation_id)
    
    Útil para rastrear uma operação completa que gerou múltiplos eventos
    """
    logs = logger.get_logs_by_correlation_id(correlation_id)
    
    return {
        "correlation_id": correlation_id,
        "total": len(logs),
        "logs": logs
    }


@router.get("/incidents")
async def get_incidents(
    limit: int = Query(50, ge=1, le=500, description="Número máximo de incidentes"),
    severity: Optional[str] = Query(None, description="Filtrar por severidade (low, medium, high, critical)")
):
    """
    Recupera incident queue com incidentes de segurança
    
    Incidentes incluem:
    - Tentativas de acesso negado
    - Violações de guardrails de IA
    - Inconsistências de dados (mismatch)
    - Erros críticos do sistema
    """
    incidents = logger.get_incidents(
        limit=limit,
        severity=severity
    )
    
    return {
        "total": len(incidents),
        "limit": limit,
        "severity_filter": severity,
        "incidents": incidents
    }


@router.get("/stats")
async def get_statistics():
    """
    Retorna estatísticas gerais do sistema
    
    Inclui contadores de eventos, taxa de erro, usuários ativos, etc.
    """
    all_logs = logger.get_logs(limit=1000)
    all_incidents = logger.get_incidents(limit=1000)
    
    # Conta eventos por tipo
    event_counts = {}
    status_counts = {"success": 0, "failed": 0, "denied": 0, "incident": 0}
    user_activity = {}
    
    for log in all_logs:
        # Verifica se é um dict válido (ignora dados corrompidos)
        if not isinstance(log, dict):
            continue
            
        event_type = log.get("event_type", "unknown")
        event_counts[event_type] = event_counts.get(event_type, 0) + 1
        
        status = log.get("status", "unknown")
        if status in status_counts:
            status_counts[status] += 1
        
        user_id = log.get("user_id")
        if user_id:
            user_activity[user_id] = user_activity.get(user_id, 0) + 1
    
    # Conta incidentes por severidade
    incident_severity = {"low": 0, "medium": 0, "high": 0, "critical": 0}
    for incident in all_incidents:
        # Verifica se é um dict válido
        if not isinstance(incident, dict):
            continue
            
        severity = incident.get("details", {}).get("severity", "unknown")
        if severity in incident_severity:
            incident_severity[severity] += 1
    
    # Calcula taxa de erro
    total_operations = sum(status_counts.values())
    error_rate = 0
    if total_operations > 0:
        error_rate = round((status_counts["failed"] + status_counts["denied"]) / total_operations * 100, 2)
    
    return {
        "summary": {
            "total_logs": len(all_logs),
            "total_incidents": len(all_incidents),
            "total_operations": total_operations,
            "error_rate_percent": error_rate
        },
        "status_counts": status_counts,
        "event_counts": event_counts,
        "incident_severity": incident_severity,
        "top_users": sorted(user_activity.items(), key=lambda x: x[1], reverse=True)[:10]
    }


@router.get("/event-types")
async def get_event_types():
    """Lista todos os tipos de eventos suportados pelo sistema"""
    return {
        "event_types": [
            {
                "name": event.name,
                "value": event.value,
                "category": event.value.split('.')[0]
            }
            for event in EventType
        ]
    }


@router.get("/compliance-results")
async def get_compliance_results():
    """
    Retorna resultados dos testes automatizados de conformidade
    
    Lê o arquivo CSV gerado pelo script de teste e retorna os dados
    para exibição no dashboard.
    """
    csv_path = Path(__file__).parent.parent.parent / "test_results.csv"
    
    if not csv_path.exists():
        return {
            "available": False,
            "message": "Arquivo de resultados não encontrado. Execute o script de teste primeiro.",
            "results": [],
            "summary": {
                "total": 0,
                "passed": 0,
                "failed": 0,
                "critical_failed": 0
            }
        }
    
    try:
        results = []
        with open(csv_path, 'r', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                results.append(row)
        
        # Calcula estatísticas
        total = len(results)
        passed = sum(1 for r in results if r.get("status") == "PASSED")
        failed = sum(1 for r in results if r.get("status") == "FAILED")
        critical_failed = sum(1 for r in results if r.get("status") == "FAILED" and r.get("severity") == "CRÍTICO")
        
        summary = {
            "total": total,
            "passed": passed,
            "failed": failed,
            "critical_failed": critical_failed,
            "pass_rate": round(passed / total * 100, 1) if total > 0 else 0,
        }

        # Tenta enriquecer com metadados da última execução, se existirem
        meta_path = csv_path.parent / "test_results_meta.json"
        if meta_path.exists():
            try:
                with open(meta_path, "r", encoding="utf-8") as meta_file:
                    meta_data = json.load(meta_file)
                summary.update(
                    {
                        "started_at_utc": meta_data.get("started_at_utc"),
                        "finished_at_utc": meta_data.get("finished_at_utc"),
                        "duration_seconds": meta_data.get("duration_seconds"),
                    }
                )
            except Exception:
                # Se não conseguir ler o meta, segue apenas com o resumo básico
                pass

        return {
            "available": True,
            "results": results,
            "summary": summary,
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao ler arquivo CSV: {str(e)}")


@router.post("/run-compliance-tests")
async def run_compliance_tests():
    """
    Executa o script de testes de conformidade e retorna o resumo da execução.

    - Roda o script test_compliance_automated.py
    - Atualiza o arquivo test_results.csv
    - Salva uma cópia com timestamp em test_results_history/
    - Atualiza o arquivo test_results_meta.json com metadados da execução
    """
    base_path = Path(__file__).parent.parent.parent
    script_path = base_path / "test_compliance_automated.py"
    csv_path = base_path / "test_results.csv"

    if not script_path.exists():
        raise HTTPException(
            status_code=500,
            detail="Script de testes automatizados não encontrado.",
        )

    started_dt = datetime.now(timezone.utc)
    started_at_utc = started_dt.replace(microsecond=0).isoformat().replace('+00:00', 'Z')

    try:
        completed = subprocess.run(
            [sys.executable, str(script_path)],
            cwd=str(base_path),
            capture_output=True,
            text=True,
            timeout=600,
        )
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Erro ao executar script de testes: {str(e)}",
        )

    finished_dt = datetime.now(timezone.utc)
    finished_at_utc = finished_dt.replace(microsecond=0).isoformat().replace('+00:00', 'Z')
    duration_seconds = (finished_dt - started_dt).total_seconds()

    if completed.returncode != 0:
        raise HTTPException(
            status_code=500,
            detail={
                "message": "Script de testes retornou código de erro.",
                "return_code": completed.returncode,
                "stderr": completed.stderr,
            },
        )

    if not csv_path.exists():
        raise HTTPException(
            status_code=500,
            detail="Arquivo de resultados não encontrado após execução dos testes.",
        )

    # Lê o CSV gerado para montar o resumo e registrar logs permanentemente
    try:
        results: List[Dict[str, Any]] = []
        with open(csv_path, "r", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                results.append(row)

        total = len(results)
        passed = sum(1 for r in results if r.get("status") == "PASSED")
        failed = sum(1 for r in results if r.get("status") == "FAILED")
        critical_failed = sum(
            1
            for r in results
            if r.get("status") == "FAILED" and r.get("severity") == "CRÍTICO"
        )
        pass_rate = round(passed / total * 100, 1) if total > 0 else 0.0

        summary = {
            "total": total,
            "passed": passed,
            "failed": failed,
            "critical_failed": critical_failed,
            "pass_rate": pass_rate,
        }
        
        # Registra execução dos testes no sistema de logs
        logger.log(
            event_type=EventType.TEST_COMPLIANCE_RUN,
            user_id="system",
            resource_type="test_suite",
            resource_id="compliance_tests",
            action="execute",
            status="success" if failed == 0 else "failed",
            details={
                "test_type": "compliance",
                "started_at_utc": started_at_utc,
                "finished_at_utc": finished_at_utc,
                "duration_seconds": duration_seconds,
                "total": total,
                "passed": passed,
                "failed": failed,
                "critical_failed": critical_failed,
                "pass_rate": pass_rate
            }
        )
        
        # Registra cada teste individual no sistema de logs
        for test_result in results:
            test_status = "success" if test_result.get("status") == "PASSED" else "failed"
            logger.log(
                event_type=EventType.TEST_COMPLIANCE_RESULT,
                user_id="system",
                resource_type="test",
                resource_id=test_result.get("service_tested", "unknown"),
                action=test_result.get("endpoint_tested", "N/A"),
                status=test_status,
                details={
                    "test_scenario": test_result.get("test_scenario"),
                    "service_tested": test_result.get("service_tested"),
                    "endpoint_tested": test_result.get("endpoint_tested"),
                    "severity": test_result.get("severity"),
                    "execution_time_ms": test_result.get("execution_time_ms"),
                    "details": test_result.get("details"),
                    "timestamp_utc": test_result.get("timestamp_utc")
                }
            )
            
            # Registra falhas críticas como incidentes
            if test_result.get("status") == "FAILED" and test_result.get("severity") == "CRÍTICO":
                logger.log_incident(
                    incident_type="test_compliance_critical_failure",
                    severity="critical",
                    user_id="system",
                    resource_id=test_result.get("service_tested", "unknown"),
                    description=f"Falha crítica em teste de conformidade: {test_result.get('test_scenario')}",
                    details={
                        "test_scenario": test_result.get("test_scenario"),
                        "service_tested": test_result.get("service_tested"),
                        "endpoint_tested": test_result.get("endpoint_tested"),
                        "execution_time_ms": test_result.get("execution_time_ms"),
                        "details": test_result.get("details")
                    }
                )
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Erro ao ler resultados de conformidade: {str(e)}",
        )

    # Salva histórico em CSV com timestamp seguro para nome de arquivo
    try:
        history_dir = base_path / "test_results_history"
        history_dir.mkdir(parents=True, exist_ok=True)
        timestamp_for_filename = started_dt.strftime("%Y%m%dT%H%M%S")
        history_csv_path = history_dir / f"test_results_{timestamp_for_filename}.csv"
        shutil.copy2(csv_path, history_csv_path)
    except Exception:
        # Se o histórico falhar, não impede a resposta principal
        pass

    # Salva metadados da última execução em JSON para uso pelo dashboard
    try:
        meta_path = base_path / "test_results_meta.json"
        meta_data = {
            "started_at_utc": started_at_utc,
            "finished_at_utc": finished_at_utc,
            "duration_seconds": duration_seconds,
            "summary": summary,
        }
        with open(meta_path, "w", encoding="utf-8") as meta_file:
            json.dump(meta_data, meta_file, ensure_ascii=False, indent=2)
    except Exception:
        # Falha ao salvar metadados não deve quebrar o endpoint
        pass

    return {
        "status": "completed",
        "started_at_utc": started_at_utc,
        "finished_at_utc": finished_at_utc,
        "duration_seconds": duration_seconds,
        "summary": summary,
    }


@router.get("/scalability-results")
async def get_scalability_results():
    """
    Retorna resultados dos testes automatizados de conformidade de escalabilidade
    
    Lê o arquivo CSV gerado pelo script de teste e retorna os dados
    para exibição no dashboard.
    """
    csv_path = Path(__file__).parent.parent.parent / "test_scalability_results.csv"
    
    if not csv_path.exists():
        return {
            "available": False,
            "message": "Arquivo de resultados não encontrado. Execute o script de teste primeiro.",
            "results": [],
            "summary": {
                "total": 0,
                "passed": 0,
                "failed": 0,
                "critical_failed": 0
            }
        }
    
    try:
        results = []
        with open(csv_path, 'r', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                results.append(row)
        
        # Calcula estatísticas
        total = len(results)
        passed = sum(1 for r in results if r.get("status") == "PASSED")
        failed = sum(1 for r in results if r.get("status") == "FAILED")
        critical_failed = sum(1 for r in results if r.get("status") == "FAILED" and r.get("severity") == "CRÍTICO")
        
        summary = {
            "total": total,
            "passed": passed,
            "failed": failed,
            "critical_failed": critical_failed,
            "pass_rate": round(passed / total * 100, 1) if total > 0 else 0,
        }

        # Tenta enriquecer com metadados da última execução, se existirem
        meta_path = csv_path.parent / "test_scalability_results_meta.json"
        if meta_path.exists():
            try:
                with open(meta_path, "r", encoding="utf-8") as meta_file:
                    meta_data = json.load(meta_file)
                summary.update(
                    {
                        "started_at_utc": meta_data.get("started_at_utc"),
                        "finished_at_utc": meta_data.get("finished_at_utc"),
                        "duration_seconds": meta_data.get("duration_seconds"),
                    }
                )
            except Exception:
                # Se não conseguir ler o meta, segue apenas com o resumo básico
                pass

        return {
            "available": True,
            "results": results,
            "summary": summary,
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao ler arquivo CSV: {str(e)}")


@router.post("/run-scalability-tests")
async def run_scalability_tests():
    """
    Executa o script de testes de conformidade de escalabilidade e retorna o resumo da execução.

    - Roda o script test_scalability_automated.py
    - Atualiza o arquivo test_scalability_results.csv
    - Salva uma cópia com timestamp em test_scalability_results_history/
    - Atualiza o arquivo test_scalability_results_meta.json com metadados da execução
    """
    base_path = Path(__file__).parent.parent.parent
    script_path = base_path / "test_scalability_automated.py"
    csv_path = base_path / "test_scalability_results.csv"

    if not script_path.exists():
        raise HTTPException(
            status_code=500,
            detail="Script de testes de escalabilidade não encontrado.",
        )

    started_dt = datetime.now(timezone.utc)
    started_at_utc = started_dt.replace(microsecond=0).isoformat().replace('+00:00', 'Z')

    try:
        completed = subprocess.run(
            [sys.executable, str(script_path)],
            cwd=str(base_path),
            capture_output=True,
            text=True,
            timeout=600,
        )
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Erro ao executar script de testes de escalabilidade: {str(e)}",
        )

    finished_dt = datetime.now(timezone.utc)
    finished_at_utc = finished_dt.replace(microsecond=0).isoformat().replace('+00:00', 'Z')
    duration_seconds = (finished_dt - started_dt).total_seconds()

    if completed.returncode != 0:
        raise HTTPException(
            status_code=500,
            detail={
                "message": "Script de testes de escalabilidade retornou código de erro.",
                "return_code": completed.returncode,
                "stderr": completed.stderr,
            },
        )

    if not csv_path.exists():
        raise HTTPException(
            status_code=500,
            detail="Arquivo de resultados de escalabilidade não encontrado após execução dos testes.",
        )

    # Lê o CSV gerado para montar o resumo
    try:
        results: List[Dict[str, Any]] = []
        with open(csv_path, "r", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                results.append(row)

        total = len(results)
        passed = sum(1 for r in results if r.get("status") == "PASSED")
        failed = sum(1 for r in results if r.get("status") == "FAILED")
        critical_failed = sum(
            1
            for r in results
            if r.get("status") == "FAILED" and r.get("severity") == "CRÍTICO"
        )
        pass_rate = round(passed / total * 100, 1) if total > 0 else 0.0

        summary = {
            "total": total,
            "passed": passed,
            "failed": failed,
            "critical_failed": critical_failed,
            "pass_rate": pass_rate,
        }
        
        # Registra execução dos testes no sistema de logs
        logger.log(
            event_type=EventType.TEST_SCALABILITY_RUN,
            user_id="system",
            resource_type="test_suite",
            resource_id="scalability_tests",
            action="execute",
            status="success" if failed == 0 else "failed",
            details={
                "test_type": "scalability",
                "started_at_utc": started_at_utc,
                "finished_at_utc": finished_at_utc,
                "duration_seconds": duration_seconds,
                "total": total,
                "passed": passed,
                "failed": failed,
                "critical_failed": critical_failed,
                "pass_rate": pass_rate
            }
        )
        
        # Registra cada teste individual no sistema de logs
        for test_result in results:
            test_status = "success" if test_result.get("status") == "PASSED" else "failed"
            logger.log(
                event_type=EventType.TEST_SCALABILITY_RESULT,
                user_id="system",
                resource_type="test",
                resource_id=test_result.get("service_tested", "unknown"),
                action=test_result.get("endpoint_tested", "N/A"),
                status=test_status,
                details={
                    "test_scenario": test_result.get("test_scenario"),
                    "service_tested": test_result.get("service_tested"),
                    "endpoint_tested": test_result.get("endpoint_tested"),
                    "severity": test_result.get("severity"),
                    "execution_time_ms": test_result.get("execution_time_ms"),
                    "details": test_result.get("details"),
                    "timestamp_utc": test_result.get("timestamp_utc")
                }
            )
            
            # Registra falhas críticas como incidentes
            if test_result.get("status") == "FAILED" and test_result.get("severity") == "CRÍTICO":
                logger.log_incident(
                    incident_type="test_scalability_critical_failure",
                    severity="critical",
                    user_id="system",
                    resource_id=test_result.get("service_tested", "unknown"),
                    description=f"Falha crítica em teste de escalabilidade: {test_result.get('test_scenario')}",
                    details={
                        "test_scenario": test_result.get("test_scenario"),
                        "service_tested": test_result.get("service_tested"),
                        "endpoint_tested": test_result.get("endpoint_tested"),
                        "execution_time_ms": test_result.get("execution_time_ms"),
                        "details": test_result.get("details")
                    }
                )
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Erro ao ler resultados de escalabilidade: {str(e)}",
        )

    # Salva histórico em CSV com timestamp seguro para nome de arquivo
    try:
        history_dir = base_path / "test_scalability_results_history"
        history_dir.mkdir(parents=True, exist_ok=True)
        timestamp_for_filename = started_dt.strftime("%Y%m%dT%H%M%S")
        history_csv_path = history_dir / f"test_scalability_results_{timestamp_for_filename}.csv"
        shutil.copy2(csv_path, history_csv_path)
    except Exception:
        # Se o histórico falhar, não impede a resposta principal
        pass

    # Salva metadados da última execução em JSON para uso pelo dashboard
    try:
        meta_path = base_path / "test_scalability_results_meta.json"
        meta_data = {
            "started_at_utc": started_at_utc,
            "finished_at_utc": finished_at_utc,
            "duration_seconds": duration_seconds,
            "summary": summary,
        }
        with open(meta_path, "w", encoding="utf-8") as meta_file:
            json.dump(meta_data, meta_file, ensure_ascii=False, indent=2)
    except Exception:
        # Falha ao salvar metadados não deve quebrar o endpoint
        pass

    return {
        "status": "completed",
        "started_at_utc": started_at_utc,
        "finished_at_utc": finished_at_utc,
        "duration_seconds": duration_seconds,
        "summary": summary,
    }
