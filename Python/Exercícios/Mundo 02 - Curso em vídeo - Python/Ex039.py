#  Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, 
# se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. 
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

ano = int(input('Digite o ano de nascimento: '))
current = 2026
idade = current - ano
alistamento = 18
falta = alistamento - idade
if idade == alistamento:
    print('Você deverá se alistar ainda esse ano!')
elif idade < alistamento:
    print(f'Ainda faltam {falta} anos para que você se aliste!')
elif idade > alistamento:
    print(f'Você está {falta*-1} anos atrasado para se alistar, procure uma junta militar urgentemente!')
