# Classe Retangulo: Crie uma classe que modele um retangulo:
# Atributos: LadoA, LadoB (ou Comprimento e Largura, ou Base e Altura, a escolher)
# Métodos: Mudar valor dos lados, Retornar valor dos lados, calcular Área e calcular Perímetro;
# Crie um programa que utilize esta classe. Ele deve pedir ao usuário que informe as medidades de 
# um local. Depois, deve criar um objeto com as medidas e calcular a quantidade de pisos e de rodapés necessárias para o local.


class Retangulo:

    def __init__(self, comprimento, largura):
        self.comprimento = comprimento
        self.largura = largura


    def mudar_valor_dos_lados(self, lado1, lado2):

        self.comprimento = lado1
        self.largura = lado2

    def mostrar_valor_dos_lados(self):

        return f'O valor do comprimento é {self.comprimento}m², e o valor da largura é {self.largura}m².'

    def calcular_area(self):
        area = self.comprimento * self.largura
        return area

    def calcular_perimetro(self):

        perimetro = (2 * self.comprimento) + ( 2 * self.largura)

        return perimetro

lado1 = int(input('Digite o valor do comprimento: '))
lado2 = int(input('Digite o valor da largura: '))

retangulo_1 = Retangulo(lado1, lado2)
# retangulo_2 = Retangulo(2, 5)
# retangulo_3 = Retangulo(3, 6)
# retangulo_1.mudar_valor_dos_lados(8, 7)
print(retangulo_1.mostrar_valor_dos_lados())
print('\nO valor da área do retanulo é ',retangulo_1.calcular_area(),)
print('\nO valor do perimetro do retangulo é', retangulo_1.calcular_perimetro())
print('\nE nescessario ', retangulo_1.calcular_area(), 'pisos e ', retangulo_1.calcular_perimetro(), 'rodapés'  )





