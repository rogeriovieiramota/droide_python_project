"""
ARQUIVO:
DESCRIÇÃO: Demonstração de todas as 71 funções built-in do Python 3.11.9
EXECUÇÃO: Rode diretamente no PyCharm 2024.1.1 Community Edition
Funções Built-in (Embutidas)
AUTOR: Rogerio V. Mota
"""
# ex_066_super.py
print("---------------------------------------------------------------------------------")
print('EXEMPLO - 66. super() - Chama métodos da classe pai (herança)')
print("---------------------------------------------------------------------------------")

class Animal:
    def falar(self):
        return "Som"

class Cachorro(Animal):
    def falar(self):
        return super().falar() + " Au Au!"

c = Cachorro()
print("=================================================================================\n")
print(f"Cachorro().falar() = {c.falar()}")
print("=================================================================================\n")
