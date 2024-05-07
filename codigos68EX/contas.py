import abc
class Conta(abc.ABC):
    def __init__(self,agencia, conta, saldo=0):
        self.agencia = agencia
        self.conta = conta
        self.saldo = saldo
    @abc.abstractclassmethod
    def sacar(self, valor):...

    def depositar(self, valor):
        self.saldo += valor
        self.detales(f'Deposito {valor}')

    
    def detales(self, msg):
        print(f'O seu saldo é de {self.saldo:.2f} {msg}')
        

class ContaPoupanca(Conta):
    def sacar(self, valor):
        valor_pos_saque = self.saldo - valor
        if valor_pos_saque > 0:
            self.saldo -= valor_pos_saque
            self.detales(f' O SAQUE DE {valor} FOI EFETUADO')
            return self.saldo
        print('Não foi possivel sacar o valor desejado')
        self.detales((f'SAQUE DE {valor} FOI NEGADO'))
        
    def __repr__(self):
        class_name = type(self).__name__
        attrs = f'({self.agencia!r}, {self.conta!r}, {self.saldo})'
        return f'{class_name}{attrs}'       

class ContaCorrente(Conta):
    def __init__(self,agencia, numero, saldo=0, limite=0):
        super().__init__(agencia, numero, saldo)
        self.limite = limite


    def sacar(self, valor):
        valor_pos_saque = self.saldo - valor
        limite_maximo = -self.limite
 
        if valor_pos_saque >= limite_maximo:
            self.saldo -= valor
            self.detales(f' (O SAQUE DE {valor} FOI EFETUADO)')
            return self.saldo
        print('Não foi possivel sacar o valor desejado.')
        print(f'Seu Limite é  {-self.limite:.2f}')
        self.detales((f'(SAQUE NEGADO {valor})'))


    def __repr__(self):
        class_name = type(self).__name__
        attrs = f'({self.agencia!r}, {self.conta!r}, {self.saldo}, {self.limite})'
        return f'{class_name}{attrs}'  


if __name__ == '__main__':
    conta_poupanca_1 = ContaPoupanca(3614, 62145, 5)
    conta_poupanca_1.sacar(2)
    conta_poupanca_1.depositar(80)
    conta_poupanca_1.sacar(50)
    conta_poupanca_1.sacar(20)

    conta_corrente_1 = ContaCorrente(3614, 62145, 0, 100)
    conta_corrente_1.sacar(1)
    conta_corrente_1.depositar(1)
    conta_corrente_1.sacar(1)
    conta_corrente_1.sacar(1)
    conta_corrente_1.sacar(98)
    conta_corrente_1.sacar(1)