# Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
#– O primeiro valor é maior
#– O segundo valor é maior
#– Não existe valor maior, os dois são iguais

numero1 = float(input('Digite um número qualquer: '))
numero2 = float(input('Digite outro número qualquer: '))
lista = [numero1, numero2]
def verifica(a):
    maior = max(lista)
    menor = min(lista)
    return maior, menor

maior, menor = verifica(lista)
print(f'O maior valor foi o {maior} e o menor foi o {menor}')