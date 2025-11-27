"""
Router da API mockada do Microsoft 365 Copilot.
Implementa endpoints para sessões, mensagens e eventos de auditoria.
"""

import random
from datetime import datetime, timedelta
from typing import Optional
from fastapi import APIRouter, Header, Query

from models.common import StandardResponse, ResponseMeta, SecurityContext, TraceabilityContext, PerformanceMetrics
from models.copilot import CopilotSession, CopilotMessage, CopilotAuditEvent
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

router = APIRouter(prefix="/copilot", tags=["Copilot"])


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
            scopes=["Copilot.Read", "Copilot.Write"]
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


@router.get("/sessions", response_model=StandardResponse)
async def list_sessions(
    page: int = Query(1, ge=1, description="Número da página"),
    page_size: int = Query(DEFAULT_PAGE_SIZE, ge=1, le=MAX_PAGE_SIZE, description="Tamanho da página"),
    user_id: Optional[str] = Query(None, description="Filtrar por usuário"),
    tenant_id: Optional[str] = Query(None, description="Filtrar por tenant"),
    x_correlation_id: Optional[str] = Header(None, description="ID de correlação")
):
    """
    Lista sessões de uso do Copilot.
    """
    correlation_id = x_correlation_id or generate_uuid()
    
    users = filter_users(tenant_id=tenant_id) if tenant_id else load_users_from_csv()
    
    source_apps = ["Word", "Excel", "PowerPoint", "Outlook", "Teams"]
    
    all_sessions = []
    for user in users:
        # Cria 2-8 sessões por usuário
        num_sessions = random.randint(2, 8)
        for sess_num in range(num_sessions):
            # Determina se é alto risco baseado no departamento
            is_high_risk = user['department'] in ['Finanças', 'Jurídico', 'TI']
            
            started = generate_random_datetime(1, 14)
            # Calcula ended_at baseado em started (30 min a 3 horas depois)
            started_dt = datetime.strptime(started, "%Y-%m-%dT%H:%M:%SZ")
            duration_minutes = random.randint(30, 180)
            ended_dt = started_dt + timedelta(minutes=duration_minutes)
            ended = ended_dt.strftime("%Y-%m-%dT%H:%M:%SZ")
            
            total_prompts = random.randint(5, 50)
            
            session = CopilotSession(
                session_id=f"copilot-sess-{user['user_id']}-{sess_num:04d}",
                user_id=user['user_id'],
                tenant_id=user['tenant_id'],
                started_at_utc=started,
                ended_at_utc=ended if random.random() > 0.1 else None,  # 10% sessões ainda ativas
                source_app=random.choice(source_apps),
                total_prompts=total_prompts,
                total_tokens_input=total_prompts * random.randint(50, 200),
                total_tokens_output=total_prompts * random.randint(80, 300),
                sensitivity_context={
                    "AccessedFinancialData": is_high_risk and random.random() > 0.5,
                    "AccessedPII": random.random() > 0.7,
                    "AccessedConfidentialDocs": is_high_risk and random.random() > 0.4
                }
            )
            all_sessions.append(session)
    
    # Filtra por user_id se especificado
    if user_id:
        all_sessions = [s for s in all_sessions if s.user_id == user_id]
    
    # Ordena por started_at (mais recente primeiro)
    all_sessions.sort(key=lambda x: x.started_at_utc, reverse=True)
    
    # Pagina os resultados
    paginated_sessions, total = paginate_items(all_sessions, page, page_size)
    
    context_user_id = paginated_sessions[0].user_id if paginated_sessions else "u001"
    context_tenant_id = tenant_id or "tenant-01"
    
    return StandardResponse(
        request_id=generate_uuid(),
        service=SERVICES["copilot"],
        timestamp_utc=datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ"),
        correlation_id=correlation_id,
        data={"sessions": [sess.model_dump() for sess in paginated_sessions]},
        meta=create_response_meta(
            user_id=context_user_id,
            tenant_id=context_tenant_id,
            items_count=len(paginated_sessions),
            page=page,
            page_size=page_size,
            total_items=total,
            correlation_id=correlation_id
        )
    )


@router.get("/sessions/{session_id}/messages", response_model=StandardResponse)
async def list_session_messages(
    session_id: str,
    page: int = Query(1, ge=1, description="Número da página"),
    page_size: int = Query(DEFAULT_PAGE_SIZE, ge=1, le=MAX_PAGE_SIZE, description="Tamanho da página"),
    x_correlation_id: Optional[str] = Header(None, description="ID de correlação")
):
    """
    Lista mensagens de uma sessão específica do Copilot.
    """
    correlation_id = x_correlation_id or generate_uuid()
    
    # Prompts de exemplo para simular interações realistas
    user_prompts = [
        "Crie uma tabela dinâmica com os dados de vendas por região",
        "Resuma os principais pontos deste documento",
        "Sugira melhorias para esta apresentação",
        "Analise os dados financeiros e identifique tendências",
        "Crie um gráfico de evolução mensal",
        "Revise o texto e corrija erros gramaticais",
        "Gere um resumo executivo baseado nesta planilha"
    ]
    
    assistant_responses = [
        "Criei a tabela dinâmica com os dados agrupados por região. Observe que...",
        "Os principais pontos são: 1) Crescimento de 15% no trimestre...",
        "Sugiro reorganizar os slides para melhor fluxo narrativo...",
        "Identifiquei as seguintes tendências nos dados financeiros...",
        "Gráfico criado. Mostra evolução positiva nos últimos 6 meses...",
        "Revisei o texto e corrigi 8 erros. Veja as alterações destacadas...",
        "Resumo executivo: O relatório apresenta crescimento consistente..."
    ]
    
    resource_types = ["Document", "Email", "Spreadsheet", None]
    
    all_messages = []
    num_messages = random.randint(10, 40)
    
    for i in range(num_messages):
        # Alterna entre user e assistant
        if i % 2 == 0:
            role = "user"
            content = random.choice(user_prompts)
            tokens_in = random.randint(50, 200)
            tokens_out = 0
        else:
            role = "assistant"
            content = random.choice(assistant_responses)
            tokens_in = 0
            tokens_out = random.randint(100, 400)
        
        # Ocasionalmente adiciona mensagens do sistema
        if random.random() > 0.9:
            role = "system"
            content = "Contexto atualizado com dados do documento"
            tokens_in = random.randint(20, 50)
            tokens_out = 0
        
        message = CopilotMessage(
            message_id=f"msg-{session_id}-{i:04d}",
            timestamp_utc=generate_random_datetime(1, 7),
            role=role,
            content=content,
            tokens_input=tokens_in,
            tokens_output=tokens_out,
            related_resource_type=random.choice(resource_types),
            related_resource_id=f"res-{random.randint(1000, 9999)}" if random.random() > 0.5 else None
        )
        all_messages.append(message)
    
    # Ordena por timestamp
    all_messages.sort(key=lambda x: x.timestamp_utc)
    
    # Pagina os resultados
    paginated_messages, total = paginate_items(all_messages, page, page_size)
    
    return StandardResponse(
        request_id=generate_uuid(),
        service=SERVICES["copilot"],
        timestamp_utc=datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ"),
        correlation_id=correlation_id,
        data={"messages": [msg.model_dump() for msg in paginated_messages]},
        meta=create_response_meta(
            user_id="u001",  # Assumindo usuário da sessão
            tenant_id="tenant-01",
            items_count=len(paginated_messages),
            page=page,
            page_size=page_size,
            total_items=total,
            correlation_id=correlation_id
        )
    )


@router.get("/audit-events", response_model=StandardResponse)
async def list_audit_events(
    page: int = Query(1, ge=1, description="Número da página"),
    page_size: int = Query(DEFAULT_PAGE_SIZE, ge=1, le=MAX_PAGE_SIZE, description="Tamanho da página"),
    user_id: Optional[str] = Query(None, description="Filtrar por usuário"),
    tenant_id: Optional[str] = Query(None, description="Filtrar por tenant"),
    x_correlation_id: Optional[str] = Header(None, description="ID de correlação")
):
    """
    Lista eventos de auditoria do Copilot.
    """
    correlation_id = x_correlation_id or generate_uuid()
    
    users = filter_users(tenant_id=tenant_id) if tenant_id else load_users_from_csv()
    
    actions = [
        "SessionStarted", "SessionEnded", "AccessedSensitiveData",
        "PromptBlocked", "DataLeakPrevented", "UnauthorizedAccessAttempt",
        "ExcessiveTokenUsage"
    ]
    resource_types = ["Document", "Email", "Spreadsheet", "Session"]
    
    all_events = []
    for i in range(random.randint(20, 100)):
        user = random.choice(users)
        action = random.choice(actions)
        
        # Determina se houve risco baseado na ação
        risk_detected = action in ["PromptBlocked", "DataLeakPrevented", "UnauthorizedAccessAttempt"]
        
        event = CopilotAuditEvent(
            event_id=f"copilot-evt-{i:06d}",
            timestamp_utc=generate_random_datetime(1, 14),
            user_id=user['user_id'],
            action=action,
            session_id=f"copilot-sess-{user['user_id']}-{random.randint(1, 100):04d}",
            resource_type=random.choice(resource_types) if random.random() > 0.3 else None,
            resource_id=f"res-{random.randint(1000, 9999)}" if random.random() > 0.5 else None,
            ip_address=generate_random_ip(),
            device_id=generate_device_id(),
            success=not risk_detected,
            risk_detected=risk_detected
        )
        all_events.append(event)
    
    # Filtra por user_id se especificado
    if user_id:
        all_events = [e for e in all_events if e.user_id == user_id]
    
    # Ordena por timestamp (mais recente primeiro)
    all_events.sort(key=lambda x: x.timestamp_utc, reverse=True)
    
    # Pagina os resultados
    paginated_events, total = paginate_items(all_events, page, page_size)
    
    context_user_id = paginated_events[0].user_id if paginated_events else "u001"
    context_tenant_id = tenant_id or "tenant-01"
    
    return StandardResponse(
        request_id=generate_uuid(),
        service=SERVICES["copilot"],
        timestamp_utc=datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ"),
        correlation_id=correlation_id,
        data={"audit_events": [evt.model_dump() for evt in paginated_events]},
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

