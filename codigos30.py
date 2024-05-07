
import datetime

class Pessoa:
    ano_atual = datetime.datetime.now().year

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        # self.ano_atual = 2023

    def get_ano_nascimento(self):
        return Pessoa.ano_atual - self.idade

    
pessoa_1 = Pessoa('João', 35)
pessoa_2 = Pessoa('Helena', 12)

# print(Pessoa.ano_atual)

print(pessoa_1.get_ano_nascimento())
print(pessoa_2.get_ano_nascimento())