# Crie um programa que leia um  número Real qualquer pelo teclado e mostre na tela sua porção inteira
#ex: Número qualquer = 6.23, porção inteira = 6

numero = float(input('Digite um número qualquer:'))
def calcular_inteiro(a):
    inteiro = round(a)
    return inteiro

inter = calcular_inteiro(numero)
print(f'O valor informado foi {numero} e seu valor inteiro é {int(inter)}')6.9