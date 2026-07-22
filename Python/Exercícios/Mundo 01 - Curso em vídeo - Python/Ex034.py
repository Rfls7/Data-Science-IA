# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento
# Para salários superiores a R$ 1.200,00, calcule um aumento de 10%
# Para os inferiores ou igual, o aumento é de 15%

salario = float(input('Digite seu salário em R$: '))
if salario > 1200: 
    aumento = salario + (salario*0.1)
else:
    aumento = salario + (salario*0.15)

print(f'Seu salário atual é de R$ {salario: .02f} e com o aumento ele passa a ser de R${aumento: .02f}')