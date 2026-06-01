# ex_018_dict.py
"""
ARQUIVO:
DESCRIÇÃO: Demonstração de todas as 71 funções built-in do Python 3.11.9
Funções Built-in (Embutidas)
EXECUÇÃO: Rode diretamente no PyCharm 2024.1.1 Community Edition
AUTOR: Rogerio V. Mota
"""
print("---------------------------------------------------------------------------------")
print('EXEMPLO - 18. dict() - Cria um dicionário (mapa chave-valor)')
print("=================================================================================\n")

print(f"dict() = {dict()}")
print("=================================================================================\n")
print(f"dict(a=1, b=2) = {dict(a=1, b=2)}")
print("=================================================================================\n")
print(f"dict([('a',1), ('b',2)]) = {dict([('a',1), ('b',2)])}")
print("=================================================================================\n")

""""
TABELA DE EXEMPLOS CORRETOS vs INCORRETOS
dict(a=1, b=2) cria um dicionário	✅ Correto	    Cria {"a": 1, "b": 2}
dict(a=1, b=2) cria uma lista	    ❌ Incorreto	Isto é um DICIONÁRIO, não lista
[1, 2] cria uma lista	✅ Correto	Isto é uma LISTA

# Isto é um DICIONÁRIO (pares de chave:valor)
dicionario = dict(a=1, b=2)
# Resultado: {"a": 1, "b": 2}

# Isto é uma LISTA (valores em sequência)
lista = [1, 2]
# Resultado: [1, 2]

DICIONÁRIO vs LISTA
Característica	Dicionário (dict)	        Lista (list)
==============  ========================    =============================
Estrutura	    Pares de chave: valor	    Sequência ordenada de valores
Acesso	        Por chave: dict["chave"]	Por índice: lista[0]
Sintaxe	        {"a": 1, "b": 2}	        [1, 2]
Ordem	Mantida (Python 3.7+)	            Mantida
Mutável	        Sim	                        Sim
Chaves únicas	Sim (não pode repetir)	    N/A

"""