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


client_1 = Cliente('Jadielson')
client_1.inserir_endereco('AV Brasil', 56)
client_1.inserir_endereco('Rua A', 478)
client_1.listar_enderecos()
client_externo = Endereco('Rua do Cabare', 24)
client_1.inserir_enderecos_externo(client_externo)

del client_1

print('###################### Seu Codigo acaba aqui')