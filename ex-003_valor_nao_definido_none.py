# None é como null em outras linguagens
valor_nao_definido = None
print("=================================================================================")
print(valor_nao_definido)  # None
print("=================================================================================")
def buscar_usuario(id):
    if id == 0:
        return None  # Usuário não encontrado
    return "João"
print("=================================================================================")
print(buscar_usuario(0))  # None
print("=================================================================================")