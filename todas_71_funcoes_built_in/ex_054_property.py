"""
ARQUIVO:

DESCRIÇÃO: Demonstração de todas as 71 funções built-in do Python 3.11.9
Funções Built-in (Embutidas)
EXECUÇÃO: Rode diretamente no PyCharm 2024.1.1 Community Edition
AUTOR: Rogerio V. Mota
"""
# ex_054_property.py
print("---------------------------------------------------------------------------------")
print('EXEMPLO - 54. property() - Cria propriedade para gerenciar atributos')
print("=================================================================================\n")


class Pessoa:
    def __init__(self, nome):
        self._nome = nome

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, valor):
        self._nome = valor


p = Pessoa("João")
print("=================================================================================\n")
print(f"Nome: {p.nome}")
print("=================================================================================\n")
p.nome = "Maria"
print(f"Nome alterado: {p.nome}")
print("=================================================================================\n")