# Faça um programa que leia o número de 0 a 9999 e mostre na tela cada um dos dígitos separados
# Ex: Digite um número: 1834
# Unidade = 4 
# Dezena = 3
# Centena = 8
# Milhar = 1

numero = input('Digite um número:')
def separar(a):
    lista = list(str(a))
    unidade = lista[3]
    dezena = lista[2]
    centena = lista[1]
    milhar = lista[0]
    return unidade, dezena, centena, milhar

unidade, dezena, centena, milhar = separar(numero)
print(f'O valor da unidade é {unidade}, o valor da dezena é {dezena}, o valor da centena é {centena} e o valor do milhar é {milhar}.')