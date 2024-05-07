def chaves_ordenadas(dicionario):
    return sorted(dicionario, reverse=False, key=lambda p: p)
    

# Exemplo de uso:
dados = {'banana': 3, 'maça': 5, 'laranja': 2, 'uva': 8}
resultado = chaves_ordenadas(dados)
print(resultado)
# Saída esperada: ['banana', 'laranja', 'maça', 'uva']
