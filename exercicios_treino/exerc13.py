# Crie uma classe chamada Funcionario que tenha atributos como nome, salário e método para calcular o
#  salário líquido após descontos.Em seguida,crie uma classe Departamento que contém uma
#   lista de funcionários e métodos para adicionar, remover e listar funcionários.


class Funcionario:
    def __init__(self,nome, salario):
        self.nome = nome
        self.salario = salario
        

    def salario_liquido(self,taxa):
        desconto  =(( self.salario / 100) * taxa)
        self.salario = self.salario - desconto
        return f'{self.salario}'


    def __repr__(self):
        class_name = type(self).__name__
        atributos = f'(Nome: "{self.nome}"), (Salario: "{self.salario:.2f}")'
        return f'{class_name} {atributos}'

class Departamento(Funcionario):
    def __init__(self):
        self.lista_de_funcionarios = []

    def adicionar_funcionario(self, funcionario):
        self.lista_de_funcionarios.append(funcionario)
        
    
    def remover_funcionario(self,funcionario):
        self.lista_de_funcionarios.remove(funcionario)

    def listar_funcionarios(self):
        for funcionario in self.lista_de_funcionarios:
            print(f'{funcionario}')
        
    def __repr__(self):
        class_name = type(self).__name__
        atributos = f'({self.nome!r}) ({self.salario!r})'
        return f'{class_name} {atributos}'


departamento = Departamento()
funcionario_1 = Funcionario('Jadielson', 2600)
funcionario_1.salario_liquido(12)
departamento.adicionar_funcionario(funcionario_1)
departamento.remover_funcionario(funcionario_1)

funcionario_2 = Funcionario('Joao', 2000)
funcionario_2.salario_liquido(9)
departamento.adicionar_funcionario(funcionario_2)
# departamento.remover_funcionario(funcionario_2)

funcionario_3 = Funcionario('Carlos', 1900)
funcionario_3.salario_liquido(9)
departamento.adicionar_funcionario(funcionario_3)

funcionario_4= Funcionario('Mateus', 1320)
funcionario_4.salario_liquido(7.5)
departamento.adicionar_funcionario(funcionario_4)

funcionario_5 = Funcionario('Fabio', 3900)
funcionario_5.salario_liquido(14)
departamento.adicionar_funcionario(funcionario_5)
print('Lista Atualizada de Funcionarios')
print()
departamento.listar_funcionarios()
print()
print('Lista Inicial\n'
    f'\nNome: {funcionario_1.nome},  Salario: {funcionario_1.salario:.2f}\n'
f'Nome: {funcionario_2.nome},  Salario: {funcionario_2.salario:.2f}\n'
f'Nome: {funcionario_3.nome},  Salario: {funcionario_3.salario:.2f}\n'
f'Nome: {funcionario_4.nome},  Salario: {funcionario_4.salario:.2f}\n'
f'Nome: {funcionario_5.nome},  Salario: {funcionario_5.salario:.2f}')


# Faixa de salário	Alíquota Aplicada
# Até um salário-mínimo (R$ 1.320,00 em 2023)	7,5%
# R$ 1.320,01 até R$ 2.571,29	9%
# R$ 2.571,30 até R$ 3.856,94	12%
# De R$ 3.856,95 até R$ 7.507,49 (Teto do INSS em 2023)	14%




# def salario_liquido(self):
#         desconto = self.salario
#         if self.salario <= 1320:
#             self.salario = (self.salario / 100) * 7.5
#         elif self.salario > 1320 and self.salario <= 2570:
#             self.salario = (self.salario / 100) * 9
#         elif self.salario > 2570 and self.salario <= 3856:
#             self.salario = (self.salario / 100) * 12
#         elif self.salario > 3856 and self.salario < 7500:
#             self.salario = (self.salario / 100) * 14
#             self.salario_descontado = self.salario
#         return f'{self.salario_descontado}'
