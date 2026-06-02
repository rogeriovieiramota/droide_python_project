"""
ARQUIVO:
DESCRIÇÃO: Demonstração de todas as 71 funções built-in do Python 3.11.9
Funções Built-in (Embutidas)
EXECUÇÃO: Rode diretamente no PyCharm 2024.1.1 Community Edition
AUTOR: Rogerio V. Mota
"""
# ex_031_hash.py
print("---------------------------------------------------------------------------------")
print('EXEMPLO - 31. hash() - Retorna valor hash (único para objetos imutáveis)')
print("=================================================================================\n")

print(f"hash('abc') = {hash('abc')}")
print("=================================================================================\n")
print(f"hash(10) = {hash(10)}")
print("=================================================================================\n")
print(f"hash((1,2,3)) = {hash((1,2,3))}")
print("=================================================================================\n")
print(f"hash(1) = {hash(1)}")
print(f"hash(2) = {hash(2)}")
print(f"hash(3) = {hash(3)}")
print(f"hash((1,2,3)) = {hash((1,2,3))}")
print("=================================================================================\n")
print("""
✅ O que PODE usar hash():
   - Strings (str)          ✅ "Python"
   - Números (int, float)   ✅ 10, 3.14
   - Tuplas (tuple)         ✅ (1, 2, 3)
   - Booleanos (bool)       ✅ True, False
   - None                   ✅ None

❌ O que NÃO PODE usar hash():
   - Listas (list)          ❌ [1, 2, 3]
   - Dicionários (dict)     ❌ {"a": 1}
   - Conjuntos (set)        ❌ {1, 2, 3}
   - Qualquer mutável       ❌

📌 Características importantes:
   1. Objetos IGUAIS → hash IGUAIS
   2. Objetos DIFERENTES → geralmente hash DIFERENTES
   3. O hash NÃO pode ser revertido para o objeto original
   4. O Python usa hash internamente para otimizar dicionários e sets
""")

# ex_031_hash_detalhado.py
print("=" * 70)
print("ENTENDENDO A FUNÇÃO hash() EM PYTHON")
print("=" * 70)

# -------------------------------------------------------------------
# EXEMPLO 1: Hash de strings
# -------------------------------------------------------------------
print("\n【1. HASH DE STRINGS】")
print("-" * 50)

nome1 = "João"
nome2 = "João"
nome3 = "Maria"

hash1 = hash(nome1)
hash2 = hash(nome2)
hash3 = hash(nome3)

print(f"hash('{nome1}') = {hash1}")
print(f"hash('{nome2}') = {hash2}")
print(f"hash('{nome3}') = {hash3}")

print(f"\n✅ Strings IGUAIS têm hash IGUAIS? {hash1 == hash2}")
print(f"❌ Strings DIFERENTES têm hash DIFERENTES? {hash1 != hash3}")

# -------------------------------------------------------------------
# EXEMPLO 2: Hash de números
# -------------------------------------------------------------------
print("\n【2. HASH DE NÚMEROS】")
print("-" * 50)

print(f"hash(10) = {hash(10)}")
print(f"hash(10) = {hash(10)} (sempre o mesmo)")
print(f"hash(3.14) = {hash(3.14)}")
print(f"hash(10) == 10? {hash(10) == 10} (para inteiros, o hash É o próprio número)")

# -------------------------------------------------------------------
# EXEMPLO 3: Hash de tuplas (imutáveis)
# -------------------------------------------------------------------
print("\n【3. HASH DE TUPLAS (imutáveis)】")
print("-" * 50)

tupla1 = (1, 2, 3)
tupla2 = (1, 2, 3)
tupla3 = (1, 2, 4)

print(f"hash({tupla1}) = {hash(tupla1)}")
print(f"hash({tupla2}) = {hash(tupla2)}")
print(f"hash({tupla3}) = {hash(tupla3)}")
print(f"\n✅ Tuplas IGUAIS têm hash IGUAIS? {hash(tupla1) == hash(tupla2)}")
print(f"❌ Tuplas DIFERENTES têm hash DIFERENTES? {hash(tupla1) != hash(tupla3)}")

# -------------------------------------------------------------------
# EXEMPLO 4: O que NÃO pode usar hash()
# -------------------------------------------------------------------
print("\n【4. O QUE NÃO PODE USAR hash() - OBJETOS MUTÁVEIS】")
print("-" * 50)

# LISTAS são mutáveis - NÃO podem ser hasheadas
minha_lista = [1, 2, 3]
print(f"minha_lista = {minha_lista}")
print("❌ hash(minha_lista) - ERRO! Listas são mutáveis")
# hash(minha_lista)  # Descomente e veja o erro: TypeError: unhashable type: 'list'

# DICIONÁRIOS são mutáveis - NÃO podem ser hasheados
meu_dict = {"a": 1, "b": 2}
print(f"\nmeu_dict = {meu_dict}")
print("❌ hash(meu_dict) - ERRO! Dicionários são mutáveis")
# hash(meu_dict)  # Descomente e veja o erro

# SETS são mutáveis - NÃO podem ser hasheados
meu_set = {1, 2, 3}
print(f"\nmeu_set = {meu_set}")
print("❌ hash(meu_set) - ERRO! Sets são mutáveis")
# hash(meu_set)  # Descomente e veja o erro

# -------------------------------------------------------------------
# EXEMPLO 5: Para que serve o hash? - Comparação rápida
# -------------------------------------------------------------------
print("\n【5. PARA QUE SERVE O HASH?】")
print("-" * 50)

print("O hash é usado INTERNAMENTE pelo Python para:")

print("\n1️⃣ DICIONÁRIOS (dict):")
dicionario = {}
dicionario["João"] = 25
dicionario["Maria"] = 30
print("   - O Python calcula o hash da chave para encontrar o valor rapidamente")

print("\n2️⃣ CONJUNTOS (set):")
conjunto = {"maçã", "banana", "laranja"}
print("   - O hash garante que não haja elementos duplicados")

print("\n3️⃣ COMPARAÇÃO RÁPIDA:")
a = "Python"
b = "Python"
print(f"   - hash('{a}') = {hash(a)}")
print(f"   - hash('{b}') = {hash(b)}")
print("   - Se os hashes são diferentes, os objetos são diferentes!")
print("   - Se os hashes são iguais, provavelmente são objetos iguais")

# -------------------------------------------------------------------
# EXEMPLO 6: Hash vs Identidade (id)
# -------------------------------------------------------------------
print("\n【6. DIFERENÇA ENTRE hash() E id()】")
print("-" * 50)

texto1 = "Python"
texto2 = "Python"

print(f"texto1 = '{texto1}'")
print(f"texto2 = '{texto2}'")

print(f"\nid(texto1) = {id(texto1)} (endereço de memória)")
print(f"id(texto2) = {id(texto2)} (pode ser diferente)")

print(f"\nhash(texto1) = {hash(texto1)} (valor baseado no conteúdo)")
print(f"hash(texto2) = {hash(texto2)} (MESMO hash, mesmo conteúdo)")

print("\n🔵 id() → ONDE o objeto está (endereço)")
print("🟢 hash() → O QUE o objeto é (conteúdo)")

# -------------------------------------------------------------------
# EXEMPLO 7: Hash em objetos customizados
# -------------------------------------------------------------------
print("\n【7. HASH EM OBJETOS CUSTOMIZADOS】")
print("-" * 50)


class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def __hash__(self):
        # Definindo como calcular o hash para esta classe
        return hash((self.nome, self.idade))

    def __eq__(self, other):
        return self.nome == other.nome and self.idade == other.idade


p1 = Pessoa("João", 25)
p2 = Pessoa("João", 25)
p3 = Pessoa("Maria", 30)

print(f"p1 e p2 têm o mesmo NOME e IDADE")
print(f"hash(p1) = {hash(p1)}")
print(f"hash(p2) = {hash(p2)}")
print(f"hash(p3) = {hash(p3)}")
print(f"\np1 e p2 têm o mesmo hash? {hash(p1) == hash(p2)}")
print(f"p1 e p3 têm o mesmo hash? {hash(p1) == hash(p3)}")

# -------------------------------------------------------------------
# RESUMO FINAL
# -------------------------------------------------------------------
print("\n" + "=" * 70)
print("RESUMO DO hash()")
print("=" * 70)

print("""
✅ O que PODE usar hash():
   - Strings (str)          ✅ "Python"
   - Números (int, float)   ✅ 10, 3.14
   - Tuplas (tuple)         ✅ (1, 2, 3)
   - Booleanos (bool)       ✅ True, False
   - None                   ✅ None

❌ O que NÃO PODE usar hash():
   - Listas (list)          ❌ [1, 2, 3]
   - Dicionários (dict)     ❌ {"a": 1}
   - Conjuntos (set)        ❌ {1, 2, 3}
   - Qualquer mutável       ❌

📌 Características importantes:
   1. Objetos IGUAIS → hash IGUAIS
   2. Objetos DIFERENTES → geralmente hash DIFERENTES
   3. O hash NÃO pode ser revertido para o objeto original
   4. O Python usa hash internamente para otimizar dicionários e sets
""")

print("=" * 70)