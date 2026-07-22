# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

preco = float(input('Digite o preço de um produto: R$'))
def desconto(a):
    cinco = a - (a*0.05)
    return cinco

desconto_5 = desconto(preco)
print(f'O valor informado é de R${preco: .02f} e o valor com o desconto de 5% é de R${desconto_5: .02f}')