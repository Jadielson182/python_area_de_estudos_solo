def calcular_fatorial(n):
    fatorial = 1
    for numero in range(n, 1, -1):
        fatorial = fatorial* numero
    return fatorial




# Exemplo de uso:
resultado = calcular_fatorial(6)
print(resultado)
# Saída esperada: 120
