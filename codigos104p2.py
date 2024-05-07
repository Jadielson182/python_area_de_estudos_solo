# argparse.ArgumentParser para argumentos mais complexos
# Tutorial Oficial:
# https://docs.python.org/pt-br/3/howto/argparse.html

from argparse import ArgumentParser

parser = ArgumentParser()

parser.add_argument(
    '-b', '--basic',
    help= 'Mostra "Ola Mundo" na tela',
    # type= str, # tipo do argumento, caso use action=appender nao pode usar str
    metavar= 'STRING',
    # default= 'Ola Mundo', # vai mostra esse valor como padrao se nao passar o valor
    required= False, # se e obrigatorio passa r o valor ou não
    action= 'append', # recebe o argumento mais de uma vez
    # nargs= '+', # cria uma lista para receber os argumentos, pois se sem isso ao passar varios argumnentos so mostra o ultimo
    
    ) 
# parser.add_argument(
#     '-v', '--verbose',
#     help='Mostra logs',
#     action='store_true'
#     )

args = parser.parse_args()
if args.basic is None:
    print('Você não passou valor de basic')
    print(args.basic)
else:
    print('O valor de basic:',args.basic)
print(args.basic)

#codigo para executar no painel  venv\scripts\python codigos104p2.py -b "llll" -b "jjjj"
