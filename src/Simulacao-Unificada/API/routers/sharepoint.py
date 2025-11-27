"""
Router da API mockada do SharePoint.
Implementa endpoints para sites, documentos e logs de auditoria.
"""

import random
from datetime import datetime
from typing import Optional
from fastapi import APIRouter, Header, Query

from models.common import StandardResponse, ResponseMeta, SecurityContext, TraceabilityContext, PerformanceMetrics
from models.sharepoint import SharePointSite, SharePointDocument, SharePointAuditLog
from core.config import DEFAULT_PAGE_SIZE, MAX_PAGE_SIZE, SERVICES, SENSITIVITY_LABELS, RETENTION_POLICIES
from core.utils import (
    load_users_from_csv, 
    filter_users, 
    generate_uuid, 
    generate_processing_time,
    generate_random_datetime,
    generate_random_ip,
    generate_device_id,
    paginate_items,
    get_random_user
)

router = APIRouter(prefix="/sharepoint", tags=["SharePoint"])


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
            scopes=["Sites.Read.All", "Files.Read.All"]
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


@router.get("/sites", response_model=StandardResponse)
async def list_sites(
    page: int = Query(1, ge=1, description="Número da página"),
    page_size: int = Query(DEFAULT_PAGE_SIZE, ge=1, le=MAX_PAGE_SIZE, description="Tamanho da página"),
    user_id: Optional[str] = Query(None, description="Filtrar por proprietário"),
    tenant_id: Optional[str] = Query(None, description="Filtrar por tenant"),
    x_correlation_id: Optional[str] = Header(None, description="ID de correlação")
):
    """
    Lista sites do SharePoint.
    Retorna todos os sites ou filtrados por proprietário/tenant.
    """
    correlation_id = x_correlation_id or generate_uuid()
    
    # Gera sites mockados baseados nos usuários do CSV
    users = filter_users(tenant_id=tenant_id) if tenant_id else load_users_from_csv()
    
    all_sites = []
    for idx, user in enumerate(users):
        # Cria 1-3 sites por usuário
        num_sites = random.randint(1, 3)
        for site_num in range(num_sites):
            site = SharePointSite(
                site_id=f"site-{user['user_id']}-{site_num:03d}",
                name=f"Portal {user['department']} - {site_num + 1}",
                url=f"https://empresa.sharepoint.com/sites/{user['department'].lower()}-{site_num + 1}",
                owner_user_id=user['user_id'],
                created_at_utc=generate_random_datetime(30, 365),
                sensitivity_label=random.choice(SENSITIVITY_LABELS),
                retention_policy=random.choice(RETENTION_POLICIES),
                is_active=user['is_active']
            )
            all_sites.append(site)
    
    # Filtra por user_id se especificado
    if user_id:
        all_sites = [s for s in all_sites if s.owner_user_id == user_id]
    
    # Pagina os resultados
    paginated_sites, total = paginate_items(all_sites, page, page_size)
    
    # Determina usuário e tenant para o contexto (usa primeiro site ou padrão)
    context_user_id = paginated_sites[0].owner_user_id if paginated_sites else "u001"
    context_tenant_id = tenant_id or "tenant-01"
    
    return StandardResponse(
        request_id=generate_uuid(),
        service=SERVICES["sharepoint"],
        timestamp_utc=datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ"),
        correlation_id=correlation_id,
        data={"sites": [site.model_dump() for site in paginated_sites]},
        meta=create_response_meta(
            user_id=context_user_id,
            tenant_id=context_tenant_id,
            items_count=len(paginated_sites),
            page=page,
            page_size=page_size,
            total_items=total,
            correlation_id=correlation_id
        )
    )


@router.get("/sites/{site_id}/documents", response_model=StandardResponse)
async def list_documents(
    site_id: str,
    page: int = Query(1, ge=1, description="Número da página"),
    page_size: int = Query(DEFAULT_PAGE_SIZE, ge=1, le=MAX_PAGE_SIZE, description="Tamanho da página"),
    user_id: Optional[str] = Query(None, description="Filtrar por último modificador"),
    x_correlation_id: Optional[str] = Header(None, description="ID de correlação")
):
    """
    Lista documentos de um site específico do SharePoint.
    """
    correlation_id = x_correlation_id or generate_uuid()
    
    users = load_users_from_csv()
    
    # Gera documentos mockados para o site
    doc_types = ["Relatório Trimestral", "Planilha Orçamentária", "Apresentação", "Manual", "Política"]
    extensions = [".docx", ".xlsx", ".pptx", ".pdf", ".txt"]
    
    all_docs = []
    for i in range(random.randint(10, 50)):
        owner = random.choice(users)
        modifier = random.choice(users)
        
        doc = SharePointDocument(
            doc_id=f"doc-{site_id}-{i:04d}",
            site_id=site_id,
            name=f"{random.choice(doc_types)}_{i+1}{random.choice(extensions)}",
            path=f"/Documentos Compartilhados/{owner['department']}/",
            version=f"{random.randint(1, 5)}.{random.randint(0, 9)}",
            last_modified_at_utc=generate_random_datetime(1, 30),
            last_modified_by_user_id=modifier['user_id'],
            sensitivity_label=random.choice(SENSITIVITY_LABELS),
            checked_out_by_user_id=random.choice([None, None, None, modifier['user_id']]),
            is_encrypted_at_rest=random.choice([True, False]),
            sharing_links_count=random.randint(0, 5)
        )
        all_docs.append(doc)
    
    # Filtra por user_id se especificado
    if user_id:
        all_docs = [d for d in all_docs if d.last_modified_by_user_id == user_id]
    
    # Pagina os resultados
    paginated_docs, total = paginate_items(all_docs, page, page_size)
    
    context_user_id = paginated_docs[0].last_modified_by_user_id if paginated_docs else "u001"
    
    return StandardResponse(
        request_id=generate_uuid(),
        service=SERVICES["sharepoint"],
        timestamp_utc=datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ"),
        correlation_id=correlation_id,
        data={"documents": [doc.model_dump() for doc in paginated_docs]},
        meta=create_response_meta(
            user_id=context_user_id,
            tenant_id="tenant-01",
            items_count=len(paginated_docs),
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
    Lista logs de auditoria do SharePoint.
    """
    correlation_id = x_correlation_id or generate_uuid()
    
    users = filter_users(tenant_id=tenant_id) if tenant_id else load_users_from_csv()
    
    actions = ["FileViewed", "FileDownloaded", "FileUploaded", "FileDeleted", 
               "PermissionChanged", "SiteAccessed", "SharingLinkCreated"]
    resource_types = ["Site", "Document"]
    
    all_logs = []
    for i in range(random.randint(50, 200)):
        user = random.choice(users)
        
        log = SharePointAuditLog(
            event_id=f"sp-evt-{i:06d}",
            timestamp_utc=generate_random_datetime(1, 7),
            user_id=user['user_id'],
            action=random.choice(actions),
            resource_type=random.choice(resource_types),
            resource_id=f"res-{random.randint(1000, 9999)}",
            ip_address=generate_random_ip(),
            device_id=generate_device_id(),
            success=random.choice([True, True, True, False]),
            reason=random.choice([None, None, None, "Permission denied"])
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
        service=SERVICES["sharepoint"],
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

