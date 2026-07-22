# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros

valor = int(input('Digite um valor em metros:'))
def converter(a):
    centimetros = a*100
    milimetros = a*1000
    return centimetros, milimetros

cent, mil = converter(valor)
print(f'O valor informado em metros é {valor}metro, o valor em centímetros é {cent}cm e o valor em milímetros é {mil}mm')