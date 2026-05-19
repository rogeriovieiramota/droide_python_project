# Curso: AS 35 PALAVRAS RESERVADAS DO PYTHON versão 3.11.9

print("---------------------------------------------------------------------------------")
print('EXEMPLO 23. with - Gerencia recursos (abre/fecha automaticamente) ===\n')
print("---------------------------------------------------------------------------------")
print("=================================================================================\n")

# Exemplo com arquivo (fecha automaticamente)
with open("teste.txt", "w") as arquivo:
    arquivo.write("Olá, EXEMPLO 23. with !")

# Sem with teria que fazer manualmente:
# arquivo = open("teste.txt", "w")
# arquivo.write("Olá")
# arquivo.close()  # Fácil esquecer!