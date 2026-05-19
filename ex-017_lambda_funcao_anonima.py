# Curso: AS 35 PALAVRAS RESERVADAS DO PYTHON versão 3.11.9

print("---------------------------------------------------------------------------------")
print('EXEMPLO 17. lambda - Função anônima de uma linha ===\n')
print("---------------------------------------------------------------------------------")

# Função normal
def dobrar(x):
    return x * 2

# Lambda equivalente
dobrar_lambda = lambda x: x * 2

print("=================================================================================\n")
print(dobrar(5))      # 10
print("=================================================================================\n")
print(dobrar_lambda(5))  # 10
print("=================================================================================\n")

# Útil em operações curtas
numeros = [1, 2, 3, 4]
dobrados = list(map(lambda x: x * 2, numeros))
print(dobrados)  # [2, 4, 6, 8]