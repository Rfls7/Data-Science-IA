# Um professor quer sortear um dos seus quatro alunos para apagar um quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome escolhido

aluno1 = str(input('Digite o nome do primeiro aluno:'))
aluno2 = str(input('Digite o nome do segundo aluno:'))
aluno3 = str(input('Digite o nome do terceiro aluno:'))
lista = [aluno1, aluno2, aluno3]
def random(a):
    import random
    escolhido = random.choice(a)
    return escolhido

esco = random(lista)
print(f'O nome escolhido foi o {esco}')
    
