def eh_palindromo(palavra):
    invetida = palavra[::-1]
    if invetida == palavra:
        return True
    else:
        return False
    
    

# Exemplo de uso:
palavra1 = "radar"
palavra2 = 'carro'
palavra3 = 'reviver'

resultado1 = eh_palindromo(palavra1)
resultado2 = eh_palindromo(palavra2)
resultado3 = eh_palindromo(palavra3)
print(resultado1)
print(resultado2)
print(resultado3)

# Saída esperada: True
