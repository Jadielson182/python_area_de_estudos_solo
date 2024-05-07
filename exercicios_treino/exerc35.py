# Aprimore a classe do exercício anterior para adicionar o método aumentarSalario (porcentualDeAumento) 
# que aumente o salário do funcionário em uma certa porcentagem.
# Exemplo de uso:
#   harry=funcionário("Harry",25000)
#   harry.aumentarSalario(10)class Funcionario:

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

    def porcentual_de_aumento(self, porcentual):
        aumento = (self.salario / 100) * porcentual
        self.salario += aumento
        return self.salario

     

funcionario_1 = Funcionario('Jadielson Silva', 1800)

print('Nome:' ,funcionario_1.get_nome(),
'\nSalário: ',funcionario_1.get_salario(),
'\nNovo Salário: ',funcionario_1.porcentual_de_aumento(10))
