def caracteres_unicos(string):
    nova_string = ''
    for letra in string[0::]:
        if letra not in nova_string:
            nova_string += letra
    return f'"{nova_string}"'



    
    

# Exemplo de uso:
entrada = "pythonprogramming"
resultado = caracteres_unicos(entrada)
print(resultado)
# Saída esperada: "pythongrami"
