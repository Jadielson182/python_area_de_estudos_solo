# Crie uma classe ContaBancaria com métodos para depositar, sacar e consultar saldo.
#  Em seguida, crie duas subclasses, ContaCorrente e ContaPoupanca,
#  que herdam da classe base, mas têm regras específicas para taxas e limites.
import abc
class ContaBancaria:
    def __init__(self, nome, banco, saldo=0):
        self.nome = nome
        self.banco = banco
        self.saldo = saldo

    @abc.abstractmethod
    def sacar(self, taxa, valor):
        ...


    def depositar(self, valor):
        self.saldo += valor
        self.detales(f'O valor do Deposito foi {valor}')
        
    def consultar_saldo(self):
        print(f'O seu salto é de {self.saldo}')

    def detales(self, mensagem):
        print(f'{mensagem} Seu saldo atual é {self.saldo}. ')

class ContaCorrente(ContaBancaria):
    def __init__(self, nome, banco, saldo=0, limite=0):
        super().__init__(nome, banco, saldo)
        self.limite = limite


    def sacar(self, taxa, valor):
        valor_saque = self.saldo - (valor + taxa)
        limite_maiximo = - self.limite
        if valor_saque >= limite_maiximo:
            self.saldo -= valor
            self.saldo -= taxa
            self.detales(f'O valor do saque foi R${valor} com uma taxa de R${taxa}.')
            return self.saldo
        print(f'Nao foi possivel realizar o saque no valor de {valor}')
        print(f'Seu limite é {self.limite}')
        self.detales(f'Saque no valor de {valor} foi negado,')

            
    

class ContaPoupanca(ContaBancaria):
    def sacar(self,valor):
        valor_pos_saque = self.saldo - valor
        # print(valor_pos_saque)
        if valor_pos_saque > 0:
            self.saldo -= valor
            self.detales(f'O valor do saque foi de {valor}')
            return self.saldo
        print(f'Não foi posivel sacar o valor desejado')
        self.detales(f'Saque de {valor} foi negado.')


cliente_1  = ContaCorrente('Jadielson', 'itau', 100, 100)
# cliente_1  = ContaPoupanca('Jadielson', 'itau', 5000)
print()
print('Conta do Jadielson')
print()
cliente_1.depositar(100)
cliente_1.sacar(7,100)
cliente_1.sacar(7, 100)
cliente_1.sacar(7, 100)

cliente_2 = ContaCorrente('Luiz', 'Banco do Brasil', 100,100)
# cliente_2 = ContaPoupanca('Luiz', 'Banco do Brasil', 4000)
print()
print('Conta do Luiz')
print()

cliente_2.depositar(300)
cliente_2.sacar(10,100)
cliente_2.sacar(10, 50)
cliente_2.sacar(10, 150)

# cliente_3 = ContaCorrente('Sergio', 'Santander', 350)
cliente_3 = ContaPoupanca('Sergio', 'Santander', 350)
print()
print('Conta do Sergio')
print()
cliente_3.depositar(300)
cliente_3.sacar(100)
cliente_3.sacar(50)
cliente_3.sacar(150)

cliente_4 = ContaPoupanca('Carlos', 'Santander', 350)
print()
print('Conta do Carlos')
print()
cliente_4.depositar(300)
cliente_4.sacar(100)
cliente_4.sacar(50)
cliente_4.sacar(150)



