
class Pessoa:
    cpf = '1234'
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrnome = sobrenome

    def falar_nome_classe(self):
        print('Estou na Classe Pessoa')
        print(self.nome, self.sobrnome, self.__class__.__name__)


class Cliente(Pessoa):
     def falar_nome_classe(self):
        print('Estou na Classe cliente')
        print(self.nome, self.sobrnome, self.__class__.__name__)
    

class Aluno(Pessoa):
    cpf = 'Aluno cpf'
    ...

cliente_1 = Cliente('Jadielson', 'Silva')
cliente_1.falar_nome_classe()
aluno_1 = Aluno('Luiz', 'Otávio')
aluno_1.falar_nome_classe()
print(aluno_1.cpf)
print(Pessoa.cpf)
help(Cliente)
