"""
Script para executar testes com output limpo e formatado
Uso: python executar_testes.py
"""
import subprocess
import sys

def main():
    print("\n" + "="*50)
    print("  EXECUTANDO TESTES DO MIDDLEWARE")
    print("="*50)
    print("\nExecutando... (aguarde)")
    
    # Executar pytest duas vezes: uma para listar testes, outra para resultados
    # Primeiro: listar todos os testes
    list_result = subprocess.run(
        ["pytest", "../Testes-Automatizados", "--collect-only", "-v"],
        capture_output=True,
        text=True,
        encoding='utf-8',
        errors='ignore'
    )
    
    # Segundo: executar testes
    result = subprocess.run(
        ["pytest", "--disable-warnings", "-p", "no:warnings", "-v"],
        capture_output=True,
        text=True,
        encoding='utf-8',
        errors='ignore'
    )
    
    # Processar lista de testes
    all_tests = []
    import re
    for line in list_result.stdout.split('\n'):
        if '<Function test_' in line:
            match = re.search(r'<Function (test_\w+)>', line)
            if match:
                all_tests.append(match.group(1))
    
    # Processar resultado da execução
    output = result.stdout + result.stderr
    lines = [l for l in output.split('\n') if l.strip()]
    
    # Coletar testes falhados
    failed_tests = []
    for line in lines:
        if 'FAILED' in line and '::' in line:
            match = re.search(r'::(test_\w+)', line)
            if match:
                failed_tests.append(match.group(1))
    
    # Testes passados = todos - falhados
    passed_tests = [t for t in all_tests if t not in failed_tests]
    
    passed = len(passed_tests)
    failed = len(failed_tests)
    total = passed + failed
    
    if total > 0:
        print(f"\n{'-'*50}")
        print(f"RESULTADOS:")
        print(f"  Total: {total} testes")
        print(f"  Aprovados: {passed}")
        print(f"  Reprovados: {failed}")
        
        percentage = round((passed / total) * 100, 1)
        print(f"\n  Taxa de sucesso: {percentage}%")
        print(f"{'-'*50}")
        
        # Mostrar testes que passaram
        if passed > 0:
            print(f"\nTestes aprovados ({passed}):")
            for test in passed_tests:
                print(f"  ✓ {test}")
        
        # Mostrar testes que falharam
        if failed > 0:
            print(f"\nTestes com falha ({failed}):")
            for test in failed_tests:
                print(f"  ✗ {test}")
        
        print()
    else:
        print("\n⚠ Não foi possível processar os resultados.\n")
    
    sys.exit(result.returncode)

if __name__ == "__main__":
    main()
