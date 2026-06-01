# ex_021_enumerate.py
"""
ARQUIVO:
DESCRIÇÃO: Demonstração de todas as 71 funções built-in do Python 3.11.9
Funções Built-in (Embutidas)
EXECUÇÃO: Rode diretamente no PyCharm 2024.1.1 Community Edition
AUTOR: Rogerio V. Mota
"""

print("---------------------------------------------------------------------------------")
print('EXEMPLO - 21. enumerate() - Retorna índice e valor de um iterável')
print("=================================================================================\n")

lista = ["a", "b", "c"]
print("Lista: {lista}")
print("=================================================================================\n")
print("enumerate(lista):")
print("=================================================================================\n")
for i, valor in enumerate(lista):
    print(f"  {i} -> {valor}")
    print("=================================================================================\n")