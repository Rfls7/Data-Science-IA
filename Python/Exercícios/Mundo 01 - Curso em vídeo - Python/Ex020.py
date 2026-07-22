# O mesmo professor do desafio anterior quer sortear a ordem de apresentaçõa de trabalhos dos alunos. 
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada. 
aluno1 = str(input('Digite o nome do primeiro aluno:'))
aluno2 = str(input('Digite o nome do segundo aluno:'))
aluno3 = str(input('Digite o nome do terceiro aluno:'))
aluno4 = str(input('Digite o nome do quarto aluno:'))
lista = [aluno1, aluno2, aluno3, aluno4]
def sortear_ordem(a):
    import random
    random.shuffle(a)
    return a
sorteamento = sortear_ordem(lista)
print(f'A ordem sorteada foi: {sorteamento}')