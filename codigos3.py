def criar_funcao(func):
    def interna(*args, **kwargs):
        for arg in args:
            e_string(arg)
        resultado = func(*args, **kwargs)
        return resultado
    return interna


def invert_string(*string):
    return string[::-1]


def e_string(param1):
    if not  isinstance(param1, str):
        raise TypeError (f'param "{param1}"deve ser uma string')


invert_string_checa_parametro = criar_funcao(invert_string)
invertida = invert_string_checa_parametro('12345')
print(invertida)


