# Curso: AS 35 PALAVRAS RESERVADAS DO PYTHON versão 3.11.9

print("---------------------------------------------------------------------------------")
print('EXEMPLO 22. as - Cria apelido (alias) para módulos/funções ===\n')
print("---------------------------------------------------------------------------------")
print("=================================================================================\n")

# EXEMPLO COMPLETO DA PALAVRA RESERVADA 'as'
# Usando apenas módulos NATIVOS do Python 3.11.9 (não precisa instalar nada)

# Exemplo 1: Apelido para módulo nativo
import datetime as dt  # datetime agora pode ser chamado de dt

# Usando o apelido
agora = dt.datetime.now()
print("=================================================================================\n")
print(f"Data/hora atual: {agora}")


# Exemplo 2: Apelido para função específica
from math import sqrt as raiz_quadrada
from math import pi as numero_pi

# Usando os apelidos
print("=================================================================================\n")
print(f"Raiz quadrada de 25: {raiz_quadrada(25)}")  # 5.0
print("=================================================================================\n")
print(f"Valor de Pi: {numero_pi}")  # 3.141592653589793


# Exemplo 3: Apelido para módulo com nome longo
import collections as col

# Usando o apelido
contador = col.Counter(['a', 'b', 'c', 'a', 'b', 'a'])
print("=================================================================================\n")
print(f"Contagem de letras: {dict(contador)}")


# Exemplo 4: Múltiplos imports com apelidos
import os as sistema_operacional
import json as js

# Criando arquivo com apelido sistema_operacional
sistema_operacional.makedirs("teste_as", exist_ok=True)
print("=================================================================================\n")
print("Pasta 'teste_as' criada com sucesso!")

# Usando json com apelido js

dados = js.dumps({"nome": "João", "idade": 30}, ensure_ascii=False)
print("=================================================================================\n")
print(f"JSON criado: {dados}")


# Exemplo 5: Apelido em import de sub-módulo
import xml.etree.ElementTree as ET
print("=================================================================================\n")
print(f"Módulo XML importado como 'ET': {ET}")


# Exemplo 6: Apelido para função com nome grande
from statistics import mean as media, median as mediana, stdev as desvio_padrao

numeros = [10, 20, 30, 40, 50]
print("=================================================================================\n")
print(f"Números: {numeros}")
print("=================================================================================\n")
print(f"Média: {media(numeros)}")
print("=================================================================================\n")
print(f"Mediana: {mediana(numeros)}")
print("=================================================================================\n")
print(f"Desvio padrão: {desvio_padrao(numeros):.2f}")


# Exemplo 7: Apelido em tempo de execução (útil para condicionais)
try:
    import tkinter as tk  # Interface gráfica nativa

    print("=================================================================================\n")
    print("Módulo tkinter importado como 'tk'")
except ImportError:
    print("=================================================================================\n")
    print("tkinter não disponível")


# Exemplo 8: Demonstração da utilidade do 'as' com nomes longos
print("=================================================================================\n")
print("\n--- Comparação: Com e sem 'as' ---")

# SEM as (nome completo)
import datetime
data1 = datetime.datetime.now()
print("=================================================================================\n")
print(f"Sem as: {data1}")

# COM as (nome mais curto)
import datetime as dt
data2 = dt.datetime.now()
print("=================================================================================\n")
print(f"Com as: {data2}")

print("\n=== FIM DO EXEMPLO 22 ===")
