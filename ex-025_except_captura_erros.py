# Curso: AS 35 PALAVRAS RESERVADAS DO PYTHON versão 3.11.9

print("---------------------------------------------------------------------------------")
print('EXEMPLO -> 25. except - Captura erros que ocorrem no try ===\n')
print("---------------------------------------------------------------------------------")
print("=================================================================================\n")

try:
    lista = [1, 2, 3]
    print("=================================================================================\n")
    print(lista[5])  # IndexError
except IndexError:
    print("=================================================================================\n")
    print("Índice não encontrado na lista")

# Pode capturar múltiplos erros
try:
    x = int("abc")
except (ValueError, TypeError):
    print("=================================================================================\n")
    print("Erro de conversão")
