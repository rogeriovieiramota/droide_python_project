# ex_023_exec.py
"""
ARQUIVO:
DESCRIÇÃO: Demonstração de todas as 71 funções built-in do Python 3.11.9
Funções Built-in (Embutidas)
EXECUÇÃO: Rode diretamente no PyCharm 2024.1.1 Community Edition
AUTOR: Rogerio V. Mota
"""

print("---------------------------------------------------------------------------------")
print('EXEMPLO - 23. exec() - Executa código Python (não retorna valor)')
print("---------------------------------------------------------------------------------")

exec("print('Olá via exec()')")
print("=================================================================================\n")
codigo = """
for i in range(3):
    print(f'  i = {i}')
"""
print("=================================================================================\n")
print("Executando código com loop:")
exec(codigo)