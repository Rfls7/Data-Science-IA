# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada
import math

numero = int(input('Digite um número inteiro:'))
def calcular(x):
    dobro = x*2
    triplo = x*3
    raiz = x**(1/2)
    return dobro, triplo, raiz

dobro, triplo, raiz = calcular(numero)

print(f'O número é {numero}, seu dobro é {dobro}, seu triplo é {triplo} e sua raiz é {raiz}')