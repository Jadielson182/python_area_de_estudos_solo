def divide(n, d):
    nao_aceita_zero(d)
    deve_ser_int_float(n)
    deve_ser_int_float(d)
    return n / d


def deve_ser_int_float(n):
    type_n = type(n)
    if not isinstance(n, (int, float)):
        raise TypeError(
            f'"{n}" deve ser int ou float'
            f'"{type_n}" enviado'
            )
    return True


def nao_aceita_zero(d):
    if d == 0:
        raise ZeroDivisionError ('Você está tentando dividir por zero')
    return True




print(divide(8,0))