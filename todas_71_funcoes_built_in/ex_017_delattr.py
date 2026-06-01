"""
ARQUIVO:
DESCRIÇÃO: Demonstração de todas as 71 funções built-in do Python 3.11.9
Funções Built-in (Embutidas)
EXECUÇÃO: Rode diretamente no PyCharm 2024.1.1 Community Edition
AUTOR: Rogerio V. Mota
"""
# ex_017_delattr.py
print("---------------------------------------------------------------------------------")
print('EXEMPLO - 17. delattr() - Deleta atributo de objeto')
print("=================================================================================\n")

class Pessoa:
    nome = "João"
    idade = 30

print(f"Antes: hasattr(Pessoa, 'idade') = {hasattr(Pessoa, 'idade')}")
print("=================================================================================\n")
delattr(Pessoa, "idade")
print("=================================================================================\n")
print(f"Depois: hasattr(Pessoa, 'idade') = {hasattr(Pessoa, 'idade')}")
print("=================================================================================\n")
print(f"Depois: hasattr(Pessoa, 'nome') = {hasattr(Pessoa, 'nome')}")