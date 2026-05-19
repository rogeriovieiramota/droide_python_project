# Curso: AS 35 PALAVRAS RESERVADAS DO PYTHON versão 3.11.9

print("---------------------------------------------------------------------------------")
print('EXEMPLO - 14. pass - Placeholder (faz nada, evita erro de sintaxe)')
print("---------------------------------------------------------------------------------")

def funcao_em_desenvolvimento():
    pass  # Vou implementar depois

class MinhaClasse:
    pass  # Classe vazia por enquanto

# Útil para estruturas ainda não implementadas

#Alternativas e boas práticas rápidas:
#Para indicar claramente que ainda falta implementação, usar raise NotImplementedError() dentro da função, que causa falha proposital quando chamada.
#ex-014_pass_placeholder.pyUsar pass quando quiser apenas evitar erro de sintaxe e não desejar falhar ao chamar o código.