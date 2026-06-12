"""
ARQUIVO:
DESCRIÇÃO: Demonstração de todas as 71 funções built-in do Python 3.11.9
EXECUÇÃO: Rode diretamente no PyCharm 2024.1.1 Community Edition
Funções Built-in (Embutidas)
AUTOR: Rogerio V. Mota
"""

# ex_070_zip.py

print("---------------------------------------------------------------------------------")
print('EXEMPLO - 70. zip() - Agrupa elementos de múltiplos iteráveis em tuplas')
print("---------------------------------------------------------------------------------")

nomes = ["Ana", "João", "Maria"]
idades = [25, 30, 28]
print("=================================================================================\n")
print(f"nomes = {nomes}")
print("=================================================================================\n")
print(f"idades = {idades}")
print("=================================================================================\n")
print(f"zip(nomes, idades) = {list(zip(nomes, idades))}")
print("=================================================================================\n")

print("Loop com zip:")
for nome, idade in zip(nomes, idades):
    print(f"  {nome} tem {idade} anos")