# Escreva um programa que leia a velocidade de um arro
# Se ele ultrapassar 80KM/h, mostre uma mensagem dizendo que ele foi multado
# A múlta vai custar R$ 7,00 por cada km acima do limite

velocidade = int(input('Digite a velocidade do carro em km/h:'))
permitido = 80
valor_acima = (velocidade - 80)
multa = valor_acima*7
if velocidade <= 80:
    print(f'Velocidade abaixo do limite, continue assim!')
else:
    print(f'Você foi multado, sua multa é de R${multa: .02f} por estar {valor_acima}km/h acima da velocidade permitida.')
