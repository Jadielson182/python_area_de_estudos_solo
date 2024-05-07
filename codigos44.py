
# class MinhaString(str):
#     def upper(self):
#         print('Chamou o upper')
#         retorno = super().upper()
#         print('Depois do upper')
#         return retorno


# string = MinhaString('Luiz')
# print(string.upper())

class A:
    atributo_a = 'Valor a'
    
    def metodo(self):
        print('A')
    

class B(A):
    atributo_b = 'Valor b'

    def metodo(self):
        print('B')


class C(B):
    atributo_c = 'valor c'
    def metodo(self):
        # super().metodo()
        # super(B, self).metodo()
        # super(A, self).metodo()
        print('C')

# print(C.mro())
# print(B.mro())
# print(A.mro())
c = C()
print(c.atributo_a)
print(c.atributo_b)
print(c.atributo_c)
c.metodo()


