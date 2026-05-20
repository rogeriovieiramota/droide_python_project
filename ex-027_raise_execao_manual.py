# Criando exceção customizada
class SaldoInsuficienteError(Exception):
    pass

def sacar(saldo, valor):
    if valor > saldo:
        raise ValueError(f"Saldo insuficiente! Disponível: {saldo}")
    return saldo - valor

def transferir(valor):
    if valor > 1000:
        raise SaldoInsuficienteError("Valor excede limite")


try:
    #novo_saldo = transferir(1001)
    novo_saldo = sacar(100, 200)
except SaldoInsuficienteError as erro:
    print(f"Erro na transferência: {erro}")
except ValueError as erro:
    print(f"Erro ao sacar: {erro}")




