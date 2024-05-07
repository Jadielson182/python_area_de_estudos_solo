# def somar_matrizes(matriz1, matriz2):
#     lista_1, lista_2 = matriz1[0], matriz2[0]
#     lista_3 , lista_4 = matriz1[1], matriz2[1]
#     menor = min(len(lista_1), len(lista_2), len(lista_3), len(lista_4))
#     resultado1 = [lista_1[indice] + lista_2[indice] for indice in range(menor)]
#     resultado2 = [lista_3[indice] + lista_4[indice] for indice in range(menor)]
#     return [resultado1, resultado2]

def somar_matrizes(matriz1, matriz2):
    lista1 = [(a+b) for a, b in zip(matriz1[0], matriz2[0])]
    lista2 = [(a+b) for a, b in zip(matriz1[1], matriz2[1])]
    return [lista1, lista2]
    

# Exemplo de uso:
matriz1 = [[1, 2, 3], [4, 5, 6]]
matriz2 = [[7, 8, 9], [10, 11, 12]]
resultado = somar_matrizes(matriz1, matriz2)
print(resultado)
# Saída esperada: [[8, 10, 12], [14, 16, 18]]
