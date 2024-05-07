import datetime

class Pessoa:
    ano = datetime.datetime.now().year

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @classmethod
    def metodo_de_classe(cls):
        print('ClassMethod')

    @classmethod
    def criar_com_50_anos(cls, nome):
        return cls(nome, 50)

    @classmethod
    def criar_sem_nome(cls, idade):
        return cls('Anônimo', idade)


pessoa_1 = Pessoa('João', 32)
pessoa_3 = Pessoa.criar_com_50_anos('Maria')
pessoa_4 = Pessoa('Anonima', 37)
pessoa_5 = Pessoa.criar_sem_nome(35)

print(pessoa_1.nome, pessoa_1.idade)
pessoa_2 = Pessoa.metodo_de_classe()
print(pessoa_3.nome, pessoa_3.idade)
print(pessoa_4.nome, pessoa_4.idade)
print(pessoa_5.nome, pessoa_5.idade)
print(Pessoa.ano)