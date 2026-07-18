class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def fazer_aniversario(self):
        self.idade += 1


class Aluno(Pessoa):
    def __init__(self, nome, idade, curso, turma):
        super().__init__(nome, idade) # Chamando o método construtor da classe pai (Pessoa) para inicializar os atributos nome e idade
        self.curso = curso
        self.turma = turma

    def fazer_matricula(self, curso, turma):
        pass


class Professor(Pessoa):
    def __init__(self, nome, idade, especialidade, nivel):
        super().__init__(nome, idade) # Chamando o método construtor da classe pai (Pessoa) para inicializar os atributos nome e idade
        self.especialidade = especialidade
        self.nivel = nivel

    def dar_aula(self):
        pass


class Funcionario(Pessoa):
    def __init__(self, nome, idade, cargo, salario):
        super().__init__(nome, idade) # Chamando o método construtor da classe pai (Pessoa) para inicializar os atributos nome e idade
        self.cargo = cargo
        self.salario = salario

    def bater_ponto(self):
        pass