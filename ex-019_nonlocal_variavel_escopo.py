# Curso: AS 35 PALAVRAS RESERVADAS DO PYTHON versão 3.11.9

print("---------------------------------------------------------------------------------")
print('EXEMPLO 18. global - Acessa/modifica variável global dentro de função ===\n')
print("---------------------------------------------------------------------------------")
print("=================================================================================\n")

def funcao_externa():
    valor_externo = 10

    def funcao_interna():
        nonlocal valor_externo  # Modifica variável da função externa
        valor_externo += 5
        print("=================================================================================\n")
        print(f"Valor dentro: {valor_externo}")
        print("=================================================================================\n")

    funcao_interna()
    print("=================================================================================\n")
    print(f"Valor externo agora: {valor_externo}")  # 15
    print("=================================================================================\n")


funcao_externa()