# Classe Bichinho Virtual:Crie uma classe que modele um Tamagushi (Bichinho Eletrônico):

# Atributos: Nome, Fome, Saúde e Idade b. Métodos: Alterar Nome, Fome, Saúde e Idade; Retornar Nome, Fome, Saúde e Idade Obs:
# Existe mais uma informação que devemos levar em consideração, o Humor do nosso tamagushi, este humor é uma combinação entre
# os atributos Fome e Saúde, ou seja, um campo calculado, então não devemos criar um atributo para armazenar esta informação por que
#  ela pode ser calculada a qualquer momento.
class Tamagushi:
    def __init__(self, nome, fome=10, saude=5, idade=1):
        self.nome = nome
        self.fome = fome
        self.saude = saude
        self.idade = idade

    def alterar_nome(self, nome):
        self.nome = nome

    def mudar_fome(self, fome):
        self.fome = fome

    def mudar_saude(self, saude):
        self.saude = saude

    def mudar_idade(self, idade):
        self.idade = idade

    def detalhar_status(self):
        return f'\nNome: {self.nome}\nFome: {self.fome}\nSaúde: {self.saude}\nIdade: {self.idade}'

    def check_condicao(self):
        if self.fome >= 7 and self.saude <= 3:
            return f'{self.nome} esta de mau humor.'
        if self.saude == 1:
            return f'{self.nome} está ficando doente, cuide da saude dele.'
        if self.fome == 1:
            return f'{self.nome} está com fome, de comida a ele.'
        else:
            return f'{self.nome} esta de bom humor.'

    def dar_comida(self):
        if self.fome <= 10 and self.fome > 0:
            self.fome -= 1

    def cuidar_da_saude(self):
        if self.saude < 10 and self.saude >= 0:
            self.saude += 1

virtual = Tamagushi('Pikachu')
virtual.mudar_idade(8)
virtual.mudar_fome(8)
virtual.mudar_saude(1)
virtual.dar_comida()
virtual.dar_comida()
virtual.dar_comida()
virtual.dar_comida()
virtual.cuidar_da_saude()
virtual.cuidar_da_saude()
virtual.cuidar_da_saude()
virtual.cuidar_da_saude()
print(virtual.check_condicao())
print(virtual.detalhar_status())
