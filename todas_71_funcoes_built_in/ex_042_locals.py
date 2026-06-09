"""
ARQUIVO:
DESCRIÇÃO: Demonstração de todas as 71 funções built-in do Python 3.11.9
Funções Built-in (Embutidas)
EXECUÇÃO: Rode diretamente no PyCharm 2024.1.1 Community Edition
AUTOR: Rogerio V. Mota
"""

# ex_042_locals.py
print("---------------------------------------------------------------------------------")
print('EXEMPLO - 42. locals() - Retorna dicionário do escopo local atual')
print("=================================================================================\n")

def funcao():
    x = 10
    y = 20
    print("=================================================================================\n")
    print(f"Dentro da função, locals() = {locals()}")

funcao()