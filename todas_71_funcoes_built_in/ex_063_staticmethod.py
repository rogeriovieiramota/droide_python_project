"""
ARQUIVO:

DESCRIÇÃO: Demonstração de todas as 71 funções built-in do Python 3.11.9
Funções Built-in (Embutidas)
EXECUÇÃO: Rode diretamente no PyCharm 2024.1.1 Community Edition
AUTOR: Rogerio V. Mota
"""
# ex_063_staticmethod.py
print("---------------------------------------------------------------------------------")
print('EXEMPLO - 63. staticmethod() - Converte método em método estático')
print("---------------------------------------------------------------------------------")

class Matematica:
    @staticmethod
    def somar(a, b):
        return a + b
print("=================================================================================\n")
print(f"Matematica.somar(5, 3) = {Matematica.somar(5, 3)}")
print("=================================================================================\n")