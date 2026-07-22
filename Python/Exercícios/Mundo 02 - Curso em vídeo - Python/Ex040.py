# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
#Média abaixo de 5.0: REPROVADO
#Média entre 5.0 e 6.9: RECUPERAÇÃO
#Média 7.0 ou superior: APROVADO

nota1 = float(input('Digite sua primeira nota: '))
nota2 = float(input('Digite sua segunda nota: '))

def media(a, b):
    media = (a+b)/2
    return media

mediaa = media(nota1, nota2)
print(f'Sua primeira nota foi {nota1}, sua segunda nota foi {nota2} e sua média é {mediaa}')