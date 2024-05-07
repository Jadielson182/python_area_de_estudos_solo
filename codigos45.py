
class A():
    atributo_a = 'valor a'
    def __init__(self, atributo):
        self.atributo = atributo

    def metodo(self):
        print('A')

class B(A):
    atributo_b = 'valor b'

    def __init__(self, atributo, outra_coisa):
        super().__init__(atributo)
        self.outra_coisa = outra_coisa

    def metodo(self):
        print('B')


class C(B):
    atributo_c = 'Valor c'

    def __init__(self, *args, **kwargs):
        print('Burlei o Sistema')
        super().__init__(*args, **kwargs)

    def metodo(self):
        # A.metodo(self)
        # B.metodo(self)
        print('C')

c = C('atributo', 'chucu')
b = B('atributo', 'chucu')
a = A('atributo')
print(c.atributo)
print(c.outra_coisa)
print(b.atributo)
print(b.outra_coisa)
print(a.atributo)
a.metodo()
b.metodo()
c.metodo()
