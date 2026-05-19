# Curso: AS 35 PALAVRAS RESERVADAS DO PYTHON versão 3.11.9

print("---------------------------------------------------------------------------------")
print('EXEMPLO - 15. def - Define uma função')
print("---------------------------------------------------------------------------------")

def saudacao(nome):
    """Função simples de saudação"""
    return f"Olá, {nome}!"

# Chamando a função
mensagem = saudacao("Maria")
print(mensagem)  # "Olá, Maria!"