"""
ARQUIVO:
DESCRIÇÃO: Demonstração de todas as 71 funções built-in do Python 3.11.9
Funções Built-in (Embutidas)
EXECUÇÃO: Rode diretamente no PyCharm 2024.1.1 Community Edition
AUTOR: Rogerio V. Mota
"""
# ex_047_next.py
print("---------------------------------------------------------------------------------")
print('EXEMPLO - 47. next() - Retorna próximo item do iterador')
print("=================================================================================\n")

it = iter([1, 2, 3])
print(f"next(it) = {next(it)}")
print("=================================================================================\n")
print(f"next(it) = {next(it)}")
print("=================================================================================\n")
print(f"next(it) = {next(it)}")
print("=================================================================================\n")
print(f"next(it, 'fim') = {next(it, 'fim')} (valor padrão quando acaba)")
print("=================================================================================\n")