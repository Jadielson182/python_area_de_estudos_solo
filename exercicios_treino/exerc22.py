# Classe Quadrado: Crie uma classe que modele um quadrado:

# Atributos: Tamanho do lado
# Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área;

class Quadrado:
    def __init__(self, tamanho_do_lado):
        self.tamanho_do_lado = tamanho_do_lado

    def mudar_valor_do_lado(self, tamanho_do_lado):
        self.tamanho_do_lado = tamanho_do_lado

    def mostra_valor_do_lado(self):
        return f'{self.tamanho_do_lado}cm'

    def calcula_area(self):
        area = self.tamanho_do_lado * self.tamanho_do_lado
        return f'{area}cm'


quadrado_1 = Quadrado(5)
quadrado_2 = Quadrado(6)
quadrado_3 = Quadrado(4)

quadrado_1.mudar_valor_do_lado(7)
quadrado_2.mudar_valor_do_lado(3)
quadrado_3.mudar_valor_do_lado(5)

print('O valor do lado  quadrado 1 é',quadrado_1.mostra_valor_do_lado())
print('O valor da área do quadrado 1 é',quadrado_1.calcula_area())

print('O valor do lado  do quadrado 2 é',quadrado_2.mostra_valor_do_lado())
print('O valor da área  do quadrado 2 é',quadrado_2.calcula_area())

print('O valor do lado do quadrado 3 é',quadrado_3.mostra_valor_do_lado())
print('O valor da área do quadrado 3 é',quadrado_3.calcula_area())




