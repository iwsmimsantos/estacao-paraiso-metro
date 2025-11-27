"""
Router da API mockada do Microsoft Sentinel.
Implementa endpoints para incidentes, alertas e eventos de segurança agregados.
Correlaciona dados dos outros serviços para simular rastreabilidade.
"""

import random
from datetime import datetime
from typing import Optional
from fastapi import APIRouter, Header, Query

from models.common import StandardResponse, ResponseMeta, SecurityContext, TraceabilityContext, PerformanceMetrics
from models.sentinel import SentinelIncident, SentinelAlert, SentinelEvent
from core.config import DEFAULT_PAGE_SIZE, MAX_PAGE_SIZE, SERVICES
from core.utils import (
    load_users_from_csv,
    filter_users,
    generate_uuid,
    generate_processing_time,
    generate_random_datetime,
    generate_random_ip,
    generate_device_id,
    paginate_items
)

router = APIRouter(prefix="/sentinel", tags=["Sentinel"])


def create_response_meta(
    user_id: str,
    tenant_id: str,
    items_count: int,
    page: Optional[int] = None,
    page_size: Optional[int] = None,
    total_items: Optional[int] = None,
    correlation_id: Optional[str] = None
) -> ResponseMeta:
    """Cria metadados padrão de resposta."""
    user = next((u for u in load_users_from_csv() if u['user_id'] == user_id), None)
    
    return ResponseMeta(
        page=page,
        page_size=page_size,
        total_items=total_items,
        security_context=SecurityContext(
            user_id=user_id,
            tenant_id=tenant_id,
            mfa_required=True,
            mfa_enabled=user['mfa_enabled'] if user else True,
            ip_address=generate_random_ip(),
            device_id=generate_device_id(),
            auth_method="OAuth2_Bearer",
            scopes=["SecurityEvents.Read.All", "SecurityIncident.ReadWrite.All"]
        ),
        traceability=TraceabilityContext(
            trace_id=generate_uuid(),
            span_id=generate_uuid(),
            source_system="mock-api",
            ingested_at_utc=datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
        ),
        performance=PerformanceMetrics(
            processing_time_ms=generate_processing_time(),
            items_in_response=items_count
        )
    )


@router.get("/incidents", response_model=StandardResponse)
async def list_incidents(
    page: int = Query(1, ge=1, description="Número da página"),
    page_size: int = Query(DEFAULT_PAGE_SIZE, ge=1, le=MAX_PAGE_SIZE, description="Tamanho da página"),
    user_id: Optional[str] = Query(None, description="Filtrar por responsável"),
    tenant_id: Optional[str] = Query(None, description="Filtrar por tenant"),
    severity: Optional[str] = Query(None, description="Filtrar por severidade"),
    x_correlation_id: Optional[str] = Header(None, description="ID de correlação")
):
    """
    Lista incidentes de segurança do Sentinel.
    Incidentes agregam múltiplos alertas relacionados.
    """
    correlation_id = x_correlation_id or generate_uuid()
    
    users = filter_users(tenant_id=tenant_id) if tenant_id else load_users_from_csv()
    
    # Títulos de incidentes realistas
    incident_titles = [
        "Acesso não autorizado a dados financeiros",
        "Tentativa de exfiltração de dados",
        "Login suspeito de múltiplas localizações",
        "Compartilhamento externo de documentos confidenciais",
        "Atividade anômala no Copilot",
        "Múltiplas falhas de autenticação",
        "Download massivo de arquivos",
        "Alteração não autorizada de permissões",
        "Suspeita de phishing em e-mails",
        "Acesso a recursos sensíveis fora do horário"
    ]
    
    descriptions = [
        "Múltiplas tentativas de acesso a documentos financeiros confidenciais",
        "Padrão de download anômalo detectado em curto período",
        "Logins do mesmo usuário de diferentes países em 1 hora",
        "Documentos com alta sensibilidade compartilhados externamente",
        "Prompts suspeitos detectados pelo Copilot guardrails",
        "Mais de 10 tentativas de login falhadas em 5 minutos",
        "Download de mais de 100 arquivos em menos de 10 minutos",
        "Usuário alterou permissões de acesso sem autorização",
        "E-mails com características de phishing detectados",
        "Acesso a sistema crítico às 3h da manhã"
    ]
    
    severities = ["Low", "Medium", "High", "Critical"]
    statuses = ["Active", "Resolved"]
    
    all_incidents = []
    for i in range(random.randint(10, 40)):
        owner = random.choice(users)
        incident_severity = random.choice(severities)
        
        # Gera alertas relacionados (2-8)
        num_alerts = random.randint(2, 8)
        related_alerts = [f"alert-{random.randint(1000, 9999):04d}" for _ in range(num_alerts)]
        
        created = generate_random_datetime(1, 30)
        updated = generate_random_datetime(1, 7)
        
        incident = SentinelIncident(
            incident_id=f"incident-{i:04d}",
            title=random.choice(incident_titles),
            severity=incident_severity,
            status=random.choice(statuses),
            owner_user_id=owner['user_id'],
            created_at_utc=created,
            updated_at_utc=updated,
            related_alert_ids=related_alerts,
            tenant_id=owner['tenant_id'],
            description=random.choice(descriptions)
        )
        all_incidents.append(incident)
    
    # Filtra por user_id se especificado
    if user_id:
        all_incidents = [i for i in all_incidents if i.owner_user_id == user_id]
    
    # Filtra por severity se especificado
    if severity:
        all_incidents = [i for i in all_incidents if i.severity == severity]
    
    # Ordena por updated_at (mais recente primeiro)
    all_incidents.sort(key=lambda x: x.updated_at_utc, reverse=True)
    
    # Pagina os resultados
    paginated_incidents, total = paginate_items(all_incidents, page, page_size)
    
    context_user_id = paginated_incidents[0].owner_user_id if paginated_incidents else "u001"
    context_tenant_id = tenant_id or "tenant-01"
    
    return StandardResponse(
        request_id=generate_uuid(),
        service=SERVICES["sentinel"],
        timestamp_utc=datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ"),
        correlation_id=correlation_id,
        data={"incidents": [inc.model_dump() for inc in paginated_incidents]},
        meta=create_response_meta(
            user_id=context_user_id,
            tenant_id=context_tenant_id,
            items_count=len(paginated_incidents),
            page=page,
            page_size=page_size,
            total_items=total,
            correlation_id=correlation_id
        )
    )


@router.get("/alerts", response_model=StandardResponse)
async def list_alerts(
    page: int = Query(1, ge=1, description="Número da página"),
    page_size: int = Query(DEFAULT_PAGE_SIZE, ge=1, le=MAX_PAGE_SIZE, description="Tamanho da página"),
    user_id: Optional[str] = Query(None, description="Filtrar por usuário"),
    tenant_id: Optional[str] = Query(None, description="Filtrar por tenant"),
    source_service: Optional[str] = Query(None, description="Filtrar por serviço de origem"),
    x_correlation_id: Optional[str] = Header(None, description="ID de correlação")
):
    """
    Lista alertas de segurança do Sentinel.
    Alertas vêm de diferentes serviços (sharepoint, miro, copilot, office).
    """
    correlation_id = x_correlation_id or generate_uuid()
    
    users = filter_users(tenant_id=tenant_id) if tenant_id else load_users_from_csv()
    
    source_services = ["sharepoint", "miro", "copilot", "office"]
    risk_levels = ["low", "medium", "high", "critical"]
    resource_types = ["Document", "Board", "Email", "Session", "Site", "Calendar"]
    
    # Descrições de alertas por serviço
    alert_descriptions = {
        "sharepoint": [
            "Download massivo de documentos confidenciais",
            "Compartilhamento externo de arquivo sensível",
            "Acesso negado a documento financeiro",
            "Modificação de permissões de site"
        ],
        "miro": [
            "Board confidencial compartilhado publicamente",
            "Exportação massiva de boards",
            "Acesso a board de projeto sensível",
            "Membro externo adicionado a board privado"
        ],
        "copilot": [
            "Prompt bloqueado por guardrails de segurança",
            "Acesso a dados financeiros via Copilot",
            "Tentativa de extrair PII via prompts",
            "Uso excessivo de tokens em sessão"
        ],
        "office": [
            "E-mail suspeito de phishing enviado",
            "Documento com malware detectado",
            "Compartilhamento externo de planilha confidencial",
            "Reunião com participante não autorizado"
        ]
    }
    
    all_alerts = []
    for i in range(random.randint(50, 200)):
        user = random.choice(users)
        service = random.choice(source_services)
        
        # Usa correlation_id para simular rastreabilidade entre serviços
        alert_correlation_id = correlation_id if random.random() > 0.7 else generate_uuid()
        
        alert = SentinelAlert(
            alert_id=f"alert-{i:05d}",
            timestamp_utc=generate_random_datetime(1, 14),
            source_service=service,
            description=random.choice(alert_descriptions[service]),
            user_id=user['user_id'],
            risk_level=random.choice(risk_levels),
            related_resource_type=random.choice(resource_types),
            related_resource_id=f"{service}-res-{random.randint(1000, 9999)}",
            correlation_id=alert_correlation_id,
            ip_address=generate_random_ip(),
            device_id=generate_device_id(),
            tenant_id=user['tenant_id']
        )
        all_alerts.append(alert)
    
    # Filtra por user_id se especificado
    if user_id:
        all_alerts = [a for a in all_alerts if a.user_id == user_id]
    
    # Filtra por source_service se especificado
    if source_service:
        all_alerts = [a for a in all_alerts if a.source_service == source_service]
    
    # Ordena por timestamp (mais recente primeiro)
    all_alerts.sort(key=lambda x: x.timestamp_utc, reverse=True)
    
    # Pagina os resultados
    paginated_alerts, total = paginate_items(all_alerts, page, page_size)
    
    context_user_id = paginated_alerts[0].user_id if paginated_alerts else "u001"
    context_tenant_id = tenant_id or "tenant-01"
    
    return StandardResponse(
        request_id=generate_uuid(),
        service=SERVICES["sentinel"],
        timestamp_utc=datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ"),
        correlation_id=correlation_id,
        data={"alerts": [alert.model_dump() for alert in paginated_alerts]},
        meta=create_response_meta(
            user_id=context_user_id,
            tenant_id=context_tenant_id,
            items_count=len(paginated_alerts),
            page=page,
            page_size=page_size,
            total_items=total,
            correlation_id=correlation_id
        )
    )


@router.get("/events", response_model=StandardResponse)
async def list_events(
    page: int = Query(1, ge=1, description="Número da página"),
    page_size: int = Query(DEFAULT_PAGE_SIZE, ge=1, le=MAX_PAGE_SIZE, description="Tamanho da página"),
    user_id: Optional[str] = Query(None, description="Filtrar por usuário"),
    tenant_id: Optional[str] = Query(None, description="Filtrar por tenant"),
    source_service: Optional[str] = Query(None, description="Filtrar por serviço"),
    status: Optional[str] = Query(None, description="Filtrar por status (Success/Failure)"),
    x_correlation_id: Optional[str] = Header(None, description="ID de correlação")
):
    """
    Lista eventos de segurança normalizados do Sentinel.
    Eventos agregam logs de todos os serviços em formato padronizado.
    """
    correlation_id = x_correlation_id or generate_uuid()
    
    users = filter_users(tenant_id=tenant_id) if tenant_id else load_users_from_csv()
    
    source_services = ["sharepoint", "miro", "copilot", "office", "sentinel"]
    
    # Operações por serviço
    operations = {
        "sharepoint": ["FileAccessed", "FileDownloaded", "FileUploaded", "SiteAccessed", "PermissionChanged"],
        "miro": ["BoardAccessed", "CardCreated", "BoardShared", "ExportPerformed"],
        "copilot": ["SessionStarted", "PromptSubmitted", "DataAccessed", "SessionEnded"],
        "office": ["EmailSent", "DocumentOpened", "MeetingScheduled", "CalendarAccessed"],
        "sentinel": ["IncidentCreated", "AlertGenerated", "PolicyEvaluated"]
    }
    
    statuses = ["Success", "Failure"]
    resource_types = ["Document", "Board", "Email", "Session", "Site", "Calendar", "Alert", "Incident"]
    
    all_events = []
    for i in range(random.randint(100, 500)):
        user = random.choice(users)
        service = random.choice(source_services)
        event_status = random.choice(statuses)
        
        # 10% de falhas
        if random.random() > 0.9:
            event_status = "Failure"
        
        event = SentinelEvent(
            event_id=f"evt-sentinel-{i:06d}",
            timestamp_utc=generate_random_datetime(1, 7),
            source_service=service,
            user_id=user['user_id'],
            operation=random.choice(operations[service]),
            status=event_status,
            ip_address=generate_random_ip(),
            device_id=generate_device_id(),
            tenant_id=user['tenant_id'],
            resource_type=random.choice(resource_types) if random.random() > 0.3 else None,
            resource_id=f"{service}-res-{random.randint(1000, 9999)}" if random.random() > 0.3 else None
        )
        all_events.append(event)
    
    # Filtra por user_id se especificado
    if user_id:
        all_events = [e for e in all_events if e.user_id == user_id]
    
    # Filtra por source_service se especificado
    if source_service:
        all_events = [e for e in all_events if e.source_service == source_service]
    
    # Filtra por status se especificado
    if status:
        all_events = [e for e in all_events if e.status == status]
    
    # Ordena por timestamp (mais recente primeiro)
    all_events.sort(key=lambda x: x.timestamp_utc, reverse=True)
    
    # Pagina os resultados
    paginated_events, total = paginate_items(all_events, page, page_size)
    
    context_user_id = paginated_events[0].user_id if paginated_events else "u001"
    context_tenant_id = tenant_id or "tenant-01"
    
    return StandardResponse(
        request_id=generate_uuid(),
        service=SERVICES["sentinel"],
        timestamp_utc=datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ"),
        correlation_id=correlation_id,
        data={"events": [evt.model_dump() for evt in paginated_events]},
        meta=create_response_meta(
            user_id=context_user_id,
            tenant_id=context_tenant_id,
            items_count=len(paginated_events),
            page=page,
            page_size=page_size,
            total_items=total,
            correlation_id=correlation_id
        )
    )

