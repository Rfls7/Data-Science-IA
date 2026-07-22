# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar


valor = float(input('Digite quanto você quer converter: R$'))
def converter_dolar(a):
    dolar = 5.08
    valor_convertido = a*dolar
    return valor_convertido

valor_convertido = converter_dolar(valor)
print(f'O valor informado foi R${valor} e o valor em dólar é ${valor_convertido}')