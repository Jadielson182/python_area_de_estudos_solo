
import os
from itertools import count

caminho  = os.path.join('\\Users','jadie', 'Desktop', 'Curso python', 'python arquivos' )
 
couter = count()
for root, dirs, files in os.walk(caminho):
    the_counter = next(couter)
    print(the_counter, 'Pasta atual', root )

    for dir_ in dirs:
        print('    ', the_counter, 'Dir:', dir_)

    for file_ in files:
        caminho_completo_arquivo = os.path.join(root, file_)
        print('     ', the_counter, 'FILE:', caminho_completo_arquivo)

