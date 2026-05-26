# Curso: AS 35 PALAVRAS RESERVADAS DO PYTHON versão 3.11.9

print("---------------------------------------------------------------------------------")
print('EXEMPLO ->33 in - Verifica se um elemento existe em sequência  ===\n')
print("---------------------------------------------------------------------------------")
print("=================================================================================\n")

"""

is - in - Verifica se um elemento existe em sequência

"""

import asyncio

async def buscar_dados():
    """Simula busca de dados demorada"""
    await asyncio.sleep(2)  # Espera 2 segundos
    return "Dados carregados"

async def main():
    print("Buscando...")
    resultado = await buscar_dados()  # Aguarda a função terminar
    print(f"Resultado: {resultado}")

# Executar função assíncrona
#asyncio.run(main())  # Descomente para testar
