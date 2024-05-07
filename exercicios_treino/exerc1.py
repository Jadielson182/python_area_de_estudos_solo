def pares_inversos(lista):
    nova_lista = []
    for numero in lista:
        if numero % 2 == 0:
            nova_lista.append(numero)
    return sorted(nova_lista, reverse=True)



# Exemplo de uso:
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
resultado = pares_inversos(numeros)
print(resultado)
# Saída esperada: [10, 8, 6, 4, 2]
