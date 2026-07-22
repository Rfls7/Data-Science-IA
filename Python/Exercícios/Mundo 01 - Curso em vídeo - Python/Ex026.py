# Faça um programa que leia uma frase e mostre:
# 1. Quantas vezes aparece a letra A
# 2. Em que posição ela aparece na primeira vez
# 3. Em que posição ela aparece a última vez

# .strip() remove espaços inúteis no início e fim. 
# .lower() transforma tudo em minúsculo para contar tanto 'A' quanto 'a'.
frase = str(input('Digite uma frase: ')).strip().lower()

def analisar_frase(texto):
    # 1. Conta quantas vezes a letra 'a' aparece
    contador = texto.count('a')
    
    if contador > 0:
        # 2. Encontra a primeira posição (somamos 1 para ficar humano: ex. posição 1 em vez de 0)
        primeira_pos = texto.index('a') + 1
        
        # 3. Encontra a última posição usando rindex (funciona direto na string)
        ultima_pos = texto.rindex('a') + 1
        
        return contador, primeira_pos, ultima_pos
    else:
        return 0, None, None

# Executa a função passando a frase digitada
contador, primeira_vez, ultima_vez = analisar_frase(frase)

# Exibe os resultados
if contador > 0:
    print(f'\nA letra "A" aparece {contador} vezes na frase.')
    print(f'A primeira letra "A" apareceu na posição {primeira_vez}.')
    print(f'A última letra "A" apareceu na posição {ultima_vez}.')
else:
    print('\nA frase não contém a letra "A".')

