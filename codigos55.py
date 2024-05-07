
class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        class_name = type(self).__name__
        return f'{class_name} (x={self.x!r}, y={self.y!r})'


    def __add__(self, other):
        novo_x = self.x + other.x
        novo_y = self.y + other.y
        return Ponto(novo_x, novo_y)


    def __gt__(self, other):
        resultado_self = self.x + self.y
        resultado_other = other.x + other.y
        return resultado_self > resultado_other
    

if __name__ == '__main__':
    ponto_1 = Ponto(4, 2)
    ponto_2 = Ponto(6, 4)
    p3 = ponto_1 + ponto_2
    print(p3)
    print('P1 e maior que P2', ponto_1 > ponto_2)
    print('P2 e maior que P1', ponto_2 > ponto_1)