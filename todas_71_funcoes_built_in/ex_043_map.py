"""
ARQUIVO:
DESCRIÇÃO: Demonstração de todas as 71 funções built-in do Python 3.11.9
Funções Built-in (Embutidas)
EXECUÇÃO: Rode diretamente no PyCharm 2024.1.1 Community Edition
AUTOR: Rogerio V. Mota
"""

# ex_043_map.py

print("---------------------------------------------------------------------------------")
print('EXEMPLO - 43. map() - Aplica função a cada elemento do iterável')
print("=================================================================================\n")

numeros = [1, 2, 3, 4]
print(f"Original: {numeros}")
dobro = map(lambda x: x * 2, numeros)
print(f"Dobro: {list(dobro)}")

def quadrado(x):
    return x ** 2
print("=================================================================================\n")
print(f"Quadrado: {list(map(quadrado, numeros))}")