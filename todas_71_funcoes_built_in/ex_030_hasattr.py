"""
ARQUIVO:
DESCRIÇÃO: Demonstração de todas as 71 funções built-in do Python 3.11.9
Funções Built-in (Embutidas)
EXECUÇÃO: Rode diretamente no PyCharm 2024.1.1 Community Edition
AUTOR: Rogerio V. Mota
"""
# ex_030_hasattr.py
print("---------------------------------------------------------------------------------")
print('EXEMPLO - 30. hasattr() - Verifica se objeto tem determinado atributo')
print("=================================================================================\n")

class Pessoa:
    nome = "João"
    idade = 30

print(f"hasattr(Pessoa, 'nome') = {hasattr(Pessoa, 'nome')}")
print("=================================================================================\n")
print(f"hasattr(Pessoa, 'idade') = {hasattr(Pessoa, 'idade')}")
print("=================================================================================\n")
print(f"hasattr(Pessoa, 'altura') = {hasattr(Pessoa, 'altura')}")
print("=================================================================================\n")
