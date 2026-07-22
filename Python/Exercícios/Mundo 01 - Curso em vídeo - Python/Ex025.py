# Crie um programa que leia o nome de uma pessoa e diga se ela tem o "SILVA" no nome

nome = str(input('Digite seu nome:')).upper()

def verificar(a):
    if "SILVA" in a:
        print('Tem')
    else:
        print('Não tem')

haha = verificar(nome)