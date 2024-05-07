# Implemente uma classe chamada GeradorSenha que seja capaz de gerar senhas seguras.
#  A classe deve permitir a personalização do comprimento da senha,
#  inclusão ou exclusão de caracteres especiais, letras maiúsculas, números, etc.

import string
import random

class GeradorSenha:
    def __init__(self, comprimento=12, incluir_especiais=True, incluir_maiusculas=True, incluir_numeros = True):
        self.comprimento = comprimento
        self.incluir_especiais = incluir_especiais 
        self.incluir_maiusculas = incluir_maiusculas
        self.incluir_numeros = incluir_numeros

    def gerar_senha(self):
        caracteres = string.digits + string.ascii_uppercase + string.punctuation  + string.ascii_lowercase 
        if self.incluir_numeros == False:
            caracteres = string.ascii_uppercase + string.punctuation  + string.ascii_lowercase
        if self.incluir_maiusculas == False:
            caracteres = string.digits  + string.punctuation  + string.ascii_lowercase 
        if self.incluir_especiais == False:
            caracteres = string.digits + string.ascii_uppercase  + string.ascii_lowercase
        senha = ''
        for digito in range(self.comprimento):
            senha += random.choice(caracteres)
        return senha


gerador = GeradorSenha(comprimento=15, incluir_especiais = True,
incluir_maiusculas=True, incluir_numeros=True)
senha_segura = gerador.gerar_senha()
print(senha_segura)     

# Exemplo de uso:
# comprimento = ''
# incluir_especiais  = ''
# incluir_maiuscula  = ''
# incluir_numeros = ''


# comprimento = int(input('Digite o numero de caracteres da senha: '))


# incluir_especiais = str(input('Digite s para [Sim] ou n para [Não] para incluir carateres especiais: '))
# if incluir_especiais == 'S' or 's':
#     incluir_especiais == True
# elif incluir_especiais == 'n' or 'N':
#     incluir_especiais == False

# incluir_maiuscula = str(input('Digite s para [Sim] ou n para [Não] para incluir letras maiusculas: '))
# if incluir_maiuscula == 'S' or 's':
#     incluir_maiuscula == True
# elif incluir_maiuscula == 'n' or 'N':
#      incluir_maiuscula== False

# incluir_numeros = str(input('Digite s para [Sim] ou n para [Não] para incluir numeros: '))
# if incluir_numeros == 'S' or 's':
#      incluir_numeros == True
# elif incluir_numeros == 'n' or 'N':
#     incluir_numeros == False

# gerador = GeradorSenha(comprimentoo=comprimento, incluir_especial=incluir_especiais,
# incluir_maiusculas=incluir_maiuscula, incluir_numero=incluir_numeros)
# senha_segura = gerador.gerar_senha()
# print(senha_segura)




# caracteres = string.ascii_lowercase + string.ascii_uppercase + string.punctuation + string.digits