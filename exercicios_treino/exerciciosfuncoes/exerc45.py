# # Faça uma função que informe a quantidade de dígitos de um determinado número inteiro informado.

def numero_de_digitos(valor):
    valor = str(valor)
    print(f'O valor informado possui {len(valor)} digitos.')


numero_de_digitos(124222)


# def contaDigito(n):
#     return len( str(n) )
# def exibe():
#     n = int(input('Forneça um inteiro: '))
#     print(contaDigito(n), ' dígitos')
    
# while True:
#     exibe()


# import math 

# def achaTamanho(numero):
#     numero = abs(int(numero))
#     if numero < 2:
#         return 1
#     count = 0
#     valor = 1
#     while valor <= numero:
#         valor *= 10
#         count += 1
#     return count

# def achaTamanho2(numero):
#     numero = abs(int(numero))
#     return (1 if numero == 0 else math.floor(math.log10(numero)) + 1)
    
# print(achaTamanho(0))
# print(achaTamanho(1))
# print(achaTamanho(2))
# print(achaTamanho(123))
# print(achaTamanho(1000))
# print(achaTamanho(-1))
# print(achaTamanho(-23))
# print(achaTamanho(45678))
# print(achaTamanho(9999))
# print ("")
# print(achaTamanho2(0))
# print(achaTamanho2(1))
# print(achaTamanho2(2))
# print(achaTamanho2(123))
# print(achaTamanho2(1000))
# print(achaTamanho2(-1))
# print(achaTamanho2(-23))
# print(achaTamanho2(45678))
# print(achaTamanho2(9999))