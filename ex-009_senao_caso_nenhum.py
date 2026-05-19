# Curso: AS 35 PALAVRAS RESERVADAS DO PYTHON versão 3.11.9

print("---------------------------------------------------------------------------------")
print('EXEMPLO - 9. else - SENÃO (caso nenhum if/elif seja verdade)')
print("---------------------------------------------------------------------------------")

senha = "1234"

if senha == "admin":
    print("Acesso total")
elif senha == "user":
    print("Acesso limitado")
else:
    print("Senha incorreta!")  # Executa isso