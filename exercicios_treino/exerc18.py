import random
import string

def gerar_senha(comprimento):
    senha = ''
    caracteres = string.digits + string.ascii_uppercase + string.ascii_lowercase
    for digito in range(comprimento):
        senha  += random.choice(caracteres)
    return senha
    

# Exemplo de uso:
senha = gerar_senha(10)
print(senha)
# Saída esperada: Uma senha aleatória de comprimento 10
caracteres = string.digits + string.ascii_uppercase + string.punctuation  + string.ascii_lowercase 