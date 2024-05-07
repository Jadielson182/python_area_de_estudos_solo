
def fabrica_de_decoradores(a=None,b=None,c=None):
    def fabrica_de_funcoes(func):
        print('Decoradora1')
        def aninhada(*args, **kwargs):
            print('parametros do decorador,', a, b, c)
            print('aninhada')
            res = func(*args, **kwargs)
            return res
        return aninhada
    return fabrica_de_funcoes

 


@fabrica_de_decoradores(1, 2, 3)
def soma(x, y):
    return x + y

# # @decoradora
# @fabrica_de_decoradores(1, 2, 3)
# def multiplica(x, y):
#     print(f'multiplica é {multiplica.__name__}')
#     return x * y

# # @decoradora
# @fabrica_de_decoradores(1, 2, 3)
# def subtracao(x, y):
#     print(f'subtraçao é {subtracao.__name__}')
#     return x - y

decoradora = fabrica_de_decoradores(1, 2, 3)
multiplica = decoradora(lambda x, y: x * y)

decoradora2 = fabrica_de_decoradores(1, 2, 4)
subtracao = decoradora2(lambda x, y: x - y)

dez_mais_cinco = soma(10, 15)
dez_vezes_cinco = multiplica(10,5)
dez_menos_cinco = subtracao(10,5)
print(dez_mais_cinco)
print(dez_vezes_cinco)
print(dez_menos_cinco)