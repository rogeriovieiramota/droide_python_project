"""
ARQUIVO:
DESCRIÇÃO: Demonstração de todas as 71 funções built-in do Python 3.11.9
Funções Built-in (Embutidas)
EXECUÇÃO: Rode diretamente no PyCharm 2024.1.1 Community Edition
AUTOR: Rogerio V. Mota
"""
# ex_049_oct.py
print("---------------------------------------------------------------------------------")
print('EXEMPLO - 49. oct() - Converte inteiro para string octal (0o)')
print("=================================================================================\n")

print(f"oct(8) = {oct(8)}")
print("=================================================================================\n")
print(f"oct(10) = {oct(10)}")
print("=================================================================================\n")
print(f"oct(255) = {oct(255)}")
print("=================================================================================\n")

#255 em decimal = 377 em octal
#Cálculo: 255 ÷ 8 = 31 resto 7, 31 ÷ 8 = 3 resto 7, 3 ÷ 8 = 0 resto 3 → 377

"""
377 (octal) = (3 × 8²) + (7 × 8¹) + (7 × 8⁰)
            = (3 × 64) + (7 × 8) + (7 × 1)
            = 192 + 56 + 7
            = 255 (decimal)
"""
