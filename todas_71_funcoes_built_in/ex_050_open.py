"""
ARQUIVO:
DESCRIÇÃO: Demonstração de todas as 71 funções built-in do Python 3.11.9
Funções Built-in (Embutidas)
EXECUÇÃO: Rode diretamente no PyCharm 2024.1.1 Community Edition
AUTOR: Rogerio V. Mota
"""

# ex_050_open.py
print("---------------------------------------------------------------------------------")
print('EXEMPLO - 50. open() - Abre arquivo e retorna objeto de arquivo')
print("=================================================================================\n")

# Criando e escrevendo em um arquivo
with open("teste_builtin.txt", "w", encoding='utf-8') as arquivo:
    arquivo.write("Olá, mundo via open()!")
print("Arquivo 'teste_builtin.txt' criado com sucesso!")
print("=================================================================================\n")

# Lendo o arquivo
with open("teste_builtin.txt", "r") as arquivo:
    conteudo = arquivo.read()
print(f"Conteúdo do arquivo: {conteudo}")
print("=================================================================================\n")

# Ler como bytes para ver a representação no disco
with open('teste_builtin.txt', 'rb') as f:
    b = f.read()
print(f"Bytes no arquivo: {b}")  # Em UTF-8 o 'á' aparece como b'\\xc3\\xa1'