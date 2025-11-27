"""
Exemplos de requisições para as APIs mockadas.
Demonstra como consumir os endpoints e trabalhar com rastreabilidade.
"""

import requests
from uuid import uuid4

# URL base das APIs
BASE_URL = "http://localhost:8000"

# Gera um correlation_id único para rastrear requisições relacionadas
correlation_id = str(uuid4())

print("=" * 60)
print("EXEMPLOS DE REQUISIÇÕES - APIs Mockadas")
print("=" * 60)
print(f"\nCorrelation ID usado: {correlation_id}\n")


def example_sharepoint():
    """Exemplo de uso da API do SharePoint."""
    print("\n📁 SHAREPOINT - Lista de Sites")
    print("-" * 60)
    
    response = requests.get(
        f"{BASE_URL}/sharepoint/sites",
        params={
            "page": 1,
            "page_size": 5,
            "tenant_id": "tenant-01"
        },
        headers={
            "X-Correlation-Id": correlation_id
        }
    )
    
    if response.status_code == 200:
        data = response.json()
        print(f"✓ Request ID: {data['request_id']}")
        print(f"✓ Service: {data['service']}")
        print(f"✓ Correlation ID: {data['correlation_id']}")
        print(f"✓ Sites encontrados: {data['meta']['total_items']}")
        print(f"✓ Processamento: {data['meta']['performance']['processing_time_ms']}ms")
        
        if data['data']['sites']:
            print(f"\nPrimeiro site:")
            site = data['data']['sites'][0]
            print(f"  - ID: {site['site_id']}")
            print(f"  - Nome: {site['name']}")
            print(f"  - Proprietário: {site['owner_user_id']}")
    else:
        print(f"❌ Erro: {response.status_code}")


def example_miro():
    """Exemplo de uso da API do Miro."""
    print("\n🎨 MIRO - Lista de Boards")
    print("-" * 60)
    
    response = requests.get(
        f"{BASE_URL}/miro/boards",
        params={
            "page": 1,
            "page_size": 3
        },
        headers={
            "X-Correlation-Id": correlation_id
        }
    )
    
    if response.status_code == 200:
        data = response.json()
        print(f"✓ Boards encontrados: {data['meta']['total_items']}")
        print(f"✓ Trace ID: {data['meta']['traceability']['trace_id']}")
        
        for board in data['data']['boards'][:3]:
            print(f"\n  Board: {board['name']}")
            print(f"    - Nível de acesso: {board['access_level']}")
            print(f"    - Última atividade: {board['last_activity_utc']}")
    else:
        print(f"❌ Erro: {response.status_code}")


def example_copilot():
    """Exemplo de uso da API do Copilot."""
    print("\n🤖 COPILOT - Sessões de Usuário")
    print("-" * 60)
    
    response = requests.get(
        f"{BASE_URL}/copilot/sessions",
        params={
            "user_id": "u002",
            "page": 1,
            "page_size": 3
        },
        headers={
            "X-Correlation-Id": correlation_id
        }
    )
    
    if response.status_code == 200:
        data = response.json()
        print(f"✓ Sessões do usuário u002: {len(data['data']['sessions'])}")
        print(f"✓ Contexto de segurança:")
        sec = data['meta']['security_context']
        print(f"  - User ID: {sec['user_id']}")
        print(f"  - MFA Habilitado: {sec['mfa_enabled']}")
        print(f"  - Scopes: {', '.join(sec['scopes'])}")
        
        for session in data['data']['sessions'][:2]:
            print(f"\n  Sessão: {session['session_id']}")
            print(f"    - App: {session['source_app']}")
            print(f"    - Prompts: {session['total_prompts']}")
            print(f"    - Tokens: {session['total_tokens_input']} in / {session['total_tokens_output']} out")
    else:
        print(f"❌ Erro: {response.status_code}")


def example_office():
    """Exemplo de uso da API do Office."""
    print("\n📄 OFFICE - Documentos")
    print("-" * 60)
    
    response = requests.get(
        f"{BASE_URL}/office/documents",
        params={
            "page": 1,
            "page_size": 5
        },
        headers={
            "X-Correlation-Id": correlation_id
        }
    )
    
    if response.status_code == 200:
        data = response.json()
        print(f"✓ Total de documentos: {data['meta']['total_items']}")
        
        for doc in data['data']['documents'][:3]:
            print(f"\n  Documento: {doc['name']}")
            print(f"    - Tipo: {doc['type']}")
            print(f"    - Sensibilidade: {doc['sensitivity_label']}")
            print(f"    - Compartilhado externamente: {doc['is_shared_externally']}")
    else:
        print(f"❌ Erro: {response.status_code}")


def example_sentinel():
    """Exemplo de uso da API do Sentinel."""
    print("\n🛡️ SENTINEL - Alertas de Segurança")
    print("-" * 60)
    
    response = requests.get(
        f"{BASE_URL}/sentinel/alerts",
        params={
            "page": 1,
            "page_size": 5,
            "source_service": "sharepoint"
        },
        headers={
            "X-Correlation-Id": correlation_id
        }
    )
    
    if response.status_code == 200:
        data = response.json()
        print(f"✓ Alertas do SharePoint: {len(data['data']['alerts'])}")
        
        for alert in data['data']['alerts'][:3]:
            print(f"\n  Alerta: {alert['alert_id']}")
            print(f"    - Descrição: {alert['description']}")
            print(f"    - Nível de risco: {alert['risk_level']}")
            print(f"    - Usuário: {alert['user_id']}")
            print(f"    - Correlation ID: {alert['correlation_id']}")
    else:
        print(f"❌ Erro: {response.status_code}")


def example_health_check():
    """Exemplo de health check."""
    print("\n❤️ HEALTH CHECK")
    print("-" * 60)
    
    response = requests.get(f"{BASE_URL}/health")
    
    if response.status_code == 200:
        data = response.json()
        print(f"✓ Status: {data['status']}")
        print(f"✓ Versão: {data['version']}")
        print(f"✓ Serviços: {', '.join(data['services'])}")
    else:
        print(f"❌ Erro: {response.status_code}")


if __name__ == "__main__":
    try:
        # Executa todos os exemplos
        example_health_check()
        example_sharepoint()
        example_miro()
        example_copilot()
        example_office()
        example_sentinel()
        
        print("\n" + "=" * 60)
        print("✓ Todos os exemplos executados com sucesso!")
        print("=" * 60)
        
    except requests.exceptions.ConnectionError:
        print("\n❌ Erro: Não foi possível conectar às APIs.")
        print("   Certifique-se de que o servidor está rodando em http://localhost:8000")
        print("   Execute: python main.py")
    except Exception as e:
        print(f"\n❌ Erro inesperado: {e}")

