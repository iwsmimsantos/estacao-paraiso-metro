"""
Testes básicos para validar o funcionamento das APIs mockadas.
Execute com: pytest test_apis.py (requer pytest instalado: pip install pytest)
Ou simplesmente: python test_apis.py
"""

import sys
from fastapi.testclient import TestClient

# Importa a aplicação FastAPI
from main import app

# Cria cliente de testes
client = TestClient(app)


def test_health_check():
    """Testa o endpoint de health check."""
    response = client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"
    assert "sharepoint" in data["services"]
    print("✓ Health check OK")


def test_sharepoint_sites():
    """Testa listagem de sites do SharePoint."""
    response = client.get("/sharepoint/sites?page=1&page_size=5")
    assert response.status_code == 200
    data = response.json()
    assert data["service"] == "sharepoint"
    assert "sites" in data["data"]
    assert "meta" in data
    assert "security_context" in data["meta"]
    print("✓ SharePoint sites OK")


def test_miro_boards():
    """Testa listagem de boards do Miro."""
    response = client.get("/miro/boards?page=1&page_size=5")
    assert response.status_code == 200
    data = response.json()
    assert data["service"] == "miro"
    assert "boards" in data["data"]
    assert "traceability" in data["meta"]
    print("✓ Miro boards OK")


def test_copilot_sessions():
    """Testa listagem de sessões do Copilot."""
    response = client.get("/copilot/sessions?page=1&page_size=5")
    assert response.status_code == 200
    data = response.json()
    assert data["service"] == "copilot"
    assert "sessions" in data["data"]
    assert "performance" in data["meta"]
    print("✓ Copilot sessions OK")


def test_office_documents():
    """Testa listagem de documentos do Office."""
    response = client.get("/office/documents?page=1&page_size=5")
    assert response.status_code == 200
    data = response.json()
    assert data["service"] == "office"
    assert "documents" in data["data"]
    print("✓ Office documents OK")


def test_sentinel_incidents():
    """Testa listagem de incidentes do Sentinel."""
    response = client.get("/sentinel/incidents?page=1&page_size=5")
    assert response.status_code == 200
    data = response.json()
    assert data["service"] == "sentinel"
    assert "incidents" in data["data"]
    print("✓ Sentinel incidents OK")


def test_correlation_id():
    """Testa se o correlation_id é preservado entre requisições."""
    correlation_id = "test-correlation-123"
    
    # Requisição 1
    response1 = client.get(
        "/sharepoint/sites",
        headers={"X-Correlation-Id": correlation_id}
    )
    assert response1.status_code == 200
    data1 = response1.json()
    assert data1["correlation_id"] == correlation_id
    
    # Requisição 2
    response2 = client.get(
        "/sentinel/alerts",
        headers={"X-Correlation-Id": correlation_id}
    )
    assert response2.status_code == 200
    data2 = response2.json()
    assert data2["correlation_id"] == correlation_id
    
    print("✓ Correlation ID preservado entre requisições")


def test_pagination():
    """Testa paginação nas respostas."""
    response = client.get("/sharepoint/sites?page=1&page_size=10")
    assert response.status_code == 200
    data = response.json()
    
    meta = data["meta"]
    assert meta["page"] == 1
    assert meta["page_size"] == 10
    assert "total_items" in meta
    assert meta["total_items"] >= 0
    print("✓ Paginação funcionando corretamente")


def test_user_filtering():
    """Testa filtro por usuário."""
    # Lista todos os sites
    response_all = client.get("/sharepoint/sites?page=1&page_size=100")
    data_all = response_all.json()
    
    if data_all["data"]["sites"]:
        # Pega o user_id do primeiro site
        user_id = data_all["data"]["sites"][0]["owner_user_id"]
        
        # Filtra por esse usuário
        response_filtered = client.get(f"/sharepoint/sites?user_id={user_id}")
        data_filtered = response_filtered.json()
        
        # Verifica se todos os sites retornados são desse usuário
        for site in data_filtered["data"]["sites"]:
            assert site["owner_user_id"] == user_id
        
        print(f"✓ Filtro por usuário OK (user_id={user_id})")


def test_response_structure():
    """Testa estrutura do envelope de resposta padrão."""
    response = client.get("/sharepoint/sites?page=1&page_size=5")
    assert response.status_code == 200
    data = response.json()
    
    # Verifica campos obrigatórios no envelope
    required_fields = ["request_id", "service", "timestamp_utc", "correlation_id", "data", "meta"]
    for field in required_fields:
        assert field in data, f"Campo obrigatório '{field}' não encontrado"
    
    # Verifica estrutura do meta
    meta = data["meta"]
    assert "security_context" in meta
    assert "traceability" in meta
    assert "performance" in meta
    
    # Verifica security_context
    sec = meta["security_context"]
    assert "user_id" in sec
    assert "tenant_id" in sec
    assert "mfa_enabled" in sec
    
    # Verifica traceability
    trace = meta["traceability"]
    assert "trace_id" in trace
    assert "span_id" in trace
    
    # Verifica performance
    perf = meta["performance"]
    assert "processing_time_ms" in perf
    assert "items_in_response" in perf
    
    print("✓ Estrutura do envelope de resposta OK")


def run_all_tests():
    """Executa todos os testes."""
    print("\n" + "=" * 60)
    print("EXECUTANDO TESTES DAS APIs MOCKADAS")
    print("=" * 60 + "\n")
    
    tests = [
        test_health_check,
        test_sharepoint_sites,
        test_miro_boards,
        test_copilot_sessions,
        test_office_documents,
        test_sentinel_incidents,
        test_correlation_id,
        test_pagination,
        test_user_filtering,
        test_response_structure
    ]
    
    passed = 0
    failed = 0
    
    for test in tests:
        try:
            test()
            passed += 1
        except AssertionError as e:
            print(f"❌ {test.__name__} falhou: {e}")
            failed += 1
        except Exception as e:
            print(f"❌ {test.__name__} erro: {e}")
            failed += 1
    
    print("\n" + "=" * 60)
    print(f"RESULTADOS: {passed} passou, {failed} falhou")
    print("=" * 60 + "\n")
    
    return failed == 0


if __name__ == "__main__":
    success = run_all_tests()
    sys.exit(0 if success else 1)

