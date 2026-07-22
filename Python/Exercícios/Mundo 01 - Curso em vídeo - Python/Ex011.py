# Faça um programa que leia a largura e a altura de uma paradeem metros, calcule a sua área e a quantidade de tinta necessária para printá-lo, 
# sabendo que cada litro de tinta, pinta uma área de 2m quadrados:

largura = float(input('Digite a largura em metros:'))
altura = float(input('Digite a altura em metros:'))

def area(a, b):
    area = a*b
    tinta = area/2
    return area, tinta

area1, tinta = area(largura, altura)
print(f'A largura informada foi de {largura}m, a altura informada foi de {altura}m. Sua área é de {area1}m2 e a quantidade de tinta necessária para pintar é de {tinta}litros')
