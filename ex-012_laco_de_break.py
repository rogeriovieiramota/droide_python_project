# Curso: AS 35 PALAVRAS RESERVADAS DO PYTHON versão 3.11.9

print("---------------------------------------------------------------------------------")
print('EXEMPLO - 12. break - Interrompe o laço imediatamente')
print("---------------------------------------------------------------------------------")

for i in range(1, 11):
    if i == 5:
        break  # Para quando chegar em 5
    print(f"Número: {i}")  # Só imprime 1,2,3,4
