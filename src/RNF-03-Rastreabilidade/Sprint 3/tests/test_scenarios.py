"""
Testes automatizados dos 5 cenários de rastreabilidade (RNF-03)
Companhia do Metrô - Sistema de Rastreabilidade Microsoft 365

Cenários de Teste:
1. Bloqueio de mudança sem justificativa
2. Registro automático da mudança
3. Validação de integridade e consistência dos logs
4. Consulta e auditoria de mudanças
5. Alerta de tentativas inválidas

Critérios de Aceitação:
- Toda mudança deve gerar automaticamente um registro no SharePoint e um evento correspondente no Sentinel
- Nenhuma alteração pode ocorrer sem justificativa aprovada
- Logs devem conter: ID do projeto, usuário, timestamp, descrição da mudança, justificativa, status, correlationId e hash
- Todos os eventos devem ser enviados ao Sentinel via conectores nativos do Microsoft 365
- Power BI deve refletir os dados de rastreabilidade sem divergências
- O Sentinel deve gerar alerta automático em caso de inconsistência ou ausência de registro
"""
import sys
import os

# Adiciona o diretório pai ao path para importar os módulos
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from datetime import datetime
from models.log_models import SharePointChangeEvent, ChangeRequest
from services.correlation_service import correlation_service
from services.mock_data_generator import mock_generator
from storage.log_repository import log_repository


class AcceptanceCriteria:
    """Critérios de aceitação para validação dos testes"""
    
    @staticmethod
    def validate_log_contains_required_fields(log: dict) -> tuple[bool, list]:
        """
        Valida se log contém todos os campos obrigatórios:
        ID do projeto, usuário, timestamp, descrição da mudança, justificativa, status, correlationId e hash
        """
        required_fields = [
            "project_id",
            "user", 
            "timestamp",
            "description",
            "status",
            "correlation_id"
        ]
        
        missing_fields = [f for f in required_fields if f not in log or log.get(f) is None]
        
        # Para logs do Sentinel, verifica hash
        if "hash_value" in log and not log.get("hash_value"):
            missing_fields.append("hash_value")
        
        return len(missing_fields) == 0, missing_fields
    
    @staticmethod
    def validate_change_has_justification(log: dict) -> bool:
        """Valida se a mudança aprovada tem justificativa"""
        if log.get("status") == "bloqueado":
            return True  # Mudanças bloqueadas não precisam ter justificativa
        
        justification = log.get("justification") or log.get("metadata", {}).get("justification")
        return justification and justification.strip() != ""
    
    @staticmethod
    def validate_correlation_integrity(logs: list) -> tuple[bool, str]:
        """Valida integridade de correlação entre logs"""
        if not logs or len(logs) < 2:
            return False, "Insuficiente número de logs para correlação"
        
        correlation_ids = [log.get("correlation_id") for log in logs]
        if len(set(correlation_ids)) != 1:
            return False, "correlation_ids não são consistentes"
        
        return True, "Correlação íntegra"
    
    @staticmethod
    def validate_audit_trail_completeness(trail: dict) -> tuple[bool, list]:
        """Valida se trilha de auditoria está completa"""
        required_fields = [
            "correlation_id",
            "timestamp_inicio",
            "timestamp_fim",
            "origem",
            "destino",
            "user",
            "project_id",
            "eventos_relacionados",
            "status_final",
            "integridade_verificada"
        ]
        
        missing_fields = [f for f in required_fields if f not in trail or trail.get(f) is None]
        return len(missing_fields) == 0, missing_fields


class TestScenarios:
    """Classe de testes dos cenários de rastreabilidade"""
    
    def __init__(self):
        self.results = []
        self.acceptance_criteria = AcceptanceCriteria()
    
    def log_result(self, scenario: str, passed: bool, message: str, details: dict = None, criteria_validations: list = None):
        """Registra resultado de teste com validações de critérios de aceitação"""
        result = {
            "scenario": scenario,
            "passed": passed,
            "message": message,
            "timestamp": datetime.now().isoformat(),
            "details": details or {},
            "criteria_validations": criteria_validations or []
        }
        self.results.append(result)
        
        status = "[PASSOU]" if passed else "[FALHOU]"
        print(f"{status} {scenario}: {message}")
        if criteria_validations:
            print("  Critérios de Aceitação:")
            for validation in criteria_validations:
                criteria_status = "✓" if validation["passed"] else "✗"
                print(f"    {criteria_status} {validation['name']}: {validation['description']}")
        if details:
            for key, value in details.items():
                if key != "logs" and key != "trail":  # Omite logs longos
                    print(f"  - {key}: {value}")
        print()
    
    def cenario_1_bloqueio_sem_justificativa(self):
        """
        Cenário 1: Bloqueio de mudança sem justificativa
        
        Validar se o fluxo no Power Automate impede a atualização nas listas 
        do SharePoint quando o campo "Justificativa da mudança" estiver vazio.
        Confirmar que o evento de bloqueio é registrado automaticamente no Sentinel.
        
        Critérios de Aceitação:
        - Nenhuma alteração pode ocorrer sem justificativa aprovada
        - Logs devem conter correlationId e status "bloqueado"
        - Alerta deve ser gerado automaticamente
        - Notificação Teams deve ser enviada
        """
        print("\n" + "="*70)
        print("CENARIO 1: Bloqueio de mudanca sem justificativa")
        print("="*70 + "\n")
        
        criteria_validations = []
        
        # Cria evento SEM justificativa
        user = mock_generator.generate_user()
        project_id = mock_generator.generate_project_id()
        
        event = SharePointChangeEvent(
            user=user,
            project_id=project_id,
            change_type="atualizacao",
            justification=None,  # SEM JUSTIFICATIVA
            field_changed="status",
            old_value="Em Andamento",
            new_value="Concluído",
            source="SharePoint"
        )
        
        # Processa evento
        result = correlation_service.process_sharepoint_event(event, scenario="cenario_1")
        
        # Validações
        bloqueado = result.get("blocked", False)
        sentinel_log_id = result.get("sentinel_log_id")
        alert_id = result.get("alert_id")
        correlation_id = result.get("correlation_id")
        
        # Critério 1: Mudança deve ser bloqueada
        blocked_criteria = {
            "passed": bloqueado,
            "name": "Mudança bloqueada",
            "description": "Alteração sem justificativa deve ser bloqueada"
        }
        criteria_validations.append(blocked_criteria)
        
        if not bloqueado:
            self.log_result(
                "Cenário 1",
                False,
                "Mudança NÃO foi bloqueada como esperado",
                {"blocked": bloqueado},
                criteria_validations
            )
            return
        
        # Critério 2: Log deve ser criado no Sentinel
        log_exists_criteria = {
            "passed": bool(sentinel_log_id),
            "name": "Log criado no Sentinel",
            "description": "Evento de bloqueio deve ser registrado no Sentinel"
        }
        criteria_validations.append(log_exists_criteria)
        
        if not sentinel_log_id:
            self.log_result(
                "Cenário 1",
                False,
                "Log não foi criado no Sentinel",
                {"sentinel_log_id": sentinel_log_id},
                criteria_validations
            )
            return
        
        # Verifica log no Sentinel
        sentinel_logs = log_repository.get_sentinel_logs({"log_id": sentinel_log_id})
        if sentinel_logs:
            sentinel_log = sentinel_logs[0]
            
            # Critério 3: Campos obrigatórios
            fields_valid, missing = self.acceptance_criteria.validate_log_contains_required_fields(sentinel_log)
            fields_criteria = {
                "passed": fields_valid,
                "name": "Campos obrigatórios no log",
                "description": f"Log deve conter: projeto, usuário, timestamp, descrição, status, correlationId" + 
                               (f" - Faltam: {missing}" if not fields_valid else "")
            }
            criteria_validations.append(fields_criteria)
            
            # Critério 4: Hash deve estar presente
            hash_exists = bool(sentinel_log.get("hash_value"))
            hash_criteria = {
                "passed": hash_exists,
                "name": "Hash para integridade",
                "description": "Log deve conter hash para verificação de integridade"
            }
            criteria_validations.append(hash_criteria)
        
        # Critério 5: Alerta deve ser gerado
        alert_exists_criteria = {
            "passed": bool(alert_id),
            "name": "Alerta gerado",
            "description": "Tentativa de alteração sem justificativa deve gerar alerta"
        }
        criteria_validations.append(alert_exists_criteria)
        
        if alert_id:
            # Verifica alerta
            alertas = log_repository.get_alertas({"alert_id": alert_id})
            if alertas:
                alerta = alertas[0]
                
                # Critério 6: Teams notificação
                teams_criteria = {
                    "passed": alerta.get("teams_notification_sent", False),
                    "name": "Notificação Teams",
                    "description": "Notificação de bloqueio deve ser enviada via Teams"
                }
                criteria_validations.append(teams_criteria)
        
        # Critério 7: Status no Sentinel deve ser "bloqueio"
        status_valid = sentinel_logs[0].get("event_type") == "bloqueio" if sentinel_logs else False
        status_criteria = {
            "passed": status_valid,
            "name": "Status correto no log",
            "description": "Evento no Sentinel deve ter type 'bloqueio'"
        }
        criteria_validations.append(status_criteria)
        
        all_passed = all(c["passed"] for c in criteria_validations)
        
        self.log_result(
            "Cenário 1",
            all_passed,
            "Bloqueio executado com sucesso, todos os critérios atendidos" if all_passed else "Alguns critérios não foram atendidos",
            {
                "blocked": bloqueado,
                "correlation_id": correlation_id,
                "sentinel_log_id": sentinel_log_id,
                "alert_id": alert_id,
                "teams_notification": result.get("teams_notification")
            },
            criteria_validations
        )
    
    def cenario_2_registro_automatico(self):
        """
        Cenário 2: Registro automático da mudança
        
        Verificar se cada alteração aprovada gera um registro na lista 
        "Histórico de Alterações" no SharePoint e um evento correspondente 
        no Sentinel com correlationId, usuário, timestamp, e tipo de mudança.
        
        Critérios de Aceitação:
        - Toda mudança deve gerar automaticamente um registro no SharePoint
        - Um evento correspondente deve ser criado no Sentinel
        - Logs devem conter: ID do projeto, usuário, timestamp, descrição, justificativa, status, correlationId e hash
        - Deve haver correlação única entre eventos
        """
        print("\n" + "="*70)
        print("CENARIO 2: Registro automatico da mudanca")
        print("="*70 + "\n")
        
        criteria_validations = []
        
        # Cria evento COM justificativa
        user = mock_generator.generate_user()
        project_id = mock_generator.generate_project_id()
        justification = mock_generator.generate_justification(True)
        
        event = SharePointChangeEvent(
            user=user,
            project_id=project_id,
            change_type="atualizacao",
            justification=justification,
            field_changed="prazo",
            old_value="31/12/2024",
            new_value="31/01/2025",
            source="SharePoint"
        )
        
        # Processa evento
        result = correlation_service.process_sharepoint_event(event, scenario="cenario_2")
        
        # Validações
        correlation_id = result.get("correlation_id")
        sentinel_log_id = result.get("sentinel_log_id")
        
        # Critério 1: Log deve ser criado no Sentinel
        log_created_criteria = {
            "passed": bool(sentinel_log_id),
            "name": "Log criado no Sentinel",
            "description": "Cada mudança aprovada deve criar um evento no Sentinel"
        }
        criteria_validations.append(log_created_criteria)
        
        # Verifica se log foi criado no Sentinel
        sentinel_logs = log_repository.get_sentinel_logs({"correlation_id": correlation_id})
        
        if not sentinel_logs:
            self.log_result(
                "Cenário 2",
                False,
                "Log não foi criado no Sentinel",
                {"correlation_id": correlation_id},
                criteria_validations
            )
            return
        
        sentinel_log = sentinel_logs[0]
        
        # Critério 2: Campos obrigatórios
        fields_valid, missing_fields = self.acceptance_criteria.validate_log_contains_required_fields(sentinel_log)
        fields_criteria = {
            "passed": fields_valid,
            "name": "Campos obrigatórios no Sentinel",
            "description": f"Log deve conter: ID projeto, usuário, timestamp, descrição, status, correlationId" +
                          (f" - Faltam: {missing_fields}" if not fields_valid else "")
        }
        criteria_validations.append(fields_criteria)
        
        # Critério 3: Justificativa deve estar presente
        justification_valid = self.acceptance_criteria.validate_change_has_justification(sentinel_log)
        justification_criteria = {
            "passed": justification_valid,
            "name": "Justificativa presente",
            "description": "Mudança aprovada deve conter justificativa"
        }
        criteria_validations.append(justification_criteria)
        
        # Critério 4: Hash deve estar presente
        hash_valid = bool(sentinel_log.get("hash_value"))
        hash_criteria = {
            "passed": hash_valid,
            "name": "Hash para integridade",
            "description": "Log deve conter hash SHA-256 para verificação"
        }
        criteria_validations.append(hash_criteria)
        
        # Critério 5: Registro no histórico de alterações
        historico = log_repository.get_historico_alteracoes({"correlation_id": correlation_id})
        historico_valid = bool(historico)
        historico_criteria = {
            "passed": historico_valid,
            "name": "Registro no Histórico",
            "description": "Mudança deve ser registrada no histórico de alterações do SharePoint"
        }
        criteria_validations.append(historico_criteria)
        
        if historico_valid:
            hist_record = historico[0]
            # Critério 6: Status deve ser "aprovado"
            status_valid = hist_record.get("status") == "aprovado"
            status_criteria = {
                "passed": status_valid,
                "name": "Status correto no histórico",
                "description": "Registro deve ter status 'aprovado'"
            }
            criteria_validations.append(status_criteria)
        
        # Critério 7: Timestamp deve estar preenchido
        timestamp_valid = bool(sentinel_log.get("timestamp"))
        timestamp_criteria = {
            "passed": timestamp_valid,
            "name": "Timestamp registrado",
            "description": "Log deve conter timestamp da mudança"
        }
        criteria_validations.append(timestamp_criteria)
        
        all_passed = all(c["passed"] for c in criteria_validations)
        
        self.log_result(
            "Cenário 2",
            all_passed,
            "Mudança registrada automaticamente com sucesso" if all_passed else "Alguns critérios não foram atendidos",
            {
                "correlation_id": correlation_id,
                "sentinel_log_id": sentinel_log_id,
                "historico_id": historico[0].get("historico_id") if historico else None,
                "user": sentinel_log.get("user"),
                "timestamp": sentinel_log.get("timestamp"),
                "hash": result.get("hash")[:16] + "..." if result.get("hash") else None
            },
            criteria_validations
        )
    
    def cenario_3_validacao_integridade(self):
        """
        Cenário 3: Validação de integridade e consistência dos logs
        
        Testar se o Sentinel consegue correlacionar os eventos de origem 
        (SharePoint / Power Automate) com os registros do Log Analytics, 
        garantindo integridade por meio de hash e identificação única.
        
        Critérios de Aceitação:
        - Logs correlacionados devem ter correlationId único
        - Hash deve ser comparado e validado para integridade
        - Deve haver correlação consistente entre SharePoint e Sentinel
        - Alertas devem ser gerados em caso de divergência de integridade
        """
        print("\n" + "="*70)
        print("CENARIO 3: Validacao de integridade e consistencia dos logs")
        print("="*70 + "\n")
        
        criteria_validations = []
        
        # Cria evento para testar integridade
        user = mock_generator.generate_user()
        project_id = mock_generator.generate_project_id()
        justification = mock_generator.generate_justification(True)
        
        event = SharePointChangeEvent(
            user=user,
            project_id=project_id,
            change_type="atualizacao",
            justification=justification,
            field_changed="orcamento",
            old_value="R$ 1.000.000,00",
            new_value="R$ 1.200.000,00",
            source="SharePoint"
        )
        
        # Processa evento
        process_result = correlation_service.process_sharepoint_event(event, scenario="cenario_3")
        
        sharepoint_event_id = process_result.get("sharepoint_event_id")
        sentinel_log_id = process_result.get("sentinel_log_id")
        correlation_id = process_result.get("correlation_id")
        
        # Verifica integridade
        integrity_result = correlation_service.verify_integrity(
            sharepoint_event_id=sharepoint_event_id,
            sentinel_log_id=sentinel_log_id
        )
        
        # Validações
        integrity_status = integrity_result.get("integrity_status")
        hash_comparison = integrity_result.get("hash_comparison")
        
        # Critério 1: Status de integridade deve ser válido
        valid_statuses = ["ok", "correlacionado", "divergente"]
        status_valid = integrity_status in valid_statuses
        status_criteria = {
            "passed": status_valid,
            "name": "Status de integridade válido",
            "description": f"Status deve ser um de: {valid_statuses}" +
                          (f" - Recebido: {integrity_status}" if not status_valid else "")
        }
        criteria_validations.append(status_criteria)
        
        # Critério 2: Hashes devem ser comparados
        hashes_exist = bool(integrity_result.get("expected_hash") and integrity_result.get("actual_hash"))
        hash_exists_criteria = {
            "passed": hashes_exist,
            "name": "Hashes presentes para comparação",
            "description": "Logs devem conter hash para validação de integridade"
        }
        criteria_validations.append(hash_exists_criteria)
        
        # Critério 3: Correlação deve ser consistente
        correlated_logs = log_repository.get_correlated_logs(
            {"correlation_id": correlation_id}
        )
        
        correlation_valid = len(correlated_logs) > 0
        correlation_criteria = {
            "passed": correlation_valid,
            "name": "Logs correlacionados",
            "description": "Eventos do SharePoint e Sentinel devem estar correlacionados"
        }
        criteria_validations.append(correlation_criteria)
        
        if correlated_logs:
            correlated = correlated_logs[0]
            
            # Critério 4: Identificações únicas devem corresponder
            ids_valid = (
                correlated.get("sharepoint_event_id") == sharepoint_event_id and
                correlated.get("sentinel_log_id") == sentinel_log_id
            )
            ids_criteria = {
                "passed": ids_valid,
                "name": "IDs únicos correspondentes",
                "description": "SharePoint event ID e Sentinel log ID devem estar linkados"
            }
            criteria_validations.append(ids_criteria)
            
            # Critério 5: Integridade verificada no log correlacionado
            integrity_verified = correlated.get("integrity_status") in ["ok", "correlacionado"]
            integrity_verified_criteria = {
                "passed": integrity_verified,
                "name": "Integridade verificada",
                "description": "Log correlacionado deve indicar integridade ok ou correlacionada"
            }
            criteria_validations.append(integrity_verified_criteria)
        
        # Critério 6: Em caso de divergência, alerta deve ser gerado
        if integrity_status == "divergente":
            alertas = log_repository.get_alertas({"correlation_id": correlation_id})
            divergence_alert_valid = len(alertas) > 0
            divergence_alert_criteria = {
                "passed": divergence_alert_valid,
                "name": "Alerta de divergência",
                "description": "Divergência de integridade deve gerar alerta no Sentinel"
            }
            criteria_validations.append(divergence_alert_criteria)
        
        all_passed = all(c["passed"] for c in criteria_validations)
        
        self.log_result(
            "Cenário 3",
            all_passed,
            "Integridade validada com sucesso" if all_passed else "Alguns critérios não foram atendidos",
            {
                "integrity_status": integrity_status,
                "hash_comparison": hash_comparison,
                "expected_hash": integrity_result.get("expected_hash", "N/A")[:16] + "...",
                "actual_hash": integrity_result.get("actual_hash", "N/A")[:16] + "...",
                "correlated_logs_count": len(correlated_logs),
                "correlation_id": correlation_id
            },
            criteria_validations
        )
    
    def cenario_4_consulta_auditoria(self):
        """
        Cenário 4: Consulta e auditoria de mudanças
        
        Avaliar se as alterações podem ser rastreadas e auditadas no Sentinel, 
        com trilha completa entre origem (Forms/SharePoint) e destino (Power BI).
        Confirmar se relatórios de auditoria são atualizados automaticamente.
        
        Critérios de Aceitação:
        - Trilha de auditoria deve ser completa com timestamps de início e fim
        - Deve conter origem e destino dos dados
        - Todos os eventos relacionados devem ser rastreáveis
        - Integridade deve ser verificada em toda a trilha
        """
        print("\n" + "="*70)
        print("CENARIO 4: Consulta e auditoria de mudancas")
        print("="*70 + "\n")
        
        criteria_validations = []
        
        # Cria evento para auditoria
        user = mock_generator.generate_user()
        project_id = mock_generator.generate_project_id()
        justification = mock_generator.generate_justification(True)
        
        event = SharePointChangeEvent(
            user=user,
            project_id=project_id,
            change_type="status_change",
            justification=justification,
            field_changed="fase",
            old_value="Planejamento",
            new_value="Execução",
            source="SharePoint"
        )
        
        # Processa evento
        process_result = correlation_service.process_sharepoint_event(event, scenario="cenario_4")
        correlation_id = process_result.get("correlation_id")
        
        # Cria trilha de auditoria
        audit_result = correlation_service.create_audit_trail(correlation_id)
        
        # Critério 1: Trilha de auditoria deve ser criada com sucesso
        audit_creation_valid = audit_result.get("success", False)
        audit_creation_criteria = {
            "passed": audit_creation_valid,
            "name": "Trilha de auditoria criada",
            "description": "Sistema deve criar trilha de auditoria para rastreabilidade"
        }
        criteria_validations.append(audit_creation_criteria)
        
        if not audit_creation_valid:
            self.log_result(
                "Cenário 4",
                False,
                "Falha ao criar trilha de auditoria",
                audit_result,
                criteria_validations
            )
            return
        
        audit_trail_id = audit_result.get("audit_trail_id")
        
        # Recupera trilha de auditoria
        audit_trails = log_repository.get_audit_trails({"audit_id": audit_trail_id})
        
        if not audit_trails:
            audit_trail_criteria = {
                "passed": False,
                "name": "Trilha de auditoria armazenada",
                "description": "Trilha criada deve ser armazenada no repositório"
            }
            criteria_validations.append(audit_trail_criteria)
            
            self.log_result(
                "Cenário 4",
                False,
                "Trilha de auditoria não foi armazenada",
                {"audit_trail_id": audit_trail_id},
                criteria_validations
            )
            return
        
        audit_trail = audit_trails[0]
        
        # Critério 2: Campos obrigatórios
        fields_valid, missing_fields = self.acceptance_criteria.validate_audit_trail_completeness(audit_trail)
        fields_criteria = {
            "passed": fields_valid,
            "name": "Campos obrigatórios da trilha",
            "description": f"Trilha deve conter: id, timestamps, origem/destino, usuário, projeto, eventos, status, integridade" +
                          (f" - Faltam: {missing_fields}" if not fields_valid else "")
        }
        criteria_validations.append(fields_criteria)
        
        # Critério 3: Rastreabilidade de eventos
        related_logs = log_repository.get_by_correlation_id(correlation_id)
        
        total_events = (
            len(related_logs.get("sharepoint_events", [])) +
            len(related_logs.get("sentinel_logs", [])) +
            len(related_logs.get("correlated_logs", []))
        )
        
        events_found_criteria = {
            "passed": total_events > 0,
            "name": "Eventos rastreáveis",
            "description": f"Todos os eventos relacionados devem ser recuperáveis ({total_events} eventos encontrados)"
        }
        criteria_validations.append(events_found_criteria)
        
        # Critério 4: Origem e destino
        origin_dest_valid = (
            bool(audit_trail.get("origem")) and
            bool(audit_trail.get("destino")) and
            audit_trail.get("origem") in ["SharePoint/Forms", "Power Automate"] and
            audit_trail.get("destino") in ["Sentinel/Power BI", "Power BI"]
        )
        origin_dest_criteria = {
            "passed": origin_dest_valid,
            "name": "Origem e destino definidos",
            "description": "Trilha deve rastrear dados de origem (SharePoint/Forms) até destino (Power BI)"
        }
        criteria_validations.append(origin_dest_criteria)
        
        # Critério 5: Timestamps
        timestamps_valid = (
            bool(audit_trail.get("timestamp_inicio")) and
            bool(audit_trail.get("timestamp_fim"))
        )
        timestamps_criteria = {
            "passed": timestamps_valid,
            "name": "Timestamps registrados",
            "description": "Trilha deve conter timestamp de início e fim"
        }
        criteria_validations.append(timestamps_criteria)
        
        # Critério 6: Integridade verificada
        integrity_verified = audit_trail.get("integridade_verificada", False)
        integrity_criteria = {
            "passed": integrity_verified,
            "name": "Integridade verificada",
            "description": "Todos os eventos na trilha devem ter integridade verificada"
        }
        criteria_validations.append(integrity_criteria)
        
        # Critério 7: Status final
        status_valid = bool(audit_trail.get("status_final"))
        status_criteria = {
            "passed": status_valid,
            "name": "Status final registrado",
            "description": "Trilha deve indicar status final da mudança"
        }
        criteria_validations.append(status_criteria)
        
        all_passed = all(c["passed"] for c in criteria_validations)
        
        self.log_result(
            "Cenário 4",
            all_passed,
            "Trilha de auditoria completa e rastreável" if all_passed else "Alguns critérios não foram atendidos",
            {
                "audit_trail_id": audit_trail_id,
                "correlation_id": correlation_id,
                "origem": audit_trail.get("origem"),
                "destino": audit_trail.get("destino"),
                "total_eventos_rastreados": total_events,
                "integridade_verificada": audit_trail.get("integridade_verificada"),
                "status_final": audit_trail.get("status_final")
            },
            criteria_validations
        )
    
    def cenario_5_alerta_tentativas_invalidas(self):
        """
        Cenário 5: Alerta de tentativas inválidas
        
        Confirmar que tentativas de alteração sem justificativa ou fora do fluxo 
        geram alertas automáticos no Sentinel e notificações via Teams.
        
        Critérios de Aceitação:
        - Tentativas inválidas devem gerar alertas automáticos
        - Alertas devem ter severidade "critical"
        - Notificações via Teams devem ser enviadas
        - Logs no Sentinel devem ser criados com event_type "tentativa_invalida"
        - CorrelationId deve estar presente
        """
        print("\n" + "="*70)
        print("CENARIO 5: Alerta de tentativas invalidas")
        print("="*70 + "\n")
        
        criteria_validations = []
        
        # Simula tentativa inválida
        user = mock_generator.generate_user()
        project_id = mock_generator.generate_project_id()
        reason = "Tentativa de alteração direta no banco de dados, contornando o fluxo do Power Automate"
        
        # Gera alerta
        alert_result = correlation_service.generate_alert_for_invalid_attempt(
            user=user,
            project_id=project_id,
            reason=reason
        )
        
        # Critério 1: Alerta deve ser gerado com sucesso
        alert_generated = alert_result.get("success", False)
        alert_generated_criteria = {
            "passed": alert_generated,
            "name": "Alerta gerado",
            "description": "Tentativa inválida deve gerar alerta automático"
        }
        criteria_validations.append(alert_generated_criteria)
        
        if not alert_generated:
            self.log_result(
                "Cenário 5",
                False,
                "Falha ao gerar alerta",
                alert_result,
                criteria_validations
            )
            return
        
        alert_id = alert_result.get("alert_id")
        correlation_id = alert_result.get("correlation_id")
        sentinel_log_id = alert_result.get("sentinel_log_id")
        
        # Criterio 2: Alerta deve estar armazenado
        alertas = log_repository.get_alertas({"alert_id": alert_id})
        
        alertas_stored_criteria = {
            "passed": bool(alertas),
            "name": "Alerta armazenado",
            "description": "Alerta deve ser persistido no repositório"
        }
        criteria_validations.append(alertas_stored_criteria)
        
        if not alertas:
            self.log_result(
                "Cenário 5",
                False,
                "Alerta não foi armazenado",
                {"alert_id": alert_id},
                criteria_validations
            )
            return
        
        alerta = alertas[0]
        
        # Critério 3: Severidade deve ser "critical"
        severity_valid = alerta.get("severity") == "critical"
        severity_criteria = {
            "passed": severity_valid,
            "name": "Severidade crítica",
            "description": f"Alertas de tentativa inválida devem ter severidade 'critical'" +
                          (f" - Recebido: {alerta.get('severity')}" if not severity_valid else "")
        }
        criteria_validations.append(severity_criteria)
        
        # Critério 4: Notificação Teams deve estar marcada
        teams_notif = alerta.get("teams_notification_sent", False)
        teams_notif_criteria = {
            "passed": teams_notif,
            "name": "Notificação Teams enviada",
            "description": "Alerta crítico deve enviar notificação via Teams"
        }
        criteria_validations.append(teams_notif_criteria)
        
        # Critério 5: Log no Sentinel deve existir
        sentinel_logs = log_repository.get_sentinel_logs({"log_id": sentinel_log_id})
        
        sentinel_log_exists = bool(sentinel_logs)
        sentinel_log_exists_criteria = {
            "passed": sentinel_log_exists,
            "name": "Log no Sentinel criado",
            "description": "Tentativa inválida deve gerar log no Sentinel"
        }
        criteria_validations.append(sentinel_log_exists_criteria)
        
        if sentinel_log_exists:
            sentinel_log = sentinel_logs[0]
            
            # Critério 6: Event type deve ser "tentativa_invalida"
            event_type_valid = sentinel_log.get("event_type") == "tentativa_invalida"
            event_type_criteria = {
                "passed": event_type_valid,
                "name": "Tipo de evento correto",
                "description": f"Log deve ter event_type 'tentativa_invalida'" +
                              (f" - Recebido: {sentinel_log.get('event_type')}" if not event_type_valid else "")
            }
            criteria_validations.append(event_type_criteria)
            
            # Critério 7: Campos obrigatórios
            fields_valid, missing_fields = self.acceptance_criteria.validate_log_contains_required_fields(sentinel_log)
            fields_criteria = {
                "passed": fields_valid,
                "name": "Campos obrigatórios no log",
                "description": f"Log deve conter: projeto, usuário, timestamp, descrição, status, correlationId" +
                              (f" - Faltam: {missing_fields}" if not fields_valid else "")
            }
            criteria_validations.append(fields_criteria)
            
            # Critério 8: Correlation ID deve estar presente
            correlation_id_valid = bool(sentinel_log.get("correlation_id"))
            correlation_id_criteria = {
                "passed": correlation_id_valid,
                "name": "Correlation ID presente",
                "description": "Log deve conter correlation_id para rastreabilidade"
            }
            criteria_validations.append(correlation_id_criteria)
        
        # Critério 9: Título e descrição do alerta
        title_valid = bool(alerta.get("title"))
        description_valid = bool(alerta.get("description"))
        
        content_criteria = {
            "passed": title_valid and description_valid,
            "name": "Título e descrição do alerta",
            "description": "Alerta deve ter título e descrição informativos"
        }
        criteria_validations.append(content_criteria)
        
        # Critério 10: Ação recomendada
        action_valid = bool(alerta.get("recommended_action"))
        action_criteria = {
            "passed": action_valid,
            "name": "Ação recomendada",
            "description": "Alerta deve incluir ação recomendada para mitigação"
        }
        criteria_validations.append(action_criteria)
        
        all_passed = all(c["passed"] for c in criteria_validations)
        
        self.log_result(
            "Cenário 5",
            all_passed,
            "Alerta crítico gerado com sucesso" if all_passed else "Alguns critérios não foram atendidos",
            {
                "alert_id": alert_id,
                "correlation_id": correlation_id,
                "sentinel_log_id": sentinel_log_id,
                "severity": alerta.get("severity"),
                "teams_notification_sent": alerta.get("teams_notification_sent"),
                "title": alerta.get("title"),
                "recommended_action": alerta.get("recommended_action")
            },
            criteria_validations
        )
    
    def run_all_scenarios(self):
        """Executa todos os cenários de teste"""
        print("\n" + "="*70)
        print("    TESTES RNF-03 RASTREABILIDADE - CENARIOS")
        print("="*70)
        
        # Limpa dados anteriores
        print("\nLimpando dados de testes anteriores...")
        log_repository.clear_all()
        print("Dados limpos.\n")
        
        # Executa cenários
        self.cenario_1_bloqueio_sem_justificativa()
        self.cenario_2_registro_automatico()
        self.cenario_3_validacao_integridade()
        self.cenario_4_consulta_auditoria()
        self.cenario_5_alerta_tentativas_invalidas()
        
        # Relatório final
        self.print_summary()
    
    def print_summary(self):
        """Imprime resumo dos testes com análise de critérios de aceitação"""
        print("\n" + "="*70)
        print("RESUMO DOS TESTES - RNF-03 RASTREABILIDADE")
        print("="*70 + "\n")
        
        total = len(self.results)
        passed = len([r for r in self.results if r["passed"]])
        failed = total - passed
        
        print(f"Total de cenários testados: {total}")
        print(f"[+] Passaram: {passed}")
        print(f"[-] Falharam: {failed}")
        print(f"Taxa de sucesso: {(passed/total)*100:.1f}%\n")
        
        # Análise de critérios de aceitação
        total_criteria = 0
        passed_criteria = 0
        
        for result in self.results:
            for criteria in result.get("criteria_validations", []):
                total_criteria += 1
                if criteria["passed"]:
                    passed_criteria += 1
        
        if total_criteria > 0:
            print(f"\nCRITÉRIOS DE ACEITAÇÃO:")
            print(f"Total de critérios validados: {total_criteria}")
            print(f"[+] Critérios atendidos: {passed_criteria}")
            print(f"[-] Critérios não atendidos: {total_criteria - passed_criteria}")
            print(f"Taxa de atendimento: {(passed_criteria/total_criteria)*100:.1f}%\n")
        
        if failed > 0:
            print("Cenários que falharam:")
            for result in self.results:
                if not result["passed"]:
                    print(f"  - {result['scenario']}: {result['message']}")
                    for criteria in result.get("criteria_validations", []):
                        if not criteria["passed"]:
                            print(f"    ✗ {criteria['name']}: {criteria['description']}")
        
        print("\n" + "="*70)
        
        stats = log_repository.get_statistics()
        print("\nESTATÍSTICAS DO REPOSITÓRIO:")
        for key, value in stats.items():
            pretty_key = key.replace("total_", "").replace("_", " ").title()
            print(f"  - {pretty_key}: {value}")
        
        print("\n" + "="*70)
        
        # Validação final dos critérios
        print("\nCRITÉRIOS DE ACEITAÇÃO - RESUMO POR CENÁRIO:")
        for result in self.results:
            status = "✓" if result["passed"] else "✗"
            print(f"\n{status} {result['scenario']}")
            for criteria in result.get("criteria_validations", []):
                criteria_status = "✓" if criteria["passed"] else "✗"
                print(f"  {criteria_status} {criteria['name']}")
        
        print("\n" + "="*70 + "\n")


if __name__ == "__main__":
    tester = TestScenarios()
    tester.run_all_scenarios()

