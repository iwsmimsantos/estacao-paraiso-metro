"""
Sistema de Logging e Rastreabilidade (RNF-03)

Implementa logging estruturado com trace_id, correlation_id e hash
para garantir rastreabilidade completa de todas as ações no sistema.
"""
import json
import hashlib
import uuid
from datetime import datetime
from pathlib import Path
from typing import Optional, Dict, Any, List
from enum import Enum

from pythonjsonlogger import jsonlogger


class LogLevel(str, Enum):
    """Níveis de log"""
    DEBUG = "DEBUG"
    INFO = "INFO"
    WARNING = "WARNING"
    ERROR = "ERROR"
    CRITICAL = "CRITICAL"


class EventType(str, Enum):
    """Tipos de evento para rastreabilidade"""
    # Autenticação
    AUTH_LOGIN = "auth.login"
    AUTH_LOGOUT = "auth.logout"
    AUTH_TOKEN_VERIFY = "auth.token_verify"
    AUTH_ACCESS_DENIED = "auth.access_denied"
    
    # Acesso a recursos
    RESOURCE_ACCESS = "resource.access"
    RESOURCE_READ = "resource.read"
    RESOURCE_WRITE = "resource.write"
    RESOURCE_DELETE = "resource.delete"
    
    # Miro
    MIRO_BOARD_ACCESS = "miro.board.access"
    MIRO_BOARD_READ = "miro.board.read"
    MIRO_BOARD_WRITE = "miro.board.write"
    
    # SharePoint
    SHAREPOINT_DOCUMENT_READ = "sharepoint.document.read"
    SHAREPOINT_DOCUMENT_WRITE = "sharepoint.document.write"
    SHAREPOINT_SYNC = "sharepoint.sync"
    
    # Validação de dados
    DATA_VALIDATION = "data.validation"
    DATA_CHECKSUM = "data.checksum"
    DATA_MISMATCH = "data.mismatch"
    
    # IA
    AI_REQUEST = "ai.request"
    AI_RESPONSE = "ai.response"
    AI_GUARDRAIL_VIOLATION = "ai.guardrail_violation"
    
    # Sistema
    SYSTEM_ERROR = "system.error"
    SYSTEM_HEALTH_CHECK = "system.health_check"


class AuditLog:
    """Registro de auditoria estruturado"""
    
    def __init__(
        self,
        event_type: EventType,
        user_id: Optional[str] = None,
        resource_type: Optional[str] = None,
        resource_id: Optional[str] = None,
        action: Optional[str] = None,
        status: str = "success",
        details: Optional[Dict[str, Any]] = None,
        trace_id: Optional[str] = None,
        correlation_id: Optional[str] = None
    ):
        self.trace_id = trace_id or str(uuid.uuid4())
        self.correlation_id = correlation_id or str(uuid.uuid4())
        self.timestamp = datetime.utcnow().isoformat() + "Z"
        self.event_type = event_type.value if isinstance(event_type, EventType) else event_type
        self.user_id = user_id
        self.resource_type = resource_type
        self.resource_id = resource_id
        self.action = action
        self.status = status
        self.details = details or {}
        
        # Gera hash do log para integridade
        self.hash = self._generate_hash()
    
    def _generate_hash(self) -> str:
        """Gera hash SHA-256 do conteúdo do log para garantir integridade"""
        content = f"{self.timestamp}|{self.event_type}|{self.user_id}|{self.resource_id}|{self.status}"
        return hashlib.sha256(content.encode()).hexdigest()
    
    def to_dict(self) -> Dict[str, Any]:
        """Converte log para dicionário"""
        return {
            "trace_id": self.trace_id,
            "correlation_id": self.correlation_id,
            "timestamp": self.timestamp,
            "event_type": self.event_type,
            "user_id": self.user_id,
            "resource_type": self.resource_type,
            "resource_id": self.resource_id,
            "action": self.action,
            "status": self.status,
            "details": self.details,
            "hash": self.hash
        }
    
    def to_json(self) -> str:
        """Converte log para JSON"""
        return json.dumps(self.to_dict(), ensure_ascii=False, indent=2)


class Logger:
    """Sistema de logging estruturado"""
    
    def __init__(self):
        self.storage_path = Path(__file__).parent.parent.parent / "storage"
        self.storage_path.mkdir(exist_ok=True)
        
        self.logs_file = self.storage_path / "audit_logs.jsonl"
        self.incidents_file = self.storage_path / "incidents.jsonl"
        
        # Cria arquivos se não existirem
        self.logs_file.touch(exist_ok=True)
        self.incidents_file.touch(exist_ok=True)
        
        print(f"📝 Logger inicializado: {self.logs_file}")
    
    def log(
        self,
        event_type: EventType,
        user_id: Optional[str] = None,
        resource_type: Optional[str] = None,
        resource_id: Optional[str] = None,
        action: Optional[str] = None,
        status: str = "success",
        details: Optional[Dict[str, Any]] = None,
        trace_id: Optional[str] = None,
        correlation_id: Optional[str] = None
    ) -> AuditLog:
        """
        Registra um evento no sistema de logs
        
        Args:
            event_type: Tipo de evento
            user_id: ID do usuário que executou a ação
            resource_type: Tipo de recurso acessado
            resource_id: ID do recurso
            action: Ação executada
            status: Status da operação (success, failed, denied)
            details: Detalhes adicionais
            trace_id: ID de rastreamento (gerado se não fornecido)
            correlation_id: ID de correlação para agrupar eventos relacionados
        
        Returns:
            AuditLog criado
        """
        audit_log = AuditLog(
            event_type=event_type,
            user_id=user_id,
            resource_type=resource_type,
            resource_id=resource_id,
            action=action,
            status=status,
            details=details,
            trace_id=trace_id,
            correlation_id=correlation_id
        )
        
        # Salva no arquivo de logs (JSONL - uma linha por log)
        with open(self.logs_file, 'a', encoding='utf-8') as f:
            f.write(json.dumps(audit_log.to_dict(), ensure_ascii=False) + '\n')
        
        return audit_log
    
    def log_incident(
        self,
        incident_type: str,
        severity: str,
        user_id: Optional[str] = None,
        resource_id: Optional[str] = None,
        description: str = "",
        details: Optional[Dict[str, Any]] = None,
        trace_id: Optional[str] = None
    ) -> AuditLog:
        """
        Registra um incidente de segurança na incident queue
        
        Args:
            incident_type: Tipo de incidente (access_denied, data_mismatch, guardrail_violation, etc)
            severity: Severidade (low, medium, high, critical)
            user_id: ID do usuário envolvido
            resource_id: ID do recurso
            description: Descrição do incidente
            details: Detalhes adicionais
            trace_id: ID de rastreamento
        
        Returns:
            AuditLog do incidente
        """
        incident_details = details or {}
        incident_details.update({
            "incident_type": incident_type,
            "severity": severity,
            "description": description
        })
        
        audit_log = AuditLog(
            event_type=EventType.AUTH_ACCESS_DENIED if "access" in incident_type else EventType.SYSTEM_ERROR,
            user_id=user_id,
            resource_id=resource_id,
            action="incident",
            status="incident",
            details=incident_details,
            trace_id=trace_id
        )
        
        # Salva no arquivo de incidentes (JSONL)
        with open(self.incidents_file, 'a', encoding='utf-8') as f:
            f.write(json.dumps(audit_log.to_dict(), ensure_ascii=False) + '\n')
        
        # Também salva nos logs gerais
        with open(self.logs_file, 'a', encoding='utf-8') as f:
            f.write(json.dumps(audit_log.to_dict(), ensure_ascii=False) + '\n')
        
        return audit_log
    
    def get_logs(
        self,
        limit: int = 50,
        user_id: Optional[str] = None,
        event_type: Optional[str] = None,
        status: Optional[str] = None
    ) -> List[Dict[str, Any]]:
        """
        Recupera logs com filtros opcionais
        
        Args:
            limit: Número máximo de logs a retornar
            user_id: Filtrar por usuário
            event_type: Filtrar por tipo de evento
            status: Filtrar por status
        
        Returns:
            Lista de logs em formato dict
        """
        logs = []
        
        if not self.logs_file.exists():
            return logs
        
        with open(self.logs_file, 'r', encoding='utf-8') as f:
            for line in f:
                try:
                    log = json.loads(line)
                    
                    # Aplica filtros
                    if user_id and log.get('user_id') != user_id:
                        continue
                    if event_type and log.get('event_type') != event_type:
                        continue
                    if status and log.get('status') != status:
                        continue
                    
                    logs.append(log)
                except json.JSONDecodeError:
                    continue
        
        # Retorna os últimos N logs (mais recentes primeiro)
        return logs[-limit:][::-1]
    
    def get_incidents(
        self,
        limit: int = 50,
        severity: Optional[str] = None
    ) -> List[Dict[str, Any]]:
        """
        Recupera incidentes da incident queue
        
        Args:
            limit: Número máximo de incidentes
            severity: Filtrar por severidade
        
        Returns:
            Lista de incidentes
        """
        incidents = []
        
        if not self.incidents_file.exists():
            return incidents
        
        with open(self.incidents_file, 'r', encoding='utf-8') as f:
            for line in f:
                try:
                    incident = json.loads(line)
                    
                    # Extrai campos importantes de details para o nível superior
                    if 'details' in incident:
                        details = incident['details']
                        if 'severity' in details and 'severity' not in incident:
                            incident['severity'] = details['severity']
                        if 'incident_type' in details and 'incident_type' not in incident:
                            incident['incident_type'] = details['incident_type']
                        if 'event_type' in details and 'event_type' not in incident:
                            incident['event_type'] = details['event_type']
                    
                    # Filtra por severidade se especificado
                    if severity and incident.get('severity') != severity:
                        continue
                    
                    incidents.append(incident)
                except json.JSONDecodeError:
                    continue
        
        # Retorna os últimos N incidentes (mais recentes primeiro)
        return incidents[-limit:][::-1]
    
    def get_log_by_trace_id(self, trace_id: str) -> Optional[Dict[str, Any]]:
        """Busca log por trace_id"""
        if not self.logs_file.exists():
            return None
        
        with open(self.logs_file, 'r', encoding='utf-8') as f:
            for line in f:
                try:
                    log = json.loads(line)
                    if log.get('trace_id') == trace_id:
                        return log
                except json.JSONDecodeError:
                    continue
        
        return None
    
    def get_logs_by_correlation_id(self, correlation_id: str) -> List[Dict[str, Any]]:
        """Busca todos os logs de uma mesma correlação (transação)"""
        logs = []
        
        if not self.logs_file.exists():
            return logs
        
        with open(self.logs_file, 'r', encoding='utf-8') as f:
            for line in f:
                try:
                    log = json.loads(line)
                    if log.get('correlation_id') == correlation_id:
                        logs.append(log)
                except json.JSONDecodeError:
                    continue
        
        return logs


# Instância global do logger
logger = Logger()


def log_event(
    event_type: EventType,
    user_id: Optional[str] = None,
    resource_type: Optional[str] = None,
    resource_id: Optional[str] = None,
    action: Optional[str] = None,
    status: str = "success",
    details: Optional[Dict[str, Any]] = None,
    trace_id: Optional[str] = None,
    correlation_id: Optional[str] = None
) -> AuditLog:
    """Função helper para registrar eventos"""
    return logger.log(
        event_type=event_type,
        user_id=user_id,
        resource_type=resource_type,
        resource_id=resource_id,
        action=action,
        status=status,
        details=details,
        trace_id=trace_id,
        correlation_id=correlation_id
    )


def log_incident(
    incident_type: str,
    severity: str,
    user_id: Optional[str] = None,
    resource_id: Optional[str] = None,
    description: str = "",
    details: Optional[Dict[str, Any]] = None,
    trace_id: Optional[str] = None
) -> AuditLog:
    """Função helper para registrar incidentes"""
    return logger.log_incident(
        incident_type=incident_type,
        severity=severity,
        user_id=user_id,
        resource_id=resource_id,
        description=description,
        details=details,
        trace_id=trace_id
    )
