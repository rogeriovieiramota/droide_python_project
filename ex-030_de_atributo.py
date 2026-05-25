# Curso: AS 35 PALAVRAS RESERVADAS DO PYTHON versão 3.11.9

print("---------------------------------------------------------------------------------")
print('EXEMPLO ->30. del - Deleta variável, atributo ou item de lista/dicionário ===\n')
print("---------------------------------------------------------------------------------")
print("=================================================================================\n")

"""

del - Deleta variável, atributo ou item de lista/dicionário

"""


# Deletar variável
nome = "João"
print(nome)
del nome
#print(nome)  # NameError: nome não existe mais!

# Deletar item de lista
frutas = ["maçã", "banana", "laranja", "uva"]
print("=================================================================================\n")
print(frutas)
print("=================================================================================\n")
print("========== # Remove laranja ===========\n")
del frutas[2]  # Remove laranja
print(frutas)  # ['maçã', 'banana', 'uva']

# Deletar pedaço da lista
del frutas[0:2]
print(frutas)  # ['uva']

# Deletar de dicionário
pessoa = {"nome": "Carlos", "idade": 30}
print(pessoa)
del pessoa["idade"]
print(pessoa)  # {'nome': 'Carlos'}