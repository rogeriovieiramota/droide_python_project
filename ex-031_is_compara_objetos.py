# Curso: AS 35 PALAVRAS RESERVADAS DO PYTHON versão 3.11.9

print("---------------------------------------------------------------------------------")
print('EXEMPLO ->310. is - Compara se dois objetos são o MESMO objeto  ===\n')
print("---------------------------------------------------------------------------------")
print("=================================================================================\n")

"""

is - Compara se dois objetos são o MESMO objeto 

"""

# is vs == (igualdade)
a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(a == b)  # True (valores iguais)
print(a is b)  # False (objetos diferentes na memória)
print(a is c)  # True (mesmo objeto)

# Uso comum com None
valor = None
if valor is None:
    print("Variável está vazia")