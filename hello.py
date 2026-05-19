# No Python, não precisamos de classes para rodar um script simples!

def main():
    # Definição de variáveis (Tipagem dinâmica, mas forte)
    nome = "Desenvolvedor"
    versao_python = "3.11.9"

    # O f-string é o equivalente ao String.format() do Java, mas muito mais elegante
    print(f"Olá, {nome}!")
    print(f"Seu ambiente Python {versao_python} está configurado com sucesso no Windows 11.")

    # Exemplo de loop simples
    print("\nIniciando contagem de prontidão:")
    for i in range(1, 4):
        print(f"Passo {i}... OK")


# Esta é a boa prática para scripts: garante que o código só rode
# se o arquivo for executado diretamente (o "main" do Java)
if __name__ == "__main__":
    main()