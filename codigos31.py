import datetime

class Pessoa:
    ano_atual = datetime.datetime.now().year

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    
    def get_ano_nascimento(self):
        return Pessoa.ano_atual - self.idade


pessoa_1 = Pessoa('João', 28)
pessoa_2 = Pessoa('Carla', 22)
print(pessoa_1.get_ano_nascimento())
print(pessoa_2.get_ano_nascimento())
pessoa_1.__dict__['sexo'] = 'Masculino'
pessoa_2.__dict__['sexo'] = 'Feminino'
print(pessoa_1.__dict__)
print(pessoa_2.__dict__)
print(vars(pessoa_1))
print(vars(pessoa_2))
del pessoa_1.__dict__['nome']
del pessoa_2.__dict__['sexo']
print(pessoa_1.__dict__)
print(pessoa_2.__dict__)
print(pessoa_1.sexo)
print(pessoa_2.nome)
