
from datetime import datetime
from dateutil.relativedelta import relativedelta


data_do_emprestimo = datetime(2020,12,20)
delta = relativedelta(years=5)
data_final = data_do_emprestimo + delta
valor_do_emprestimo = 1000000

data_parcelas = []
data_parcela = data_do_emprestimo
while data_parcela < data_final:
    data_parcelas.append(data_parcela)
    data_parcela += relativedelta(months=+1)
numero_parcelas = len(data_parcelas)
valor_parcela = valor_do_emprestimo / numero_parcelas
fmt = '%d/%m/%Y'
count = 1
for data in data_parcelas:  
    print(f'\n{count}ª Parcela.\nData de pagamento: {data.strftime(fmt)}. Valor da parcela: R${valor_parcela:,.2f}')
    count += 1

print()
print(f'Você pegou R${valor_do_emprestimo:,.2f} para pagar em {delta.years} anos ({numero_parcelas} meses) em parcelas de {valor_parcela:,.2f} por mês.')