"""
ARQUIVO:
DESCRIÇÃO: Demonstração de todas as 71 funções built-in do Python 3.11.9
Funções Built-in (Embutidas)
EXECUÇÃO: Rode diretamente no PyCharm 2024.1.1 Community Edition
AUTOR: Rogerio V. Mota
"""

# ex_012_callable.py
print("---------------------------------------------------------------------------------")
print('EXEMPLO - 12. callable() - Verifica se objeto pode ser chamado como função')
print("=================================================================================\n")

def minha_funcao():
    pass

print(f"callable(print) = {callable(print)}")
print("=================================================================================\n")
print(f"callable(len) = {callable(len)}")
print("=================================================================================\n")
print(f"callable(10) = {callable(10)}")
print("=================================================================================\n")
print(f"callable('abc') = {callable('abc')}")
print("=================================================================================\n")
print(f"callable(minha_funcao) = {callable(minha_funcao)}")
print("=================================================================================\n")