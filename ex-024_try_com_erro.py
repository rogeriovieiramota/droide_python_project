# Curso: AS 35 PALAVRAS RESERVADAS DO PYTHON versão 3.11.9

print("---------------------------------------------------------------------------------")
print('EXEMPLO 24. try - Tenta executar código que pode dar erro ===\n')
print("---------------------------------------------------------------------------------")
print("=================================================================================\n")

try:
    numero = int(input("Digite um número: "))
    resultado = 10 / numero
    print("=================================================================================\n")
    print(f"Resultado: {resultado}")
except ValueError:
    print("=================================================================================\n")
    print("Erro: Isso não é um número válido!")
except ZeroDivisionError:
    print("=================================================================================\n")
    print("Erro: Não pode dividir por zero!")
