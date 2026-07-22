# Desenvolva um programa que pergunte a distância de uma viagem em KM. 
# Calcule o preço da passagem, cobrando R$ 0,50 por KM para viagens de até 200Km e R$0,45 para viagens mais longas

distancia = int(input('Digite a distância da sua viagem em KM: '))
if distancia <= 200:
    preco = 0.50
    preco_final = distancia * preco
    print(f'O preço da sua viagem é de R$ {preco_final: .02f}')
else:
    preco1 = 0.45
    preco_final1 = distancia * preco1
    print(f'O preço da sua viagem é de R$ {preco_final1: .02f}')