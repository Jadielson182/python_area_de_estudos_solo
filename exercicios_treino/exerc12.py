# Modifique a função abaixo para adicionar anotações de tipo de variável usando a PEP 484. 
# Certifique-se de incluir tipos para os argumentos e o valor de retorno.



def soma(a:int | float, b:int | float)-> int | float:
    """ 
    | = ou
    :param a: primeiro numero
    :type a: int | foat
    :param b: segundo numero
    :type b: int | float
    :return: a soma de a + b
    :Type return: int | float
    """
    return a + b

    

help(soma)
# Modifique a função para incluir anotações de tipo
# Exemplo: def soma(a: int, b: int) -> int:


