"""
Router da API mockada do Miro.
Implementa endpoints para boards, atividades e logs de auditoria.
"""

import random
from datetime import datetime
from typing import Optional
from fastapi import APIRouter, Header, Query

from models.common import StandardResponse, ResponseMeta, SecurityContext, TraceabilityContext, PerformanceMetrics
from models.miro import MiroBoard, MiroActivity, MiroAuditLog
from core.config import DEFAULT_PAGE_SIZE, MAX_PAGE_SIZE, SERVICES, SENSITIVITY_LABELS
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

router = APIRouter(prefix="/miro", tags=["Miro"])


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
            scopes=["board:read", "board:write"]
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


@router.get("/boards", response_model=StandardResponse)
async def list_boards(
    page: int = Query(1, ge=1, description="Número da página"),
    page_size: int = Query(DEFAULT_PAGE_SIZE, ge=1, le=MAX_PAGE_SIZE, description="Tamanho da página"),
    user_id: Optional[str] = Query(None, description="Filtrar por proprietário"),
    tenant_id: Optional[str] = Query(None, description="Filtrar por tenant"),
    x_correlation_id: Optional[str] = Header(None, description="ID de correlação")
):
    """
    Lista boards do Miro.
    Retorna todos os boards ou filtrados por proprietário/tenant.
    """
    correlation_id = x_correlation_id or generate_uuid()
    
    users = filter_users(tenant_id=tenant_id) if tenant_id else load_users_from_csv()
    
    board_names = [
        "Sprint Planning", "Retrospectiva", "Brainstorming", "Arquitetura",
        "Roadmap Produto", "User Journey", "Design System", "Workflow"
    ]
    access_levels = ["private", "team", "public"]
    
    all_boards = []
    for user in users:
        # Cria 1-4 boards por usuário
        num_boards = random.randint(1, 4)
        for board_num in range(num_boards):
            board = MiroBoard(
                board_id=f"board-{user['user_id']}-{board_num:03d}",
                name=f"{random.choice(board_names)} {user['department']} Q{random.randint(1,4)}",
                owner_user_id=user['user_id'],
                created_at_utc=generate_random_datetime(7, 180),
                last_activity_utc=generate_random_datetime(1, 7),
                access_level=random.choice(access_levels),
                sensitivity_label=random.choice(SENSITIVITY_LABELS),
                tenant_id=user['tenant_id']
            )
            all_boards.append(board)
    
    # Filtra por user_id se especificado
    if user_id:
        all_boards = [b for b in all_boards if b.owner_user_id == user_id]
    
    # Pagina os resultados
    paginated_boards, total = paginate_items(all_boards, page, page_size)
    
    context_user_id = paginated_boards[0].owner_user_id if paginated_boards else "u001"
    context_tenant_id = tenant_id or "tenant-01"
    
    return StandardResponse(
        request_id=generate_uuid(),
        service=SERVICES["miro"],
        timestamp_utc=datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ"),
        correlation_id=correlation_id,
        data={"boards": [board.model_dump() for board in paginated_boards]},
        meta=create_response_meta(
            user_id=context_user_id,
            tenant_id=context_tenant_id,
            items_count=len(paginated_boards),
            page=page,
            page_size=page_size,
            total_items=total,
            correlation_id=correlation_id
        )
    )


@router.get("/boards/{board_id}/activities", response_model=StandardResponse)
async def list_board_activities(
    board_id: str,
    page: int = Query(1, ge=1, description="Número da página"),
    page_size: int = Query(DEFAULT_PAGE_SIZE, ge=1, le=MAX_PAGE_SIZE, description="Tamanho da página"),
    user_id: Optional[str] = Query(None, description="Filtrar por usuário"),
    x_correlation_id: Optional[str] = Header(None, description="ID de correlação")
):
    """
    Lista atividades em um board específico do Miro.
    """
    correlation_id = x_correlation_id or generate_uuid()
    
    users = load_users_from_csv()
    
    actions = [
        "CardCreated", "CardMoved", "CardUpdated", "CardDeleted",
        "CommentAdded", "ShapeMoved", "StickyNoteAdded",
        "ImageUploaded", "TextEdited", "ConnectorDrawn"
    ]
    
    details_templates = [
        "Card '{}' criado na coluna {}",
        "Comentário adicionado: '{}'",
        "Shape movido para posição ({}, {})",
        "Sticky note '{}' adicionado",
        "Imagem carregada: {}",
        "Texto editado em {}",
        "Conector desenhado entre elementos"
    ]
    
    all_activities = []
    for i in range(random.randint(20, 100)):
        user = random.choice(users)
        action = random.choice(actions)
        
        # Gera detalhes contextuais baseado na ação
        if "Card" in action:
            details = random.choice(details_templates[:1]).format(
                f"Task {random.randint(1, 50)}",
                random.choice(["To Do", "In Progress", "Done", "Review"])
            )
        elif "Comment" in action:
            details = details_templates[1].format("Ótima ideia! Vamos implementar isso.")
        elif "Shape" in action:
            details = details_templates[2].format(random.randint(0, 1000), random.randint(0, 1000))
        else:
            details = random.choice(details_templates)
        
        activity = MiroActivity(
            activity_id=f"miro-act-{board_id}-{i:05d}",
            timestamp_utc=generate_random_datetime(1, 7),
            user_id=user['user_id'],
            action=action,
            details=details,
            ip_address=generate_random_ip(),
            device_id=generate_device_id()
        )
        all_activities.append(activity)
    
    # Filtra por user_id se especificado
    if user_id:
        all_activities = [a for a in all_activities if a.user_id == user_id]
    
    # Ordena por timestamp (mais recente primeiro)
    all_activities.sort(key=lambda x: x.timestamp_utc, reverse=True)
    
    # Pagina os resultados
    paginated_activities, total = paginate_items(all_activities, page, page_size)
    
    context_user_id = paginated_activities[0].user_id if paginated_activities else "u001"
    
    return StandardResponse(
        request_id=generate_uuid(),
        service=SERVICES["miro"],
        timestamp_utc=datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ"),
        correlation_id=correlation_id,
        data={"activities": [act.model_dump() for act in paginated_activities]},
        meta=create_response_meta(
            user_id=context_user_id,
            tenant_id="tenant-01",
            items_count=len(paginated_activities),
            page=page,
            page_size=page_size,
            total_items=total,
            correlation_id=correlation_id
        )
    )


@router.get("/audit-logs", response_model=StandardResponse)
async def list_audit_logs(
    page: int = Query(1, ge=1, description="Número da página"),
    page_size: int = Query(DEFAULT_PAGE_SIZE, ge=1, le=MAX_PAGE_SIZE, description="Tamanho da página"),
    user_id: Optional[str] = Query(None, description="Filtrar por usuário"),
    tenant_id: Optional[str] = Query(None, description="Filtrar por tenant"),
    x_correlation_id: Optional[str] = Header(None, description="ID de correlação")
):
    """
    Lista logs de auditoria do Miro.
    """
    correlation_id = x_correlation_id or generate_uuid()
    
    users = filter_users(tenant_id=tenant_id) if tenant_id else load_users_from_csv()
    
    actions = [
        "BoardCreated", "BoardShared", "BoardDeleted", "BoardExported",
        "MemberAdded", "MemberRemoved", "PermissionChanged",
        "ExternalShareCreated", "ApiKeyGenerated"
    ]
    resource_types = ["Board", "Member", "Permission", "ApiKey"]
    
    all_logs = []
    for i in range(random.randint(30, 150)):
        user = random.choice(users)
        
        log = MiroAuditLog(
            event_id=f"miro-evt-{i:06d}",
            timestamp_utc=generate_random_datetime(1, 14),
            user_id=user['user_id'],
            action=random.choice(actions),
            resource_type=random.choice(resource_types),
            resource_id=f"board-{random.randint(1000, 9999)}",
            ip_address=generate_random_ip(),
            device_id=generate_device_id(),
            success=random.choice([True, True, True, False])
        )
        all_logs.append(log)
    
    # Filtra por user_id se especificado
    if user_id:
        all_logs = [l for l in all_logs if l.user_id == user_id]
    
    # Ordena por timestamp (mais recente primeiro)
    all_logs.sort(key=lambda x: x.timestamp_utc, reverse=True)
    
    # Pagina os resultados
    paginated_logs, total = paginate_items(all_logs, page, page_size)
    
    context_user_id = paginated_logs[0].user_id if paginated_logs else "u001"
    context_tenant_id = tenant_id or "tenant-01"
    
    return StandardResponse(
        request_id=generate_uuid(),
        service=SERVICES["miro"],
        timestamp_utc=datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ"),
        correlation_id=correlation_id,
        data={"audit_logs": [log.model_dump() for log in paginated_logs]},
        meta=create_response_meta(
            user_id=context_user_id,
            tenant_id=context_tenant_id,
            items_count=len(paginated_logs),
            page=page,
            page_size=page_size,
            total_items=total,
            correlation_id=correlation_id
        )
    )

