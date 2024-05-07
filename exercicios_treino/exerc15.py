def sao_anagramas(palavra1, palavra2):
    if sorted(palavra1) == sorted(palavra2):
        return True
    else:
        return False
    
    #

# Exemplo de uso:
resultado = sao_anagramas("listen", "silent")
print(resultado)
# Saída esperada: True
