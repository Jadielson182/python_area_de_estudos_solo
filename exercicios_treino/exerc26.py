# Classe Conta Corrente: Crie uma classe para implementar uma conta corrente.
#  A classe deve possuir os seguintes atributos: número da conta, nome do correntista e saldo. Os métodos são os seguintes: alterarNome,
#  depósito e saque; No construtor, saldo é opcional, com valor default zero e os demais atributos são obrigatórios.

class ContaCorrente:
    def __init__(self, numero_conta, nome_correntista, saldo=0):
        self.numero_conta = numero_conta
        self.nome_correntista = nome_correntista
        self.saldo = saldo


    def alterar_nome(self, novo_nome):
        self.nome_correntista = novo_nome
        print(f'O nome do correntista foi alterado para { self.nome_correntista}')

    def depositar(self, valor):
        self.saldo += valor 
        self.detalhe(f'Confirmado deposito de R$ R${valor},00.')

    def saque(self, valor):
        if self.saldo > valor:
            self.saldo -= valor
            self.detalhe(f'Confirmado saque de R${valor},00.')
        if self.saldo < valor:
            self.detalhe(f'Saque de {valor} negado, saldo insuficiente. ')
        
    def detalhe(self, msg):
        print(f'{msg} O saldo da conta {self.numero_conta} no nome de {self.nome_correntista} é de R$ {self.saldo},00')



conta_1 = ContaCorrente(521469, 'Jadielson Silva', 1000)
conta_2 = ContaCorrente(457896, 'Carlos Silva')
conta_3 = ContaCorrente(789654, 'Maria Helena', 500)
print(conta_1.nome_correntista)
print()
conta_1.depositar(500)
conta_1.saque(500)
conta_1.alterar_nome('Joao Carlos')
print()
print(conta_2.nome_correntista)
conta_2.depositar(600)
conta_2.saque(700)
conta_2.alterar_nome('Joao Carlos')
print()
print(conta_3.nome_correntista)
print()
conta_3.depositar(1500)
conta_3.saque(1600)
conta_3.alterar_nome('Maria Aparecida')
print()