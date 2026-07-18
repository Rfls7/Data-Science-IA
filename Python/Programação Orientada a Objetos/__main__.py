from rich import inspect
from classes import Aluno, Professor, Funcionario #Importando as classes do arquivo classes.py

def main():
    a1 = Aluno(nome="João", idade=20, curso="Engenharia", turma="A")
    p1 = Professor(nome="Maria", idade=35, especialidade="Matemática", nivel="Doutorado em Educação")
    f1 = Funcionario(nome="Carlos", idade=40, cargo="Gerente", salario=5000)


    inspect(a1, methods=True)  # aluno só tem curso e turma, nome e idade são herdados da classe Pessoa
    inspect(p1, methods=True)  # professor só tem especialidade e nivel, nome e idade são herdados da classe Pessoa
    inspect(f1, methods=True)  # funcionário só tem cargo e salario, nome e idade são herdados da classe Pessoa

if __name__ == "__main__": 
    main()
    

# if __name__ == "__main__": main() serve para verificar se o arquivo está sendo executado diretamente ou importado como módulo. Se for executado diretamente, o bloco de código dentro do if será executado.