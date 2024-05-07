# Classe Bola: Crie uma classe que modele uma bola:

# Atributos: Cor, circunferência, material
# Métodos: trocaCor e mostraCor

class Bola:
    def __init__(self, cor, circuferencia, material):
        self.cor = cor
        self.circuferencia = circuferencia
        self.material = material

    def trocarCor(self, cor):
        self.cor = cor

    def mostraCor(self):
        return print(f'A cor da Bola é {self.cor}')


    
bola_1 = Bola('Verde', 9,  'plastico')
bola_2 = Bola('amarelo', 6, 'Couro' )
bola_3 = Bola('Branca', 8, 'Elastico')
bola_3.trocarCor('Vermelho')
bola_1.trocarCor('Preto')
bola_2.trocarCor('Azul')
bola_1.mostraCor()
bola_2.mostraCor()
bola_3.mostraCor()
