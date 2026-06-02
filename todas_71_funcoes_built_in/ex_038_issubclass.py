""""
ARQUIVO:
DESCRIÇÃO: Demonstração de todas as 71 funções built-in do Python 3.11.9
Funções Built-in (Embutidas)
EXECUÇÃO: Rode diretamente no PyCharm 2024.1.1 Community Edition
AUTOR: Rogerio V. Mota
"""
# ex_038_issubclass.py
print("---------------------------------------------------------------------------------")
print('EXEMPLO - 38. issubclass() - Verifica se classe é subclasse de outra')
print("=================================================================================\n")

class Animal:
    pass

class Cachorro(Animal):
    pass

print(f"issubclass(Cachorro, Animal) = {issubclass(Cachorro, Animal)}")
print(f"issubclass(Cachorro, object) = {issubclass(Cachorro, object)}")
