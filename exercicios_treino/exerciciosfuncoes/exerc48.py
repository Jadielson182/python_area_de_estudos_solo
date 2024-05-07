# Data com mês por extenso. Construa uma função que receba uma data no formato DD/MM/AAAA e
#  devolva uma string no formato D de mesPorExtenso de AAAA.
#  Opcionalmente, valide a data e retorne NULL caso a data seja inválida.

def converte(dia, mes, ano):
    meses ={1:'janeiro' ,2 : 'Fevereiro' , 3 : 'Março', 4 : 'Abril',5 : 'Maio',6: 'Junho',7:  'Julho',
     8 :'Agosto', 9 : 'Setembro' ,10 : 'Outubro', 11 : 'Novembro', 12 : 'Dezembro'}
    mes_por_extenso = meses[mes]
    return f'{dia} de {mes_por_extenso} de {ano}.'


    





data = converte(13, 2, 1988)
print(data)