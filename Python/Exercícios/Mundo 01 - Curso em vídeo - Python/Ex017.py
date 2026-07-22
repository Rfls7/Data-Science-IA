# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimeiro da hipotenusa

oposto = float(input('Digite o valor do cateto oposto:'))
adjacente = float(input('Digite o valor do cateto adjacente:'))

def triangulo_ret(a, b):
    import math
    hipotenusa = math.hypot(a, b)
    return hipotenusa

hipo = triangulo_ret(oposto, adjacente)
print(f'O valor do cateto oposto é {oposto}, o valor do cateto adjacente é {adjacente} e o comprimento da hipotenusa é {hipo}')