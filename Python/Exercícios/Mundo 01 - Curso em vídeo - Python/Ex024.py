# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO"

cidade = str(input('Digite o nome de uma cidade: ')).strip()

def verificar(a):
    # .startswith() garante que a string começa com a palavra digitada
    if a.upper().startswith("SANTO"):
        print('A cidade começa com "SANTO"')
    else:
        print('A cidade NÃO começa com "SANTO"')

verificar(cidade)