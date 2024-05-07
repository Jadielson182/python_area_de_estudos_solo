#ZIP - ccompactando/descompactando arquivos com zipfile.ZipFile 
import os
import shutil
from pathlib import Path
from zipfile import ZipFile

#Caminhos

CAMINHO_RAIZ = Path(__file__).parent
CAMINHO_ZIPIR_DIR = CAMINHO_RAIZ / 'codigos102_diretorio_zip'
CAMINHO_COMPACTADO = CAMINHO_RAIZ / 'codigos102_compactado.zip'
CAMINHO_DESCOMPACTADO = CAMINHO_RAIZ /  'codigos102_descompactado'

shutil.rmtree(CAMINHO_ZIPIR_DIR, ignore_errors=True)
Path.unlink(CAMINHO_COMPACTADO, missing_ok=True)
shutil.rmtree(str(CAMINHO_COMPACTADO).replace('.zip', ''), ignore_errors=True)
shutil.rmtree(CAMINHO_DESCOMPACTADO, ignore_errors=True)

CAMINHO_ZIPIR_DIR.mkdir(exist_ok=True)

def criar_arquivos(qtd:int, zip_dir: Path):
    for i in range(qtd):
        texto = f'arquivo_{i}'
        with open(zip_dir / f'{texto}.txt', 'w') as arquivo:
            arquivo.write(texto)


criar_arquivos(10, CAMINHO_ZIPIR_DIR)

# Criando um zip e adicionando arquivos
with ZipFile(CAMINHO_COMPACTADO, 'w') as zip:
    for root, dirs, files in os.walk(CAMINHO_ZIPIR_DIR):
        for file in files:
            zip.write(os.path.join(root, file), file)


#lendo arquivos de um zip    
with ZipFile(CAMINHO_COMPACTADO, 'r') as zip:
    for arquivo in zip.namelist():
        print(arquivo)

# Extraindo arquivos de um zip
with ZipFile(CAMINHO_COMPACTADO, 'r') as zip:
    zip.extractall(CAMINHO_DESCOMPACTADO)