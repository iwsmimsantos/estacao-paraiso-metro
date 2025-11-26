"""
Serviço de correlação e rastreabilidade (Middleware)
"""
import hashlib
from datetime import datetime
from typing import Optional, Dict, Any
from uuid import uuid4

from models.log_models import (
    SharePointChangeEvent,
    SentinelLogEvent,
    CorrelatedLog,
    HistoricoAlteracoes,
    AlertaSentinel,
    AuditTrail
)
from storage.log_repository import log_repository
from services.mock_data_generator import mock_generator


class CorrelationService:
    """Serviço de correlação entre eventos SharePoint e logs Sentinel"""
    
    def __init__(self):
        self.repository = log_repository
    
    def _generate_hash(self, data: str) -> str:
        """Gera hash SHA-256 para verificação de integridade"""
        return hashlib.sha256(data.encode()).hexdigest()
    
    def _normalize_event_data(self, event: SharePointChangeEvent) -> str:
        """Normaliza dados do evento para geração de hash"""
        return f"{event.user}|{event.project_id}|{event.change_type}|{event.timestamp.isoformat()}"
    
    def process_sharepoint_event(
        self,
        event: SharePointChangeEvent,
        scenario: str = "default"
    ) -> Dict[str, Any]:
        """
        Processa evento do SharePoint e cria logs correspondentes
        
        Args:
            event: Evento do SharePoint
            scenario: Cenário de teste (cenario_1 a cenario_5)
        
        Returns:
            Dicionário com resultados do processamento
        """
        correlation_id = str(uuid4())
        
        # 1. Armazena evento do SharePoint
        event_dict = event.model_dump(mode='json')
        self.repository.add_sharepoint_event(event_dict)
        
        # 2. Valida justificativa
        blocked = False
        if not event.justification or event.justification.strip() == "":
            blocked = True
            return self._handle_blocked_change(event, correlation_id, scenario)
        
        # 3. Gera hash para integridade
        normalized_data = self._normalize_event_data(event)
        hash_value = self._generate_hash(normalized_data)
        
        # 4. Cria log no Sentinel
        sentinel_log = SentinelLogEvent(
            correlation_id=correlation_id,
            event_type="mudanca_aprovada",
            severity="medium",
            user=event.user,
            project_id=event.project_id,
            description=f"Mudança {event.change_type} no campo {event.field_changed}",
            source_system="SharePoint",
            hash_value=hash_value,
            metadata={
                "field_changed": event.field_changed,
                "old_value": event.old_value,
                "new_value": event.new_value,
                "justification": event.justification
            },
            status="processado"
        )
        
        sentinel_dict = sentinel_log.model_dump(mode='json')
        self.repository.add_sentinel_log(sentinel_dict)
        
        # 5. Cria log correlacionado
        correlated = CorrelatedLog(
            correlation_id=correlation_id,
            sharepoint_event_id=event.event_id,
            sentinel_log_id=sentinel_log.log_id,
            integrity_status="correlacionado",
            hash_comparison=True,
            user=event.user,
            project_id=event.project_id,
            change_description=f"{event.change_type} - {event.field_changed}",
            justification=event.justification
        )
        
        correlated_dict = correlated.model_dump(mode='json')
        self.repository.add_correlated_log(correlated_dict)
        
        # 6. Registra no histórico de alterações
        historico = HistoricoAlteracoes(
            correlation_id=correlation_id,
            user=event.user,
            project_id=event.project_id,
            change_type=event.change_type,
            justification=event.justification,
            status="aprovado",
            sentinel_log_id=sentinel_log.log_id
        )
        
        historico_dict = historico.model_dump(mode='json')
        self.repository.add_historico_alteracao(historico_dict)
        
        return {
            "success": True,
            "blocked": False,
            "correlation_id": correlation_id,
            "sharepoint_event_id": event.event_id,
            "sentinel_log_id": sentinel_log.log_id,
            "hash": hash_value,
            "integrity_status": "correlacionado",
            "message": "Mudança processada e registrada com sucesso"
        }
    
    def _handle_blocked_change(
        self,
        event: SharePointChangeEvent,
        correlation_id: str,
        scenario: str
    ) -> Dict[str, Any]:
        """Trata mudança bloqueada por falta de justificativa"""
        
        # 1. Cria log de bloqueio no Sentinel
        sentinel_log = SentinelLogEvent(
            correlation_id=correlation_id,
            event_type="bloqueio",
            severity="high",
            user=event.user,
            project_id=event.project_id,
            description=f"Tentativa de {event.change_type} bloqueada - justificativa ausente",
            source_system="SharePoint",
            hash_value=self._generate_hash(f"blocked|{event.user}|{event.project_id}"),
            metadata={
                "reason": "Justificativa ausente",
                "field_attempted": event.field_changed
            },
            status="processado"
        )
        
        sentinel_dict = sentinel_log.model_dump(mode='json')
        self.repository.add_sentinel_log(sentinel_dict)
        
        # 2. Gera alerta
        alerta = AlertaSentinel(
            severity="high",
            title="Tentativa de mudança sem justificativa",
            description=f"Usuário {event.user} tentou realizar {event.change_type} no projeto {event.project_id} sem fornecer justificativa",
            affected_user=event.user,
            affected_project=event.project_id,
            correlation_id=correlation_id,
            recommended_action="Solicitar justificativa antes de aprovar mudança",
            teams_notification_sent=True
        )
        
        alerta_dict = alerta.model_dump(mode='json')
        self.repository.add_alerta(alerta_dict)
        
        # 3. Registra no histórico como bloqueado
        historico = HistoricoAlteracoes(
            correlation_id=correlation_id,
            user=event.user,
            project_id=event.project_id,
            change_type=event.change_type,
            justification="N/A - Bloqueado",
            status="bloqueado",
            sentinel_log_id=sentinel_log.log_id
        )
        
        historico_dict = historico.model_dump(mode='json')
        self.repository.add_historico_alteracao(historico_dict)
        
        return {
            "success": False,
            "blocked": True,
            "correlation_id": correlation_id,
            "sentinel_log_id": sentinel_log.log_id,
            "alert_id": alerta.alert_id,
            "message": "Mudança bloqueada - justificativa obrigatória ausente",
            "teams_notification": "Notificação enviada via Teams (simulado)"
        }
    
    def verify_integrity(
        self,
        sharepoint_event_id: str,
        sentinel_log_id: str
    ) -> Dict[str, Any]:
        """
        Verifica integridade entre evento SharePoint e log Sentinel
        
        Simula a comparação de hashes e correlação de IDs
        """
        # Busca eventos
        sp_events = self.repository.get_sharepoint_events({"event_id": sharepoint_event_id})
        sentinel_logs = self.repository.get_sentinel_logs({"log_id": sentinel_log_id})
        
        if not sp_events or not sentinel_logs:
            return {
                "integrity_status": "inconsistente",
                "hash_comparison": False,
                "message": "Evento ou log não encontrado"
            }
        
        sp_event = sp_events[0]
        sentinel_log = sentinel_logs[0]
        
        # Simula verificação de hash
        expected_hash = self._generate_hash(
            f"{sp_event.get('user')}|{sp_event.get('project_id')}|{sp_event.get('change_type')}|{sp_event.get('timestamp')}"
        )
        
        actual_hash = sentinel_log.get('hash_value', '')
        
        # Simula possível divergência (10% de chance)
        if mock_generator.simulate_integrity_issue(probability=0.1):
            return {
                "integrity_status": "divergente",
                "hash_comparison": False,
                "expected_hash": expected_hash,
                "actual_hash": actual_hash + "xxx",  # Simula hash divergente
                "message": "Divergência detectada - hashes não correspondem",
                "alert_generated": True
            }
        
        return {
            "integrity_status": "ok",
            "hash_comparison": True,
            "expected_hash": expected_hash,
            "actual_hash": actual_hash,
            "message": "Integridade verificada com sucesso"
        }
    
    def create_audit_trail(
        self,
        correlation_id: str
    ) -> Dict[str, Any]:
        """
        Cria trilha de auditoria completa para um correlation_id
        """
        # Busca todos os logs relacionados
        related_logs = self.repository.get_by_correlation_id(correlation_id)
        
        if not related_logs.get("sentinel_logs"):
            return {
                "success": False,
                "message": "Nenhum log encontrado para o correlation_id fornecido"
            }
        
        sentinel_log = related_logs["sentinel_logs"][0]
        historico = related_logs["historico_alteracoes"][0] if related_logs["historico_alteracoes"] else {}
        
        # Cria audit trail
        audit_trail = AuditTrail(
            correlation_id=correlation_id,
            timestamp_inicio=datetime.fromisoformat(sentinel_log["timestamp"]),
            timestamp_fim=datetime.now(),
            origem="SharePoint/Forms",
            destino="Sentinel/Power BI",
            user=sentinel_log["user"],
            project_id=sentinel_log["project_id"],
            eventos_relacionados=[
                sentinel_log["log_id"]
            ],
            status_final=historico.get("status", "processado"),
            integridade_verificada=True
        )
        
        audit_dict = audit_trail.model_dump(mode='json')
        self.repository.add_audit_trail(audit_dict)
        
        return {
            "success": True,
            "audit_trail_id": audit_trail.audit_id,
            "correlation_id": correlation_id,
            "trail": audit_dict,
            "related_events_count": len(related_logs["sentinel_logs"]),
            "message": "Trilha de auditoria criada com sucesso"
        }
    
    def generate_alert_for_invalid_attempt(
        self,
        user: str,
        project_id: str,
        reason: str
    ) -> Dict[str, Any]:
        """Gera alerta para tentativa inválida"""
        
        correlation_id = str(uuid4())
        
        # Cria evento no Sentinel
        sentinel_log = SentinelLogEvent(
            correlation_id=correlation_id,
            event_type="tentativa_invalida",
            severity="critical",
            user=user,
            project_id=project_id,
            description=f"Tentativa inválida detectada: {reason}",
            source_system="Sentinel",
            hash_value=self._generate_hash(f"invalid|{user}|{project_id}|{datetime.now().isoformat()}"),
            status="processado"
        )
        
        sentinel_dict = sentinel_log.model_dump(mode='json')
        self.repository.add_sentinel_log(sentinel_dict)
        
        # Cria alerta
        alerta = AlertaSentinel(
            severity="critical",
            title="Tentativa de alteração inválida detectada",
            description=f"Usuário {user} tentou realizar alteração fora do fluxo autorizado no projeto {project_id}. Motivo: {reason}",
            affected_user=user,
            affected_project=project_id,
            correlation_id=correlation_id,
            recommended_action="Investigar e bloquear acesso se necessário",
            teams_notification_sent=True
        )
        
        alerta_dict = alerta.model_dump(mode='json')
        self.repository.add_alerta(alerta_dict)
        
        return {
            "success": True,
            "alert_id": alerta.alert_id,
            "correlation_id": correlation_id,
            "sentinel_log_id": sentinel_log.log_id,
            "severity": "critical",
            "teams_notification": "Notificação crítica enviada via Teams (simulado)",
            "message": "Alerta gerado e registrado com sucesso"
        }


# Singleton
correlation_service = CorrelationService()

