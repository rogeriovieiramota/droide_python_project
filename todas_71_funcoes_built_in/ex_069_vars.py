# ex_069_vars.py

"""
ARQUIVO:
DESCRIÇÃO: Demonstração de todas as 71 funções built-in do Python 3.11.9
EXECUÇÃO: Rode diretamente no PyCharm 2024.1.1 Community Edition
Funções Built-in (Embutidas)
AUTOR: Rogerio V. Mota
"""

print("---------------------------------------------------------------------------------")
print('EXEMPLO - 69. vars() - Retorna dicionário com atributos do objeto (__dict__)')
print("---------------------------------------------------------------------------------")

class Pessoa:
    def __init__(self):
        self.nome = "João"
        self.idade = 30

p = Pessoa()
print("=================================================================================\n")
print(f"vars(p) = {vars(p)}")
print("=================================================================================\n")