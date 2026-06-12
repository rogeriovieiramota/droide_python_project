"""
ARQUIVO:

DESCRIÇÃO: Demonstração de todas as 71 funções built-in do Python 3.11.9
Funções Built-in (Embutidas)
EXECUÇÃO: Rode diretamente no PyCharm 2024.1.1 Community Edition
AUTOR: Rogerio V. Mota
"""

# ex_057_reversed.py
print("---------------------------------------------------------------------------------")
print('EXEMPLO - 57. reversed() - Retorna iterador reverso da sequência')
print("---------------------------------------------------------------------------------")

print("=================================================================================\n")
print(f"list(reversed([1,2,3])) = {list(reversed([1,2,3]))}")
print("=================================================================================\n")
print("for i in reversed('abc'):", end=" ")
print("=================================================================================\n")
for i in reversed('abc'):
    print(i, end=" ")
print()
print("=================================================================================\n")

