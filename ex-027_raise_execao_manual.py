# Curso: AS 35 PALAVRAS RESERVADAS DO PYTHON versão 3.11.9

print("---------------------------------------------------------------------------------")
print('EXEMPLO ->27. raise - Lança/exceção manualmente ===\n')
print("---------------------------------------------------------------------------------")
print("=================================================================================\n")

def sacar(saldo, valor):
    if valor > saldo:
        raise ValueError(f"Saldo insuficiente! Disponível: {saldo}")
    return saldo - valor

try:
    novo_saldo = sacar(2500, 1100)
except ValueError as erro:
    print("=================================================================================\n")
    print(f"Erro ao sacar: {erro}")
    print("=================================================================================\n")

# Criando exceção customizada
class SaldoInsuficienteError(Exception):
    pass

def transferir(valor):
    if valor > 1000:
        raise SaldoInsuficienteError("Valor excede limite")
