# Classe Bichinho Virtual++: Melhore o programa do bichinho virtual, 
# permitindo que o usuário especifique quanto de comida ele fornece ao bichinho e por quanto tempo ele brinca com o bichinho.
#  Faça com que estes valores afetem quão rapidamente os níveis de fome e tédio caem.
# status padrao: fome =100, saude = 100
class Tamagushi:
    def __init__(self, nome, fome=80, saude=50, idade=1):
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

    # def detalhar_status(self):
    #     return f'\nNome: {self.nome}\nFome: {self.fome}\nSaúde: {self.saude}\nIdade: {self.idade}'

    def check_condicao(self):
        if self.fome <= 7 and self.saude <= 7:
            return 'Seu bixinho vitrual esta de mau humor.'
        if self.saude == 5:
            return 'Seu bixinho vitrual está ficando doente, cuide da saude dele.'
        if self.fome == 5:
            return 'Seu bixinho vitrual está com fome, ofereça comida a ele.'
        if self.fome >= 10 or self.saude >= 10:
            return 'Seu bixinho vitrual esta de bom humor.'

    def dar_comida(self, comida):
        if self.fome >=0 and self.fome < 100:
            ...

    def cuidar_da_saude(self):
        if self.saude < 100 and self.saude >= 0:
            self.saude += 10

    def brincar(self, tempo):
        
        if self.fome - tempo <= 0 or self.saude - tempo <= 0:
            print(f'Seu bixinho virtual está com status:\nFome {self.fome} e Saúde {self.saude}, e não tem humor para brincar.')
        self.saude -= tempo  
        self.fome -= tempo

    

virtual = Tamagushi('Pikachu')
virtual.mudar_idade(10)
# virtual.mudar_fome(80)
# virtual.mudar_saude(50)
virtual.dar_comida(10)
virtual.dar_comida(10)
virtual.dar_comida(10)
virtual.dar_comida(10)
virtual.cuidar_da_saude()
virtual.cuidar_da_saude()
virtual.cuidar_da_saude()
virtual.cuidar_da_saude()
virtual.brincar(15)
virtual.brincar(15)
virtual.brincar(15)
virtual.brincar(15)
virtual.brincar(15)
virtual.brincar(15)

print(virtual.check_condicao())
# print(virtual.detalhar_status())