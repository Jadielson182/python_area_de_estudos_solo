

def contar_palavras(frase):
    frase_separada = frase.split()
    frase_contada = len(frase_separada)
    return f'{frase_contada} {frase_separada}'

# Exemplo de uso:
frase = "Python é uma linguagem de programação Python"
resultado = contar_palavras(frase)
print(resultado)
# Saída esperada: 6 (Python, é, uma, linguagem, de, programação)
