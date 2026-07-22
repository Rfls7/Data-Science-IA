# Crie um programa que leia o nome completo de uma pessoa e mostre:
# 1. O nome com todas as letras maiúsculas
# 2. O nome com todas as letras minúsculas
# 3. Quantas letras ao todo
# 4. Quantas letras o primeiro nome

nome = str(input('Digite o seu nome completo:'))

def exer(a):
    maius = a.upper()
    minus = a.lower()
    qntd = len(a.replace(" ", ""))
    espac = len(a.split()[0])
    return maius, minus, qntd, espac

maius, minus, qntd, espac = exer(nome)

print(f'O nome todo maiúsculo fica:{maius}, O nome todo minúsculo fica:{minus}, A quantidade de letras do nome sem espaço é {qntd}, A quantidade de letras do primeiro nome é {espac}')