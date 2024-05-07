# Faça um programa que use a função valorPagamento para determinar o valor a ser pago por uma prestação de uma conta.
#  O programa deverá solicitar ao usuário o valor da prestação e o número de dias em atraso e passar estes valores para a função valorPagamento, 
#  que calculará o valor a ser pago e devolverá este valor ao programa que a chamou. O programa deverá então exibir o valor a ser pago na tela.
#   Após a execução o programa deverá voltar a pedir outro valor de prestação e assim continuar até que seja informado um valor igual a zero
#    para a prestação. Neste momento o programa deverá ser encerrado, exibindo o relatório do dia, que conterá a quantidade e o valor total de
#     prestações pagas no dia. O cálculo do valor a ser pago é feito da seguinte forma.
#  Para pagamentos sem atraso, cobrar o valor da prestação. Quando houver atraso, cobrar 3% de multa, mais 0,1% de juros por dia de atraso.
from time import sleep
relatorio = []

def relatorio_dia(receber):
    quantidade = len(receber)
    total = sum(receber)
    print('========Encerrando o horario de pagamento========')
    sleep(1)
    print('\n==========Gerando relatorio do dia==========')
    sleep(2)
    print(f'\nNúmeros de pagamentos do dia: {quantidade} Pretações.')
    cont = 1
    for prestacao in receber:
        print(f'Valor da {cont}ª Prestação: R${prestacao:.2f} ')
        cont += 1
    print(40 *'_')
    print(f'O valor total foi de R${total:.2f}')
        

def valorPagamento(valor, atraso):   
    if atraso == 0:
        relatorio.append(valor)
    if atraso != 0:
        multa = (valor / 100) * 3
        juros = (valor / 100) *(atraso * 0.1)
        valor_final = valor + multa + juros
        relatorio.append(valor_final)
    
    
while True:
    valor = int(input('Digite o valor da prestação: '))  
    if valor == 0:   
        relatorio_dia(relatorio)
        print('\n==========Finalizando o Programa==========')
        break

    atraso = int(input('Digite quantos dias de atraso tem a prestação: '))
    valorPagamento(valor, atraso)

    
