class Endereco:
    def __init__(self, rua, numero):
        self.rua = rua
        self.numero = numero


    def __del__(self):
        print('APAGANDO', self.rua, self.numero)


class Cliente:
    def __init__(self, nome):
        self.nome = nome
        self.enderecos = []


    def inserir_endereco(self, rua, numero):
        self.enderecos.append(Endereco(rua, numero))


    def inserir_enderecos_externo(self, endereco):
        self.enderecos.append(endereco)


    def listar_enderecos(self):
        for endereco in self.enderecos:
            print(endereco.rua, endereco.numero)


    def __del__(self):
        print('APAGANDO', self.nome)


cliente_1 = Cliente('Jadielson')
cliente_1.inserir_endereco('AV Brasil', 54)
cliente_1.inserir_endereco('Rua B', 6745)
cliente_1.listar_enderecos()
endereco_externo = Endereco('AV Saudade', 1587)
cliente_1.inserir_enderecos_externo(endereco_externo)

del cliente_1

print('#' * 15, 'AQUI TERMINA SEU CODIGO')
