# Curso: AS 35 PALAVRAS RESERVADAS DO PYTHON versão 3.11.9

print("---------------------------------------------------------------------------------")
print('EXEMPLO - 8. elif - SENÃO SE (else if)')
print("---------------------------------------------------------------------------------")

nota = 65

if nota >= 90:
    print("A")
elif nota >= 80:  # SENÃO SE for >= 80
    print("B")
elif nota >= 70:  # SENÃO SE for >= 70
    print("C")
elif nota >= 60:  # SENÃO SE for >= 60 (executa isso)
    print("D")
else:
    print("F")