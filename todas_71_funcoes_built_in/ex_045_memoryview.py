"""
ARQUIVO:
DESCRIÇÃO: Demonstração de todas as 71 funções built-in do Python 3.11.9
Funções Built-in (Embutidas)
EXECUÇÃO: Rode diretamente no PyCharm 2024.1.1 Community Edition
AUTOR: Rogerio V. Mota
"""

# ex_045_memoryview.py
print("---------------------------------------------------------------------------------")
print('EXEMPLO - 45. memoryview() - Cria view sobre memória de bytes (sem copiar)')
print("=================================================================================\n")

b = bytearray(b'abcdef') #
mv = memoryview(b)  #Cria uma memoryview que aponta para a mesma região de memória de b, sem duplicar os dados.

print(f"Original: {b}")
print("=================================================================================\n")
mv[0] = 88 #Modifica o primeiro byte via memoryview. O valor 88 é o código ASCII de 'X'. # Crucial: essa modificação afeta diretamente o bytearray original b, pois compartilham a mesma memória.
print(f"Após modificar via memoryview: {b}") #
print("=================================================================================\n")