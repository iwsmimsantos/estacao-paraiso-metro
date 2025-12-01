"""
Script auxiliar para executar testes do Middleware de Validação.
Pode ser executado diretamente: python run_tests.py
"""
import subprocess
import sys
import os
from pathlib import Path


def print_header(text):
    """Imprime cabeçalho formatado"""
    print("\n" + "=" * 60)
    print(f"  {text}")
    print("=" * 60 + "\n")


def run_command(cmd, description):
    """Executa comando e exibe resultado"""
    print(f"🚀 {description}...")
    print(f"   Comando: {' '.join(cmd)}\n")
    
    result = subprocess.run(cmd, capture_output=False)
    
    if result.returncode == 0:
        print(f"\n✅ {description} - SUCESSO")
    else:
        print(f"\n❌ {description} - FALHOU")
        sys.exit(result.returncode)
    
    return result.returncode


def main():
    """Menu principal de testes"""
    print_header("Testes Unitários - Middleware de Validação")
    
    # Verifica se está no diretório correto
    if not Path("tests").exists():
        print("❌ Erro: Diretório 'tests' não encontrado.")
        print("   Execute este script a partir do diretório Middleware-Validacao")
        sys.exit(1)
    
    print("Selecione o tipo de teste:")
    print("1. Todos os testes (45 testes)")
    print("2. RNF-01: Segurança (12 testes)")
    print("3. RNF-02: Escalabilidade (15 testes)")
    print("4. RNF-03: Rastreabilidade (18 testes)")
    print("5. Testes rápidos (excluir lentos)")
    print("6. Testes com coverage HTML")
    print("7. Executar teste específico")
    print("0. Sair")
    
    choice = input("\nDigite sua escolha (0-7): ").strip()
    
    commands = {
        "1": (
            ["pytest", "-v", "--cov=src", "--cov-report=term-missing"],
            "Executando TODOS os testes"
        ),
        "2": (
            ["pytest", "tests/unit/test_rnf01_seguranca.py", "-v", "--cov=src"],
            "Executando RNF-01 (Segurança)"
        ),
        "3": (
            ["pytest", "tests/unit/test_rnf02_escalabilidade.py", "-v", "--cov=src"],
            "Executando RNF-02 (Escalabilidade)"
        ),
        "4": (
            ["pytest", "tests/unit/test_rnf03_rastreabilidade.py", "-v", "--cov=src"],
            "Executando RNF-03 (Rastreabilidade)"
        ),
        "5": (
            ["pytest", "-v", "-m", "not slow", "--cov=src"],
            "Executando testes rápidos"
        ),
        "6": (
            ["pytest", "-v", "--cov=src", "--cov-report=html"],
            "Executando com relatório HTML"
        ),
    }
    
    if choice == "0":
        print("\n👋 Saindo...")
        sys.exit(0)
    
    elif choice == "7":
        test_path = input("\nDigite o caminho do teste (ex: tests/unit/test_rnf01_seguranca.py::TestRNF01Seguranca::test_cenario1): ")
        cmd = ["pytest", test_path, "-v", "-s"]
        description = f"Executando teste: {test_path}"
        run_command(cmd, description)
    
    elif choice in commands:
        cmd, description = commands[choice]
        run_command(cmd, description)
        
        if choice == "6":
            print("\n📊 Relatório HTML gerado em: htmlcov/index.html")
            open_report = input("Deseja abrir o relatório? (s/n): ").strip().lower()
            if open_report == "s":
                import webbrowser
                webbrowser.open("htmlcov/index.html")
    
    else:
        print("\n❌ Opção inválida")
        sys.exit(1)
    
    print_header("Execução concluída!")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n⚠️  Execução interrompida pelo usuário")
        sys.exit(130)
    except Exception as e:
        print(f"\n❌ Erro: {e}")
        sys.exit(1)
