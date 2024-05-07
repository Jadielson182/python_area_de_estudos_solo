

def cria_funcao(func):
    def interna(*args, **kwargs):
        print('Vai copmeçar etapa de decoração')
        for arg in args:
            check_number(arg)
        result = func(*args,**kwargs)
        # result *= 2
        print(f'O resultado nessa etapa foi {result}')
        print('Decoramento finalizado.')
        return result
    return interna


@cria_funcao
def soma_numero(*numbers):
    print(f'{soma_numero.__name__}')
    return sum(numbers)



def check_number(numbers):
    if not isinstance(numbers, (int, float)):
        raise TypeError(f'Erro no parametro "{numbers}", verifique se digitou corretamente.')





# somando_numeros =cria_funcao(soma_numero)
# resultado = somando_numeros(2,3,4)
resultado = soma_numero(2,4,5,7,7)
print(resultado)