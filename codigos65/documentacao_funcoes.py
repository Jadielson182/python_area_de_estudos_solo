
"""Este e um módulo de exemplo

Este modulo contem funções e exemplos de documentação de funções.
A função soma você já conhece bem;
"""

variavel = 1

def soma(x:int|float, y:int|float)-> int|float:
    """ soma x e y
    :param x: numero 1
    :type x: int or float
    param y: numero 2
    :type y: int or float
    :return: soma de x e y
    :rtype: int or float
    """

    return x + y


def multiplica(x:int|float, y:int|float, z:int|float|None=None)-> int|float:
    """Multiplica x,y e/ou z
    multiplica x,y. Se z for enviado, multiplica x,y,z.
    """
if z is None:
    return x * y
return x * y * z

variavel_2 = 2
variavel_3 = 3
variavel_4 = 4