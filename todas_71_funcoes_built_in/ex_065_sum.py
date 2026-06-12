# ex_065_sum.py

"""
ARQUIVO:
DESCRIÇÃO: Demonstração de todas as 71 funções built-in do Python 3.11.9
EXECUÇÃO: Rode diretamente no PyCharm 2024.1.1 Community Edition
Funções Built-in (Embutidas)
AUTOR: Rogerio V. Mota

Em Python, colchetes definem listas e parênteses definem tuplas.

"""

print("---------------------------------------------------------------------------------")
print('EXEMPLO - 65. sum() - Soma todos os elementos do iterável')
print("---------------------------------------------------------------------------------")

print("=================================================================================\n")
print(f"sum([1,2,3,4]) = {sum([1,2,3,4])}")
print("=================================================================================\n")
print(f"sum([1,2,3], 10) = {sum([1,2,3], 10)}")
print("=================================================================================\n")
t = tuple([1, 2, 3])      # tupla de números
print("t =", t)
print("sum(t) =", sum(t))  # soma dos elementos

print("=================================================================================\n")
lista = [1, 2, 3, 4]
print("lista",lista)
print("sum(lista) =", sum(lista))  # soma dos elementos
print("=================================================================================\n")
tupla = (1, 2, 3, 4)
print("tupla",tupla)
print("sum(tupla) =", sum(tupla))  # soma dos elementos
print("=================================================================================\n")