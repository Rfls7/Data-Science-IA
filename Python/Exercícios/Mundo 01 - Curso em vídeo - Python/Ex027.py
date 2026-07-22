# Faça um programa que leia o nome completo de uma pessoa, mostrnado em seguida o primeiro e o último nome separadamente.

nome = str(input('Digite o nome completo aqui:'))

def verificar(a):
    primeiro_nome = nome.split()[0]
    ultimo_nome = nome.split()[-1]
    return primeiro_nome, ultimo_nome

primeiro_nome, ultimo_nome = verificar(nome)
print(f'O primeiro nome é {primeiro_nome} e o último nome é {ultimo_nome}')