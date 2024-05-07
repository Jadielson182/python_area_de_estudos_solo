# continuando codigos94
from pathlib import Path
from shutil import rmtree

caminho_projeto = Path()

caminho_arquivo = Path.home() / 'Desktop' / 'arquivo_txt'
caminho_arquivo.touch()
caminho_arquivo.write_text('Olá mundo')
# print(caminho_arquivo.read_text())
# caminho_arquivo.unlink()

caminho_pasta= Path.home() / 'Desktop' / 'Python é legal'

caminho_pasta.mkdir(exist_ok=True)
subpasta = caminho_pasta / 'subpasta'
subpasta.mkdir(exist_ok=True)

outro_arquivo = subpasta / 'arquivo_txt'
outro_arquivo.touch()
outro_arquivo.write_text('Olá')

mais_arquivo = caminho_pasta / 'arquivo_txt'
mais_arquivo.touch()
mais_arquivo.write_text('Oi')

# caminho_pasta.rmdir()

files = caminho_pasta / 'files'
files.mkdir(exist_ok=True)

for i in range(10):
    file = files / f'file_{i}.txt'

    if file.exists():  # file. is file, file.dirname  comandos que poderia ser usados tambem
        file.unlink()
    else:
        file.touch()
    
    with file.open('a+') as  text_file:
        text_file.write('Olá Mundo.\n')
        text_file.write(f'file_{i}')

# rmtree(caminho_pasta) esse e modo mais facil usando shutil para remover todos arquivos 

def rmtree(root:Path, remove_root=True):
    for file in root.glob('*'):
        if file.is_dir():
            print('Dir', file)
            rmtree(file, False)
            file.rmdir()
        else:
            print('FILE:', file)
            file.unlink()
    if remove_root:
        root.rmdir()


rmtree(caminho_pasta)
        