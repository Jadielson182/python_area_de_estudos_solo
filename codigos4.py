def invert_string(*string):
    return string[::-1]

def cria_funcao(func):
    def interna(*args,**kwargs):     
        for arg in args:
            is_string(arg)
        resultado = func(*args,*kwargs)
        return resultado
    return interna


def is_string(param):
    if not isinstance(param, str):
        raise TypeError (f'Erro com o parametro "{param}", verifique se digitou corretamente.')
    


verificador_de_string= cria_funcao(invert_string)
string_invertida = verificador_de_string(input('Digite ulguma coisa: '))
print(string_invertida)