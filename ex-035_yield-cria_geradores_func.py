# Curso: AS 35 PALAVRAS RESERVADAS DO PYTHON versão 3.11.9

print("---------------------------------------------------------------------------------")
print('EXEMPLO ->35. yield - Cria geradores (funções que "lembram" seu estado)  ===\n')
print("---------------------------------------------------------------------------------")
print("=================================================================================\n")

"""

yield - Cria geradores (funções que "lembram" seu estado)

"""

def contador(maximo):
    """Gerador que conta de 0 até maximo"""
    n = 0
    while n <= maximo:
        yield n  # Pausa e retorna o valor
        n += 1

# Usando o gerador
for numero in contador(5):
    print(f"Número: {numero}")

# Geradores economizam memória
def fibonacci(limite):
    a, b = 0, 1
    while a <= limite:
        yield a
        a, b = b, a + b

print("Sequência Fibonacci:")
for num in fibonacci(100):
    print(num, end=" ")