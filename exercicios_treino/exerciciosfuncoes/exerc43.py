# Faça um programa que converta da notação de 24 horas para a notação de 12 horas. Por exemplo,
#  o programa deve converter 14:25 em 2:25 P.M. A entrada é dada em dois inteiros.
#   Deve haver pelo menos duas funções: uma para fazer a conversão e uma para a saída.
#    Registre a informação A.M./P.M. como um valor ‘A’ para A.M. e ‘P’ para P.M. Assim,
#     a função para efetuar as conversões terá um parâmetro formal para registrar se é A.M. ou P.M.
#  Inclua um loop que permita que o usuário repita esse cálculo para novos valores de entrada todas as vezes que desejar.

def mostrar_horario(horas, minutos, conversao):
    print(f'{horas}:{minutos} {conversao}')


def conversão(horas, minutos):
    if horas >= 0 and horas < 12 :
        conversão = 'A.M'
        mostrar_horario(horas, minutos, conversão)
    elif horas >=12 and horas < 24:
        conversao = 'P.M'
        if horas !=12:
            horas -= 12
        mostrar_horario(horas, minutos, conversao)
    
    elif horas == 24:
        conversao = 'A.M'
        horas = 0
        mostrar_horario(horas, minutos, conversao)
    else:
        print('Valor informado não corresponde a um horario, tente de novo.')


while True:
    horas = int(input('Digite o valor da hora de 1 ate 24: '))
    if horas == 999:
        print('Finalizando o programa')
        break
    minutos = int(input('Digite o valor dos minutos de 1 ate 60: '))
    conversão(horas, minutos)















# def mostrar_horario(horas, minutos):
#     if 0 < horas <= 12 and 0 < minutos < 60:
#         print(f'{horas}:{minutos} A.M')
#     elif 12 < horas < 24 and 0 < minutos < 60:
#         print(f'{horas - 12}:{minutos} P.M')
#     else:
#         print('Valor não corrsponde a um horario')


# while True:
#     horas = int(input('Digite o valor em horas de 1 a 24: '))
#     minutos = int(input('Digite o valor em minutos de 1 a 60: '))
#     mostrar_horario(horas, minutos)
#     if horas == 999 or minutos == 999:
#         break
#     print('Finalizando relogio python')
    
