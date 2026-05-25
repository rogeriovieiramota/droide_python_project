# Curso: AS 35 PALAVRAS RESERVADAS DO PYTHON versão 3.11.9

print("---------------------------------------------------------------------------------")
print('EXEMPLO ->29.  class - Define uma classe (molde para objetos) ===\n')
print("---------------------------------------------------------------------------------")
print("=================================================================================\n")

"""
class - Define uma classe (molde para objetos)
"""


class Pessoa:
    # Construtor
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    # Método
    def saudacao(self):
        return f"Olá, eu sou {self.nome} e tenho {self.idade} anos"


# Usando a classe
pessoa = Pessoa("Ana", 25)
print(pessoa.saudacao())

# Atributos
print(pessoa.nome)  # Ana