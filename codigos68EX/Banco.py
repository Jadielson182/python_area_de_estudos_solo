import contas
import pessoa
from dataclasses import dataclass



class Banco:
    def __init__(self,
    agencias: list[int] | None = None, 
    clientes: list[pessoa.Pessoa] | None = None, 
    contas : contas.Conta | None = None):

        self.agencias = agencias or []
        self.clientes = clientes or []
        self.contas = contas or []

    def checar_agencia(self, conta):
        if conta.agencia in self.agencias:
            print('checa_agencia', True)
            return True
        print('checa_agencia', False)
        return False

    
    
    def checar_cliente(self, cliente):
        if cliente in self.clientes:
            print('checar cliente ', True)
            return True
        print('checar cliente ', False)
        return False

        
    def checar_conta(self, conta):
        if conta in self.contas:
            print('checar conta', True)
            return True
        print('checar  conta ', False)
        return False

    def checar_se_a_conta_cliente(self, cliente, conta):
        if conta is cliente.conta:
            print('checar conta do cliente,', True)
            return True
        print('checar conta do cliente,', False)

        return False

    def checar_autenticacao(self, cliente:pessoa.Pessoa, conta:contas.Conta):
        return  self.checar_agencia(conta) and \
                self.checar_cliente(cliente) and \
                self.checar_conta(conta) and \
                self.checar_se_a_conta_cliente(cliente, conta)

    def __repr__(self):
        class_name = type(self).__name__
        attr = f'({self.agencias!r}, {self.clientes!r}, {self.contas!r})'
        return f'{class_name} {attr}'

        
if __name__ == '__main__':
    cliente_1 = pessoa.Cliente('Jadielson', 35)
    contacorrent_1 = contas.ContaCorrente(111, 222, 0, 0)
    cliente_1.conta = contacorrent_1

    cliente_2 = pessoa.Cliente('Luiz Otávio', 45)
    contapoupanca_1 = contas.ContaPoupanca(112, 223, 100)
    cliente_2.conta = contapoupanca_1

    banco = Banco()
    banco.clientes.extend([cliente_1, cliente_2])
    banco.contas.extend([contacorrent_1, contapoupanca_1])
    banco.agencias.extend([111,112])

    if banco.checar_autenticacao(cliente_1, contacorrent_1):
        contacorrent_1.depositar(10)
        cliente_1.conta.depositar(100)
        print(cliente_1.conta)
    
 
    



# if __name__ == '__main__':
#     c1 = pessoa.Cliente('Luiz', 30)
#     cc1 = contas.ContaCorrente(111, 222, 0, 0)
#     c1.conta = cc1
#     c2 = pessoa.Cliente('Maria', 18)
#     cp1 = contas.ContaPoupanca(112, 223, 100)
#     c2.conta = cp1
#     banco = Banco()
#     banco.clientes.extend([c1, c2])
#     banco.contas.extend([cc1, cp1])
#     banco.agencias.extend([111, 222])

#     if banco.checar_autenticacao(c1, cc1):
#         cc1.depositar(10)
#         c1.conta.depositar(100)
#         print(c1.conta)
