# Curso: AS 35 PALAVRAS RESERVADAS DO PYTHON versão 3.11.9

print("---------------------------------------------------------------------------------")
print('EXEMPLO ->32. in - Verifica se um elemento existe em sequência  ===\n')
print("---------------------------------------------------------------------------------")
print("=================================================================================\n")

"""

is - Compara se dois objetos são o MESMO objeto 

"""

# Em listas
frutas = ["maçã", "banana", "laranja"]
if "banana" in frutas:
    print("=================================================================================\n")
    print("Temos banana!")

# Em strings
texto = "Python é incrível"
if "Python" in texto:
    print("=================================================================================\n")
    print("Texto fala sobre Python")

# Em dicionários (verifica chaves)
dados = {"nome": "Ana", "idade": 25}
if "nome" in dados:
    print("=================================================================================\n")
    print(f'Nome: {dados["nome"]}')

# Em for loops
for i in range(5):  # i in range(5)
    print(i)

# Usando com not
if "uva" not in frutas:
    print("=================================================================================\n")
    print("Não temos uva")