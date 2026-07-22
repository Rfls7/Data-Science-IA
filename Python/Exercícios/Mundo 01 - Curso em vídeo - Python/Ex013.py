# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento

salario = float(input('Digite o valor do seu salário: R$'))
def aumento(a):
    salario = a + (a*0.15)
    return salario

aumento_15 = aumento(salario)
print(f'O valor de salário era de R${salario: .02f} e agora passa a ser de R${aumento_15: .02f} com 15% de aumento.')