"""
Script de demonstração interativa do sistema RNF-03 Rastreabilidade
"""
import sys
import os
import time

# Adiciona o diretório pai ao path
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from models.log_models import SharePointChangeEvent
from services.correlation_service import correlation_service
from services.mock_data_generator import mock_generator
from storage.log_repository import log_repository


def print_header(title: str):
    """Imprime cabeçalho formatado"""
    print("\n" + "╔" + "="*78 + "╗")
    print(f"║  {title:^74}  ║")
    print("╚" + "="*78 + "╝\n")


def print_section(title: str):
    """Imprime seção formatada"""
    print("\n" + "-"*80)
    print(f"  {title}")
    print("-"*80)


def print_result(data: dict, indent: int = 2):
    """Imprime resultado formatado"""
    for key, value in data.items():
        if isinstance(value, dict):
            print(" " * indent + f"• {key}:")
            print_result(value, indent + 2)
        elif isinstance(value, list):
            print(" " * indent + f"• {key}: [{len(value)} itens]")
        else:
            print(" " * indent + f"• {key}: {value}")


def wait_for_user():
    """Aguarda usuário pressionar Enter"""
    input("\nPressione ENTER para continuar...")


def demo_cenario_1():
    """Demonstra Cenário 1: Bloqueio de mudança sem justificativa"""
    print_header("CENÁRIO 1: Bloqueio de Mudança Sem Justificativa")
    
    print("Contexto:")
    print("  Este cenário simula uma tentativa de alteração em um projeto")
    print("  do SharePoint SEM fornecer justificativa.")
    print("\n  Resultado esperado:")
    print("  • Mudança deve ser BLOQUEADA")
    print("  • Evento de bloqueio registrado no Sentinel")
    print("  • Alerta crítico gerado")
    print("  • Notificação enviada via Teams (simulado)")
    
    wait_for_user()
    
    print_section("Executando simulação...")
    
    # Gera dados mockados
    user = mock_generator.generate_user()
    project_id = mock_generator.generate_project_id()
    
    print(f"\nUsuário: {user}")
    print(f"Projeto: {project_id}")
    print("Campo a alterar: status")
    print("Valor antigo: 'Em Andamento'")
    print("Valor novo: 'Concluído'")
    print("Justificativa: (VAZIA) ❌")
    
    # Cria evento sem justificativa
    event = SharePointChangeEvent(
        user=user,
        project_id=project_id,
        change_type="atualizacao",
        justification=None,
        field_changed="status",
        old_value="Em Andamento",
        new_value="Concluído",
        source="SharePoint"
    )
    
    print("\n⏳ Processando evento através do middleware...")
    time.sleep(1)
    
    # Processa
    result = correlation_service.process_sharepoint_event(event, scenario="cenario_1")
    
    print("\n✅ Resultado:")
    print_result(result)
    
    if result.get("blocked"):
        print("\n🚫 MUDANÇA BLOQUEADA COM SUCESSO!")
        print("   O Power Automate impediu a atualização conforme esperado.")
    else:
        print("\n⚠️  ATENÇÃO: Mudança não foi bloqueada!")


def demo_cenario_2():
    """Demonstra Cenário 2: Registro automático da mudança"""
    print_header("CENÁRIO 2: Registro Automático da Mudança")
    
    print("Contexto:")
    print("  Este cenário simula uma alteração APROVADA com justificativa válida.")
    print("\n  Resultado esperado:")
    print("  • Mudança deve ser APROVADA")
    print("  • Registro criado na lista 'Histórico de Alterações'")
    print("  • Log enviado ao Sentinel com correlationId")
    print("  • Hash de integridade gerado")
    
    wait_for_user()
    
    print_section("Executando simulação...")
    
    # Gera dados mockados
    user = mock_generator.generate_user()
    project_id = mock_generator.generate_project_id()
    field, old_val, new_val = mock_generator.generate_field_change()
    justification = mock_generator.generate_justification(True)
    
    print(f"\nUsuário: {user}")
    print(f"Projeto: {project_id}")
    print(f"Campo a alterar: {field}")
    print(f"Valor antigo: '{old_val}'")
    print(f"Valor novo: '{new_val}'")
    print(f"Justificativa: '{justification}' ✅")
    
    # Cria evento com justificativa
    event = SharePointChangeEvent(
        user=user,
        project_id=project_id,
        change_type="atualizacao",
        justification=justification,
        field_changed=field,
        old_value=old_val,
        new_value=new_val,
        source="SharePoint"
    )
    
    print("\n⏳ Processando evento através do middleware...")
    time.sleep(1)
    
    # Processa
    result = correlation_service.process_sharepoint_event(event, scenario="cenario_2")
    
    print("\n✅ Resultado:")
    print_result(result)
    
    if result.get("success") and not result.get("blocked"):
        print("\n✅ MUDANÇA APROVADA E REGISTRADA COM SUCESSO!")
        print("   Todos os logs foram criados e correlacionados.")


def demo_cenario_3():
    """Demonstra Cenário 3: Validação de integridade"""
    print_header("CENÁRIO 3: Validação de Integridade e Consistência dos Logs")
    
    print("Contexto:")
    print("  Este cenário valida a integridade entre eventos do SharePoint")
    print("  e logs do Sentinel através de comparação de hashes.")
    print("\n  Resultado esperado:")
    print("  • Hashes devem ser comparados")
    print("  • Status de integridade deve ser determinado")
    print("  • Eventos devem ser correlacionados")
    
    wait_for_user()
    
    print_section("Executando simulação...")
    
    # Cria evento
    user = mock_generator.generate_user()
    project_id = mock_generator.generate_project_id()
    justification = mock_generator.generate_justification(True)
    
    event = SharePointChangeEvent(
        user=user,
        project_id=project_id,
        change_type="atualizacao",
        justification=justification,
        field_changed="orcamento",
        old_value="R$ 1.000.000,00",
        new_value="R$ 1.500.000,00",
        source="SharePoint"
    )
    
    print(f"\nUsuário: {user}")
    print(f"Projeto: {project_id}")
    
    print("\n⏳ Processando evento...")
    time.sleep(0.5)
    
    process_result = correlation_service.process_sharepoint_event(event, scenario="cenario_3")
    
    print("✅ Evento processado")
    
    print("\n⏳ Verificando integridade...")
    time.sleep(0.5)
    
    # Verifica integridade
    integrity_result = correlation_service.verify_integrity(
        sharepoint_event_id=process_result.get("sharepoint_event_id"),
        sentinel_log_id=process_result.get("sentinel_log_id")
    )
    
    print("\n✅ Resultado da Verificação:")
    print_result(integrity_result)
    
    if integrity_result.get("hash_comparison"):
        print("\n✅ INTEGRIDADE VERIFICADA COM SUCESSO!")
    else:
        print("\n⚠️  DIVERGÊNCIA DETECTADA!")


def demo_cenario_4():
    """Demonstra Cenário 4: Consulta e auditoria"""
    print_header("CENÁRIO 4: Consulta e Auditoria de Mudanças")
    
    print("Contexto:")
    print("  Este cenário demonstra a criação de uma trilha de auditoria")
    print("  completa, rastreando a mudança desde a origem até o destino.")
    print("\n  Resultado esperado:")
    print("  • Trilha de auditoria completa criada")
    print("  • Todos os eventos relacionados rastreados")
    print("  • Dados prontos para visualização no Power BI")
    
    wait_for_user()
    
    print_section("Executando simulação...")
    
    # Cria evento
    user = mock_generator.generate_user()
    project_id = mock_generator.generate_project_id()
    justification = mock_generator.generate_justification(True)
    
    event = SharePointChangeEvent(
        user=user,
        project_id=project_id,
        change_type="status_change",
        justification=justification,
        field_changed="fase",
        old_value="Planejamento",
        new_value="Execução",
        source="SharePoint"
    )
    
    print(f"\nUsuário: {user}")
    print(f"Projeto: {project_id}")
    print(f"Mudança: Fase 'Planejamento' → 'Execução'")
    
    print("\n⏳ Processando evento...")
    time.sleep(0.5)
    
    process_result = correlation_service.process_sharepoint_event(event, scenario="cenario_4")
    correlation_id = process_result.get("correlation_id")
    
    print(f"✅ Evento processado (Correlation ID: {correlation_id})")
    
    print("\n⏳ Criando trilha de auditoria...")
    time.sleep(0.5)
    
    # Cria audit trail
    audit_result = correlation_service.create_audit_trail(correlation_id)
    
    print("\n✅ Trilha de Auditoria:")
    print_result(audit_result)
    
    # Recupera todos os eventos relacionados
    related = log_repository.get_by_correlation_id(correlation_id)
    
    print("\n📊 Eventos Rastreados:")
    print(f"  • Eventos SharePoint: {len(related.get('sharepoint_events', []))}")
    print(f"  • Logs Sentinel: {len(related.get('sentinel_logs', []))}")
    print(f"  • Logs Correlacionados: {len(related.get('correlated_logs', []))}")
    print(f"  • Histórico de Alterações: {len(related.get('historico_alteracoes', []))}")
    
    print("\n✅ TRILHA DE AUDITORIA COMPLETA CRIADA!")
    print("   Pronta para visualização no Power BI.")


def demo_cenario_5():
    """Demonstra Cenário 5: Alerta de tentativas inválidas"""
    print_header("CENÁRIO 5: Alerta de Tentativas Inválidas")
    
    print("Contexto:")
    print("  Este cenário simula a detecção de uma tentativa de alteração")
    print("  FORA DO FLUXO autorizado, como acesso direto ao banco de dados.")
    print("\n  Resultado esperado:")
    print("  • Alerta CRÍTICO gerado no Sentinel")
    print("  • Notificação enviada via Teams")
    print("  • Log de tentativa inválida criado")
    print("  • Ação recomendada fornecida")
    
    wait_for_user()
    
    print_section("Executando simulação...")
    
    # Gera dados mockados
    user = mock_generator.generate_user()
    project_id = mock_generator.generate_project_id()
    reason = "Tentativa de alteração direta no banco de dados, contornando o fluxo do Power Automate"
    
    print(f"\n🚨 TENTATIVA SUSPEITA DETECTADA!")
    print(f"Usuário: {user}")
    print(f"Projeto: {project_id}")
    print(f"Motivo: {reason}")
    
    print("\n⏳ Gerando alerta no Sentinel...")
    time.sleep(1)
    
    # Gera alerta
    result = correlation_service.generate_alert_for_invalid_attempt(
        user=user,
        project_id=project_id,
        reason=reason
    )
    
    print("\n🚨 ALERTA CRÍTICO GERADO!")
    print_result(result)
    
    # Recupera alerta
    alertas = log_repository.get_alertas({"alert_id": result.get("alert_id")})
    
    if alertas:
        alerta = alertas[0]
        print("\n📧 Notificação Teams (Simulado):")
        print(f"  Título: {alerta.get('title')}")
        print(f"  Severidade: {alerta.get('severity').upper()}")
        print(f"  Descrição: {alerta.get('description')}")
        print(f"  Ação Recomendada: {alerta.get('recommended_action')}")
    
    print("\n✅ ALERTA E NOTIFICAÇÃO ENVIADOS COM SUCESSO!")


def demo_statistics():
    """Mostra estatísticas do sistema"""
    print_header("ESTATÍSTICAS DO SISTEMA")
    
    stats = log_repository.get_statistics()
    
    print("📊 Total de Registros:")
    print_result(stats)
    
    # Estatísticas de alertas por severidade
    alertas = log_repository.get_alertas()
    
    if alertas:
        print("\n🚨 Alertas por Severidade:")
        by_severity = {}
        for alerta in alertas:
            sev = alerta.get("severity", "unknown")
            by_severity[sev] = by_severity.get(sev, 0) + 1
        
        for severity, count in sorted(by_severity.items()):
            print(f"  • {severity}: {count}")
    
    # Estatísticas de logs por tipo
    logs = log_repository.get_sentinel_logs()
    
    if logs:
        print("\n📝 Logs por Tipo de Evento:")
        by_type = {}
        for log in logs:
            event_type = log.get("event_type", "unknown")
            by_type[event_type] = by_type.get(event_type, 0) + 1
        
        for event_type, count in sorted(by_type.items()):
            print(f"  • {event_type}: {count}")
    
    # Estatísticas de integridade
    correlated = log_repository.get_correlated_logs()
    
    if correlated:
        print("\n✓ Status de Integridade:")
        by_status = {}
        for log in correlated:
            status = log.get("integrity_status", "unknown")
            by_status[status] = by_status.get(status, 0) + 1
        
        for status, count in sorted(by_status.items()):
            print(f"  • {status}: {count}")


def main_menu():
    """Menu principal da demonstração"""
    while True:
        print_header("DEMONSTRAÇÃO RNF-03 RASTREABILIDADE")
        
        print("Escolha um cenário para demonstração:\n")
        print("  1. Cenário 1 - Bloqueio de mudança sem justificativa")
        print("  2. Cenário 2 - Registro automático da mudança")
        print("  3. Cenário 3 - Validação de integridade e consistência dos logs")
        print("  4. Cenário 4 - Consulta e auditoria de mudanças")
        print("  5. Cenário 5 - Alerta de tentativas inválidas")
        print("  6. Executar TODOS os cenários")
        print("  7. Ver estatísticas do sistema")
        print("  8. Limpar todos os dados")
        print("  0. Sair")
        
        choice = input("\nEscolha uma opção: ").strip()
        
        if choice == "1":
            demo_cenario_1()
            wait_for_user()
        elif choice == "2":
            demo_cenario_2()
            wait_for_user()
        elif choice == "3":
            demo_cenario_3()
            wait_for_user()
        elif choice == "4":
            demo_cenario_4()
            wait_for_user()
        elif choice == "5":
            demo_cenario_5()
            wait_for_user()
        elif choice == "6":
            demo_cenario_1()
            time.sleep(1)
            demo_cenario_2()
            time.sleep(1)
            demo_cenario_3()
            time.sleep(1)
            demo_cenario_4()
            time.sleep(1)
            demo_cenario_5()
            wait_for_user()
        elif choice == "7":
            demo_statistics()
            wait_for_user()
        elif choice == "8":
            print("\n⚠️  Limpando todos os dados...")
            log_repository.clear_all()
            print("✅ Dados limpos com sucesso!")
            time.sleep(1)
        elif choice == "0":
            print("\n👋 Encerrando demonstração. Até logo!")
            break
        else:
            print("\n❌ Opção inválida. Tente novamente.")
            time.sleep(1)


if __name__ == "__main__":
    main_menu()

