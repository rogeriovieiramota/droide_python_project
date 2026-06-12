# ex_068_type.py

"""
ARQUIVO:
DESCRIÇÃO: Demonstração de todas as 71 funções built-in do Python 3.11.9
EXECUÇÃO: Rode diretamente no PyCharm 2024.1.1 Community Edition
Funções Built-in (Embutidas)
AUTOR: Rogerio V. Mota
"""

print("---------------------------------------------------------------------------------")
print('EXEMPLO - 68. type() - Retorna tipo do objeto OU cria nova classe dinâmica')
print("---------------------------------------------------------------------------------")

print("=================================================================================\n")
print(f"type(10) = {type(10)}")
print("=================================================================================\n")
print(f"type('abc') = {type('abc')}")
print("=================================================================================\n")
print(f"type([1,2]) = {type([1,2])}")
print("=================================================================================\n")

# Criando classe dinamicamente
MinhaClasse = type("MinhaClasse", (), {"x": 10})
print("=================================================================================\n")
print(f"Classe criada dinamicamente: {MinhaClasse}")
print("=================================================================================\n")
print(f"MinhaClasse.x = {MinhaClasse.x}")
print("=================================================================================\n")