
import csv
from pathlib import Path


CAMINHO_CSV = Path(__file__).parent / 'codigos96.csv'
print(CAMINHO_CSV)

# with open(CAMINHO_CSV, 'r') as arquivo:
#     leitor = csv.reader(arquivo) # csv. reader() vai ler em formato de lista
#     # next(leitor)
    # # next(leitor)
    # print(next(leitor))
    # for linha in leitor:
    #     print(linha)  # linha[0], linha[1] para da print em colunas especificas

    
with open(CAMINHO_CSV, 'r') as arquivo:
    leitor = csv.DictReader(arquivo)  # csv.dictReader() vai ler em formato de dicionario

    for linha in leitor:
        print(linha) # linha['Nome'], linha['idade'] para selecionar chave e valor
