#Crie uma classe chamada ContaBancaria com métodos para depositar, sacar e verificar o saldo.
#Adicione também um método extrato que imprima um extrato com as transações realizadas.

class ContaBancaria:
    def __init__(self,saldo=0):
        self.saldo = saldo


    def depositar(self, depositar):
        self.saldo = self.saldo + depositar
        self.extrato(f'deposito de R${depositar:.2f}')
        return self.saldo


    def sacar(self, valor):
        saldo_atual = self.saldo - valor
        if saldo_atual < 0:
            raise print('Saldo insuficiente, saque foi negado.')
        self.saldo = self.saldo - valor
        self.extrato(f'saque de R${valor:.2f}')
        return self.saldo



    def verificar_saldo(self):
        print(f'O seu saldo atual é {self.saldo:.2f}')


    def extrato(self, msg):
        print(f'Voçe fez um {msg}. O seu saldo atual é R${self.saldo:.2f}')

    def __repr__(self):
        class_name = type(self).__name__
        formatacao = f'{self.saldo!r}'
        return f'({class_name}- {formatacao})'


conta_1 = ContaBancaria(1000)
conta_1.depositar(500)
conta_1.sacar(300)
conta_1.depositar(800)
conta_1.sacar(500)
conta_1.depositar(2000)
conta_1.verificar_saldo()
print(conta_1)





