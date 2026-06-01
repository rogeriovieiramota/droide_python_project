# ex_024_filter.py
"""
ARQUIVO:
DESCRIÇÃO: Demonstração de todas as 71 funções built-in do Python 3.11.9
Funções Built-in (Embutidas)
EXECUÇÃO: Rode diretamente no PyCharm 2024.1.1 Community Edition
AUTOR: Rogerio V. Mota
"""

print("---------------------------------------------------------------------------------")
print('EXEMPLO - 24. filter() - Filtra elementos que atendem a uma condição')
print("=================================================================================\n")

numeros = [1, 2, 3, 4, 5, 6]
print(f"Lista original: {numeros}")
print("=================================================================================\n")
pares = filter(lambda x: x % 2 == 0, numeros)
print(f"Filtrando pares: {list(pares)}")
print("=================================================================================\n")

def maior_que_3(x):
    return x > 3
print(f"Filtrando > 3: {list(filter(maior_que_3, numeros))}")
print("=================================================================================\n")