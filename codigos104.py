
from argparse import ArgumentParser

parser = ArgumentParser()

# # parte 1
# parser.add_argument('-b')
# args = parsetr.parse_args()
# if args.b is None:
#     print('Você não passou valor de b')
# else:
#     print('O valor de b:',args.b)
# print(args.b)



#parte 2
parser.add_argument('-b', '--basic') # vai elimina a primeira e pega o segundo argumento
args = parser.parse_args()
if args.basic is None:
    print('Você não passou valor de basic')
else:
    print('O valor de basic:',args.basic)
print(args.basic)

#  venv\scripts\pyhon codigos104.py -b "errss" -b "ghhh" -b " gggg"  
# para usar no terminal o -b chave e 123 o valor precisa de ambos ou retorna None