# Classe Funcionário: Implemente a classe Funcionário. Um empregado tem um nome (um string) e um salário(um double).
#  Escreva um construtor com dois parâmetros (nome e salário) e métodos para devolver nome e salário.
#  Escreva um pequeno programa que teste sua classe.

class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    # def detalhe(self):
    #     print(f'Nome: {self.nome}\nSalário: {self.salario}')

    def get_nome(self):
        return self.nome

    def get_salario(self):
        return self.salario

     

funcionario_1 = Funcionario('Jadielson', 1800)

print('Nome:' ,funcionario_1.get_nome(),'\nSalário: ',funcionario_1.get_salario())


