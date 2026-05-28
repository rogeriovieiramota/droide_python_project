"""
ARQUIVO:
DESCRIÇÃO: Demonstração de todas as 71 funções built-in do Python 3.11.9
Funções Built-in (Embutidas)
EXECUÇÃO: Rode diretamente no PyCharm 2024.1.1 Community Edition
AUTOR: Rogerio V. Mota
"""

# ex_014_classmethod.py
print("---------------------------------------------------------------------------------")
print('EXEMPLO - 14. classmethod() - Converte método em método de classe')
print("=================================================================================\n")

class MinhaClasse:
    @classmethod
    def meu_metodo(cls):
        return f"Chamado da classe: {cls.__name__}"
print("=================================================================================\n")
print(f"MinhaClasse.meu_metodo() = {MinhaClasse.meu_metodo()}")