# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. 
# Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. 
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

valor = float(input('Digite o valor da casa que quer financiar em R$: '))
salario = float(input('Digite o seu salário em R$: '))
anos = int(input('Digite em quantos anos deseja pagar: '))

prestacao_trashold = salario*0.3
meses = anos*12
prestacao = valor/meses

if prestacao > prestacao_trashold:
    print(f'O valor do seu salário é R${salario: .02f}')
    print(f'O valor do imóvel é R${valor: .02f}')
    print(f'O valor máximo para comprometimento de sua renda disponível é de R${prestacao_trashold: .02f}')
    print(f'O valor da prestação deste imóivel é de R${prestacao: .02f}')
    print('O valor da prestação excede o limite de 30% da sua renda, empréstimo negado!')
else:
    print(f'O valor do seu salário é R${salario: .02f}')
    print(f'O valor do imóvel é R${valor: .02f}')
    print(f'O valor máximo para comprometimento de sua renda disponível é de R${prestacao_trashold: .02f}')
    print(f'O valor da prestação deste imóivel é de R${prestacao: .02f}')
    print('Empréstimo aprovado!')