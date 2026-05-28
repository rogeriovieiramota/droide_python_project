# ex_015_compile.py
"""
ARQUIVO:
DESCRIÇÃO: Demonstração de todas as 71 funções built-in do Python 3.11.9
Funções Built-in (Embutidas)
EXECUÇÃO: Rode diretamente no PyCharm 2024.1.1 Community Edition
AUTOR: Rogerio V. Mota
"""

print("---------------------------------------------------------------------------------")
print('EXEMPLO - 15. compile() - Compila código fonte em objeto de código')
print("---------------------------------------------------------------------------------")

codigo = compile("print('Olá mundo')", "<string>", "exec")
exec(codigo)
print("=================================================================================\n")
print("Código compilado e executado com sucesso!")

"""
Seu código Python
       │
       ▼
┌─────────────────────────────────────────────────────────────┐
│  codigo = compile("print('Olá mundo')", "<string>", "exec") │
└─────────────────────────────────────────────────────────────┘
       │
       ▼
┌─────────────────────────────────────────────────────────────┐
│         O Python compila o código na HORA                   │
│         Resultado fica na MEMÓRIA RAM                       │
│                                                             │
│ ┌─────────────────────────────────────────────────────────┐ │
│ │           OBJETO CODE (na memória RAM)                  │ │
│ │  ┌─────────────────────────────────────────────────────┐│ │
│ │  │  Instruções em bytecode (prontas para executar)     ││ │
│ │  │  Ex: b'\x00\x01\x02\x03...' (código intermediário)  ││ │
│ │  └─────────────────────────────────────────────────────┘│ │
│ └─────────────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────────┘
       │
       ▼
┌─────────────────────────────────────────────────────────────┐
│  exec(codigo)  ← Executa o código que está na memória       │
└─────────────────────────────────────────────────────────────┘
       │
       ▼
┌─────────────────────────────────────────────────────────────┐
│  Após execução: objeto code É PERDIDO (se não for guardado) │
└─────────────────────────────────────────────────────────────┘
"""