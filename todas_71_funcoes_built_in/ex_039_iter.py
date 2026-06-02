"""
ARQUIVO:
DESCRIÇÃO: Demonstração de todas as 71 funções built-in do Python 3.11.9
Funções Built-in (Embutidas)
EXECUÇÃO: Rode diretamente no PyCharm 2024.1.1 Community Edition
AUTOR: Rogerio V. Mota
"""

# ex_039_iter.py
print("---------------------------------------------------------------------------------")
print('EXEMPLO - 39. iter() - Retorna iterador de um objeto')
print("=================================================================================\n")

lista = [1, 2, 3]
it = iter(lista)
print(f"iter([1,2,3]) = {it}")
print("=================================================================================\n")
print(f"next(it) = {next(it)}")
print("=================================================================================\n")
print(f"next(it) = {next(it)}")
print("=================================================================================\n")
print(f"next(it) = {next(it)}")
print("=================================================================================\n")

"""
# Visualização do iterador:
lista = [1, 2, 3]
         ↑  ↑  ↑
         
it = iter(lista)
# O iterador começa APONTANDO para a posição 0
# Ele "lembra" onde está

"""

# SEM iterador (lista comum)
lista_gigante = [1, 2, 3, ..., 1_000_000]  # 1 MILHÃO de números
# Consome MUITA memória!

# COM iterador (economiza memória)
def gerador_numeros():
    for i in range(1_000_000):
        yield i  # Só gera UM número por vez

it = gerador_numeros()  # Memória mínima!
# Cada next(it) gera um número sem carregar todos na memória