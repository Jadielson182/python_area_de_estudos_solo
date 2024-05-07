# Classe Conta de Investimento: Faça uma classe contaInvestimento que seja semelhante a classe contaBancaria,
# com a diferença de que se adicione um atributo taxaJuros.
# Forneça um construtor que configure tanto o saldo inicial como a taxa de juros.
# Forneça um método adicioneJuros (sem parâmetro explícito) que adicione juros à conta.
# Escreva um programa que construa uma poupança com um saldo inicial de R$1000,00 e uma taxa de juros de 10%.
# Depois aplique o método adicioneJuros() cinco vezes e imprime o saldo resultante.

class ContaInvestimento:
    def __init__(self, numero_conta,nome_correntista, saldo=1000, taxa_juros=10):
        self.numero_conta = numero_conta
        self.nome_correntista = nome_correntista
        self.saldo= saldo
        self.taxa_juros = taxa_juros

    def alterar_nome(self, nome):
        self.nome_correntista = nome

    def depositar(self, valor):
        self.saldo += valor
        self.detalhe(f'Confirmado deposito de R${valor:.2f}')
        
    def detalhe(self, msg):
        print(f'{msg}\nO saldo da conta número: {self.numero_conta}\nNome: {self.nome_correntista}\nSaldo atual: R${self.saldo:.2f}.')
    
    def sacar(self, valor):
        if self.saldo > valor:
            self.saldo -= valor
            self.detalhe(f'Confirmado um saque no valor de R${valor:.2f}.')
        if self.saldo < valor:
            self.detalhe(f'Saldo insuficiente, saque no valor de R${valor} negado.')
    
    def adicionar_juros(self, cont):
        resultado = (self.saldo / 100) * self.taxa_juros
        self.saldo += resultado
        print(f'Foi contabilizado os juros do {cont}º més de {self.taxa_juros}%.\nO valor do saldo atual é R${self.saldo:.2f}.')

conta_1 = ContaInvestimento(521469, 'Jadielson Silva')
conta_1.depositar(1000)
conta_1.adicionar_juros(1)
conta_1.adicionar_juros(2)
conta_1.adicionar_juros(3)
conta_1.adicionar_juros(4)
conta_1.adicionar_juros(5)
