"""
ARQUIVO:
DESCRIÇÃO: Demonstração de todas as 71 funções built-in do Python 3.11.9
Funções Built-in (Embutidas)
EXECUÇÃO: Rode diretamente no PyCharm 2024.1.1 Community Edition
AUTOR: Rogerio V. Mota
"""

# ex_028_getattr.py
print("---------------------------------------------------------------------------------")
print('EXEMPLO - 28. getattr() - Retorna valor de atributo de objeto')
print("=================================================================================\n")

class Pessoa:
    nome = "João"
    idade = 30

print(f"getattr(Pessoa, 'nome') = {getattr(Pessoa, 'nome')}")
print("=================================================================================\n")
print(f"getattr(Pessoa, 'idade', 'N/A') = {getattr(Pessoa, 'idade', 'N/A')}")
print("=================================================================================\n")
print(f"getattr(Pessoa, 'altura', 'Não existe') = {getattr(Pessoa, 'altura', 'Não existe')}")
print("=================================================================================\n")

"""

Procura 'idade'.

O atributo existe, então retorna 30.

O valor padrão 'N/A' é ignorado, porque só é usado se o atributo não existir.

"""