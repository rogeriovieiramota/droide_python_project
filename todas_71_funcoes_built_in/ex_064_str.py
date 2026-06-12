"""
ARQUIVO:

DESCRIÇÃO: Demonstração de todas as 71 funções built-in do Python 3.11.9
Funções Built-in (Embutidas)
EXECUÇÃO: Rode diretamente no PyCharm 2024.1.1 Community Edition
AUTOR: Rogerio V. Mota
"""

# ex_064_str.py
print("---------------------------------------------------------------------------------")
print('EXEMPLO - 64. str() - Converte objeto para string')
print("---------------------------------------------------------------------------------")

print("=================================================================================\n")
print(f"str(123) = {str(123)}")
print(type(str(123)))
print(isinstance(str(123), str))
print("=================================================================================\n")
print(f"str(3.14) = {str(3.14)}")
print("=================================================================================\n")
print(f"str([1,2,3]) = {str([1,2,3])}")
print("=================================================================================\n")


# python
# converte e guarda em uma variável
valor = str(3.14)

# mostra valor e tipo
print("valor:", valor)
print("type(valor):", type(valor))

# verifica com isinstance (recomendado)
print("isinstance(valor, str):", isinstance(valor, str))

# verifica tipo exato
print("type(valor) is str:", type(valor) is str)

# opção para garantir em tempo de execução
assert isinstance(valor, str)
