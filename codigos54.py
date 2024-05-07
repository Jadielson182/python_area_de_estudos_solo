
class Ponto:
    def __init__(self, x, y, z='String'):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f'{self.x}, {self.y}, {self.z}'

    def __repr__(self):
        #class_name = self.__class__.__name__
        class_name = type(self).__name__
        return f'{class_name}, ({self.x!r}, {self.y!r}, {self.z!r})'

ponto_1 = Ponto(1, 2)
ponto_2 = Ponto(978, 876)
print(ponto_1)
print(repr(ponto_2))
print(f'{ponto_2!r}')