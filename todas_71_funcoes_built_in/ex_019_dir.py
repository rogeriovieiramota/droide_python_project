# ex_019_dir.py
"""
ARQUIVO:
DESCRIÇÃO: Demonstração de todas as 71 funções built-in do Python 3.11.9
Funções Built-in (Embutidas)
EXECUÇÃO: Rode diretamente no PyCharm 2024.1.1 Community Edition
AUTOR: Rogerio V. Mota
"""
print("---------------------------------------------------------------------------------")
print('EXEMPLO - 19. dir() - Retorna lista de nomes no escopo atual ou atributos')
print("=================================================================================\n")

print(f"dir() primeiros 15 itens: {dir()[:15]}")
print("=================================================================================\n")
print(f"dir(str) primeiros 15 itens: {dir(str)[:15]}")
print("=================================================================================\n")


# ex_dir_diferenca.py
print("=" * 70)
print("DIFERENÇA ENTRE dir() E dir(str)")
print("=" * 70)

# Criando algumas variáveis no escopo atual
nome = "João"
idade = 30
minha_lista = [1, 2, 3]
minha_funcao = lambda x: x * 2

print("\n【1. dir()】- Inspeciona o ESCOPO ATUAL")
print("-" * 50)
print(f"dir() retorna: {dir()[:10]}...")  # Mostra só os 10 primeiros
print("\nO que apareceu?")
print("✅ '__name__' - variável especial do Python")
print("✅ '__doc__' - documentação")
print("✅ 'nome' - a variável que criamos")
print("✅ 'idade' - a variável que criamos")
print("✅ 'minha_lista' - a variável que criamos")
print("✅ 'minha_funcao' - a função que criamos")
print("✅ 'print' - função built-in disponível")
print("✅ 'len' - função built-in disponível")

print("\n【2. dir(str)】- Inspeciona a CLASSE str (strings)")
print("-" * 50)
print(f"dir(str) retorna: {dir(str)[:15]}...")
print("\nO que apareceu?")
print("✅ 'capitalize' - método para strings")
print("✅ 'upper' - método para strings")
print("✅ 'lower' - método para strings")
print("✅ 'find' - método para strings")
print("✅ 'replace' - método para strings")
print("✅ NENHUMA variável que criamos!")

print("\n" + "=" * 70)
print("COMPARAÇÃO VISUAL")
print("=" * 70)

print(f"\n{'dir()':<20} | {'dir(str)':<30}")
print("-" * 50)
print(f"{'Mostra variáveis do programa':<20} | {'Mostra métodos das strings':<30}")
print(f"{'Ex: nome, idade, lista':<20} | {'Ex: upper(), lower(), find()':<30}")
print(f"{'Muda conforme seu código':<20} | {'É sempre igual (fixo)':<30}")


"""
# dir() SEM argumento
dir()  
# 👆 Pergunta: "Quais variáveis existem no meu programa agora?"

# dir(ALGO) COM argumento
dir(str)
# 👆 Pergunta: "Quais métodos e atributos a classe str (strings) possui?"
"""