# Classe Ponto e Retangulo: Faça um programa completo utilizando funções e classes que:
# Possua uma classe chamada Ponto, com os atributos x e y.
# Possua uma classe chamada Retangulo, com os atributos largura e altura.
# Possua uma função para imprimir os valores da classe Ponto
# Possua uma função para encontrar o centro de um Retângulo.
# Você deve criar alguns objetos da classe Retangulo.
# Cada objeto deve ter um vértice de partida, por exemplo, o vértice inferior esquerdo do retângulo, 
# que deve ser um objeto da classe Ponto.
# A função para encontrar o centro do retângulo deve retornar o valor para um objeto do tipo ponto 
# que indique os valores de x e y para o centro do objeto.
# O valor do centro do objeto deve ser mostrado na tela
# Crie um menu para alterar os valores do retângulo e imprimir o centro deste retângulo.

class Retangulo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura


    def encontrar_centro(self):
        if self.largura % 2 == 1 and self.altura % 2 == 1:
            centro_largura = (self.largura / 2) 
            centro_altura = (self.altura / 2)
            print(f'O centro do retangulo esta na posição:\nLargura {centro_largura}\nAltura {centro_altura}')
        else:
            print('Não foi possivel char o centro')

class Ponto:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y


    def imprimir_valores(self):
        if self.x == 0 or self.y ==0:
            ponto = Ponto.ponto_partida(self)
            print(f'\nO ponto esta na posição inicial: Largura: {self.x}\nAltura: {self.y}')
        else:
            print(f'O ponto está na posição:\nLargura: {self.x}\nAltura: {self.y}')


    def ponto_partida(self):
        largurinicial = 2
        altura_inicial = self.y - 1
        print(f'\nO ponto está  na posição inicial:\nLargura: {largurinicial}\nAltura: {altura_inicial}')
        inicio_do_ponto = [largurinicial, altura_inicial]
        return inicio_do_ponto



retangulo_1 = Retangulo(7, 5)
retangulo_1.encontrar_centro()

retangulo_1 = Ponto(5, 6)
retangulo_1.imprimir_valores()
retangulo_1.ponto_partida()
        