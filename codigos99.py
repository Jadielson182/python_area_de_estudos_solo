
import locale
import string
from datetime import datetime
from pathlib import Path

locale.setlocale(locale.LC_ALL, '')

def converte_para_brl(numero: float)-> str:
    brl = 'R$' + locale.currency(numero, symbol=False, grouping=True)
    return brl

data = datetime(2022, 12, 28)
dados = dict(
    nome = 'João',
    valor = converte_para_brl(1_234_456),
    data = data.strftime('%d/%m/%Y'),
    empresa = 'O. M.',
    telefone = '+55 (11) 7890-5432',
)

# import json

# print(json.dumps(dados, indent=2, ensure_ascii=False))

# texto = '''
# Prezado(a) $nome,

# Informamos que sua mensalidade será cobrada no valor de ${valor} no dia $data.
# Caso deseje cancelar o serviço, entre em contato com a $empresa pelo telefone $telefone.

# Atenciosamente,

# ${empresa}
# '''

# template = string.Template(texto)
# print(template.substitute(dados))

# class MyTemplate(string.Template):  #class para modificar delimitador das variaveis que no momento e $, caso mude precisa mudar no texto
    # delimiter = '%'  # caso use substituir string.Template por MyTemplate

CAMINHO_ARQUIVO = Path(__file__).parent / 'codigos99.txt'

with open(CAMINHO_ARQUIVO, 'r',encoding='utf8') as arquivo:
    texto = arquivo.read()
    template = string.Template(texto)
    print(template.substitute(dados))