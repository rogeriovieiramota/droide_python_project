# Curso: AS 35 PALAVRAS RESERVADAS DO PYTHON versão 3.11.9

print("---------------------------------------------------------------------------------")
print('EXEMPLO - 13. continue - Pula para próxima iteração')
print("---------------------------------------------------------------------------------")

for i in range(1, 6):
    if i == 3:
        continue  # Pula o 3
    print(f"Número: {i}")  # Imprime 1,2,4,5