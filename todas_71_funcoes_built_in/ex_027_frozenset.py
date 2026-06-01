"""
ARQUIVO:
DESCRIÇÃO: Demonstração de todas as 71 funções built-in do Python 3.11.9
Funções Built-in (Embutidas)
EXECUÇÃO: Rode diretamente no PyCharm 2024.1.1 Community Edition
AUTOR: Rogerio V. Mota
"""
# ex_027_frozenset.py
print("---------------------------------------------------------------------------------")
print('EXEMPLO - 27. frozenset() - Cria conjunto imutável (não pode ser modificado)')
print("=================================================================================\n")

fs = frozenset([1, 2, 3, 4, 1])
print(f"frozenset([1,2,3,2,1]) = {fs}")
print("=================================================================================\n")
print("Não é possível adicionar/remover elementos (imutável)")
print("=================================================================================\n")

"""
A lista vira um conjunto
Conjuntos eliminam duplicatas automaticamente.

Então:

Código
[1, 2, 3, 2, 1]  →  {1, 2, 3}
✔ O conjunto é congelado

Agora ele vira um frozenset, que:
não permite .add()
não permite .remove()
não permite .clear()
não permite .update()

Ele é imutável.

"""