# Classe Pessoa: Crie uma classe que modele uma pessoa:

# Atributos: nome, idade, peso e altura
# Métodos: Envelhercer, engordar, emagrecer, crescer. Obs: Por padrão, a cada ano que nossa pessoa envelhece,
#  sendo a idade dela menor que 21 anos, ela deve crescer 0,5 cm.

class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def envelhecer(self, anos):
        self.idade += anos
        print(f'{self.nome} envelheceu {anos} anos e sua idade atual é {self.idade} anos.')
        
    def engordar(self, peso):
        self.peso += peso
        print(f'{self.nome} ganhou {peso} kg e seu peso atual é {self.peso} kg.')
        

    def emagracer(self, perdeu_peso):
        self.peso -= perdeu_peso
        print(f'{self.nome} perdeu {perdeu_peso} kg e seu peso atual é {self.peso} kg.')

    def crescer(self, anos):
        self.idade += anos
        if self.idade < 21:
            crescimento = anos * 0.05
            self.altura += crescimento
            print(f'{self.nome} cresceu {crescimento:.2f}cm em {anos} anos e sua altura atual é {self.altura}.')
        else:
            print('{self.nome} não cresceu.')


pessoa_1 = Pessoa('Jadielçso', 36, 92, 1.75)
pessoa_2 = Pessoa('Carlos', 14, 38, 1.40)
pessoa_3 = Pessoa('Paulo',12, 29, 1.45 )
pessoa_4 = Pessoa('Marta', 18, 59, 1.60)

pessoa_2.crescer(6)
pessoa_2.emagracer(10)
pessoa_2.engordar(15)
pessoa_2.envelhecer(20)