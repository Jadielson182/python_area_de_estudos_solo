def obterTemperatura(option):
  
    temp = float(input("Qual é a temperatura ? "))
    
    calculos = {
        1: lambda temp: temp * 1.8 + 32,
        2: lambda temp: 5 * (temp - 32) / 9,
        3: lambda temp: temp + 273.15,
        4: lambda temp: temp - 273.15,
        5: lambda temp: (temp + 459.67) / 1.8,
        6: lambda temp: temp * 1.8 - 459.67
        }
    return calculos[option](temp)

param = float(input("Qual Opção vai escolher ? "))

print(obterTemperatura(param))




def contar_vogais(palavra):
    vogais = "aeiouAEIOU"
    return sum(1 for letra in palavra if letra in vogais)

# Teste
print(contar_vogais("Python")) 




def elevar_ao_quadrado(lista):
    return list(map(lambda x: x**2, lista))

# Teste
numeros = [1, 2, 3, 4, 5]
print(elevar_ao_quadrado(numeros))


import random
import string

def gerar_senha(comprimento=12, incluir_maiusculas=True, incluir_numeros=True, incluir_simbolos=True):
    caracteres = string.ascii_lowercase
    if incluir_maiusculas:
        caracteres += string.ascii_uppercase
    if incluir_numeros:
        caracteres += string.digits
    if incluir_simbolos:
        caracteres += string.punctuation

    senha = ''.join(random.choice(caracteres) for _ in range(comprimento))
    return senha

# Teste
print(gerar_senha())
