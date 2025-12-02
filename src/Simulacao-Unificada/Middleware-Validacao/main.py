from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import uvicorn

from src.api import auth as auth_routes
from src.api import monitoring as monitoring_routes
from src.api import validation_simple as validation_simple_routes
from src.api import workflows as workflow_routes
from src.api import test_support as test_support_routes

app = FastAPI(
    title="Middleware de Validação - Metrô SP",
    description="""
    Middleware responsável por:
    - Validação de autenticação e autorização (SSO simulado)
    - Controle de acesso por projeto
    - Validação de integridade de dados (checksum)
    - Rastreabilidade de ações
    - Guardrails para agentes de IA
    
    Integra-se com a API mockada para simular o ambiente real do Metrô.
    
    **Integrações:**
    - 🎨 Miro: Boards e planejamento
    - 📁 SharePoint: Documentos e sites
    - 🤖 Microsoft 365 Copilot: IA e assistência
    - 📧 Microsoft 365 Office: Documentos, emails e calendário
    - 🛡️ Microsoft Sentinel: Auditoria e segurança
    
    ---
    
    **🚀 Como usar:**
    
    Todos os endpoints de validação usam **autenticação simplificada** que simula SSO corporativo.
    Basta adicionar o header `X-User-Id` nas requisições!
    
    **👤 Usuários de teste:**
    - `u001` - Admin (acesso total)
    - `u010` - Manager (gerenciamento)
    - `u025` - Analyst (análise)
    - `u050` - Viewer (apenas leitura - vai gerar incidentes!)
    
    ---
    
    **📊 Recursos:**
    - **Dashboard em tempo real:** [/dashboard](/dashboard)
    - **Documentação interativa:** [/docs](/docs)
    - **Health check:** [/health](/health)
    
    **Em produção real:** Seria usado Microsoft Entra ID (Azure AD) com SSO automático.
    """,
    version="1.0.0"
)

# Registra rotas
app.include_router(auth_routes.router)
app.include_router(monitoring_routes.router)
app.include_router(validation_simple_routes.router)  # Validação simplificada (SSO simulado)
app.include_router(workflow_routes.router)
app.include_router(test_support_routes.router)  # Endpoints para testes unitários


@app.get("/", response_class=HTMLResponse)
async def root():
    """Página inicial com informações do middleware"""
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Middleware de Validação - Metrô SP</title>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <style>
            * {
                box-sizing: border-box;
                margin: 0;
                padding: 0;
            }
            body {
                font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
                background: #f5f7fa;
                min-height: 100vh;
                padding: 20px;
                color: #2c3e50;
            }
            .container {
                max-width: 1200px;
                margin: 0 auto;
            }
            .header {
                background: white;
                padding: 30px 40px;
                border-radius: 8px;
                box-shadow: 0 2px 4px rgba(0,0,0,0.1);
                margin-bottom: 24px;
                display: flex;
                align-items: center;
                gap: 20px;
            }
            .logo {
                width: 50px;
                height: 50px;
                background: #3b82f6;
                border-radius: 8px;
                display: flex;
                align-items: center;
                justify-content: center;
                font-size: 1.8em;
            }
            h1 {
                font-size: 1.8em;
                color: #1e293b;
                font-weight: 600;
            }
            .subtitle {
                font-size: 0.95em;
                color: #64748b;
                margin-top: 4px;
            }
            .status-grid {
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
                gap: 16px;
                margin-bottom: 24px;
            }
            .status-card {
                background: white;
                padding: 24px;
                border-radius: 8px;
                box-shadow: 0 2px 4px rgba(0,0,0,0.1);
                display: flex;
                align-items: center;
                gap: 16px;
            }
            .status-icon {
                font-size: 2em;
                width: 50px;
                height: 50px;
                display: flex;
                align-items: center;
                justify-content: center;
                background: #f1f5f9;
                border-radius: 8px;
            }
            .status-content h3 {
                font-size: 1em;
                margin-bottom: 4px;
                font-weight: 600;
                color: #1e293b;
            }
            .status-content p {
                color: #64748b;
                font-size: 0.875em;
            }
            .features {
                background: white;
                padding: 32px;
                border-radius: 8px;
                box-shadow: 0 2px 4px rgba(0,0,0,0.1);
                margin-bottom: 24px;
            }
            .features h2 {
                font-size: 1.5em;
                margin-bottom: 24px;
                font-weight: 600;
                color: #1e293b;
            }
            .feature-grid {
                display: grid;
                gap: 20px;
            }
            .feature {
                padding: 20px;
                border-radius: 6px;
                background: #f8fafc;
                border-left: 3px solid #3b82f6;
            }
            .feature h4 {
                font-size: 1.1em;
                margin-bottom: 8px;
                font-weight: 600;
                color: #1e293b;
            }
            .feature p {
                color: #64748b;
                line-height: 1.6;
                font-size: 0.95em;
            }
            .links {
                display: flex;
                gap: 12px;
                flex-wrap: wrap;
            }
            .link-button {
                background: #3b82f6;
                color: white;
                padding: 12px 24px;
                border-radius: 6px;
                text-decoration: none;
                font-weight: 500;
                font-size: 0.95em;
                transition: all 0.2s;
                display: inline-flex;
                align-items: center;
                gap: 8px;
            }
            .link-button:hover {
                background: #2563eb;
                transform: translateY(-1px);
                box-shadow: 0 4px 6px rgba(0,0,0,0.1);
            }
            .link-button.secondary {
                background: white;
                color: #3b82f6;
                border: 1px solid #e2e8f0;
            }
            .link-button.secondary:hover {
                background: #f8fafc;
                border-color: #cbd5e1;
            }
            .footer {
                text-align: center;
                margin-top: 32px;
                padding: 24px;
                background: white;
                border-radius: 8px;
                box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            }
            .footer p {
                color: #64748b;
                font-size: 0.875em;
            }
            .footer p:first-child {
                font-weight: 600;
                color: #1e293b;
                margin-bottom: 4px;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <div class="header">
                <div class="logo">🔒</div>
                <div>
                    <h1>Middleware de Validação</h1>
                    <p class="subtitle">Sistema de Gestão de Projetos - Metrô de São Paulo</p>
                </div>
            </div>
            
            <div class="status-grid">
                <div class="status-card">
                    <div class="status-icon">✓</div>
                    <div class="status-content">
                        <h3>Sistema Online</h3>
                        <p>Todos os serviços operacionais</p>
                    </div>
                </div>
                <div class="status-card">
                    <div class="status-icon">🔗</div>
                    <div class="status-content">
                        <h3>APIs Integradas</h3>
                        <p>Conectado a 5 serviços</p>
                    </div>
                </div>
                <div class="status-card">
                    <div class="status-icon">📊</div>
                    <div class="status-content">
                        <h3>Monitoramento Ativo</h3>
                        <p>Rastreabilidade completa</p>
                    </div>
                </div>
            </div>

            <div class="features">
                <h2>Requisitos Não Funcionais Implementados</h2>
                <div class="feature-grid">
                    <div class="feature">
                        <h4>🔐 RNF-01: Segurança</h4>
                        <p>Autenticação SSO simulada, controle de acesso granular por projeto e role, validação de integridade de dados com checksum, e guardrails para agentes de IA.</p>
                    </div>
                    <div class="feature">
                        <h4>📈 RNF-02: Escalabilidade</h4>
                        <p>Rate limiting para prevenir sobrecarga, circuit breaker para integrações resilientes, cache de permissões e monitoramento de performance em tempo real.</p>
                    </div>
                    <div class="feature">
                        <h4>🔍 RNF-03: Rastreabilidade</h4>
                        <p>Sistema de logs estruturado em JSONL, incident queue para eventos de segurança, auditoria completa com trace_id e correlation_id.</p>
                    </div>
                </div>
                
                <div style="margin-top: 24px;">
                    <div class="links">
                        <a href="/dashboard" class="link-button">
                            <span>📊</span>
                            <span>Dashboard</span>
                        </a>
                        <a href="/docs" class="link-button secondary">
                            <span>📚</span>
                            <span>Documentação</span>
                        </a>
                        <a href="/health" class="link-button secondary">
                            <span>💚</span>
                            <span>Health Check</span>
                        </a>
                    </div>
                </div>
            </div>

            <div class="footer">
                <p>Middleware de Validação v1.0.0</p>
                <p>Integrando Miro, SharePoint, Copilot, Office 365 e Sentinel</p>
            </div>
        </div>
    </body>
    </html>
    """


@app.get("/health")
async def health_check():
    """Endpoint de health check"""
    return {
        "status": "healthy",
        "service": "middleware-validacao",
        "version": "1.0.0",
        "components": {
            "authentication": "operational",
            "logging": "operational",
            "api_integration": "operational"
        }
    }


@app.get("/logs", response_class=HTMLResponse)
async def all_logs_page():
    """Página com todos os logs em formato de tabela"""
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Todos os Logs - Middleware de Validação</title>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
        <style>
            * { margin: 0; padding: 0; box-sizing: border-box; }
            body {
                font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
                background: #f8f9fa;
                color: #212529;
            }
            .header {
                background: #ffffff;
                border-bottom: 1px solid #e9ecef;
                padding: 16px 32px;
                display: flex;
                justify-content: space-between;
                align-items: center;
                box-shadow: 0 2px 8px rgba(0, 0, 0, 0.05);
            }
            .header-left { display: flex; align-items: center; gap: 15px; }
            .back-btn {
                background: #6c757d;
                color: white;
                border: none;
                padding: 8px 16px;
                border-radius: 6px;
                cursor: pointer;
                font-weight: 500;
                font-size: 0.875em;
                text-decoration: none;
                display: flex;
                align-items: center;
                gap: 6px;
            }
            .back-btn:hover { background: #5c636a; }
            .container { padding: 30px; max-width: 1800px; margin: 0 auto; }
            h1 { font-size: 1.5em; font-weight: 600; color: #212529; }
            .filters {
                background: white;
                padding: 20px;
                border-radius: 8px;
                margin-bottom: 20px;
                display: flex;
                gap: 10px;
                flex-wrap: wrap;
                border: 1px solid #dee2e6;
            }
            .filter-btn {
                background: white;
                border: 1px solid #dee2e6;
                color: #495057;
                padding: 8px 16px;
                border-radius: 6px;
                cursor: pointer;
                font-size: 0.875em;
                font-weight: 500;
                transition: all 0.2s;
            }
            .filter-btn:hover { background: #f8f9fa; border-color: #0d6efd; }
            .filter-btn.active { background: #0d6efd; border-color: #0d6efd; color: white; }
            .table-container {
                background: white;
                border-radius: 8px;
                border: 1px solid #dee2e6;
                overflow: hidden;
            }
            table {
                width: 100%;
                border-collapse: collapse;
            }
            thead {
                background: #f8f9fa;
                border-bottom: 2px solid #dee2e6;
            }
            th {
                padding: 12px 16px;
                text-align: left;
                font-size: 0.75em;
                font-weight: 600;
                text-transform: uppercase;
                letter-spacing: 0.5px;
                color: #495057;
            }
            td {
                padding: 12px 16px;
                border-bottom: 1px solid #f0f0f0;
                font-size: 0.875em;
            }
            tr:hover { background: #f8f9fa; }
            .badge {
                padding: 4px 10px;
                border-radius: 4px;
                font-size: 0.75em;
                font-weight: 600;
                text-transform: uppercase;
                letter-spacing: 0.3px;
            }
            .badge-success { background: #d1e7dd; color: #0f5132; }
            .badge-failed { background: #f8d7da; color: #842029; }
            .badge-denied { background: #fff3cd; color: #856404; }
            .badge-incident { background: #cfe2ff; color: #084298; }
            .loading {
                text-align: center;
                padding: 40px;
                color: #6c757d;
            }
            .pagination {
                display: flex;
                justify-content: center;
                align-items: center;
                gap: 10px;
                padding: 20px;
                background: white;
                border-radius: 8px;
                margin-top: 20px;
                border: 1px solid #dee2e6;
            }
            .page-btn {
                background: white;
                border: 1px solid #dee2e6;
                color: #495057;
                padding: 8px 12px;
                border-radius: 6px;
                cursor: pointer;
                font-size: 0.875em;
                font-weight: 500;
                min-width: 40px;
            }
            .page-btn:hover:not(:disabled) { background: #f8f9fa; }
            .page-btn.active { background: #0d6efd; border-color: #0d6efd; color: white; }
            .page-btn:disabled { opacity: 0.5; cursor: not-allowed; }
            .page-info { color: #6c757d; font-size: 0.875em; }
            tr { cursor: pointer; }
            .modal {
                display: none;
                position: fixed;
                top: 0;
                left: 0;
                right: 0;
                bottom: 0;
                background: rgba(0, 0, 0, 0.5);
                z-index: 1000;
                align-items: center;
                justify-content: center;
            }
            .modal.active { display: flex; }
            .modal-content {
                background: white;
                border-radius: 8px;
                width: 90%;
                max-width: 800px;
                max-height: 80vh;
                overflow-y: auto;
                box-shadow: 0 4px 20px rgba(0, 0, 0, 0.15);
            }
            .modal-header {
                padding: 20px 24px;
                border-bottom: 1px solid #dee2e6;
                display: flex;
                justify-content: space-between;
                align-items: center;
            }
            .modal-header h2 { font-size: 1.25em; font-weight: 600; }
            .close-btn {
                background: none;
                border: none;
                font-size: 1.5em;
                color: #6c757d;
                cursor: pointer;
                padding: 0;
                width: 32px;
                height: 32px;
                display: flex;
                align-items: center;
                justify-content: center;
                border-radius: 4px;
            }
            .close-btn:hover { background: #f8f9fa; }
            .modal-body { padding: 24px; }
            .detail-row {
                display: grid;
                grid-template-columns: 150px 1fr;
                gap: 12px;
                padding: 12px 0;
                border-bottom: 1px solid #f0f0f0;
            }
            .detail-row:last-child { border-bottom: none; }
            .detail-label {
                font-weight: 600;
                color: #495057;
                font-size: 0.875em;
            }
            .detail-value {
                color: #212529;
                font-size: 0.875em;
                word-break: break-word;
            }
            .json-viewer {
                background: #f8f9fa;
                padding: 12px;
                border-radius: 6px;
                font-family: 'Courier New', monospace;
                font-size: 0.8em;
                overflow-x: auto;
                white-space: pre-wrap;
                word-wrap: break-word;
            }
        </style>
    </head>
    <body>
        <div class="header">
            <div class="header-left">
                <a href="/dashboard" class="back-btn"><i class="fas fa-arrow-left"></i> Voltar ao Dashboard</a>
                <h1>Todos os Logs</h1>
            </div>
            <div id="total-count" style="color: #6c757d; font-size: 0.9em;"></div>
        </div>
        
        <div class="container">
            <div class="filters">
                <button class="filter-btn active" onclick="filterTable('all')">Todos</button>
                <button class="filter-btn" onclick="filterTable('success')">Sucesso</button>
                <button class="filter-btn" onclick="filterTable('failed')">Falha</button>
                <button class="filter-btn" onclick="filterTable('denied')">Negado</button>
                <button class="filter-btn" onclick="filterTable('incident')">Incidente</button>
            </div>
            
            <div class="table-container">
                <table>
                    <thead>
                        <tr>
                            <th>Timestamp</th>
                            <th>Status</th>
                            <th>Evento</th>
                            <th>Usuário</th>
                            <th>Projeto</th>
                            <th>Recurso</th>
                            <th>Trace ID</th>
                        </tr>
                    </thead>
                    <tbody id="logs-tbody">
                        <tr><td colspan="7" class="loading">Carregando logs...</td></tr>
                    </tbody>
                </table>
            </div>
            
            <div class="pagination">
                <button class="page-btn" onclick="changePage('first')" id="first-btn"><i class="fas fa-angle-double-left"></i></button>
                <button class="page-btn" onclick="changePage('prev')" id="prev-btn"><i class="fas fa-angle-left"></i></button>
                <span class="page-info" id="page-info">Página 1 de 1</span>
                <button class="page-btn" onclick="changePage('next')" id="next-btn"><i class="fas fa-angle-right"></i></button>
                <button class="page-btn" onclick="changePage('last')" id="last-btn"><i class="fas fa-angle-double-right"></i></button>
            </div>
        </div>
        
        <div class="modal" id="log-modal">
            <div class="modal-content">
                <div class="modal-header">
                    <h2>Detalhes do Log</h2>
                    <button class="close-btn" onclick="closeModal()"><i class="fas fa-times"></i></button>
                </div>
                <div class="modal-body" id="modal-body">
                </div>
            </div>
        </div>
        
        <script>
            let allLogs = [];
            let currentFilter = 'all';
            let currentPage = 1;
            const logsPerPage = 15;
            
            async function loadAllLogs() {
                try {
                    const response = await fetch('/monitoring/logs');
                    const data = await response.json();
                    allLogs = data.logs || [];
                    renderTable();
                } catch (error) {
                    console.error('Erro ao carregar logs:', error);
                    document.getElementById('logs-tbody').innerHTML = '<tr><td colspan="7" class="loading">Erro ao carregar logs</td></tr>';
                }
            }
            
            function filterTable(filter) {
                currentFilter = filter;
                currentPage = 1;
                document.querySelectorAll('.filter-btn').forEach((btn, idx) => {
                    btn.classList.remove('active');
                    if ((filter === 'all' && idx === 0) ||
                        (filter === 'success' && idx === 1) ||
                        (filter === 'failed' && idx === 2) ||
                        (filter === 'denied' && idx === 3) ||
                        (filter === 'incident' && idx === 4)) {
                        btn.classList.add('active');
                    }
                });
                renderTable();
            }
            
            function changePage(action) {
                const filteredLogs = currentFilter === 'all' ? allLogs : allLogs.filter(log => log.status === currentFilter);
                const totalPages = Math.ceil(filteredLogs.length / logsPerPage);
                
                if (action === 'first') currentPage = 1;
                if (action === 'prev' && currentPage > 1) currentPage--;
                if (action === 'next' && currentPage < totalPages) currentPage++;
                if (action === 'last') currentPage = totalPages;
                
                renderTable();
            }
            
            function renderTable() {
                let filteredLogs = allLogs;
                if (currentFilter !== 'all') {
                    filteredLogs = allLogs.filter(log => log.status === currentFilter);
                }
                
                const totalPages = Math.ceil(filteredLogs.length / logsPerPage);
                const startIdx = (currentPage - 1) * logsPerPage;
                const endIdx = startIdx + logsPerPage;
                const paginatedLogs = filteredLogs.slice(startIdx, endIdx);
                
                document.getElementById('total-count').textContent = `${filteredLogs.length} logs`;
                document.getElementById('page-info').textContent = `Página ${currentPage} de ${totalPages || 1}`;
                
                document.getElementById('first-btn').disabled = currentPage === 1;
                document.getElementById('prev-btn').disabled = currentPage === 1;
                document.getElementById('next-btn').disabled = currentPage === totalPages || totalPages === 0;
                document.getElementById('last-btn').disabled = currentPage === totalPages || totalPages === 0;
                
                if (paginatedLogs.length === 0) {
                    document.getElementById('logs-tbody').innerHTML = '<tr><td colspan="7" class="loading">Nenhum log encontrado</td></tr>';
                    return;
                }
                
                const tbody = document.getElementById('logs-tbody');
                tbody.innerHTML = paginatedLogs.map((log, idx) => {
                    let badgeClass = 'badge-success';
                    let statusLabel = log.status || 'unknown';
                    
                    if (log.status === 'success') { badgeClass = 'badge-success'; statusLabel = 'Sucesso'; }
                    if (log.status === 'failed') { badgeClass = 'badge-failed'; statusLabel = 'Falha'; }
                    if (log.status === 'denied') { badgeClass = 'badge-denied'; statusLabel = 'Negado'; }
                    if (log.status === 'incident') { badgeClass = 'badge-incident'; statusLabel = 'Incidente'; }
                    
                    return `
                        <tr onclick='showLogDetails(${JSON.stringify(log).replace(/'/g, "&apos;")})'>
                            <td>${new Date(log.timestamp).toLocaleString('pt-BR')}</td>
                            <td><span class="badge ${badgeClass}">${statusLabel}</span></td>
                            <td>${log.event_type || 'N/A'}</td>
                            <td>${log.user_id || 'N/A'}</td>
                            <td>${log.project_id || '-'}</td>
                            <td>${log.resource_id || '-'}</td>
                            <td style="font-family: monospace; font-size: 0.8em;">${log.trace_id ? log.trace_id.substring(0, 16) + '...' : '-'}</td>
                        </tr>
                    `;
                }).join('');
            }
            
            function showLogDetails(log) {
                let badgeClass = 'badge-success';
                let statusLabel = log.status || 'unknown';
                
                if (log.status === 'success') { badgeClass = 'badge-success'; statusLabel = 'Sucesso'; }
                if (log.status === 'failed') { badgeClass = 'badge-failed'; statusLabel = 'Falha'; }
                if (log.status === 'denied') { badgeClass = 'badge-denied'; statusLabel = 'Negado'; }
                if (log.status === 'incident') { badgeClass = 'badge-incident'; statusLabel = 'Incidente'; }
                
                const modalBody = document.getElementById('modal-body');
                modalBody.innerHTML = `
                    <div class="detail-row">
                        <div class="detail-label">Timestamp</div>
                        <div class="detail-value">${new Date(log.timestamp).toLocaleString('pt-BR')}</div>
                    </div>
                    <div class="detail-row">
                        <div class="detail-label">Status</div>
                        <div class="detail-value"><span class="badge ${badgeClass}">${statusLabel}</span></div>
                    </div>
                    <div class="detail-row">
                        <div class="detail-label">Tipo de Evento</div>
                        <div class="detail-value">${log.event_type || 'N/A'}</div>
                    </div>
                    <div class="detail-row">
                        <div class="detail-label">Usuário</div>
                        <div class="detail-value">${log.user_id || 'N/A'}</div>
                    </div>
                    <div class="detail-row">
                        <div class="detail-label">Projeto</div>
                        <div class="detail-value">${log.project_id || '-'}</div>
                    </div>
                    <div class="detail-row">
                        <div class="detail-label">Recurso</div>
                        <div class="detail-value">${log.resource_id || '-'}</div>
                    </div>
                    <div class="detail-row">
                        <div class="detail-label">Ação</div>
                        <div class="detail-value">${log.action || '-'}</div>
                    </div>
                    <div class="detail-row">
                        <div class="detail-label">IP de Origem</div>
                        <div class="detail-value">${log.source_ip || '-'}</div>
                    </div>
                    <div class="detail-row">
                        <div class="detail-label">Trace ID</div>
                        <div class="detail-value" style="font-family: monospace; font-size: 0.85em;">${log.trace_id || '-'}</div>
                    </div>
                    ${log.metadata ? `
                    <div class="detail-row">
                        <div class="detail-label">Metadata</div>
                        <div class="detail-value">
                            <div class="json-viewer">${syntaxHighlight(JSON.stringify(log.metadata, null, 2))}</div>
                        </div>
                    </div>
                    ` : ''}
                    ${log.details ? `
                    <div class="detail-row">
                        <div class="detail-label">Detalhes</div>
                        <div class="detail-value">
                            ${typeof log.details === 'object' ? `<div class="json-viewer">${syntaxHighlight(JSON.stringify(log.details, null, 2))}</div>` : log.details}
                        </div>
                    </div>
                    ` : ''}
                `;
                
                document.getElementById('log-modal').classList.add('active');
            }
            
            function closeModal() {
                document.getElementById('log-modal').classList.remove('active');
            }
            
            function syntaxHighlight(json) {
                return json.replace(/("(\\u[a-zA-Z0-9]{4}|\\[^u]|[^\\"])*"(\s*:)?|\b(true|false|null)\b|-?\d+(?:\.\d*)?(?:[eE][+\-]?\d+)?)/g, function (match) {
                    let cls = 'json-number';
                    if (/^"/.test(match)) {
                        if (/:$/.test(match)) {
                            cls = 'json-key';
                        } else {
                            cls = 'json-string';
                        }
                    } else if (/true|false/.test(match)) {
                        cls = 'json-boolean';
                    } else if (/null/.test(match)) {
                        cls = 'json-null';
                    }
                    return '<span class="' + cls + '">' + match + '</span>';
                });
            }
            
            document.getElementById('log-modal').addEventListener('click', function(e) {
                if (e.target === this) closeModal();
            });
            
            loadAllLogs();
        </script>
    </body>
    </html>
    """


@app.get("/dashboard", response_class=HTMLResponse)
async def dashboard():
    """Dashboard de monitoramento em tempo real"""
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Dashboard - Middleware de Validação</title>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
        <style>
            * {
                box-sizing: border-box;
                margin: 0;
                padding: 0;
            }
            body {
                font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
                background: #f8f9fa;
                color: #212529;
                min-height: 100vh;
                padding: 0;
                overflow-x: hidden;
                line-height: 1.6;
            }
            
            /* Header */
            .header {
                background: #ffffff;
                border-bottom: 1px solid #e9ecef;
                padding: 16px 32px;
                display: flex;
                justify-content: space-between;
                align-items: center;
                position: sticky;
                top: 0;
                z-index: 100;
                box-shadow: 0 2px 8px rgba(0, 0, 0, 0.05);
            }
            .header-left {
                display: flex;
                align-items: center;
                gap: 15px;
            }
            .logo {
                width: 36px;
                height: 36px;
                background: #0d6efd;
                border-radius: 6px;
                display: flex;
                align-items: center;
                justify-content: center;
                color: white;
                font-size: 1.2em;
            }
            h1 {
                font-size: 1.25em;
                font-weight: 600;
                color: #212529;
                margin: 0;
            }
            .header-subtitle {
                font-size: 0.75em;
                color: #6c757d;
                font-weight: 400;
                margin-top: 2px;
            }
            .header-right {
                display: flex;
                align-items: center;
                gap: 15px;
            }
            .refresh-info {
                color: rgba(0, 0, 0, 0.6);
                font-size: 0.85em;
                display: flex;
                align-items: center;
                gap: 8px;
            }
            .status-dot {
                width: 8px;
                height: 8px;
                background: #10b981;
                border-radius: 50%;
                animation: pulse 2s infinite;
            }
            @keyframes pulse {
                0%, 100% { opacity: 1; }
                50% { opacity: 0.5; }
            }
            .refresh-btn {
                background: #0d6efd;
                color: white;
                border: none;
                padding: 8px 16px;
                border-radius: 6px;
                cursor: pointer;
                font-weight: 500;
                font-size: 0.875em;
                transition: all 0.2s;
                display: flex;
                align-items: center;
                gap: 6px;
            }
            .refresh-btn:hover {
                background: #0b5ed7;
            }
            .refresh-btn:active {
                background: #0a58ca;
            }
            
            /* Container */
            .container {
                padding: 30px;
                max-width: 1600px;
                margin: 0 auto;
            }
            
            /* Dashboard Grid */
            .dashboard-grid {
                display: grid;
                gap: 24px;
            }
            
            /* Layout de 2 colunas */
            .two-column-layout {
                display: grid;
                grid-template-columns: 2fr 1fr;
                gap: 24px;
                margin-top: 24px;
            }
            
            @media (max-width: 1200px) {
                .two-column-layout {
                    grid-template-columns: 1fr;
                }
            }
            
            /* Cards */
            .card {
                background: #ffffff;
                border-radius: 8px;
                padding: 24px;
                border: 1px solid #dee2e6;
                box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
                transition: all 0.2s;
            }
            .card:hover {
                box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
            }
            .card-header {
                display: flex;
                justify-content: space-between;
                align-items: center;
                margin-bottom: 20px;
            }
            .card-title {
                font-size: 0.95em;
                font-weight: 600;
                color: #495057;
                text-transform: uppercase;
                letter-spacing: 0.5px;
                display: flex;
                align-items: center;
                gap: 8px;
            }
            .card-icon {
                font-size: 1em;
                color: #0d6efd;
            }
            
            /* Stats Grid */
            .stats-grid {
                display: grid;
                grid-template-columns: repeat(4, 1fr);
                gap: 16px;
                margin-bottom: 24px;
            }
            
            @media (max-width: 768px) {
                .stats-grid {
                    grid-template-columns: repeat(2, 1fr);
                }
            }
            .stat-card {
                background: white;
                border-radius: 8px;
                padding: 16px;
                border: 1px solid #dee2e6;
                text-align: center;
                transition: all 0.2s;
                position: relative;
                overflow: hidden;
                box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
            }
            .stat-card::before {
                content: '';
                position: absolute;
                top: 0;
                left: 0;
                right: 0;
                height: 3px;
                background: #0d6efd;
            }
            .stat-card:hover {
                box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
            }
            .stat-icon {
                font-size: 1.2em;
                margin-bottom: 6px;
                color: #0d6efd;
            }
            .stat-value {
                font-size: 1.75em;
                font-weight: 600;
                margin: 6px 0;
                color: #212529;
            }
            .stat-label {
                color: #6c757d;
                font-size: 0.75em;
                text-transform: uppercase;
                letter-spacing: 0.5px;
                font-weight: 500;
            }
            .stat-change {
                margin-top: 8px;
                font-size: 0.85em;
                padding: 4px 12px;
                border-radius: 20px;
                display: inline-block;
            }
            .stat-change.positive {
                background: rgba(0, 255, 136, 0.2);
                color: #00ff88;
            }
            .stat-change.negative {
                background: rgba(255, 68, 68, 0.2);
                color: #ff4444;
            }
            
            /* Integrations */
            .integrations-section {
                grid-column: span 12;
            }
            .integration-grid {
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
                gap: 16px;
            }
            .integration-card {
                background: white;
                padding: 16px;
                border-radius: 8px;
                text-align: center;
                border: 1px solid #dee2e6;
                transition: all 0.2s;
                cursor: pointer;
            }
            .integration-card.healthy {
                border-left: 3px solid #198754;
            }
            .integration-card.unhealthy {
                border-left: 3px solid #dc3545;
            }
            .integration-card:hover {
                box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
            }
            .integration-icon {
                font-size: 1.5em;
                margin-bottom: 8px;
                color: #495057;
            }
            .integration-name {
                font-weight: 600;
                margin-bottom: 6px;
                font-size: 0.9em;
                color: #212529;
            }
            .integration-status {
                font-size: 0.75em;
                padding: 4px 8px;
                border-radius: 4px;
                display: inline-block;
                font-weight: 500;
                text-transform: uppercase;
                letter-spacing: 0.3px;
            }
            .status-healthy {
                background: #d1e7dd;
                color: #0f5132;
            }
            .status-unhealthy {
                background: #f8d7da;
                color: #842029;
            }
            
            /* Logs */
            .logs-section {
                height: 100%;
            }
            .log-controls {
                display: flex;
                gap: 10px;
                margin-bottom: 16px;
                flex-wrap: wrap;
            }
            .filter-btn {
                background: white;
                border: 1px solid #dee2e6;
                color: #495057;
                padding: 6px 12px;
                border-radius: 4px;
                cursor: pointer;
                font-size: 0.8em;
                transition: all 0.2s;
                font-weight: 500;
            }
            .filter-btn:hover {
                background: #f8f9fa;
                border-color: #0d6efd;
            }
            .filter-btn.active {
                background: #0d6efd;
                border-color: #0d6efd;
                color: white;
            }
            .log-container {
                max-height: 600px;
                overflow-y: auto;
                padding: 4px;
            }
            .log-entry {
                background: white;
                padding: 16px;
                margin: 8px 0;
                border-radius: 8px;
                border-left: 4px solid #0d6efd;
                transition: all 0.2s;
                cursor: pointer;
                box-shadow: 0 1px 3px rgba(0, 0, 0, 0.08);
                border: 1px solid #e9ecef;
                border-left: 4px solid #0d6efd;
                display: grid;
                grid-template-columns: auto 1fr auto;
                gap: 16px;
                align-items: center;
            }
            .log-entry:hover {
                background: #f8f9fa;
                box-shadow: 0 4px 12px rgba(0, 0, 0, 0.12);
                transform: translateY(-1px);
            }
            .log-entry.incident {
                border-left-color: #0dcaf0;
                background: #f8fcff;
            }
            .log-entry.success {
                border-left-color: #198754;
            }
            .log-entry.warning {
                border-left-color: #ffc107;
            }
            .log-entry.failed {
                border-left-color: #dc3545;
            }
            .log-left {
                display: flex;
                flex-direction: column;
                gap: 4px;
                min-width: 140px;
            }
            .log-center {
                flex: 1;
                display: flex;
                flex-direction: column;
                gap: 6px;
            }
            .log-right {
                display: flex;
                align-items: center;
                gap: 12px;
            }
            .log-timestamp {
                color: #6c757d;
                font-size: 0.8em;
                font-family: 'Courier New', monospace;
                font-weight: 500;
            }
            .log-status-indicator {
                width: 8px;
                height: 8px;
                border-radius: 50%;
                display: inline-block;
            }
            .log-status-indicator.success { background: #198754; }
            .log-status-indicator.failed { background: #dc3545; }
            .log-status-indicator.denied { background: #ffc107; }
            .log-status-indicator.incident { background: #0dcaf0; }
            .log-badge {
                padding: 6px 12px;
                border-radius: 6px;
                font-size: 0.7em;
                font-weight: 600;
                text-transform: uppercase;
                letter-spacing: 0.5px;
                white-space: nowrap;
            }
            .badge-success {
                background: #d1e7dd;
                color: #0f5132;
                border: 1px solid #a3cfbb;
            }
            .badge-failed {
                background: #f8d7da;
                color: #842029;
                border: 1px solid #f1aeb5;
            }
            .badge-denied {
                background: #fff3cd;
                color: #856404;
                border: 1px solid #ffe69c;
            }
            .badge-incident {
                background: #cfe2ff;
                color: #084298;
                border: 1px solid #9ec5fe;
            }
            .log-event {
                font-weight: 600;
                font-size: 0.95em;
                color: #212529;
                display: flex;
                align-items: center;
                gap: 8px;
            }
            .log-user {
                color: #6c757d;
                font-size: 0.85em;
                display: flex;
                align-items: center;
                gap: 6px;
            }
            .log-meta {
                display: flex;
                gap: 12px;
                flex-wrap: wrap;
                margin-top: 4px;
            }
            .log-meta-item {
                color: #6c757d;
                font-size: 0.75em;
                display: flex;
                align-items: center;
                gap: 4px;
                background: #f8f9fa;
                padding: 2px 8px;
                border-radius: 4px;
            }
            .log-meta-item i {
                font-size: 0.9em;
                opacity: 0.7;
            }
            
            /* Loading */
            .loading {
                text-align: center;
                padding: 40px;
                color: rgba(0, 0, 0, 0.5);
            }
            .spinner {
                border: 3px solid rgba(0, 0, 0, 0.1);
                border-radius: 50%;
                border-top: 3px solid #667eea;
                width: 40px;
                height: 40px;
                animation: spin 1s linear infinite;
                margin: 0 auto 16px;
            }
            @keyframes spin {
                0% { transform: rotate(0deg); }
                100% { transform: rotate(360deg); }
            }
            
            /* No Data */
            .no-data {
                text-align: center;
                padding: 60px 20px;
                color: rgba(0, 0, 0, 0.4);
            }
            .no-data-icon {
                font-size: 4em;
                margin-bottom: 16px;
                opacity: 0.3;
            }
            
            /* Modal */
            .modal {
                display: none;
                position: fixed;
                top: 0;
                left: 0;
                right: 0;
                bottom: 0;
                background: rgba(0, 0, 0, 0.5);
                z-index: 1000;
                padding: 20px;
                overflow-y: auto;
                animation: fadeIn 0.3s ease-out;
            }
            @keyframes fadeIn {
                from { opacity: 0; }
                to { opacity: 1; }
            }
            .modal.active {
                display: flex;
                align-items: center;
                justify-content: center;
            }
            .modal-content {
                background: white;
                border-radius: 8px;
                max-width: 800px;
                width: 100%;
                max-height: 90vh;
                overflow-y: auto;
                box-shadow: 0 10px 40px rgba(0, 0, 0, 0.2);
                animation: slideUp 0.3s ease-out;
            }
            @keyframes slideUp {
                from {
                    opacity: 0;
                    transform: translateY(30px);
                }
                to {
                    opacity: 1;
                    transform: translateY(0);
                }
            }
            .modal-header {
                padding: 24px;
                border-bottom: 1px solid rgba(0, 0, 0, 0.1);
                display: flex;
                justify-content: space-between;
                align-items: center;
            }
            .modal-title {
                font-size: 1.5em;
                font-weight: 600;
                color: #1f2937;
            }
            .modal-close {
                background: none;
                border: none;
                font-size: 1.3em;
                cursor: pointer;
                color: #6c757d;
                width: 32px;
                height: 32px;
                display: flex;
                align-items: center;
                justify-content: center;
                border-radius: 4px;
                transition: all 0.2s;
            }
            .modal-close:hover {
                background: #e9ecef;
                color: #212529;
            }
            .modal-body {
                padding: 24px;
            }
            .detail-section {
                margin-bottom: 24px;
            }
            .detail-section:last-child {
                margin-bottom: 0;
            }
            .detail-label {
                font-size: 0.75em;
                text-transform: uppercase;
                letter-spacing: 1px;
                color: #6b7280;
                font-weight: 600;
                margin-bottom: 8px;
            }
            .detail-value {
                font-size: 1em;
                color: #1f2937;
                padding: 12px;
                background: #f9fafb;
                border-radius: 8px;
                font-family: 'Courier New', monospace;
                word-break: break-all;
            }
            .detail-value.large {
                font-size: 1.1em;
                font-weight: 600;
                background: #e7f1ff;
                color: #0d6efd;
            }
            .detail-grid {
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
                gap: 16px;
            }
            .json-viewer {
                background: #f8f9fa;
                border: 1px solid #dee2e6;
                padding: 20px;
                border-radius: 8px;
                font-family: 'Consolas', 'Monaco', 'Courier New', monospace;
                font-size: 0.875em;
                overflow-x: auto;
                max-height: 500px;
                line-height: 1.6;
                color: #212529;
            }
            .json-key {
                color: #0550ae;
                font-weight: 600;
            }
            .json-string {
                color: #0a3069;
            }
            .json-number {
                color: #0969da;
            }
            .json-boolean {
                color: #8250df;
                font-weight: 600;
            }
            .json-null {
                color: #6e7781;
                font-style: italic;
            }
            
            /* Scrollbar */
            ::-webkit-scrollbar {
                width: 10px;
                height: 10px;
            }
            ::-webkit-scrollbar-track {
                background: #f3f4f6;
                border-radius: 10px;
            }
            ::-webkit-scrollbar-thumb {
                background: #adb5bd;
                border-radius: 10px;
            }
            ::-webkit-scrollbar-thumb:hover {
                background: #6c757d;
            }
            
            /* Responsive */
            @media (max-width: 768px) {
                .header {
                    flex-direction: column;
                    gap: 15px;
                }
                .stats-grid {
                    grid-template-columns: 1fr;
                }
                .charts-row {
                    grid-template-columns: 1fr;
                }
            }
            
        </style>
    </head>
    <body>
        <!-- Header -->
        <div class="header">
            <div class="header-left">
                <div class="logo"><i class="fas fa-shield-alt"></i></div>
                <div>
                    <h1>Middleware de Validação</h1>
                    <div style="font-size: 0.8em; color: rgba(255,255,255,0.6); margin-top: 2px;">
                        Metrô de São Paulo - Sistema de Gestão de Projetos
                    </div>
                </div>
            </div>
            <div class="header-right">
                <div class="refresh-info">
                    <div class="status-dot"></div>
                    <span id="last-update">Carregando...</span>
                </div>
                <button class="refresh-btn" onclick="loadAllData()">
                    <span><i class="fas fa-sync-alt"></i></span>
                    <span>Atualizar</span>
                </button>
            </div>
        </div>

        <!-- Container -->
        <div class="container">
            <div class="dashboard-grid">
                
                <!-- Estatísticas Principais -->
                <div class="stats-grid">
                    <div class="stat-card">
                        <div class="stat-icon"><i class="fas fa-chart-line"></i></div>
                        <div class="stat-value" id="stat-total-logs">0</div>
                        <div class="stat-label">Total de Logs</div>
                        <div class="stat-change positive" id="stat-logs-change" style="display:none;">+12% hoje</div>
                    </div>
                    <div class="stat-card">
                        <div class="stat-icon"><i class="fas fa-exclamation-triangle"></i></div>
                        <div class="stat-value" id="stat-total-incidents">0</div>
                        <div class="stat-label">Incidentes</div>
                        <div class="stat-change negative" id="stat-incidents-change" style="display:none;">+3 hoje</div>
                    </div>
                    <div class="stat-card">
                        <div class="stat-icon"><i class="fas fa-users"></i></div>
                        <div class="stat-value" id="stat-unique-users">0</div>
                        <div class="stat-label">Usuários Ativos</div>
                    </div>
                    <div class="stat-card">
                        <div class="stat-icon"><i class="fas fa-chart-bar"></i></div>
                        <div class="stat-value" id="stat-error-rate">0%</div>
                        <div class="stat-label">Taxa de Erro</div>
                    </div>
                </div>

                <!-- Integrações -->
                <div class="card">
                    <div class="card-header">
                        <div class="card-title">
                            <span class="card-icon"><i class="fas fa-plug"></i></span>
                            <span>STATUS DAS INTEGRAÇÕES</span>
                        </div>
                    </div>
                    <div id="integrations-container" class="integration-grid">
                        <div class="loading">
                            <div class="spinner"></div>
                            <div>Carregando integrações...</div>
                        </div>
                    </div>
                </div>

                <!-- Testes Automatizados de Segurança -->
                <div id="compliance-dashboard-card" class="card">
                    <div class="card-header">
                        <div class="card-title">
                            <span class="card-icon"><i class="fas fa-check-circle"></i></span>
                            <span>TESTES AUTOMATIZADOS DE SEGURANÇA</span>
                        </div>
                        <button class="refresh-btn" onclick="if(typeof loadComplianceResults === 'function') loadComplianceResults();" style="padding: 6px 12px; font-size: 0.85em;">
                            <i class="fas fa-sync-alt"></i> Atualizar
                        </button>
                    </div>
                    <div id="compliance-container" style="
                        min-height: 300px; 
                        padding: 24px;
                    ">
                        <div style="
                            padding: 30px; 
                            text-align: center; 
                            background: linear-gradient(135deg, #e7f3ff 0%, #cfe2ff 100%); 
                            border: 3px solid #0d6efd; 
                            border-radius: 12px; 
                            margin-bottom: 20px;
                            box-shadow: 0 2px 8px rgba(13, 110, 253, 0.2);
                        ">
                            <div style="font-size: 3em; margin-bottom: 16px;">📊</div>
                            <div style="font-size: 1.4em; font-weight: 700; color: #084298; margin-bottom: 12px;">Dashboard de Testes Automatizados</div>
                            <div style="color: #084298; margin-bottom: 20px; font-size: 1.05em;">Carregando resultados de conformidade...</div>
                            <div style="background: white; padding: 16px; border-radius: 8px; color: #495057; font-size: 1em; max-width: 600px; margin: 0 auto; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">
                                <strong>Esta seção exibe:</strong><br/>
                                • Resultados dos testes automatizados de segurança (RNF-02)<br/>
                                • Resultados dos testes de rastreabilidade (RNF-03)<br/>
                                • Taxa de conformidade e estatísticas detalhadas
                            </div>
                        </div>
                        <div class="loading" id="compliance-loading" style="display: none; text-align: center; padding: 20px;">
                            <div class="spinner"></div>
                            <div>Carregando resultados de conformidade...</div>
                        </div>
                    </div>
                </div>
            </div>
            
            <!-- Layout de 2 Colunas: Incidentes (maior, esquerda) + Logs (menor, direita) -->
            <div class="two-column-layout">
                    <!-- Incidentes (Esquerda - Maior com Destaque) -->
                    <div class="card logs-section">
                        <div class="card-header">
                            <div class="card-title">
                                <span class="card-icon"><i class="fas fa-bell"></i></span>
                                <span>INCIDENT QUEUE</span>
                            </div>
                        </div>
                        <div class="log-controls" id="incident-filters">
                            <button class="filter-btn active" onclick="filterIncidents('all')">Todos</button>
                            <button class="filter-btn" onclick="filterIncidents('critical')">Crítico</button>
                            <button class="filter-btn" onclick="filterIncidents('high')">Alto</button>
                            <button class="filter-btn" onclick="filterIncidents('medium')">Médio</button>
                            <button class="filter-btn" onclick="filterIncidents('low')">Baixo</button>
                        </div>
                        <div id="incidents-container" class="log-container">
                            <div class="loading">
                                <div class="spinner"></div>
                                <div>Carregando incidentes...</div>
                            </div>
                        </div>
                    </div>

                    <!-- Logs Recentes (Direita - Menor) -->
                    <div class="card logs-section">
                        <div class="card-header">
                            <div class="card-title">
                                <span class="card-icon"><i class="fas fa-clipboard-list"></i></span>
                                <span>LOGS RECENTES</span>
                            </div>
                            <a href="/logs" style="background: #0d6efd; color: white; padding: 6px 12px; border-radius: 6px; text-decoration: none; font-size: 0.85em; font-weight: 500; display: flex; align-items: center; gap: 6px; transition: all 0.2s;" onmouseover="this.style.background='#0b5ed7'" onmouseout="this.style.background='#0d6efd'">
                                <i class="fas fa-external-link-alt"></i> Ver Todos
                            </a>
                        </div>
                        <div class="log-controls" id="log-filters">
                            <button class="filter-btn active" onclick="filterLogs('all')">Todos</button>
                            <button class="filter-btn" onclick="filterLogs('success')">Sucesso</button>
                            <button class="filter-btn" onclick="filterLogs('failed')">Falha</button>
                            <button class="filter-btn" onclick="filterLogs('denied')">Negado</button>
                            <button class="filter-btn" onclick="filterLogs('incident')">Incidente</button>
                        </div>
                        <div id="logs-container" class="log-container">
                            <div class="loading">
                                <div class="spinner"></div>
                                <div>Carregando logs...</div>
                            </div>
                        </div>
                    </div>
                </div>

            </div>
        </div>

        <!-- Modal de Detalhes do Log -->
        <div id="logModal" class="modal">
            <div class="modal-content">
                <div class="modal-header">
                    <div class="modal-title"><i class="fas fa-info-circle"></i> Detalhes do Log</div>
                    <button class="modal-close" onclick="closeModal()">×</button>
                </div>
                <div class="modal-body" id="modalBody">
                    <!-- Conteúdo será inserido dinamicamente -->
                </div>
            </div>
        </div>

        <script>
            // ========== CONFIGURAÇÕES ==========
            const integrationIcons = {
                miro: '<i class="fas fa-palette"></i>',
                sharepoint: '<i class="fas fa-folder"></i>',
                copilot: '<i class="fas fa-robot"></i>',
                office: '<i class="fas fa-envelope"></i>',
                sentinel: '<i class="fas fa-shield-alt"></i>'
            };
            
            let currentLogFilter = 'all';
            let currentIncidentFilter = 'all';
            let allLogs = [];
            let allIncidents = [];
            let allLogsWithIndex = []; // Para armazenar referência aos logs
            let allIncidentsWithIndex = []; // Para armazenar referência aos incidentes

            // ========== FUNÇÕES AUXILIARES ==========
            function syntaxHighlight(json) {
                if (typeof json !== 'string') {
                    json = JSON.stringify(json, null, 2);
                }
                
                json = json.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
                
                return json.replace(/("(\\u[a-zA-Z0-9]{4}|\\[^u]|[^\\"])*"(\s*:)?|\b(true|false|null)\b|-?\d+(?:\.\d*)?(?:[eE][+\-]?\d+)?)/g, function (match) {
                    let cls = 'json-number';
                    if (/^"/.test(match)) {
                        if (/:$/.test(match)) {
                            cls = 'json-key';
                        } else {
                            cls = 'json-string';
                        }
                    } else if (/true|false/.test(match)) {
                        cls = 'json-boolean';
                    } else if (/null/.test(match)) {
                        cls = 'json-null';
                    }
                    return '<span class="' + cls + '">' + match + '</span>';
                });
            }

            // ========== MODAL ==========
            function openModal(index, isIncident = false) {
                const logData = isIncident ? allIncidentsWithIndex[index] : allLogsWithIndex[index];
                if (!logData) {
                    console.error('Log não encontrado:', index);
                    return;
                }
                
                const modal = document.getElementById('logModal');
                const modalBody = document.getElementById('modalBody');
                
                // Determina status e cores
                let statusBadge = '';
                let statusColor = '#667eea';
                
                if (isIncident) {
                    const severity = logData.details?.severity || 'medium';
                    let severityIcon = '<i class="fas fa-circle" style="color: #ffc107;"></i>';
                    let severityColor = '#ffc107';
                    
                    if (severity === 'critical') { severityIcon = '<i class="fas fa-circle" style="color: #dc3545;"></i>'; severityColor = '#dc3545'; }
                    if (severity === 'high') { severityIcon = '<i class="fas fa-circle" style="color: #fd7e14;"></i>'; severityColor = '#fd7e14'; }
                    if (severity === 'low') { severityIcon = '<i class="fas fa-circle" style="color: #198754;"></i>'; severityColor = '#198754'; }
                    
                    statusBadge = `<span style="background: ${severityColor}20; color: ${severityColor}; padding: 6px 12px; border-radius: 20px; font-size: 0.9em; font-weight: 600;">${severityIcon} ${severity.toUpperCase()}</span>`;
                } else {
                    const status = logData.status || 'unknown';
                    if (status === 'success') { statusColor = '#10b981'; }
                    if (status === 'failed') { statusColor = '#ef4444'; }
                    if (status === 'denied') { statusColor = '#f59e0b'; }
                    
                    statusBadge = `<span style="background: ${statusColor}20; color: ${statusColor}; padding: 6px 12px; border-radius: 20px; font-size: 0.9em; font-weight: 600;">${status.toUpperCase()}</span>`;
                }
                
                // Monta o conteúdo do modal
                modalBody.innerHTML = `
                    <div class="detail-section">
                        <div class="detail-label">Status</div>
                        <div>${statusBadge}</div>
                    </div>
                    
                    <div class="detail-section">
                        <div class="detail-label">Tipo de Evento</div>
                        <div class="detail-value large">${logData.event_type || 'N/A'}</div>
                    </div>
                    
                    <div class="detail-grid">
                        <div class="detail-section">
                            <div class="detail-label">Timestamp</div>
                            <div class="detail-value">${logData.timestamp ? new Date(logData.timestamp).toLocaleString('pt-BR') : 'N/A'}</div>
                        </div>
                        <div class="detail-section">
                            <div class="detail-label">Usuário</div>
                            <div class="detail-value"><i class="fas fa-user"></i> ${logData.user_id || 'N/A'}</div>
                        </div>
                    </div>
                    
                    ${logData.project_id ? `
                    <div class="detail-section">
                        <div class="detail-label">Projeto</div>
                        <div class="detail-value"><i class="fas fa-folder"></i> ${logData.project_id}</div>
                    </div>
                    ` : ''}
                    
                    ${logData.resource_type ? `
                    <div class="detail-grid">
                        <div class="detail-section">
                            <div class="detail-label">Tipo de Recurso</div>
                            <div class="detail-value">${logData.resource_type}</div>
                        </div>
                        <div class="detail-section">
                            <div class="detail-label">ID do Recurso</div>
                            <div class="detail-value">${logData.resource_id || 'N/A'}</div>
                        </div>
                    </div>
                    ` : ''}
                    
                    ${logData.action ? `
                    <div class="detail-section">
                        <div class="detail-label">Ação</div>
                        <div class="detail-value">${logData.action}</div>
                    </div>
                    ` : ''}
                    
                    ${logData.reason || logData.details?.reason ? `
                    <div class="detail-section">
                        <div class="detail-label">Motivo / Descrição</div>
                        <div class="detail-value">${logData.reason || logData.details?.reason}</div>
                    </div>
                    ` : ''}
                    
                    <div class="detail-grid">
                        ${logData.trace_id ? `
                        <div class="detail-section">
                            <div class="detail-label">Trace ID</div>
                            <div class="detail-value" style="font-size: 0.8em;"><i class="fas fa-fingerprint"></i> ${logData.trace_id}</div>
                        </div>
                        ` : ''}
                        
                        ${logData.correlation_id ? `
                        <div class="detail-section">
                            <div class="detail-label">Correlation ID</div>
                            <div class="detail-value" style="font-size: 0.8em;"><i class="fas fa-link"></i> ${logData.correlation_id}</div>
                        </div>
                        ` : ''}
                    </div>
                    
                    ${logData.ip_address ? `
                    <div class="detail-section">
                        <div class="detail-label">Endereço IP</div>
                        <div class="detail-value"><i class="fas fa-globe"></i> ${logData.ip_address}</div>
                    </div>
                    ` : ''}
                    
                    <div class="detail-section">
                        <div class="detail-label"><i class="fas fa-code"></i> Dados Completos (JSON)</div>
                        <div class="json-viewer"><pre style="margin: 0; white-space: pre-wrap; word-wrap: break-word;">${syntaxHighlight(logData)}</pre></div>
                    </div>
                `;
                
                modal.classList.add('active');
            }
            
            function closeModal() {
                const modal = document.getElementById('logModal');
                modal.classList.remove('active');
            }
            
            // Fechar modal ao clicar fora
            document.addEventListener('click', (e) => {
                const modal = document.getElementById('logModal');
                if (e.target === modal) {
                    closeModal();
                }
            });
            
            // Fechar modal com ESC
            document.addEventListener('keydown', (e) => {
                if (e.key === 'Escape') {
                    closeModal();
                }
            });

            // ========== TIMESTAMP ==========
            function updateTimestamp() {
                const now = new Date();
                document.getElementById('last-update').textContent = 
                    now.toLocaleTimeString('pt-BR', { hour: '2-digit', minute: '2-digit', second: '2-digit' });
            }

            // ========== INTEGRAÇÕES ==========
            async function loadIntegrations() {
                try {
                    const response = await fetch('/workflows/integration/health');
                    if (!response.ok) {
                        throw new Error(`HTTP ${response.status}: ${response.statusText}`);
                    }
                    const data = await response.json();
                    
                    const container = document.getElementById('integrations-container');
                    if (!container) {
                        console.error('Container integrations-container não encontrado');
                        return;
                    }
                    container.innerHTML = '';

                    for (const [name, status] of Object.entries(data.integrations || {})) {
                        const isHealthy = status === 'healthy';
                        const card = document.createElement('div');
                        card.className = `integration-card ${isHealthy ? 'healthy' : 'unhealthy'}`;
                        card.innerHTML = `
                            <div class="integration-icon">${integrationIcons[name] || '🔌'}</div>
                            <div class="integration-name">${name.toUpperCase()}</div>
                            <div class="integration-status ${isHealthy ? 'status-healthy' : 'status-unhealthy'}">
                                ${isHealthy ? '✓ Online' : '✗ Offline'}
                            </div>
                        `;
                        container.appendChild(card);
                    }
                } catch (error) {
                    console.error('Erro ao carregar integrações:', error);
                    const container = document.getElementById('integrations-container');
                    if (container) {
                        container.innerHTML = 
                            '<div class="no-data"><div class="no-data-icon"><i class="fas fa-exclamation-triangle"></i></div>Erro ao carregar integrações: ' + error.message + '</div>';
                    }
                }
            }

            // ========== ESTATÍSTICAS ==========
            async function loadStats() {
                try {
                    const response = await fetch('/monitoring/stats');
                    if (!response.ok) {
                        throw new Error(`HTTP ${response.status}: ${response.statusText}`);
                    }
                    const data = await response.json();
                    
                    const summary = data.summary || {};
                    const topUsers = data.top_users || [];
                    
                    // Busca resultados de testes automatizados para incluir nas estatísticas
                    let testLogsCount = 0;
                    let testFailedCount = 0;
                    try {
                        const complianceResponse = await fetch('/monitoring/compliance-results');
                        const complianceData = await complianceResponse.json();
                        if (complianceData.available && complianceData.results) {
                            testLogsCount = complianceData.results.length;
                            testFailedCount = complianceData.results.filter(r => r.status === 'FAILED').length;
                        }
                    } catch (complianceError) {
                        // Ignora erro se compliance-results não estiver disponível
                    }
                    
                    // Atualiza cards de estatísticas
                    const totalLogsEl = document.getElementById('stat-total-logs');
                    const totalIncidentsEl = document.getElementById('stat-total-incidents');
                    const uniqueUsersEl = document.getElementById('stat-unique-users');
                    const errorRateEl = document.getElementById('stat-error-rate');
                    
                    // Total de logs inclui logs de auditoria + logs de testes
                    const totalLogs = (summary.total_logs || 0) + testLogsCount;
                    if (totalLogsEl) totalLogsEl.textContent = totalLogs;
                    
                    // Incidentes permanece o mesmo (não inclui testes)
                    if (totalIncidentsEl) totalIncidentsEl.textContent = summary.total_incidents || 0;
                    
                    // Usuários ativos permanece o mesmo
                    if (uniqueUsersEl) uniqueUsersEl.textContent = topUsers.length || 0;
                    
                    // Taxa de erro inclui falhas de testes
                    const statusCounts = data.status_counts || {};
                    const auditFailed = (statusCounts.failed || 0) + (statusCounts.denied || 0);
                    const totalFailed = auditFailed + testFailedCount;
                    const totalForErrorRate = totalLogs;
                    const errorRate = totalForErrorRate > 0 ? (totalFailed / totalForErrorRate * 100) : 0;
                    if (errorRateEl) errorRateEl.textContent = errorRate.toFixed(1) + '%';
                    
                } catch (error) {
                    console.error('Erro ao carregar estatísticas:', error);
                }
            }

            // ========== LOGS ==========
            async function loadLogs() {
                try {
                    const response = await fetch('/monitoring/logs?limit=50');
                    const data = await response.json();
                    let auditLogs = data.logs || [];
                    
                    // Busca resultados de testes automatizados e converte para formato de log
                    try {
                        const complianceResponse = await fetch('/monitoring/compliance-results');
                        const complianceData = await complianceResponse.json();
                        
                        if (complianceData.available && complianceData.results) {
                            const testLogs = complianceData.results.map(test => ({
                                timestamp: test.timestamp_utc || new Date().toISOString(),
                                event_type: `test.${test.test_scenario?.toLowerCase().replace(/\s+/g, '_') || 'compliance'}`,
                                user_id: 'system',
                                resource_type: 'test',
                                resource_id: test.service_tested || 'unknown',
                                action: test.endpoint_tested || 'N/A',
                                status: test.status === 'PASSED' ? 'success' : 'failed',
                                details: {
                                    test_scenario: test.test_scenario,
                                    service: test.service_tested,
                                    endpoint: test.endpoint_tested,
                                    severity: test.severity,
                                    execution_time_ms: test.execution_time_ms,
                                    details: test.details
                                },
                                trace_id: null,
                                correlation_id: null
                            }));
                            
                            // Mescla logs de auditoria com logs de testes
                            auditLogs = [...auditLogs, ...testLogs];
                        }
                    } catch (complianceError) {
                        // Ignora erro se compliance-results não estiver disponível
                    }
                    
                    // Ordena por timestamp (mais recente primeiro)
                    auditLogs.sort((a, b) => new Date(b.timestamp) - new Date(a.timestamp));
                    
                    allLogs = auditLogs;
                    allLogsWithIndex = [...allLogs];
                    renderLogs();
                } catch (error) {
                    console.error('Erro ao carregar logs:', error);
                    document.getElementById('logs-container').innerHTML = 
                        '<div class="no-data"><div class="no-data-icon"><i class="fas fa-exclamation-triangle"></i></div>Erro ao carregar logs</div>';
                }
            }
            
            function filterLogs(filter) {
                currentLogFilter = filter;
                
                // Atualiza botões
                document.querySelectorAll('#log-filters .filter-btn').forEach((btn, idx) => {
                    btn.classList.remove('active');
                    if ((filter === 'all' && idx === 0) ||
                        (filter === 'success' && idx === 1) ||
                        (filter === 'failed' && idx === 2) ||
                        (filter === 'denied' && idx === 3) ||
                        (filter === 'incident' && idx === 4)) {
                        btn.classList.add('active');
                    }
                });
                
                renderLogs();
            }
            
            function renderLogs() {
                const container = document.getElementById('logs-container');
                
                let filteredLogs = allLogs;
                if (currentLogFilter !== 'all') {
                    filteredLogs = allLogs.filter(log => log.status === currentLogFilter);
                }
                
                if (filteredLogs.length === 0) {
                    container.innerHTML = '<div class="no-data"><div class="no-data-icon"><i class="fas fa-inbox"></i></div>Nenhum log encontrado</div>';
                    return;
                }

                // Atualiza o índice dos logs renderizados
                allLogsWithIndex = [...filteredLogs.slice(0, 20)];

                container.innerHTML = filteredLogs.slice(0, 20).map((log, index) => {
                    const timestamp = log.timestamp || 'N/A';
                    let eventType = log.event_type || 'unknown';
                    const userId = log.user_id || 'N/A';
                    const status = log.status || 'unknown';
                    const projectId = log.project_id || null;
                    let resourceId = log.resource_id || null;
                    const traceId = log.trace_id || null;
                    
                    // Formata event_type para logs de teste
                    if (eventType.startsWith('test.')) {
                        eventType = eventType.replace('test.', '').replace(/_/g, ' ').replace(/\b\w/g, l => l.toUpperCase());
                    }
                    
                    // Para logs de teste, usa o endpoint como resource_id se não houver
                    if (!resourceId && log.details && log.details.endpoint) {
                        resourceId = log.details.endpoint;
                    }
                    
                    let statusClass = '';
                    let statusBadgeClass = 'badge-success';
                    let statusLabel = status;
                    
                    if (status === 'success') { 
                        statusClass = 'success'; 
                        statusBadgeClass = 'badge-success';
                        statusLabel = 'Sucesso';
                    }
                    if (status === 'failed') { 
                        statusClass = 'failed'; 
                        statusBadgeClass = 'badge-failed';
                        statusLabel = 'Falha';
                    }
                    if (status === 'denied') { 
                        statusClass = 'warning'; 
                        statusBadgeClass = 'badge-denied';
                        statusLabel = 'Negado';
                    }
                    if (status === 'incident') { 
                        statusClass = 'incident'; 
                        statusBadgeClass = 'badge-incident';
                        statusLabel = 'Incidente';
                    }
                    
                    const metaItems = [];
                    if (projectId) metaItems.push(`<span class="log-meta-item"><i class="fas fa-folder"></i>${projectId}</span>`);
                    if (resourceId) {
                        const displayResourceId = resourceId.length > 20 ? resourceId.substring(0, 20) + '...' : resourceId;
                        metaItems.push(`<span class="log-meta-item"><i class="fas fa-link"></i>${displayResourceId}</span>`);
                    }
                    if (traceId) metaItems.push(`<span class="log-meta-item"><i class="fas fa-fingerprint"></i>${traceId.substring(0, 12)}...</span>`);
                    
                    return `
                    <div class="log-entry ${statusClass}" onclick="openModal(${index}, false)">
                        <div class="log-left">
                            <div class="log-timestamp">${new Date(timestamp).toLocaleString('pt-BR', { 
                                day: '2-digit', 
                                month: '2-digit', 
                                hour: '2-digit', 
                                minute: '2-digit' 
                            })}</div>
                            <div class="log-badge ${statusBadgeClass}">
                                <span class="log-status-indicator ${status}"></span> ${statusLabel}
                            </div>
                        </div>
                        <div class="log-center">
                            <div class="log-event">${eventType}</div>
                            <div class="log-user"><i class="fas fa-user"></i> ${userId}</div>
                            ${metaItems.length > 0 ? `<div class="log-meta">${metaItems.join('')}</div>` : ''}
                        </div>
                        <div class="log-right">
                            <i class="fas fa-chevron-right" style="color: #adb5bd; font-size: 0.9em;"></i>
                        </div>
                    </div>
                `}).join('');
            }

            // ========== INCIDENTES ==========
            async function loadIncidents() {
                try {
                    const response = await fetch('/monitoring/incidents?limit=50');
                    const data = await response.json();
                    allIncidents = data.incidents || [];
                    allIncidentsWithIndex = [...allIncidents]; // Cria cópia para indexação
                    renderIncidents();
                } catch (error) {
                    console.error('Erro ao carregar incidentes:', error);
                    document.getElementById('incidents-container').innerHTML = 
                        '<div class="no-data"><div class="no-data-icon"><i class="fas fa-exclamation-triangle"></i></div>Erro ao carregar incidentes</div>';
                }
            }
            
            function filterIncidents(filter) {
                currentIncidentFilter = filter;
                
                // Atualiza botões
                document.querySelectorAll('#incident-filters .filter-btn').forEach((btn, idx) => {
                    btn.classList.remove('active');
                    if ((filter === 'all' && idx === 0) ||
                        (filter === 'critical' && idx === 1) ||
                        (filter === 'high' && idx === 2) ||
                        (filter === 'medium' && idx === 3) ||
                        (filter === 'low' && idx === 4)) {
                        btn.classList.add('active');
                    }
                });
                
                renderIncidents();
            }
            
            function renderIncidents() {
                const container = document.getElementById('incidents-container');
                
                let filteredIncidents = allIncidents;
                if (currentIncidentFilter !== 'all') {
                    filteredIncidents = allIncidents.filter(incident => {
                        const severity = incident.details?.severity || 'medium';
                        return severity === currentIncidentFilter;
                    });
                }
                
                if (filteredIncidents.length === 0) {
                    container.innerHTML = '<div class="no-data"><div class="no-data-icon"><i class="fas fa-check-circle"></i></div>Nenhum incidente encontrado - Sistema operando normalmente</div>';
                    return;
                }

                // Atualiza o índice dos incidentes renderizados
                allIncidentsWithIndex = [...filteredIncidents.slice(0, 20)];

                container.innerHTML = filteredIncidents.slice(0, 20).map((incident, index) => {
                    const timestamp = incident.timestamp || 'N/A';
                    const eventType = incident.event_type || 'unknown';
                    const userId = incident.user_id || 'N/A';
                    
                    // Busca a razão em diferentes campos possíveis
                    let reason = incident.reason || 
                                incident.details?.reason || 
                                incident.details?.message || 
                                incident.message ||
                                (incident.details?.error ? `Erro: ${incident.details.error}` : null) ||
                                'Incidente detectado - clique para mais detalhes';
                    
                    const severity = incident.details?.severity || 'medium';
                    const resourceId = incident.resource_id || null;
                    const traceId = incident.trace_id || null;
                    
                    let severityIcon = '<i class="fas fa-circle" style="color: #ffc107;"></i>';
                    let badgeClass = 'badge-denied';
                    let statusClass = 'warning';
                    let severityLabel = 'Médio';
                    
                    if (severity === 'critical') { 
                        severityIcon = '<i class="fas fa-circle" style="color: #dc3545;"></i>'; 
                        badgeClass = 'badge-failed'; 
                        statusClass = 'failed';
                        severityLabel = 'Crítico';
                    }
                    if (severity === 'high') { 
                        severityIcon = '<i class="fas fa-circle" style="color: #fd7e14;"></i>'; 
                        badgeClass = 'badge-failed'; 
                        statusClass = 'failed';
                        severityLabel = 'Alto';
                    }
                    if (severity === 'medium') {
                        severityLabel = 'Médio';
                    }
                    if (severity === 'low') { 
                        severityIcon = '<i class="fas fa-circle" style="color: #198754;"></i>'; 
                        badgeClass = 'badge-success'; 
                        statusClass = 'success';
                        severityLabel = 'Baixo';
                    }
                    
                    const metaItems = [];
                    if (resourceId) metaItems.push(`<span class="log-meta-item"><i class="fas fa-link"></i>${resourceId}</span>`);
                    if (traceId) metaItems.push(`<span class="log-meta-item"><i class="fas fa-fingerprint"></i>${traceId.substring(0, 12)}...</span>`);
                    
                    return `
                    <div class="log-entry ${statusClass}" onclick="openModal(${index}, true)">
                        <div class="log-left">
                            <div class="log-timestamp">${new Date(timestamp).toLocaleString('pt-BR', { 
                                day: '2-digit', 
                                month: '2-digit', 
                                hour: '2-digit', 
                                minute: '2-digit' 
                            })}</div>
                            <div class="log-badge ${badgeClass}">
                                ${severityIcon} ${severityLabel}
                            </div>
                        </div>
                        <div class="log-center">
                            <div class="log-event"><i class="fas fa-exclamation-triangle"></i> ${eventType}</div>
                            <div class="log-user"><i class="fas fa-user"></i> ${userId}</div>
                            <div style="color: #6c757d; font-size: 0.85em; margin-top: 4px;">${reason}</div>
                            ${metaItems.length > 0 ? `<div class="log-meta">${metaItems.join('')}</div>` : ''}
                        </div>
                        <div class="log-right">
                            <i class="fas fa-chevron-right" style="color: #adb5bd; font-size: 0.9em;"></i>
                        </div>
                    </div>
                `}).join('');
            }

            // Testes Automatizados de Segurança
            async function loadComplianceResults() {
                const container = document.getElementById('compliance-container');
                if (!container) {
                    return;
                }
                
                // Preserva estado dos dropdowns antes de atualizar
                if (window.complianceDropdownsState) {
                    const allScenarios = document.querySelectorAll('[id^="scenario-"]');
                    allScenarios.forEach(s => {
                        const isVisible = s.style.display !== 'none' && window.getComputedStyle(s).display !== 'none';
                        window.complianceDropdownsState[s.id] = isVisible;
                    });
                }
                
                // Preserva estado dos dropdowns de serviço antes de atualizar
                if (window.complianceServiceDropdownsState) {
                    const allServices = document.querySelectorAll('[id^="service-tests-"]');
                    allServices.forEach(s => {
                        const isVisible = s.style.display !== 'none' && window.getComputedStyle(s).display !== 'none';
                        window.complianceServiceDropdownsState[s.id] = isVisible;
                    });
                }

                // Preserva estado do dropdown "Todos os Testes Executados"
                const allTestsContainer = document.getElementById('all-tests-container');
                if (allTestsContainer) {
                    window.complianceAllTestsExpanded = (allTestsContainer.style.display !== 'none' && window.getComputedStyle(allTestsContainer).display !== 'none');
                }
                
                try {
                    console.log('🔍 Carregando resultados de conformidade...');
                    const response = await fetch('/monitoring/compliance-results');
                    
                    if (!response.ok) {
                        container.innerHTML = `
                            <div style="padding: 40px; text-align: center; background: #fff3cd; border: 2px solid #ffc107; border-radius: 8px;">
                                <div style="font-size: 3em; margin-bottom: 16px;">⚠️</div>
                                <div style="font-size: 1.2em; font-weight: 600; color: #856404; margin-bottom: 8px;">Erro ${response.status}: ${response.statusText}</div>
                                <div style="color: #856404; margin-bottom: 16px;">O endpoint /monitoring/compliance-results não está disponível.</div>
                                <div style="background: white; padding: 16px; border-radius: 8px; color: #495057;">
                                    <strong>SOLUÇÃO:</strong><br/>
                                    1. Pare o servidor (Ctrl+C)<br/>
                                    2. Reinicie: <code style="background: #f8f9fa; padding: 4px 8px; border-radius: 4px;">python main.py</code><br/>
                                    3. Recarregue esta página (Ctrl+Shift+R)
                                </div>
                            </div>
                        `;
                        return;
                    }
                    
                    const data = await response.json();
                    console.log('✅ Dados recebidos:', data);
                    
                    if (!data.available) {
                        container.innerHTML = `
                            <div style="padding: 40px; text-align: center; background: #e7f3ff; border: 2px solid #0d6efd; border-radius: 8px;">
                                <div style="font-size: 3em; margin-bottom: 16px;">📋</div>
                                <div style="font-size: 1.2em; font-weight: 600; color: #084298; margin-bottom: 8px;">Nenhum resultado disponível</div>
                                <div style="color: #084298; margin-bottom: 16px;">${data.message || 'Execute o script de teste primeiro'}</div>
                                <div style="background: white; padding: 16px; border-radius: 8px; color: #495057;">
                                    <strong>Execute no terminal:</strong><br/>
                                    <code style="background: #f8f9fa; padding: 8px 16px; border-radius: 4px; display: inline-block; margin-top: 8px; font-size: 1.1em;">python test_compliance_automated.py</code>
                                </div>
                            </div>
                        `;
                        return;
                    }
                    
                    const summary = data.summary || {};
                    const results = data.results || [];
                    
                    // Agrupa por cenário
                    const byScenario = {};
                    results.forEach(r => {
                        const scenario = r.test_scenario || 'Unknown';
                        if (!byScenario[scenario]) {
                            byScenario[scenario] = { passed: 0, failed: 0, total: 0, severity: r.severity || 'ALTO' };
                        }
                        byScenario[scenario].total++;
                        if (r.status === 'PASSED') {
                            byScenario[scenario].passed++;
                        } else {
                            byScenario[scenario].failed++;
                        }
                    });
                    
                    // Renderiza resumo
                    let html = `
                        <div style="margin-bottom: 20px;">
                            <div style="background: #e7f3ff; border: 2px solid #0d6efd; border-radius: 8px; padding: 16px; margin-bottom: 16px;">
                                <div style="font-size: 1em; font-weight: 600; color: #084298; margin-bottom: 8px; display: flex; align-items: center; gap: 8px;">
                                    <i class="fas fa-info-circle"></i> Sobre os Testes Automatizados de Segurança
                                </div>
                                <div style="font-size: 0.9em; color: #084298; line-height: 1.5;">
                                    Estes testes validam a conformidade das APIs Unificadas com os Requisitos Não Funcionais (RNF) de Segurança (RNF-02) e Rastreabilidade (RNF-03). Eles garantem que as APIs estão retornando os contextos de segurança e rastreabilidade esperados, e que a correlação de eventos funciona corretamente.
                                </div>
                            </div>
                            
                            <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 12px; margin-bottom: 16px;">
                                <div style="background: #f8f9fa; padding: 16px; border-radius: 8px; text-align: center; border: 2px solid #dee2e6;">
                                    <div style="font-size: 2em; font-weight: 700; color: #212529; margin-bottom: 4px;">${summary.total || 0}</div>
                                    <div style="font-size: 0.8em; color: #6c757d; font-weight: 500;">Total de Testes Executados</div>
                                </div>
                                <div style="background: #d1e7dd; padding: 16px; border-radius: 8px; text-align: center; border: 2px solid #a3cfbb;">
                                    <div style="font-size: 2em; font-weight: 700; color: #0f5132; margin-bottom: 4px;">✓ ${summary.passed || 0}</div>
                                    <div style="font-size: 0.8em; color: #0f5132; font-weight: 500;">Testes Aprovados</div>
                                </div>
                                <div style="background: #f8d7da; padding: 16px; border-radius: 8px; text-align: center; border: 2px solid #f1aeb5;">
                                    <div style="font-size: 2em; font-weight: 700; color: #842029; margin-bottom: 4px;">✗ ${summary.failed || 0}</div>
                                    <div style="font-size: 0.8em; color: #842029; font-weight: 500;">Testes Falharam</div>
                                </div>
                                <div style="background: ${summary.critical_failed > 0 ? '#f8d7da' : '#d1e7dd'}; padding: 16px; border-radius: 8px; text-align: center; border: 2px solid ${summary.critical_failed > 0 ? '#f1aeb5' : '#a3cfbb'};">
                                    <div style="font-size: 2em; font-weight: 700; color: ${summary.critical_failed > 0 ? '#842029' : '#0f5132'}; margin-bottom: 4px;">${summary.critical_failed > 0 ? '⚠️' : '✓'} ${summary.critical_failed || 0}</div>
                                    <div style="font-size: 0.8em; color: ${summary.critical_failed > 0 ? '#842029' : '#0f5132'}; font-weight: 500;">Falhas Críticas</div>
                                </div>
                            </div>
                            
                            <div style="background: ${summary.pass_rate >= 90 ? '#d1e7dd' : summary.pass_rate >= 70 ? '#fff3cd' : '#f8d7da'}; border: 2px solid ${summary.pass_rate >= 90 ? '#a3cfbb' : summary.pass_rate >= 70 ? '#ffc107' : '#f1aeb5'}; padding: 16px; border-radius: 8px; text-align: center;">
                                <div style="font-size: 1.1em; font-weight: 600; color: ${summary.pass_rate >= 90 ? '#0f5132' : summary.pass_rate >= 70 ? '#856404' : '#842029'}; margin-bottom: 4px;">
                                    Taxa de Conformidade: <span style="font-size: 1.3em;">${summary.pass_rate || 0}%</span>
                                </div>
                                <div style="font-size: 0.85em; color: ${summary.pass_rate >= 90 ? '#0f5132' : summary.pass_rate >= 70 ? '#856404' : '#842029'};">
                                    ${summary.pass_rate >= 90 ? '✅ Sistema em conformidade' : summary.pass_rate >= 70 ? '⚠️ Atenção necessária' : '❌ Ação imediata requerida'}
                                </div>
                            </div>
                        </div>
                    `;
                    
                    // Renderiza resultados por cenário com dropdown e explicações
                    html += `
                        <div style="margin-top: 24px;">
                            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 16px;">
                                <h3 style="font-size: 1em; font-weight: 600; color: #212529; display: flex; align-items: center; gap: 8px;">
                                    <i class="fas fa-list-check"></i> Detalhamento por Cenário de Teste
                                </h3>
                                <button onclick="toggleAllScenarios()" style="background: #0d6efd; color: white; border: none; padding: 6px 12px; border-radius: 6px; font-size: 0.85em; cursor: pointer; font-weight: 500;">
                                    <i class="fas fa-chevron-down" id="toggle-all-icon"></i> <span id="toggle-all-text">Expandir Todos</span>
                                </button>
                            </div>
                    `;
                    
                    // Mapeia cenários para descrições claras com explicações técnicas
                    const scenarioDescriptions = {
                        'Validação de Correlação': {
                            icon: '🔗',
                            description: 'Verifica se o UUID enviado no header x-correlation-id é retornado corretamente no campo correlation_id da resposta. Garante rastreabilidade entre serviços.',
                            rnf: 'Segurança',
                            technicalDetails: {
                                'x-correlation-id': 'Header HTTP enviado na requisição contendo um UUID único gerado dinamicamente',
                                'correlation_id': 'Campo no corpo da resposta JSON que deve conter o mesmo UUID enviado no header. Permite rastrear uma operação através de múltiplos serviços.',
                                'Por que é importante?': 'Garante que você pode rastrear uma operação completa mesmo quando ela passa por vários serviços (SharePoint → Sentinel → Office, etc.)'
                            }
                        },
                        'Presença do Contexto de Segurança': {
                            icon: '🔐',
                            description: 'Valida se o objeto meta.security_context contém os campos obrigatórios: user_id, tenant_id e mfa_enabled. Essencial para auditoria de segurança.',
                            rnf: 'Segurança',
                            technicalDetails: {
                                'meta.security_context': 'Objeto dentro da resposta JSON que contém informações sobre quem fez a requisição e como foi autenticado',
                                'user_id': 'Identificador único do usuário que fez a requisição (ex: "u001", "u002")',
                                'tenant_id': 'Identificador da organização/empresa (ex: "tenant-01"). Permite multi-tenancy (várias empresas no mesmo sistema)',
                                'mfa_enabled': 'Indica se o usuário tem autenticação de dois fatores (MFA) habilitada. Valores: true ou false',
                                'Por que é importante?': 'Permite auditoria completa: saber QUEM fez o quê, de QUAL organização, e se tinha segurança adicional (MFA)'
                            }
                        },
                        'Presença do Contexto de Rastreabilidade': {
                            icon: '📊',
                            description: 'Valida se o objeto meta.traceability contém trace_id, span_id e ingested_at_utc (ISO 8601). Permite rastrear operações completas.',
                            rnf: 'Segurança',
                            technicalDetails: {
                                'meta.traceability': 'Objeto dentro da resposta JSON que contém informações para rastrear a operação em sistemas de monitoramento',
                                'trace_id': 'ID único que identifica toda a "jornada" de uma requisição através de múltiplos serviços. Permite ver todos os logs relacionados a uma operação',
                                'span_id': 'ID único que identifica uma etapa específica dentro de uma trace. Uma trace pode ter vários spans (ex: chamada ao SharePoint, depois ao Sentinel)',
                                'ingested_at_utc': 'Data e hora em formato ISO 8601 (ex: "2025-12-02T10:15:00Z") indicando quando o evento foi registrado no sistema. O "Z" significa UTC (horário universal)',
                                'Por que é importante?': 'Permite rastrear operações complexas: ver todos os passos de uma requisição, quando cada etapa aconteceu, e correlacionar eventos entre serviços'
                            }
                        }
                    };
                    
                    let scenarioIndex = 0;
                    Object.entries(byScenario).forEach(([scenario, stats]) => {
                        const passRate = stats.total > 0 ? Math.round(stats.passed / stats.total * 100) : 0;
                        const severityColor = stats.severity === 'CRÍTICO' ? '#dc3545' : '#fd7e14';
                        const scenarioInfo = scenarioDescriptions[scenario] || { icon: '📋', description: 'Teste de conformidade', rnf: 'RNF', technicalDetails: {} };
                        const statusIcon = stats.failed === 0 ? '✅' : stats.failed < stats.total ? '⚠️' : '❌';
                        const scenarioId = `scenario-${scenarioIndex++}`;
                        
                        html += `
                            <div style="background: white; border: 2px solid ${stats.failed === 0 ? '#d1e7dd' : '#f8d7da'}; border-left: 5px solid ${severityColor}; border-radius: 8px; margin-bottom: 12px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); overflow: hidden;">
                                <!-- Cabeçalho clicável -->
                                <div onclick="toggleScenario('${scenarioId}', event)" style="padding: 20px; cursor: pointer; display: flex; justify-content: space-between; align-items: start; transition: background 0.2s;" onmouseover="this.style.background='#f8f9fa'" onmouseout="this.style.background='white'">
                                    <div style="flex: 1;">
                                        <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 8px;">
                                            <span style="font-size: 1.5em;">${scenarioInfo.icon}</span>
                                            <div>
                                                <div style="font-weight: 700; color: #212529; font-size: 1.05em; margin-bottom: 2px;">${scenario}</div>
                                                <div style="font-size: 0.8em; color: #6c757d;">${scenarioInfo.rnf}</div>
                                            </div>
                                        </div>
                                        <div style="font-size: 0.9em; color: #495057; line-height: 1.5;">
                                            ${scenarioInfo.description}
                                        </div>
                                    </div>
                                    <div style="text-align: right; margin-left: 16px; display: flex; flex-direction: column; align-items: flex-end; gap: 8px;">
                                        <div style="font-size: 0.85em; padding: 6px 14px; border-radius: 20px; background: ${severityColor}20; color: ${severityColor}; font-weight: 600;">
                                            ${stats.severity}
                                        </div>
                                        <div style="font-size: 1.5em; font-weight: 700; color: ${stats.failed === 0 ? '#198754' : '#dc3545'};">
                                            ${statusIcon} ${passRate}%
                                        </div>
                                        <div style="font-size: 1.2em; color: #6c757d; transition: transform 0.3s;" id="icon-${scenarioId}">
                                            <i class="fas fa-chevron-down"></i>
                                        </div>
                                    </div>
                                </div>
                                
                                <!-- Conteúdo expansível -->
                                <div id="${scenarioId}" onclick="event.stopPropagation();" style="display: none; padding: 0 20px 20px 20px; border-top: 1px solid #e9ecef;">
                                    <!-- Estatísticas -->
                                    <div style="display: flex; gap: 20px; font-size: 0.9em; margin-bottom: 20px; padding-top: 16px;">
                                        <div style="flex: 1; text-align: center; padding: 12px; background: #f8f9fa; border-radius: 6px;">
                                            <div style="font-weight: 600; color: #198754; font-size: 1.3em; margin-bottom: 4px;">✓ ${stats.passed}</div>
                                            <div style="color: #6c757d; font-size: 0.85em;">Aprovados</div>
                                        </div>
                                        <div style="flex: 1; text-align: center; padding: 12px; background: #f8f9fa; border-radius: 6px;">
                                            <div style="font-weight: 600; color: #dc3545; font-size: 1.3em; margin-bottom: 4px;">✗ ${stats.failed}</div>
                                            <div style="color: #6c757d; font-size: 0.85em;">Falharam</div>
                                        </div>
                                        <div style="flex: 1; text-align: center; padding: 12px; background: #f8f9fa; border-radius: 6px;">
                                            <div style="font-weight: 600; color: #212529; font-size: 1.3em; margin-bottom: 4px;">${stats.total}</div>
                                            <div style="color: #6c757d; font-size: 0.85em;">Total de Testes</div>
                                        </div>
                                    </div>
                                    
                                    <!-- Explicações técnicas -->
                                    <div style="background: #f8f9fa; border-radius: 8px; padding: 16px; margin-top: 16px;">
                                        <div style="font-weight: 600; color: #212529; margin-bottom: 12px; display: flex; align-items: center; gap: 8px;">
                                            <i class="fas fa-question-circle"></i> O que significa cada campo técnico?
                                        </div>
                                        ${Object.entries(scenarioInfo.technicalDetails).map(([term, explanation]) => `
                                            <div style="margin-bottom: 12px; padding-bottom: 12px; border-bottom: 1px solid #dee2e6; ${Object.keys(scenarioInfo.technicalDetails).indexOf(term) === Object.keys(scenarioInfo.technicalDetails).length - 1 ? 'border-bottom: none; margin-bottom: 0; padding-bottom: 0;' : ''}">
                                                <div style="font-weight: 600; color: #0d6efd; margin-bottom: 4px; font-family: monospace; font-size: 0.9em;">
                                                    ${term}
                                                </div>
                                                <div style="color: #495057; font-size: 0.9em; line-height: 1.5;">
                                                    ${explanation}
                                                </div>
                                            </div>
                                        `).join('')}
                                    </div>
                                </div>
                            </div>
                        `;
                    });
                    
                    html += '</div>';
                    
                    // Agrupa por serviço para mostrar quais APIs foram testadas
                    const byService = {};
                    results.forEach(r => {
                        const service = r.service_tested || 'unknown';
                        if (!byService[service]) {
                            byService[service] = { passed: 0, failed: 0, total: 0, tests: [] };
                        }
                        byService[service].total++;
                        if (r.status === 'PASSED') {
                            byService[service].passed++;
                        } else {
                            byService[service].failed++;
                        }
                        byService[service].tests.push(r);
                    });
                    
                    // Mostra APIs testadas
                    html += `
                        <div style="margin-top: 24px;">
                            <h3 style="font-size: 1em; font-weight: 600; color: #212529; margin-bottom: 12px; display: flex; align-items: center; gap: 8px;">
                                <i class="fas fa-cloud"></i> APIs Testadas
                            </h3>
                            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 12px; margin-bottom: 20px;">
                                ${Object.entries(byService).map(([service, stats]) => {
                                    const servicePassRate = stats.total > 0 ? Math.round(stats.passed / stats.total * 100) : 0;
                                    const serviceIcons = {
                                        'sharepoint': '📁',
                                        'miro': '🎨',
                                        'copilot': '🤖',
                                        'office': '📧',
                                        'sentinel': '🛡️'
                                    };
                                    const serviceId = 'service-tests-' + service.replace(/\s+/g, '-').toLowerCase();
                                    const serviceTests = stats.tests; // Todos os testes para este serviço
                                    return `
                                        <div style="background: white; border: 2px solid ${stats.failed === 0 ? '#d1e7dd' : '#f8d7da'}; padding: 16px; border-radius: 8px; text-align: center; cursor: pointer; box-shadow: 0 2px 4px rgba(0,0,0,0.1); transition: all 0.2s;" onclick="toggleServiceTests('${serviceId}', event)" onmouseover="this.style.background='#f8f9fa'" onmouseout="this.style.background='white'">
                                            <div style="font-size: 2em; margin-bottom: 8px;">${serviceIcons[service] || '🔌'}</div>
                                            <div style="font-weight: 600; color: #212529; margin-bottom: 4px; text-transform: capitalize;">${service}</div>
                                            <div style="font-size: 0.85em; color: #6c757d; margin-bottom: 8px;">${stats.total} testes</div>
                                            <div style="font-size: 1.1em; font-weight: 700; color: ${stats.failed === 0 ? '#198754' : '#dc3545'}; margin-bottom: 8px;">
                                                ${stats.failed === 0 ? '✅' : '⚠️'} ${servicePassRate}%
                                            </div>
                                            <div style="font-size: 0.75em; color: #0d6efd; margin-top: 8px; padding-top: 8px; border-top: 1px solid #e9ecef;">
                                                <i class="fas fa-chevron-down" id="icon-${serviceId}"></i> Ver testes
                                            </div>
                                            <div id="${serviceId}" onclick="event.stopPropagation();" style="display: none; margin-top: 12px; padding-top: 12px; border-top: 2px solid #dee2e6; text-align: left;">
                                                ${serviceTests.map(test => `
                                                    <div style="padding: 10px; margin-bottom: 8px; background: ${test.status === 'PASSED' ? '#d1e7dd' : '#f8d7da'}; border-radius: 6px; border-left: 4px solid ${test.status === 'PASSED' ? '#198754' : '#dc3545'};">
                                                        <div style="display: flex; justify-content: space-between; align-items: start; margin-bottom: 4px;">
                                                            <div style="font-weight: 600; color: #212529; font-size: 0.9em;">${test.test_scenario || 'N/A'}</div>
                                                            <span style="padding: 3px 8px; border-radius: 4px; font-size: 0.75em; font-weight: 600; ${test.status === 'PASSED' ? 'background: #198754; color: white;' : 'background: #dc3545; color: white;'}">
                                                                ${test.status === 'PASSED' ? '✓' : '✗'} ${test.status || 'N/A'}
                                                            </span>
                                                        </div>
                                                        <div style="font-size: 0.8em; color: #6c757d; margin-bottom: 4px; font-family: monospace;">
                                                            ${test.endpoint_tested || 'N/A'}
                                                        </div>
                                                        <div style="font-size: 0.75em; color: #495057;">
                                                            <strong>Severidade:</strong> ${test.severity || 'N/A'} | 
                                                            <strong>Tempo:</strong> ${test.execution_time_ms || 'N/A'}ms
                                                        </div>
                                                        ${test.details ? `<div style="font-size: 0.75em; color: #6c757d; margin-top: 4px; font-style: italic;">${test.details}</div>` : ''}
                                                    </div>
                                                `).join('')}
                                            </div>
                                        </div>
                                    `;
                                }).join('')}
                            </div>
                        </div>
                    `;
                    
                    // Seção de todos os testes executados (clicável)
                    if (results.length > 0) {
                        html += `
                            <div style="margin-top: 24px;">
                                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px;">
                                    <h3 style="font-size: 1em; font-weight: 600; color: #212529; display: flex; align-items: center; gap: 8px;">
                                        <i class="fas fa-list"></i> Todos os Testes Executados
                                    </h3>
                                    <button onclick="toggleAllTests()" style="background: #0d6efd; color: white; border: none; padding: 6px 12px; border-radius: 6px; font-size: 0.85em; cursor: pointer; font-weight: 500;">
                                        <i class="fas fa-chevron-down" id="toggle-all-tests-icon"></i> <span id="toggle-all-tests-text">Expandir Todos</span>
                                    </button>
                                </div>
                                <div id="all-tests-container" style="display: none; max-height: 500px; overflow-y: auto; border: 1px solid #dee2e6; border-radius: 8px; background: white; padding: 12px;">
                                    ${results.map((test, idx) => `
                                        <div style="padding: 12px; margin-bottom: 8px; background: ${test.status === 'PASSED' ? '#d1e7dd' : '#f8d7da'}; border-radius: 6px; border-left: 4px solid ${test.status === 'PASSED' ? '#198754' : '#dc3545'};">
                                            <div style="display: flex; justify-content: space-between; align-items: start; margin-bottom: 6px;">
                                                <div style="flex: 1;">
                                                    <div style="font-weight: 700; color: #212529; font-size: 0.95em; margin-bottom: 4px;">
                                                        ${test.test_scenario || 'N/A'}
                                                    </div>
                                                    <div style="font-size: 0.8em; color: #6c757d; margin-bottom: 4px;">
                                                        <strong>API:</strong> <span style="text-transform: capitalize;">${test.service_tested || 'N/A'}</span> | 
                                                        <strong>Endpoint:</strong> <span style="font-family: monospace;">${test.endpoint_tested || 'N/A'}</span>
                                                    </div>
                                                    <div style="font-size: 0.75em; color: #495057;">
                                                        <strong>Severidade:</strong> ${test.severity || 'N/A'} | 
                                                        <strong>Tempo:</strong> ${test.execution_time_ms || 'N/A'}ms | 
                                                        <strong>Executado:</strong> ${test.timestamp_utc || 'N/A'}
                                                    </div>
                                                    ${test.details ? `<div style="font-size: 0.8em; color: #6c757d; margin-top: 6px; padding: 8px; background: rgba(255,255,255,0.7); border-radius: 4px; font-style: italic;">${test.details}</div>` : ''}
                                                </div>
                                                <span style="padding: 4px 10px; border-radius: 4px; font-size: 0.8em; font-weight: 600; margin-left: 12px; ${test.status === 'PASSED' ? 'background: #198754; color: white;' : 'background: #dc3545; color: white;'}">
                                                    ${test.status === 'PASSED' ? '✓ PASSED' : '✗ FAILED'}
                                                </span>
                                            </div>
                                        </div>
                                    `).join('')}
                                </div>
                            </div>
                        `;
                    }
                    
                    // Tabela de resultados recentes (simplificada)
                    if (results.length > 0) {
                        html += `
                            <div style="margin-top: 24px;">
                                <h3 style="font-size: 1em; font-weight: 600; color: #212529; margin-bottom: 12px; display: flex; align-items: center; gap: 8px;">
                                    <i class="fas fa-history"></i> Histórico Resumido (Últimos 15)
                                </h3>
                                <div style="max-height: 250px; overflow-y: auto; border: 1px solid #dee2e6; border-radius: 8px; background: white;">
                                    <table style="width: 100%; border-collapse: collapse;">
                                        <thead style="background: #f8f9fa; position: sticky; top: 0;">
                                            <tr>
                                                <th style="padding: 10px 12px; text-align: left; font-size: 0.75em; text-transform: uppercase; color: #495057; font-weight: 600;">API</th>
                                                <th style="padding: 10px 12px; text-align: left; font-size: 0.75em; text-transform: uppercase; color: #495057; font-weight: 600;">Cenário</th>
                                                <th style="padding: 10px 12px; text-align: center; font-size: 0.75em; text-transform: uppercase; color: #495057; font-weight: 600;">Resultado</th>
                                            </tr>
                                        </thead>
                                        <tbody>
                                            ${results.slice(-15).reverse().map(r => `
                                                <tr style="border-bottom: 1px solid #f0f0f0; ${r.status === 'FAILED' ? 'background: #fff5f5;' : ''}">
                                                    <td style="padding: 10px 12px; font-size: 0.85em;">
                                                        <div style="font-weight: 600; color: #212529; text-transform: capitalize;">${r.service_tested || 'N/A'}</div>
                                                        <div style="color: #6c757d; font-size: 0.75em; margin-top: 2px; font-family: monospace;">${(r.endpoint_tested || '').substring(0, 35)}${(r.endpoint_tested || '').length > 35 ? '...' : ''}</div>
                                                    </td>
                                                    <td style="padding: 10px 12px; font-size: 0.85em; color: #495057;">${r.test_scenario || 'N/A'}</td>
                                                    <td style="padding: 10px 12px; text-align: center;">
                                                        <span style="padding: 4px 10px; border-radius: 4px; font-size: 0.75em; font-weight: 600; ${r.status === 'PASSED' ? 'background: #d1e7dd; color: #0f5132;' : 'background: #f8d7da; color: #842029;'}">
                                                            ${r.status === 'PASSED' ? '✓' : '✗'} ${r.status || 'N/A'}
                                                        </span>
                                                    </td>
                                                </tr>
                                            `).join('')}
                                        </tbody>
                                    </table>
                                </div>
                            </div>
                        `;
                    }
                    
                    container.innerHTML = html;
                    
                    setTimeout(() => {
                        if (window.restoreComplianceDropdownsState) {
                            window.restoreComplianceDropdownsState();
                        }
                    }, 200);
                    
                } catch (error) {
                    const container = document.getElementById('compliance-container');
                    if (container) {
                        container.innerHTML = `
                            <div style="padding: 40px; text-align: center; background: #f8d7da; border: 2px solid #dc3545; border-radius: 8px;">
                                <div style="font-size: 3em; margin-bottom: 16px;">🚨</div>
                                <div style="font-size: 1.2em; font-weight: 600; color: #842029; margin-bottom: 8px;">Erro ao carregar resultados</div>
                                <div style="color: #842029; margin-bottom: 16px;">${error.message || 'Erro desconhecido'}</div>
                                <div style="background: white; padding: 16px; border-radius: 8px; color: #495057; text-align: left; max-width: 500px; margin: 0 auto;">
                                    <strong>Verifique:</strong><br/>
                                    1. O servidor está rodando?<br/>
                                    2. O endpoint /monitoring/compliance-results existe?<br/>
                                    3. O arquivo test_results.csv existe?<br/>
                                    <br/>
                                    <button onclick="loadComplianceResults()" style="background: #dc3545; color: white; border: none; padding: 8px 16px; border-radius: 4px; cursor: pointer; margin-top: 8px;">
                                        🔄 Tentar Novamente
                                    </button>
                                </div>
                            </div>
                        `;
                    }
                }
            }
            
            // Funções para dropdowns de cenários
            window.complianceDropdownsState = window.complianceDropdownsState || {};
            window.complianceServiceDropdownsState = window.complianceServiceDropdownsState || {};
            window.complianceAllTestsExpanded = window.complianceAllTestsExpanded || false;
            
            // Função para salvar o estado dos dropdowns antes de um refresh
            window.saveComplianceDropdownsState = function() {
                const allScenarios = document.querySelectorAll('[id^="scenario-"]');
                allScenarios.forEach(s => {
                    const isVisible = s.style.display !== 'none' && window.getComputedStyle(s).display !== 'none';
                    window.complianceDropdownsState[s.id] = isVisible;
                });
                
                const allServices = document.querySelectorAll('[id^="service-tests-"]');
                allServices.forEach(s => {
                    const isVisible = s.style.display !== 'none' && window.getComputedStyle(s).display !== 'none';
                    window.complianceServiceDropdownsState[s.id] = isVisible;
                });

                const allTestsContainer = document.getElementById('all-tests-container');
                if (allTestsContainer) {
                    window.complianceAllTestsExpanded = (allTestsContainer.style.display !== 'none' && window.getComputedStyle(allTestsContainer).display !== 'none');
                }
            };
            
            window.toggleScenario = function(scenarioId, event) {
                if (event) {
                    event.stopPropagation();
                    event.preventDefault();
                }
                const content = document.getElementById(scenarioId);
                const icon = document.getElementById('icon-' + scenarioId);
                if (!content || !icon) return;
                
                const isHidden = content.style.display === 'none' || !content.style.display || window.getComputedStyle(content).display === 'none';
                
                if (isHidden) {
                    content.style.display = 'block';
                    icon.style.transform = 'rotate(180deg)';
                    window.complianceDropdownsState[scenarioId] = true;
                } else {
                    content.style.display = 'none';
                    icon.style.transform = 'rotate(0deg)';
                    window.complianceDropdownsState[scenarioId] = false;
                }
            };
            
            window.toggleAllScenarios = function(event) {
                if (event) {
                    event.stopPropagation();
                    event.preventDefault();
                }
                const allScenarios = document.querySelectorAll('[id^="scenario-"]');
                const toggleBtn = document.getElementById('toggle-all-text');
                const toggleIcon = document.getElementById('toggle-all-icon');
                
                if (allScenarios.length === 0) return;
                
                let allExpanded = true;
                allScenarios.forEach(s => {
                    if (s.style.display === 'none' || !s.style.display) {
                        allExpanded = false;
                    }
                });
                
                allScenarios.forEach((s, idx) => {
                    const scenarioId = s.id;
                    const icon = document.getElementById('icon-' + scenarioId);
                    if (allExpanded) {
                        s.style.display = 'none';
                        if (icon) icon.style.transform = 'rotate(0deg)';
                        window.complianceDropdownsState[scenarioId] = false;
                    } else {
                        s.style.display = 'block';
                        if (icon) icon.style.transform = 'rotate(180deg)';
                        window.complianceDropdownsState[scenarioId] = true;
                    }
                });
                
                if (toggleBtn) {
                    toggleBtn.textContent = allExpanded ? 'Expandir Todos' : 'Recolher Todos';
                }
                if (toggleIcon) {
                    toggleIcon.style.transform = allExpanded ? 'rotate(0deg)' : 'rotate(180deg)';
                }
            };
            
            // Função para restaurar o estado dos dropdowns após um refresh
            window.restoreComplianceDropdownsState = function() {
                let restoredScenarios = 0;
                for (const id in window.complianceDropdownsState) {
                    const content = document.getElementById(id);
                    const icon = document.getElementById('icon-' + id);
                    if (content && icon) {
                        if (window.complianceDropdownsState[id]) {
                            content.style.display = 'block';
                            icon.style.transform = 'rotate(180deg)';
                            restoredScenarios++;
                        } else {
                            content.style.display = 'none';
                            icon.style.transform = 'rotate(0deg)';
                        }
                    }
                }
                if (restoredScenarios > 0) {
                    console.log(`✅ Restaurados ${restoredScenarios} dropdown(s) de cenário abertos`);
                }

                let restoredServices = 0;
                for (const id in window.complianceServiceDropdownsState) {
                    const content = document.getElementById(id);
                    const icon = document.getElementById('icon-' + id);
                    if (content && icon) {
                        if (window.complianceServiceDropdownsState[id]) {
                            content.style.display = 'block';
                            icon.style.transform = 'rotate(180deg)';
                            restoredServices++;
                        } else {
                            content.style.display = 'none';
                            icon.style.transform = 'rotate(0deg)';
                        }
                    }
                }
                if (restoredServices > 0) {
                    console.log(`✅ Restaurados ${restoredServices} dropdown(s) de serviço abertos`);
                }

                const allTestsContainer = document.getElementById('all-tests-container');
                const toggleAllTestsIcon = document.getElementById('toggle-all-tests-icon');
                const toggleAllTestsText = document.getElementById('toggle-all-tests-text');
                if (allTestsContainer && toggleAllTestsIcon && toggleAllTestsText) {
                    if (window.complianceAllTestsExpanded) {
                        allTestsContainer.style.display = 'block';
                        toggleAllTestsIcon.style.transform = 'rotate(180deg)';
                        toggleAllTestsText.textContent = 'Recolher Todos';
                    } else {
                        allTestsContainer.style.display = 'none';
                        toggleAllTestsIcon.style.transform = 'rotate(0deg)';
                        toggleAllTestsText.textContent = 'Expandir Todos';
                    }
                }
            };
            
            // Função para expandir/recolher testes de um serviço específico
            window.toggleServiceTests = function(serviceId, event) {
                if (event) event.stopPropagation();
                const content = document.getElementById(serviceId);
                const icon = document.getElementById('icon-' + serviceId);
                if (!content || !icon) return;

                const isHidden = content.style.display === 'none' || !content.style.display || window.getComputedStyle(content).display === 'none';
                
                if (isHidden) {
                    content.style.display = 'block';
                    icon.style.transform = 'rotate(180deg)';
                    window.complianceServiceDropdownsState[serviceId] = true;
                } else {
                    content.style.display = 'none';
                    icon.style.transform = 'rotate(0deg)';
                    window.complianceServiceDropdownsState[serviceId] = false;
                }
            };
            
            // Função para expandir/recolher todos os testes
            window.toggleAllTests = function(event) {
                if (event) {
                    event.stopPropagation();
                    event.preventDefault();
                }
                const container = document.getElementById('all-tests-container');
                const toggleIcon = document.getElementById('toggle-all-tests-icon');
                const toggleText = document.getElementById('toggle-all-tests-text');

                if (!container || !toggleIcon || !toggleText) return;

                const isHidden = container.style.display === 'none' || !container.style.display || window.getComputedStyle(container).display === 'none';

                if (isHidden) {
                    container.style.display = 'block';
                    toggleIcon.style.transform = 'rotate(180deg)';
                    toggleText.textContent = 'Recolher Todos';
                    window.complianceAllTestsExpanded = true;
                } else {
                    container.style.display = 'none';
                    toggleIcon.style.transform = 'rotate(0deg)';
                    toggleText.textContent = 'Expandir Todos';
                    window.complianceAllTestsExpanded = false;
                }
            };
            

            // Carregar todos os dados
            async function loadAllData() {
                updateTimestamp();
                // Salva o estado dos dropdowns de compliance antes de carregar outros dados
                window.saveComplianceDropdownsState(); 
                await Promise.all([
                    loadIntegrations(),
                    loadStats(),
                    loadLogs(),
                    loadIncidents()
                    // loadComplianceResults() -- Removido do auto-refresh
                ]);
                // Restaura o estado dos dropdowns de compliance após carregar outros dados
                setTimeout(() => {
                    window.restoreComplianceDropdownsState();
                }, 200); // Pequeno delay para garantir que o DOM foi atualizado
            }

            // Auto-refresh a cada 15 segundos (sem atualizar compliance)
            setInterval(loadAllData, 15000);

            // Carregar dados iniciais
            console.log('🚀 Dashboard iniciado - carregando todos os dados...');
            loadAllData();
            
            setTimeout(() => {
                loadComplianceResults();
            }, 1000);
        </script>
    </body>
    </html>
    """


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8001,
        reload=True
    )
