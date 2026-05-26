# Curso: AS 35 PALAVRAS RESERVADAS DO PYTHON versão 3.11.9

print("---------------------------------------------------------------------------------")
print('EXEMPLO ->34. async - Define função assíncrona  ===\n')
print("---------------------------------------------------------------------------------")
print("=================================================================================\n")

"""

async - Define função assíncrona

"""

import asyncio

# Função assíncrona (pode usar await dentro)
async def tarefa_demorada():
    print("Início da tarefa")
    await asyncio.sleep(1)
    print("Tarefa completada")
    return "OK"

async def executar_tudo():
    # Executa várias tarefas "simultaneamente"
    tarefas = [tarefa_demorada() for _ in range(3)]
    resultados = await asyncio.gather(*tarefas)
    print(f"Todos resultados: {resultados}")

#asyncio.run(executar_tudo())  # Descomente para testar