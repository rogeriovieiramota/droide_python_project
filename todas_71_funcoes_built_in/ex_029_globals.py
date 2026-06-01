"""
ARQUIVO:
DESCRIÇÃO: Demonstração de todas as 71 funções built-in do Python 3.11.9
Funções Built-in (Embutidas)
EXECUÇÃO: Rode diretamente no PyCharm 2024.1.1 Community Edition
AUTOR: Rogerio V. Mota
"""

# ex_029_globals.py
print("---------------------------------------------------------------------------------")
print('EXEMPLO - 29. globals() - Retorna dicionário do escopo global')
print("=================================================================================\n")

x = 10
y = 20
globals_dict = globals()
print(f"Variável 'x' no globals: {globals_dict.get('x')}")
print("=================================================================================\n")
print(f"Variável 'y' no globals: {globals_dict.get('y')}")
print("=================================================================================\n")