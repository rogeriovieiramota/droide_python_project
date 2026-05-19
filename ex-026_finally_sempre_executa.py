# Curso: AS 35 PALAVRAS RESERVADAS DO PYTHON versão 3.11.9

print("---------------------------------------------------------------------------------")
print('EXEMPLO -> 26. finally - Sempre executa, ocorrendo erro ou não ===\n')
print("---------------------------------------------------------------------------------")
print("=================================================================================\n")

try:
    arquivo = open("dados.txt", "r")
    conteudo = arquivo.read()
except FileNotFoundError:
    print("=================================================================================\n")
    print("Arquivo não encontrado")
finally:
    # Isso SEMPRE executa, mesmo com erro
    print("Fechando conexões/recursos")
    if 'arquivo' in locals():
        arquivo.close()
