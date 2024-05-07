
import math
import os
from itertools import count

def formata_tamanho(tamanho_em_bytes:int, base:int = 1000):
    if tamanho_em_bytes <= 0:
        return '0Bytes'

    abreviacao_tamanhos = 'B', 'KB', 'MB', 'GB', 'TB', 'PB'

    indice_abreviacao_tamanhos = int(math.log(tamanho_em_bytes, base))
    potencia = base ** indice_abreviacao_tamanhos
    tamanho_final = tamanho_em_bytes / potencia
    abreviacao_tamanho = abreviacao_tamanhos[indice_abreviacao_tamanhos]
    return f'{tamanho_final:.2f} {abreviacao_tamanho}'


caminho  = os.path.join('\\Users','jadie', 'Desktop', 'Curso python', 'python arquivos' )
 
couter = count()
for root, dirs, files in os.walk(caminho):
    the_counter = next(couter)
    print(the_counter, 'Pasta atual', root )

    for dir_ in dirs:
        print('    ', the_counter, 'Dir:', dir_)

    for file_ in files:
        caminho_completo_arquivo = os.path.join(root, file_)
        # tamanho = os.path.getsize(caminho_completo_arquivo) #opção 1
        stats = os.stat(caminho_completo_arquivo)
        tamanho = stats.st_size # st.size  faz o msm os.path.getsize
        print('     ', the_counter, 'FILE:', file_, formata_tamanho(tamanho))


print(formata_tamanho(10000))