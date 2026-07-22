#  Desenvolva um programa que leia as duas notas de um anulo, calcule e mostre sua média

nota1 = float(input('Digite a primeira nota:'))
nota2 = float(input('Digite a segunda nota:'))

def media(a, b):
    media = (nota1 + nota2) /2
    return media

media_calculada = media(nota1, nota2)

print(f'A primeira nota do aluno é {nota1}, a segunda nota é {nota2} e a média das notas é {media_calculada}')
