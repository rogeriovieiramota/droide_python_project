"""
ARQUIVO:

DESCRIÇÃO: Demonstração de todas as 71 funções built-in do Python 3.11.9
Funções Built-in (Embutidas)
EXECUÇÃO: Rode diretamente no PyCharm 2024.1.1 Community Edition
AUTOR: Rogerio V. Mota
"""
# ex_061_slice.py
print("---------------------------------------------------------------------------------")
print('EXEMPLO - 61. slice() - Cria objeto slice (fatia) para sequências')
print("---------------------------------------------------------------------------------")

s = slice(2, 5)
print("=================================================================================\n")
print(f"slice(2,5) = {s}")
print("=================================================================================\n")
print(f"'abcdefg'[{s}] = {'abcdefg'[s]}")

s2 = slice(1, 8, 2)
print("=================================================================================\n")
print(f"'abcdefghij'[{s2}] = {'abcdefghij'[s2]}")
print("=================================================================================\n")

s3 = slice(1, 8, 3)
print(f"'abcdefghij'[{s3}] = {'abcdefghij'[s3]}")
"""
slice(1, 8, 2) cria um objeto slice com:
início: 1 (começa no índice 1)
fim: 8 (vai até o índice 7, não incluindo o 8)
passo: 2 (pula de 2 em 2 posições)
"""