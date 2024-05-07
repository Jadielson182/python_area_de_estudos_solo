def eh_primo(numero):
    multiplos = 0
    for num in range(2, numero):
        if numero % num == 0:
            multiplos += 1
    if multiplos == 0:
        return f'O número {numero} e um número primo'
    else:
        return f'O número {numero} não e um número primo'

    

# Exemplo de uso:
resultado = eh_primo(11)
print(resultado)
# Saída esperada: True
