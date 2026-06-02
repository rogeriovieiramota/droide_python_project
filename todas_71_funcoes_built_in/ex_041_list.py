"""
ARQUIVO:
DESCRIÇÃO: Demonstração de todas as 71 funções built-in do Python 3.11.9
Funções Built-in (Embutidas)
EXECUÇÃO: Rode diretamente no PyCharm 2024.1.1 Community Edition
AUTOR: Rogerio V. Mota
"""


# ex_041_list.py
print("---------------------------------------------------------------------------------")
print('EXEMPLO - 41. list() - Cria lista (converte iterável para lista)')
print("=================================================================================\n")

print(f"list() = {list()}")
print("=================================================================================\n")
print(f"list('abc') = {list('abc')}")
print("=================================================================================\n")
print(f"list((1,2,3)) = {list((1,2,3))}")
print("=================================================================================\n")
print(f"list([1,2,3,4]) = {list([1,2,3,4])}")

"""
📊 TABELA COMPARATIVA DETALHADA
Característica	                list((1,2,3))	            list([1,2,3,4])
Entrada	Tupla:                  (1, 2, 3)	                Lista: [1, 2, 3, 4]
O que a função list() faz?	    Converte a tupla em lista	Converte a lista em lista (cria uma cópia)
Resultado	                    [1, 2, 3]	                [1, 2, 3, 4]
Tipo do resultado	            list	                    list
Número de elementos	            3 elementos	                4 elementos
"""