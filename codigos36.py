class Caneta:
    def __init__(self,cor):
        self.cor_tinta = cor

    @property
    def cor(self):
        print('propenty')
        return self.cor_tinta

    @property
    def cor_tampa(self):
        return 'Azul Claro'

caneta = Caneta('Azul')
print(caneta.cor)
print(caneta.cor)
print(caneta.cor)
print(caneta.cor_tampa)