# Usando Herança
class MyReprMixin:
    def __repr__(self):
        class_name = self.__class__.__name__
        class_dict = self.__dict__
        class_repr = f'{class_name} ({class_dict})'
        return class_repr



class Time(MyReprMixin):
    def __init__(self, nome):
        self.nome = nome


class Planeta(MyReprMixin):
    def __init__(self, nome):
        self.nome = nome



brasil = Time('Brasil')
portugal = Time('Portugal')

terra = Planeta('Terra')
marte = Planeta('Marte')

print(brasil)
print(portugal)
print(terra)
print(marte)

