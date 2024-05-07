
import contas


class Pessoa():
    def __init__(self,nome:str, idade:int):
        self.nome:str = nome
        self.idade:int = idade


    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome:str):
        self._nome = nome

    @property
    def idade(self):
        return self._idade


    @idade.setter
    def idade(self, idade:int):
        self._idade = idade

    def __repr__(self):
        class_name = type(self).__name__
        attrs = f'({self.nome!r}), ({self.idade!r})'
        return f'{class_name}{attrs}'


class Cliente(Pessoa):
    def __init__(self,nome, idade):
        super().__init__(nome, idade)
        self.conta: contas.Conta | None = None
        

    # @Pessoa.nome.setter
    # def nome(self, nome):
    #     self.nome = nome

    # @Pessoa.idade.setter
    # def idade(self, idade):
    #     self.idade = idade


if  __name__ == '__main__':

    cliente_1 = Cliente('jadielson', 35)
    cliente_2 = Cliente('Luiz Otávio', 45)
    cliente_1.conta = contas.ContaCorrente(3614, 62145, 0, 100)
    cliente_2.conta = contas.ContaPoupanca(2144, 41256, 100)
    
    print(cliente_1)
    print(cliente_1.conta)
    print()
    print(cliente_2)
    print(cliente_2.conta)










