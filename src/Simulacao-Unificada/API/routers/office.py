"""
Router da API mockada do Microsoft 365 Office.
Implementa endpoints para documentos, e-mails e eventos de calendário.
"""

import random
from datetime import datetime, timedelta
from typing import Optional
from fastapi import APIRouter, Header, Query

from models.common import StandardResponse, ResponseMeta, SecurityContext, TraceabilityContext, PerformanceMetrics
from models.office import OfficeDocument, Email, CalendarEvent
from core.config import DEFAULT_PAGE_SIZE, MAX_PAGE_SIZE, SERVICES, SENSITIVITY_LABELS, RETENTION_POLICIES
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

router = APIRouter(prefix="/office", tags=["Office"])


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
            scopes=["Files.ReadWrite.All", "Mail.ReadWrite", "Calendars.ReadWrite"]
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


@router.get("/documents", response_model=StandardResponse)
async def list_documents(
    page: int = Query(1, ge=1, description="Número da página"),
    page_size: int = Query(DEFAULT_PAGE_SIZE, ge=1, le=MAX_PAGE_SIZE, description="Tamanho da página"),
    user_id: Optional[str] = Query(None, description="Filtrar por proprietário"),
    tenant_id: Optional[str] = Query(None, description="Filtrar por tenant"),
    x_correlation_id: Optional[str] = Header(None, description="ID de correlação")
):
    """
    Lista documentos do Office (Word, Excel, PowerPoint).
    """
    correlation_id = x_correlation_id or generate_uuid()
    
    users = filter_users(tenant_id=tenant_id) if tenant_id else load_users_from_csv()
    
    doc_types = ["Word", "Excel", "PowerPoint"]
    doc_names = {
        "Word": ["Relatório_Anual", "Proposta_Comercial", "Manual_Procedimentos", "Ata_Reuniao"],
        "Excel": ["Budget_2026", "Forecast_Vendas", "Dashboard_KPIs", "Controle_Estoque"],
        "PowerPoint": ["Apresentacao_Resultados", "Treinamento_Equipe", "Pitch_Clientes", "Revisao_Estrategia"]
    }
    
    all_documents = []
    for user in users:
        # Cria 2-6 documentos por usuário
        num_docs = random.randint(2, 6)
        for doc_num in range(num_docs):
            doc_type = random.choice(doc_types)
            name = f"{random.choice(doc_names[doc_type])}_{doc_num + 1}"
            
            document = OfficeDocument(
                document_id=f"office-doc-{user['user_id']}-{doc_num:03d}",
                type=doc_type,
                owner_user_id=user['user_id'],
                created_at_utc=generate_random_datetime(7, 365),
                last_modified_at_utc=generate_random_datetime(1, 30),
                sensitivity_label=random.choice(SENSITIVITY_LABELS),
                retention_policy=random.choice(RETENTION_POLICIES),
                is_shared_externally=random.choice([False, False, False, True]),  # 25% compartilhado externamente
                last_access_by_user_id=random.choice(users)['user_id'],
                name=name
            )
            all_documents.append(document)
    
    # Filtra por user_id se especificado
    if user_id:
        all_documents = [d for d in all_documents if d.owner_user_id == user_id]
    
    # Ordena por last_modified (mais recente primeiro)
    all_documents.sort(key=lambda x: x.last_modified_at_utc, reverse=True)
    
    # Pagina os resultados
    paginated_docs, total = paginate_items(all_documents, page, page_size)
    
    context_user_id = paginated_docs[0].owner_user_id if paginated_docs else "u001"
    context_tenant_id = tenant_id or "tenant-01"
    
    return StandardResponse(
        request_id=generate_uuid(),
        service=SERVICES["office"],
        timestamp_utc=datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ"),
        correlation_id=correlation_id,
        data={"documents": [doc.model_dump() for doc in paginated_docs]},
        meta=create_response_meta(
            user_id=context_user_id,
            tenant_id=context_tenant_id,
            items_count=len(paginated_docs),
            page=page,
            page_size=page_size,
            total_items=total,
            correlation_id=correlation_id
        )
    )


@router.get("/emails", response_model=StandardResponse)
async def list_emails(
    page: int = Query(1, ge=1, description="Número da página"),
    page_size: int = Query(DEFAULT_PAGE_SIZE, ge=1, le=MAX_PAGE_SIZE, description="Tamanho da página"),
    user_id: Optional[str] = Query(None, description="Filtrar por remetente"),
    tenant_id: Optional[str] = Query(None, description="Filtrar por tenant"),
    x_correlation_id: Optional[str] = Header(None, description="ID de correlação")
):
    """
    Lista e-mails do Outlook.
    """
    correlation_id = x_correlation_id or generate_uuid()
    
    users = filter_users(tenant_id=tenant_id) if tenant_id else load_users_from_csv()
    
    subjects = [
        "Revisão do Orçamento Trimestral",
        "Convite: Reunião de Planejamento",
        "FW: Documentação do Projeto",
        "RE: Aprovação de Proposta",
        "Relatório Mensal - Novembro",
        "Atualização: Status do Desenvolvimento",
        "Solicitação de Acesso",
        "Confirmação de Entrega"
    ]
    
    all_emails = []
    for user in users:
        # Cria 5-15 e-mails por usuário
        num_emails = random.randint(5, 15)
        for email_num in range(num_emails):
            # Seleciona destinatários aleatórios (1-4)
            num_recipients = random.randint(1, 4)
            recipients = random.sample([u['user_id'] for u in users if u['user_id'] != user['user_id']], 
                                     min(num_recipients, len(users) - 1))
            
            email = Email(
                email_id=f"email-{user['user_id']}-{email_num:04d}",
                subject=random.choice(subjects),
                sender_user_id=user['user_id'],
                recipient_user_ids=recipients,
                sent_at_utc=generate_random_datetime(1, 14),
                has_attachments=random.choice([True, False]),
                sensitivity_label=random.choice(SENSITIVITY_LABELS),
                is_phishing_suspected=random.choice([False, False, False, False, False, True])  # 16% suspeita
            )
            all_emails.append(email)
    
    # Filtra por user_id se especificado
    if user_id:
        all_emails = [e for e in all_emails if e.sender_user_id == user_id]
    
    # Ordena por sent_at (mais recente primeiro)
    all_emails.sort(key=lambda x: x.sent_at_utc, reverse=True)
    
    # Pagina os resultados
    paginated_emails, total = paginate_items(all_emails, page, page_size)
    
    context_user_id = paginated_emails[0].sender_user_id if paginated_emails else "u001"
    context_tenant_id = tenant_id or "tenant-01"
    
    return StandardResponse(
        request_id=generate_uuid(),
        service=SERVICES["office"],
        timestamp_utc=datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ"),
        correlation_id=correlation_id,
        data={"emails": [email.model_dump() for email in paginated_emails]},
        meta=create_response_meta(
            user_id=context_user_id,
            tenant_id=context_tenant_id,
            items_count=len(paginated_emails),
            page=page,
            page_size=page_size,
            total_items=total,
            correlation_id=correlation_id
        )
    )


@router.get("/calendar-events", response_model=StandardResponse)
async def list_calendar_events(
    page: int = Query(1, ge=1, description="Número da página"),
    page_size: int = Query(DEFAULT_PAGE_SIZE, ge=1, le=MAX_PAGE_SIZE, description="Tamanho da página"),
    user_id: Optional[str] = Query(None, description="Filtrar por organizador"),
    tenant_id: Optional[str] = Query(None, description="Filtrar por tenant"),
    x_correlation_id: Optional[str] = Header(None, description="ID de correlação")
):
    """
    Lista eventos de calendário do Outlook.
    """
    correlation_id = x_correlation_id or generate_uuid()
    
    users = filter_users(tenant_id=tenant_id) if tenant_id else load_users_from_csv()
    
    event_subjects = [
        "Reunião de Planejamento Estratégico",
        "Daily Standup",
        "Revisão de Sprint",
        "Apresentação de Resultados",
        "Treinamento: Novas Ferramentas",
        "1:1 com Gestor",
        "Workshop: Segurança da Informação",
        "Alinhamento com Cliente"
    ]
    
    locations = ["Sala de Conferência 3A", "Escritório Principal", "Virtual", None]
    
    all_events = []
    for user in users:
        # Cria 3-10 eventos por usuário
        num_events = random.randint(3, 10)
        for event_num in range(num_events):
            # Gera horário do evento (futuro ou passado recente)
            days_offset = random.randint(-7, 14)
            hour = random.randint(8, 18)
            start_dt = datetime.utcnow() + timedelta(days=days_offset, hours=hour - datetime.utcnow().hour)
            start_dt = start_dt.replace(minute=0, second=0, microsecond=0)
            
            # Duração: 30min, 1h ou 2h
            duration_hours = random.choice([0.5, 1, 2])
            end_dt = start_dt + timedelta(hours=duration_hours)
            
            # Seleciona participantes (2-5)
            num_attendees = random.randint(2, 5)
            attendees = random.sample([u['user_id'] for u in users], min(num_attendees, len(users)))
            
            is_online = random.choice([True, False])
            location = "Virtual" if is_online else random.choice(locations)
            
            event = CalendarEvent(
                event_id=f"cal-evt-{user['user_id']}-{event_num:04d}",
                organizer_user_id=user['user_id'],
                start_utc=start_dt.strftime("%Y-%m-%dT%H:%M:%SZ"),
                end_utc=end_dt.strftime("%Y-%m-%dT%H:%M:%SZ"),
                subject=random.choice(event_subjects),
                attendee_user_ids=attendees,
                location=location,
                is_online_meeting=is_online,
                meeting_url=f"https://teams.microsoft.com/meet/{generate_uuid()[:8]}" if is_online else None,
                sensitivity_label=random.choice(SENSITIVITY_LABELS)
            )
            all_events.append(event)
    
    # Filtra por user_id se especificado
    if user_id:
        all_events = [e for e in all_events if e.organizer_user_id == user_id]
    
    # Ordena por start_utc (mais próximo primeiro)
    all_events.sort(key=lambda x: x.start_utc)
    
    # Pagina os resultados
    paginated_events, total = paginate_items(all_events, page, page_size)
    
    context_user_id = paginated_events[0].organizer_user_id if paginated_events else "u001"
    context_tenant_id = tenant_id or "tenant-01"
    
    return StandardResponse(
        request_id=generate_uuid(),
        service=SERVICES["office"],
        timestamp_utc=datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ"),
        correlation_id=correlation_id,
        data={"calendar_events": [evt.model_dump() for evt in paginated_events]},
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

