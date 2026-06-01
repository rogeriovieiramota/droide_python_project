# ex_022_eval.py
"""
ARQUIVO:
DESCRIÇÃO: Demonstração de todas as 71 funções built-in do Python 3.11.9
Funções Built-in (Embutidas)
EXECUÇÃO: Rode diretamente no PyCharm 2024.1.1 Community Edition
AUTOR: Rogerio V. Mota
"""
print("---------------------------------------------------------------------------------")
print('EXEMPLO - 22. eval() - Executa string como código Python e retorna resultado')
print("=================================================================================\n")

# MÉTODO 1: Aspas duplas fora, simples dentro
print(f"eval('2 + 2') = {eval('2 + 2')}")
print("=================================================================================\n")

# MÉTODO 2: Usando variável auxiliar (mais limpo)
expressao = "len('abc')"
print(f"eval(\"len('abc')\") = {eval(expressao)}")
print("=================================================================================\n")

# MÉTODO 3: Calculando fora da f-string
resultado = eval("len('abc')")
print(f"eval(\"len('abc')\") = {resultado}")
print("=================================================================================\n")

# MÉTODO 4: Com variável existente
x = 10
print(f"eval('x * 2') = {eval('x * 2')}")
print("=================================================================================\n")

# MÉTODO 5: Expressão matemática
print(f"eval('10 / 2') = {eval('10 / 2')}")
print("=================================================================================\n")

x = 10
print(f"eval('x * 2') = {eval('x * 2')}")
print("=================================================================================\n")
