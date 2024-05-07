# Implemente uma metaclass chamada SingletonMeta que garanta que uma classe tenha apenas uma instância.
#  Utilize essa metaclass em uma classe de exemplo.

def meu_repr(self):
    return f'{type(self)>__name__}({self.__dict__})'

class SingletonMeta(type):
    def __new__(metaclass_, name_, bases_, dict_):
        cls = super().__new__(metaclass_, name_, bases_, dict_)
        cls.__repr__ = meu_repr
        return cls


    def __call__(cls, *args, **kwargs):
        instancia = super().__call__(*args, **kwargs)
        return instancia


class MinhaClasse(metaclass=SingletonMeta):
    def __new__(cls, *args, **kwargs):
        instancia = super().__new__(cls)
        return instancia

    def __init__(self, nome):
        self.nome = nome

    def falar(self):
        print('falando')

classe_1 = MinhaClasse('Metaclass')
classe_1.falar()