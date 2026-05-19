"""
EXEMPLO COMPLETO com todas as principais palavras reservadas
- Funciona no PyCharm 2024.1.1 no Windows 11
- Python 3.11.9
"""


def main():
    print("=" * 50)
    print("DEMONSTRAÇÃO DE PALAVRAS RESERVADAS PYTHON 3.11.9")
    print("=" * 50)

    # 1. Booleanos e None
    print("-" * 50)
    print("\n[Booleanos e None]")
    ativo = True
    inativo = False
    valor_vazio = None

    print(f"Ativo: {ativo}, Inativo: {inativo}, Vazio: {valor_vazio}")

    # 2. Estruturas condicionais (if, elif, else)
    print("-" * 50)
    print("\n[Estruturas Condicionais]")
    nota = 85

    if nota >= 90:
        conceito = "A"
    elif nota >= 80:
        conceito = "B"  # Vai executar este
    elif nota >= 70:
        conceito = "C"
    else:
        conceito = "F"

    print(f"Nota {nota} = Conceito {conceito}")

    # 3. Operadores lógicos (and, or, not)
    print("-" * 50)
    print("\n[Operadores Lógicos]")
    idade = 25
    tem_carteira = True

    if idade >= 18 and tem_carteira:
        print("Pode dirigir (and)")

    if idade < 18 or tem_carteira:
        print("Pode fazer algo (or)")

    if not False:
        print("Not inverte valores booleanos")

    # 4. Laços de repetição (for, while)
    print("-" * 50)
    print("\n[Laços de Repetição]")

    # For com range
    print("For com range:")
    for i in range(1, 4):
        print(f"  Contagem {i}")

    # While
    print("-" * 50)
    print("While:")
    contador = 1
    while contador <= 3:
        print(f"  Volta {contador}")
        contador += 1

    # 5. Break e Continue
    print("-" * 50)
    print("\n[Break e Continue]")
    print("Break (para no 5):")
    for i in range(1, 8):
        if i == 5:
            break
        print(f"  {i}", end=" ")

    print("-" * 50)
    print("\nContinue (pula o 3):")
    for i in range(1, 6):
        if i == 3:
            continue
        print(f"{i}", end=" ")

    # 6. Def, Return e Lambda
    print("-" * 50)
    print("\n\n[Funções e Lambda]")

    def somar(a, b):
        return a + b

    dobrar = lambda x: x * 2

    print(f"Somar 5+3 = {somar(5, 3)}")
    print(f"Dobrar 7 = {dobrar(7)}")

    # 7. Try, Except, Finally
    print("-" * 50)
    print("\n[Tratamento de Erros]")
    try:
        resultado = 10 / 0
    except ZeroDivisionError:
        print("Erro capturado: Divisão por zero")
    finally:
        print("Isso sempre executa!")

    # 8. Classes
    print("-" * 50)
    print("\n[Classes e Objetos]")

    class Carro:
        def __init__(self, marca, modelo):
            self.marca = marca
            self.modelo = modelo

        def info(self):
            return f"{self.marca} {self.modelo}"

    carro1 = Carro("Toyota", "Corolla")
    print(f"Carro: {carro1.info()}")

    # 9. Assert (debugging)
    print("-" * 50)
    print("\n[Assert - Validação]")
    x = 10
    assert x > 0, "x deve ser positivo"
    print(f"Assert passou: x={x} é positivo")

    # 10. Yield (geradores)
    print("-" * 50)
    print("\n[Yield - Gerador]")

    def gerar_pares(limite):
        for i in range(0, limite, 2):
            yield i

    for num in gerar_pares(10):
        print(f"  {num}", end=" ")

    # 11. With (gerenciador de contexto)
    print("-" * 50)
    print("\n\n[With - Arquivo]")
    with open("teste_pycharm.txt", "w") as arquivo:
        arquivo.write("Testando palavras reservadas do Python 3.11.9!")
    print("Arquivo 'teste_pycharm.txt' criado com sucesso!")

    print("\n" + "=" * 50)
    print("EXECUÇÃO CONCLUÍDA COM SUCESSO!")
    print("=" * 50)


# Ponto de entrada principal
if __name__ == "__main__":
    main()