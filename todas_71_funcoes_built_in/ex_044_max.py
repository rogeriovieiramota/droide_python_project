"""
ARQUIVO:
DESCRIÇÃO: Demonstração de todas as 71 funções built-in do Python 3.11.9
Funções Built-in (Embutidas)
EXECUÇÃO: Rode diretamente no PyCharm 2024.1.1 Community Edition
AUTOR: Rogerio V. Mota
"""

# ex_044_max.py
print("---------------------------------------------------------------------------------")
print('EXEMPLO - 44. max() - Retorna maior valor (ou máximo por critério)')
print("=================================================================================\n")

print(f"max([1, 5, 2, 8]) = {max([1, 5, 2, 8])}")
print("=================================================================================\n")
print(f"max(10, 20, 5) = {max(10, 20, 5)}")
print("=================================================================================\n")
print(f"max('abc') = {max('abc')}") # Retorna: 'c' (o maior caractere, baseado na ordem Unicode)
print("=================================================================================\n")

dados = {'a': 10, 'b': 20, 'c': 5}
print(f"max(dados) = {max(dados)}")  # Retorna max de um dicionário: 'c' (a última chave alfabeticamente)
print("=================================================================================\n")
print(f"max(dados.values()) = {max(dados.values())}")  # Retorna: 20 (o maior valor)
print("=================================================================================\n")