# Classe Macaco: Desenvolva uma classe Macaco,que possua os atributos nome e bucho (estomago) e 
# pelo menos os métodos comer(), verBucho() e digerir(). Faça um programa ou teste interativamente,
#  criando pelo menos dois macacos, alimentando-os com pelo menos 3 alimentos diferentes e verificando o conteúdo do estomago a cada refeição. 
# Experimente fazer com que um macaco coma o outro. É possível criar um macaco canibal?

class Macaco:
    def __init__(self, nome):
        self.nome = nome
        self.estomago = []


    def comer(self, alimentos):
        self.estomago.append(alimentos)
        self.ver_bucho()

    
    def ver_bucho(self):
        print(f'{self.nome} comeu {self.estomago}.')

    
    def digerir(self, comida):
        if comida in self.estomago:
            self.estomago.remove(comida)
            self.ver_bucho()
        else:
            print(f'{self.nome} não comeu {comida}')


macaco_1 = Macaco('Junior')
print(macaco_1.nome)
print()
macaco_1.comer('Banana')
macaco_1.comer('Maçã')
macaco_1.comer('Picanha')
macaco_1.digerir('Picanhas')
print()
macaco_2 = Macaco('Pibinha')
print(macaco_2.nome)
macaco_2.comer('Uva')
macaco_2.comer('mel')
macaco_2.comer('pizza')
print()
macaco_1.comer(macaco_2.nome)

    
