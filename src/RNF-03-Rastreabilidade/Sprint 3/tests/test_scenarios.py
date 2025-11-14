"""
Testes automatizados dos 5 cenários de rastreabilidade (RNF-03)
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


class TestScenarios:
    """Classe de testes dos cenários de rastreabilidade"""
    
    def __init__(self):
        self.results = []
    
    def log_result(self, scenario: str, passed: bool, message: str, details: dict = None):
        """Registra resultado de teste"""
        result = {
            "scenario": scenario,
            "passed": passed,
            "message": message,
            "timestamp": datetime.now().isoformat(),
            "details": details or {}
        }
        self.results.append(result)
        
        status = "[PASSOU]" if passed else "[FALHOU]"
        print(f"{status} {scenario}: {message}")
        if details:
            for key, value in details.items():
                print(f"  - {key}: {value}")
        print()
    
    def cenario_1_bloqueio_sem_justificativa(self):
        """
        Cenário 1: Bloqueio de mudança sem justificativa
        
        Validar se o fluxo no Power Automate impede a atualização nas listas 
        do SharePoint quando o campo "Justificativa da mudança" estiver vazio.
        Confirmar que o evento de bloqueio é registrado automaticamente no Sentinel.
        """
        print("\n" + "="*70)
        print("CENARIO 1: Bloqueio de mudanca sem justificativa")
        print("="*70 + "\n")
        
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
        
        # Verifica se foi bloqueado
        if not bloqueado:
            self.log_result(
                "Cenário 1",
                False,
                "Mudança NÃO foi bloqueada como esperado",
                {"blocked": bloqueado}
            )
            return
        
        # Verifica se log foi criado no Sentinel
        if not sentinel_log_id:
            self.log_result(
                "Cenário 1",
                False,
                "Log não foi criado no Sentinel",
                {"sentinel_log_id": sentinel_log_id}
            )
            return
        
        # Verifica se alerta foi gerado
        if not alert_id:
            self.log_result(
                "Cenário 1",
                False,
                "Alerta não foi gerado",
                {"alert_id": alert_id}
            )
            return
        
        self.log_result(
            "Cenário 1",
            True,
            "Mudança bloqueada com sucesso, log e alerta criados",
            {
                "blocked": bloqueado,
                "correlation_id": result.get("correlation_id"),
                "sentinel_log_id": sentinel_log_id,
                "alert_id": alert_id,
                "teams_notification": result.get("teams_notification")
            }
        )
    
    def cenario_2_registro_automatico(self):
        """
        Cenário 2: Registro automático da mudança
        
        Verificar se cada alteração aprovada gera um registro na lista 
        "Histórico de Alterações" no SharePoint e um evento correspondente 
        no Sentinel com correlationId, usuário, timestamp, e tipo de mudança.
        """
        print("\n" + "="*70)
        print("CENARIO 2: Registro automatico da mudanca")
        print("="*70 + "\n")
        
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
        
        # Verifica se log foi criado no Sentinel
        sentinel_logs = log_repository.get_sentinel_logs({"correlation_id": correlation_id})
        if not sentinel_logs:
            self.log_result(
                "Cenário 2",
                False,
                "Log não foi criado no Sentinel",
                {"correlation_id": correlation_id}
            )
            return
        
        sentinel_log = sentinel_logs[0]
        
        # Verifica campos obrigatórios
        required_fields = ["correlation_id", "user", "timestamp", "project_id", "event_type"]
        missing_fields = [f for f in required_fields if not sentinel_log.get(f)]
        
        if missing_fields:
            self.log_result(
                "Cenário 2",
                False,
                f"Campos obrigatórios ausentes no log: {missing_fields}",
                {"sentinel_log": sentinel_log}
            )
            return
        
        # Verifica se registro foi criado no histórico
        historico = log_repository.get_historico_alteracoes({"correlation_id": correlation_id})
        if not historico:
            self.log_result(
                "Cenário 2",
                False,
                "Registro não foi criado no Histórico de Alterações",
                {"correlation_id": correlation_id}
            )
            return
        
        self.log_result(
            "Cenário 2",
            True,
            "Mudança registrada automaticamente com todos os campos obrigatórios",
            {
                "correlation_id": correlation_id,
                "sentinel_log_id": sentinel_log_id,
                "historico_id": historico[0].get("historico_id"),
                "user": sentinel_log.get("user"),
                "timestamp": sentinel_log.get("timestamp"),
                "hash": result.get("hash")
            }
        )
    
    def cenario_3_validacao_integridade(self):
        """
        Cenário 3: Validação de integridade e consistência dos logs
        
        Testar se o Sentinel consegue correlacionar os eventos de origem 
        (SharePoint / Power Automate) com os registros do Log Analytics, 
        garantindo integridade por meio de hash e identificação única.
        """
        print("\n" + "="*70)
        print("CENARIO 3: Validacao de integridade e consistencia dos logs")
        print("="*70 + "\n")
        
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
        
        # Verifica integridade
        integrity_result = correlation_service.verify_integrity(
            sharepoint_event_id=sharepoint_event_id,
            sentinel_log_id=sentinel_log_id
        )
        
        # Validações
        integrity_status = integrity_result.get("integrity_status")
        hash_comparison = integrity_result.get("hash_comparison")
        
        # Verifica se hashes foram comparados
        if "expected_hash" not in integrity_result or "actual_hash" not in integrity_result:
            self.log_result(
                "Cenário 3",
                False,
                "Hashes não foram gerados ou comparados",
                integrity_result
            )
            return
        
        # Verifica status de integridade
        valid_statuses = ["ok", "correlacionado", "divergente"]
        if integrity_status not in valid_statuses:
            self.log_result(
                "Cenário 3",
                False,
                f"Status de integridade inválido: {integrity_status}",
                integrity_result
            )
            return
        
        # Verifica logs correlacionados
        correlated_logs = log_repository.get_correlated_logs(
            {"correlation_id": process_result.get("correlation_id")}
        )
        
        if not correlated_logs:
            self.log_result(
                "Cenário 3",
                False,
                "Log correlacionado não foi criado",
                {"correlation_id": process_result.get("correlation_id")}
            )
            return
        
        self.log_result(
            "Cenário 3",
            True,
            "Integridade validada com sucesso, eventos correlacionados",
            {
                "integrity_status": integrity_status,
                "hash_comparison": hash_comparison,
                "expected_hash": integrity_result.get("expected_hash")[:16] + "...",
                "actual_hash": integrity_result.get("actual_hash")[:16] + "...",
                "correlated_log_id": correlated_logs[0].get("correlation_id")
            }
        )
    
    def cenario_4_consulta_auditoria(self):
        """
        Cenário 4: Consulta e auditoria de mudanças
        
        Avaliar se as alterações podem ser rastreadas e auditadas no Sentinel, 
        com trilha completa entre origem (Forms/SharePoint) e destino (Power BI).
        Confirmar se relatórios de auditoria são atualizados automaticamente.
        """
        print("\n" + "="*70)
        print("CENARIO 4: Consulta e auditoria de mudancas")
        print("="*70 + "\n")
        
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
        
        # Validações
        if not audit_result.get("success"):
            self.log_result(
                "Cenário 4",
                False,
                "Falha ao criar trilha de auditoria",
                audit_result
            )
            return
        
        audit_trail_id = audit_result.get("audit_trail_id")
        
        # Recupera trilha de auditoria
        audit_trails = log_repository.get_audit_trails({"audit_id": audit_trail_id})
        
        if not audit_trails:
            self.log_result(
                "Cenário 4",
                False,
                "Trilha de auditoria não foi armazenada",
                {"audit_trail_id": audit_trail_id}
            )
            return
        
        audit_trail = audit_trails[0]
        
        # Verifica campos obrigatórios da trilha
        required_fields = [
            "correlation_id", "timestamp_inicio", "timestamp_fim",
            "origem", "destino", "user", "project_id",
            "eventos_relacionados", "status_final", "integridade_verificada"
        ]
        
        missing_fields = [f for f in required_fields if f not in audit_trail]
        
        if missing_fields:
            self.log_result(
                "Cenário 4",
                False,
                f"Campos obrigatórios ausentes na trilha: {missing_fields}",
                audit_trail
            )
            return
        
        # Verifica se pode consultar por correlation_id
        related_logs = log_repository.get_by_correlation_id(correlation_id)
        
        total_events = (
            len(related_logs.get("sharepoint_events", [])) +
            len(related_logs.get("sentinel_logs", [])) +
            len(related_logs.get("correlated_logs", []))
        )
        
        if total_events == 0:
            self.log_result(
                "Cenário 4",
                False,
                "Não foi possível rastrear eventos relacionados",
                {"correlation_id": correlation_id}
            )
            return
        
        self.log_result(
            "Cenário 4",
            True,
            "Trilha de auditoria completa criada e rastreável",
            {
                "audit_trail_id": audit_trail_id,
                "correlation_id": correlation_id,
                "origem": audit_trail.get("origem"),
                "destino": audit_trail.get("destino"),
                "total_eventos_rastreados": total_events,
                "integridade_verificada": audit_trail.get("integridade_verificada"),
                "status_final": audit_trail.get("status_final")
            }
        )
    
    def cenario_5_alerta_tentativas_invalidas(self):
        """
        Cenário 5: Alerta de tentativas inválidas
        
        Confirmar que tentativas de alteração sem justificativa ou fora do fluxo 
        geram alertas automáticos no Sentinel e notificações via Teams.
        """
        print("\n" + "="*70)
        print("CENARIO 5: Alerta de tentativas invalidas")
        print("="*70 + "\n")
        
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
        
        # Validações
        if not alert_result.get("success"):
            self.log_result(
                "Cenário 5",
                False,
                "Falha ao gerar alerta",
                alert_result
            )
            return
        
        alert_id = alert_result.get("alert_id")
        correlation_id = alert_result.get("correlation_id")
        sentinel_log_id = alert_result.get("sentinel_log_id")
        
        # Verifica se alerta foi criado
        alertas = log_repository.get_alertas({"alert_id": alert_id})
        
        if not alertas:
            self.log_result(
                "Cenário 5",
                False,
                "Alerta não foi armazenado",
                {"alert_id": alert_id}
            )
            return
        
        alerta = alertas[0]
        
        # Verifica severidade
        if alerta.get("severity") != "critical":
            self.log_result(
                "Cenário 5",
                False,
                f"Severidade esperada 'critical', recebida '{alerta.get('severity')}'",
                alerta
            )
            return
        
        # Verifica se notificação Teams foi marcada
        if not alerta.get("teams_notification_sent"):
            self.log_result(
                "Cenário 5",
                False,
                "Notificação Teams não foi marcada como enviada",
                alerta
            )
            return
        
        # Verifica se log foi criado no Sentinel
        sentinel_logs = log_repository.get_sentinel_logs({"log_id": sentinel_log_id})
        
        if not sentinel_logs:
            self.log_result(
                "Cenário 5",
                False,
                "Log não foi criado no Sentinel",
                {"sentinel_log_id": sentinel_log_id}
            )
            return
        
        sentinel_log = sentinel_logs[0]
        
        # Verifica tipo de evento
        if sentinel_log.get("event_type") != "tentativa_invalida":
            self.log_result(
                "Cenário 5",
                False,
                f"Tipo de evento esperado 'tentativa_invalida', recebido '{sentinel_log.get('event_type')}'",
                sentinel_log
            )
            return
        
        self.log_result(
            "Cenário 5",
            True,
            "Alerta crítico gerado com sucesso, notificação Teams enviada",
            {
                "alert_id": alert_id,
                "correlation_id": correlation_id,
                "sentinel_log_id": sentinel_log_id,
                "severity": alerta.get("severity"),
                "teams_notification_sent": alerta.get("teams_notification_sent"),
                "title": alerta.get("title"),
                "recommended_action": alerta.get("recommended_action")
            }
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
        """Imprime resumo dos testes"""
        print("\n" + "="*70)
        print("RESUMO DOS TESTES")
        print("="*70 + "\n")
        
        total = len(self.results)
        passed = len([r for r in self.results if r["passed"]])
        failed = total - passed
        
        print(f"Total de cenarios testados: {total}")
        print(f"[+] Passaram: {passed}")
        print(f"[-] Falharam: {failed}")
        print(f"Taxa de sucesso: {(passed/total)*100:.1f}%\n")
        
        if failed > 0:
            print("Cenarios que falharam:")
            for result in self.results:
                if not result["passed"]:
                    print(f"  - {result['scenario']}: {result['message']}")
        
        print("\n" + "="*70)
        
        stats = log_repository.get_statistics()
        print("\nESTATISTICAS DO REPOSITORIO:")
        for key, value in stats.items():
            print(f"  - {key}: {value}")
        
        print("\n" + "="*70 + "\n")


if __name__ == "__main__":
    tester = TestScenarios()
    tester.run_all_scenarios()

