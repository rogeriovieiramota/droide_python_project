"""
ARQUIVO:

DESCRIÇÃO: Demonstração de todas as 71 funções built-in do Python 3.11.9
Funções Built-in (Embutidas)
EXECUÇÃO: Rode diretamente no PyCharm 2024.1.1 Community Edition
AUTOR: Rogerio V. Mota
"""
# ex_060_setattr.py
print("---------------------------------------------------------------------------------")
print('EXEMPLO - 60. setattr() - Define valor de atributo de objeto')
print("---------------------------------------------------------------------------------")

class Pessoa:
    pass

p = Pessoa()
setattr(p, "nome", "João")
setattr(p, "idade", 30)
print("=================================================================================\n")
print(f"p.nome = {p.nome}")
print("=================================================================================\n")
print(f"p.idade = {p.idade}")
print("=================================================================================\n")