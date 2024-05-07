#Faça um programa, com uma função que necessite de um argumento. 
# A função retorna o valor de caractere ‘P’, se seu argumento for positivo,
#  e ‘N’, se seu argumento for zero ou negativo.

def negativo_positivo(number):
    if number < 0:
        return 'Número negativo'
    if number >= 0:
        return 'Número positivo'

print(negativo_positivo(5))