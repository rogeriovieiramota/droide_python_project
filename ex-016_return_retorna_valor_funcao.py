# Curso: AS 35 PALAVRAS RESERVADAS DO PYTHON versão 3.11.9

print("---------------------------------------------------------------------------------")
print('EXEMPLO - 16. return - Retorna valor de uma função ===\n')
print("---------------------------------------------------------------------------------")



# Exemplo 1: Return básico
def somar(a, b):
    resultado = a + b
    return resultado  # Retorna o valor para quem chamou


# Usando a função
valor = somar(5, 3)
print(f"somar(5, 3) = {valor}")  # 8
print("=================================================================================\n")

# Exemplo 2: Return com condição
def verificar_idade(idade):
    if idade >= 18:
        return "Maior de idade"
    else:
        return "Menor de idade"

print(f"Idade 20: {verificar_idade(20)}")  # Maior de idade
print(f"Idade 15: {verificar_idade(15)}")  # Menor de idade

print("=================================================================================\n")

# Exemplo 3: Return para evitar erro
def dividir(a, b):
    if b == 0:
        return "Erro: divisão por zero"
    return a / b

print(f"10 / 2 = {dividir(10, 2)}")  # 5.0
print(f"10 / 0 = {dividir(10, 0)}")  # Erro: divisão por zero

print("=================================================================================\n")

# Exemplo 4: Return múltiplos valores
def calcular_circulo(raio):
    area = 3.14 * raio ** 2
    perimetro = 2 * 3.14 * raio
    return area, perimetro  # Retorna uma tupla


area, perimetro = calcular_circulo(5)
print(f"Raio 5 -> Área: {area:.2f}, Perímetro: {perimetro:.2f}")
print("=================================================================================\n")

# Exemplo 5: Return precoce (early return)
def processar_pedido(produto, quantidade):
    if quantidade <= 0:
        return "Erro: Quantidade inválida"  # Sai da função aqui

    if produto not in ["camisa", "calça"]:
        return "Erro: Produto não encontrado"  # Sai da função aqui

    return f"Pedido aprovado: {quantidade}x {produto}"


print(processar_pedido("camisa", 3))  # Pedido aprovado: 3x camisa
print(processar_pedido("camisa", -1))  # Erro: Quantidade inválida
print(processar_pedido("bone", 2))  # Erro: Produto não encontrado
print("=================================================================================\n")

# Exemplo 6: Return sem valor (retorna None)
def mostrar_mensagem(texto):
    print(f"Mensagem: {texto}")
    return  # Apenas encerra a função


resultado = mostrar_mensagem("Olá!")
print(f"Valor retornado: {resultado}")  # None
print("=================================================================================\n")

# Exemplo 7: Função sem return (retorna None automaticamente)
def funcao_sem_return(x):
    x = x * 2
    # Não tem return


valor = funcao_sem_return(5)
print(f"Função sem return retorna: {valor}")  # None
print("=================================================================================\n")

# Exemplo 8: Código após return NÃO executa
def funcao_com_problema():
    return "Primeiro valor"
    print("Isso NUNCA será executado")  # Código morto
    return "Segundo valor"  # Também nunca executa


print(f"Retorno: {funcao_com_problema()}")  # Só retorna "Primeiro valor"
print("=================================================================================\n")
print("\n=== FIM DO EXEMPLO 16 ===")