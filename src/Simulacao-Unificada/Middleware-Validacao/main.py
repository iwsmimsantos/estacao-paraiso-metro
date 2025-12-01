from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import uvicorn

from src.api import auth as auth_routes
from src.api import monitoring as monitoring_routes
from src.api import validation_simple as validation_simple_routes
from src.api import workflows as workflow_routes

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
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                min-height: 100vh;
                display: flex;
                align-items: center;
                justify-content: center;
                padding: 20px;
                color: #2c3e50;
            }
            .container {
                max-width: 1000px;
                width: 100%;
                background: white;
                backdrop-filter: blur(20px);
                border-radius: 24px;
                padding: 50px;
                box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3);
                border: 1px solid rgba(255, 255, 255, 0.5);
            }
            .header {
                text-align: center;
                margin-bottom: 50px;
            }
            .logo {
                width: 80px;
                height: 80px;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                border-radius: 20px;
                display: flex;
                align-items: center;
                justify-content: center;
                font-size: 3em;
                margin: 0 auto 20px;
                box-shadow: 0 8px 30px rgba(102, 126, 234, 0.4);
            }
            h1 {
                font-size: 2.5em;
                margin-bottom: 10px;
                font-weight: 700;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                background-clip: text;
            }
            .subtitle {
                font-size: 1.1em;
                color: #6b7280;
                font-weight: 400;
            }
            .status-grid {
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
                gap: 20px;
                margin: 40px 0;
            }
            .status-card {
                background: #f9fafb;
                padding: 30px;
                border-radius: 16px;
                text-align: center;
                transition: all 0.3s;
                border: 1px solid rgba(0, 0, 0, 0.08);
            }
            .status-card:hover {
                transform: translateY(-8px);
                box-shadow: 0 12px 40px rgba(102, 126, 234, 0.2);
                background: white;
                border-color: #667eea;
            }
            .status-icon {
                font-size: 3em;
                margin-bottom: 15px;
            }
            .status-card h3 {
                font-size: 1.3em;
                margin-bottom: 10px;
                font-weight: 600;
                color: #1f2937;
            }
            .status-card p {
                color: #6b7280;
                line-height: 1.5;
            }
            .features {
                margin: 50px 0;
            }
            .features h2 {
                text-align: center;
                font-size: 2em;
                margin-bottom: 30px;
                font-weight: 600;
            }
            .feature-grid {
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
                gap: 20px;
            }
            .feature {
                background: #f9fafb;
                padding: 25px;
                border-radius: 16px;
                border-left: 4px solid #667eea;
                transition: all 0.3s;
            }
            .feature:hover {
                background: white;
                transform: translateX(8px);
                box-shadow: 0 4px 20px rgba(102, 126, 234, 0.15);
            }
            .feature h4 {
                font-size: 1.2em;
                margin-bottom: 10px;
                font-weight: 600;
                color: #1f2937;
            }
            .feature p {
                color: #6b7280;
                line-height: 1.6;
            }
            .links {
                display: flex;
                gap: 20px;
                justify-content: center;
                flex-wrap: wrap;
                margin-top: 50px;
            }
            .link-button {
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                color: white;
                padding: 18px 36px;
                border-radius: 12px;
                text-decoration: none;
                font-weight: 700;
                font-size: 1.1em;
                transition: all 0.3s;
                box-shadow: 0 8px 25px rgba(102, 126, 234, 0.3);
                display: flex;
                align-items: center;
                gap: 10px;
            }
            .link-button:hover {
                transform: translateY(-4px);
                box-shadow: 0 12px 35px rgba(102, 126, 234, 0.4);
            }
            .link-button.secondary {
                background: white;
                color: #667eea;
                border: 2px solid #667eea;
            }
            .link-button.secondary:hover {
                background: #f9fafb;
            }
            .footer {
                text-align: center;
                margin-top: 50px;
                padding-top: 30px;
                border-top: 1px solid rgba(0, 0, 0, 0.1);
                color: #6b7280;
                font-size: 0.9em;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <div class="header">
                <div class="logo">🔒</div>
                <h1>Middleware de Validação</h1>
                <p class="subtitle">Sistema de Gestão de Projetos - Metrô de São Paulo</p>
            </div>
            
            <div class="status-grid">
                <div class="status-card">
                    <div class="status-icon">✅</div>
                    <h3>Sistema Online</h3>
                    <p>Todos os serviços operacionais</p>
                </div>
                <div class="status-card">
                    <div class="status-icon">🔗</div>
                    <h3>APIs Integradas</h3>
                    <p>Conectado a 5 serviços</p>
                </div>
                <div class="status-card">
                    <div class="status-icon">📊</div>
                    <h3>Monitoramento Ativo</h3>
                    <p>Rastreabilidade completa</p>
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
            </div>

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

            <div class="footer">
                <p><strong>Middleware de Validação v1.0.0</strong></p>
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
                    const data = await response.json();
                    
                    const container = document.getElementById('integrations-container');
                    container.innerHTML = '';

                    for (const [name, status] of Object.entries(data.integrations)) {
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
                    document.getElementById('integrations-container').innerHTML = 
                        '<div class="no-data"><div class="no-data-icon"><i class="fas fa-exclamation-triangle"></i></div>Erro ao carregar integrações</div>';
                }
            }

            // ========== ESTATÍSTICAS ==========
            async function loadStats() {
                try {
                    const response = await fetch('/monitoring/stats');
                    const data = await response.json();
                    
                    const summary = data.summary || {};
                    const topUsers = data.top_users || [];
                    
                    // Atualiza cards de estatísticas
                    document.getElementById('stat-total-logs').textContent = summary.total_logs || 0;
                    document.getElementById('stat-total-incidents').textContent = summary.total_incidents || 0;
                    document.getElementById('stat-unique-users').textContent = topUsers.length || 0;
                    
                    const errorRate = summary.error_rate_percent || 0;
                    const errorElement = document.getElementById('stat-error-rate');
                    errorElement.textContent = errorRate.toFixed(1) + '%';
                    
                } catch (error) {
                    console.error('Erro ao carregar estatísticas:', error);
                }
            }

            // ========== LOGS ==========
            async function loadLogs() {
                try {
                    const response = await fetch('/monitoring/logs?limit=50');
                    const data = await response.json();
                    allLogs = data.logs || [];
                    allLogsWithIndex = [...allLogs]; // Cria cópia para indexação
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
                    const eventType = log.event_type || 'unknown';
                    const userId = log.user_id || 'N/A';
                    const status = log.status || 'unknown';
                    const projectId = log.project_id || null;
                    const resourceId = log.resource_id || null;
                    const traceId = log.trace_id || null;
                    
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
                    if (resourceId) metaItems.push(`<span class="log-meta-item"><i class="fas fa-link"></i>${resourceId}</span>`);
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

            // ========== CARREGAR TUDO ==========
            async function loadAllData() {
                updateTimestamp();
                await Promise.all([
                    loadIntegrations(),
                    loadStats(),
                    loadLogs(),
                    loadIncidents()
                ]);
            }

            // Auto-refresh a cada 15 segundos
            setInterval(loadAllData, 15000);

            // Carregar dados iniciais
            loadAllData();
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
