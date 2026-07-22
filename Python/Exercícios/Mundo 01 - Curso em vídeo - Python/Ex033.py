# Faça um programa que leia três números e mostre qual é o maior e qual é o menor

numero1 = float(input('Digite o primeiro número: '))
numero2 = float(input('Digite o segundo número: '))
numero3 = float(input('Digite o terceiro número: '))
lista = [numero1, numero2, numero3]
def verificar_maior_menor(a):
    maior = max(lista)
    menor = min(lista)
    return maior, menor

maior, menor = verificar_maior_menor(lista)
print(f'O maior valor é {maior} e o menor é {menor}')