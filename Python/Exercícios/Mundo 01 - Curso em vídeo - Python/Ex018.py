# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo

angulo = int(input('Digite o valor de um ângulo:'))
def seno_cos_tan(a):
    import math
    rad = math.radians(a)
    seno = math.sin(rad)
    cosseno = math.cos(rad)
    tangente = math.tan(rad)
    return seno, cosseno, tangente

seno, cosseno, tangente = seno_cos_tan(angulo)
print(f'O ângulo informado foi de {angulo}, o seno é {seno}, o cosseno é {cosseno} e a tangente é {round(tangente)}')
