"""
ARQUIVO:
DESCRIÇÃO: Demonstração de todas as 71 funções built-in do Python 3.11.9
Funções Built-in (Embutidas)
EXECUÇÃO: Rode diretamente no PyCharm 2024.1.1 Community Edition
AUTOR: Rogerio V. Mota
"""
# ex_034_id.py
print("---------------------------------------------------------------------------------")
print('EXEMPLO - 34. id() - Retorna identidade única do objeto (endereço de memória)')
print("=================================================================================\n")

x = 10
y = 10
z = [1, 2]
print(f"id(x) = {id(x)}")
print("=================================================================================\n")
print(f"id(y) = {id(y)} (mesmo que x, compartilham memória)")
print("=================================================================================\n")
print(f"id(z) = {id(z)}")
print("=================================================================================\n")