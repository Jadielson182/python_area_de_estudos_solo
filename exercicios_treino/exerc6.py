def ordenar_por_comprimento(lista):
    lista_ordenada = sorted(lista, key=lambda ordena:len(ordena))
    return lista_ordenada
# Exemplo de uso:
palavras = ["python", "programação", "é", "poderosa"]
resultado = ordenar_por_comprimento(palavras)
print(resultado)
# Saída esperada: ['é', 'python', 'poderosa', 'programação']
