# 'C:\\Users\\jadie\\Desktop\\Curso python\\python arquivos'

import os
import shutil

HOME = os.path.expanduser('~')
DESKTOP = os.path.join(HOME, 'Desktop')
PASTA_ORIGINAL = os.path.join(DESKTOP, 'python arquivos')
NOVA_PASTA = os.path.join(DESKTOP, 'Curso python', 'NOVA PASTA')
# print(os.path.exists(NOVA_PASTA))
os.makedirs(NOVA_PASTA, exist_ok=True)

for root, dirs, files in os.walk(PASTA_ORIGINAL):
    for dir_ in dirs:
        caminho_novo_diretorio = os.path.join(root.replace(PASTA_ORIGINAL, NOVA_PASTA), dir_)
        os.makedirs(caminho_novo_diretorio , exist_ok=True)

    for file_ in files:
        caminho_arquivo = os.path.join(root, file_)
        caminho_novo_arquivo = os.path.join(root.replace(PASTA_ORIGINAL, NOVA_PASTA), file_)
        shutil.copy(caminho_arquivo, caminho_novo_arquivo)
        print(caminho_arquivo)

