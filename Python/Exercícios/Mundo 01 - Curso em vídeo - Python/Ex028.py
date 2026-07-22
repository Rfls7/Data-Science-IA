# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça pro usuário tentar descobrir qual foi o número escolhido pelo computador.
# O usuário deverá escrever na tela se o usuário venceu ou perdeu.

import random 
pensado_pelo_pc = random.randint(0,5)

valor = int(input('Escreva um númeiro inteiro para tentar acertar o mesmo número "pensado" pelo computador, lembrando que é um valor entre 0 e 5: '))
if valor == pensado_pelo_pc:
    print(f'Meu Deus! Você acertou na mosca! o número "pensado" pelo computador foi {pensado_pelo_pc}')
else:
    print(f'Você errou, o número "pensado" pelo computador foi {pensado_pelo_pc}')