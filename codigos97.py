import csv
from pathlib import Path

CAMINHO_CSV = Path(__file__).parent / 'codigos97.csv'
# # para lista de dicionarios

lista_clientes = [
    {'Nome': 'Luiz Otavio', 'Endereco': 'AV 1, 22'},
    {'Nome': 'Joao Silva', 'Endereco':'R. 2, "1"'},
    {'Nome': 'Maria Sol', 'Endereco':'Av B, 3A'}
]


# with open(CAMINHO_CSV, 'w') as arquivo:
#     nome_colunas = lista_clientes[0].keys() 
#     escritor = csv.writer(arquivo)

#     escritor.writerow(nome_colunas)
#     for cliente in lista_clientes:
#         escritor.writerow(cliente.values())

with open(CAMINHO_CSV, 'w') as arquivo:
    nome_colunas = lista_clientes[0].keys() 
    escritor = csv.DictWriter(
        arquivo,
        fieldnames=nome_colunas 
    )
    escritor.writeheader()    
    for cliente in lista_clientes:
        print(cliente)
        escritor.writerow(cliente)



# #para listas

lista_clientes = [
    ['Luiz Otavio', 'AV 1, 22'],
    ['Joao Silva', 'R. 2, "1"'],
    ['Maria Sol', 'Av B, 3A'],
]

with open(CAMINHO_CSV, 'w') as arquivo:
    nome_colunas = ['Nome', 'enderecos']
    escritor = csv.writer(arquivo)

    escritor.writerow(nome_colunas)
    for cliente in lista_clientes:
        escritor.writerow(cliente)
