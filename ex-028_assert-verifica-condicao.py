# Curso: AS 35 PALAVRAS RESERVADAS DO PYTHON versão 3.11.9

print("---------------------------------------------------------------------------------")
print('EXEMPLO ->28. assert - Verifica condição (para debugging) ===\n')
print("---------------------------------------------------------------------------------")
print("=================================================================================\n")

"""
O assert NÃO é para validar entrada do usuário, é para DEBUGGING!
"""

# Se você quer validar idade sem quebrar o programa:
#idade = -17
idade = 18

if idade >= 18:
    print("Pode votar")
else:
    print("Menor de idade não pode votar")  # Programa continua rodando

# assert é só para debug (encontrar bugs):
assert idade >= 0, "Idade não pode ser negativa"  # Isso é uma pré-condição