"""
ARQUIVO:
DESCRIÇÃO: Demonstração de todas as 71 funções built-in do Python 3.11.9
Funções Built-in (Embutidas)
EXECUÇÃO: Rode diretamente no PyCharm 2024.1.1 Community Edition
AUTOR: Rogerio V. Mota
"""
# ex_010_bytearray.py
print("---------------------------------------------------------------------------------")
print('EXEMPLO - 10. bytearray() - Cria array mutável de bytes (0-255)')
print("=================================================================================\n")

print(f"bytearray(5) = {bytearray(5)}")
print("=================================================================================\n")
print(f"bytearray([65,66,67]) = {bytearray([65,66,67])}")
ba = bytearray([65,66,67])
ba[0] = 88
print("=================================================================================\n")
print(f"Modificando: bytearray([88,66,67]) = {ba}")