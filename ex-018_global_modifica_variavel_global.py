# Curso: AS 35 PALAVRAS RESERVADAS DO PYTHON versão 3.11.9

print("---------------------------------------------------------------------------------")
print('EXEMPLO 18. global - Acessa/modifica variável global dentro de função ===\n')
print("---------------------------------------------------------------------------------")

contador_global = 0

def incrementar():
    global contador_global  # Diz que vai usar a variável global
    contador_global += 1
    print("=================================================================================\n")
    print(f"Valor global agora: {contador_global}")
    print("=================================================================================\n")

incrementar()  # Valor global agora: 1
incrementar()  # Valor global agora: 2