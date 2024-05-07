caminho_arquivo = 'arquivo2.txt'

with open(caminho_arquivo, 'w+') as arquivo:
    arquivo.write('Linha 1\n')
    arquivo.write('linha 2\n')
    arquivo.writelines(
        ('linha 3\n', 'Linha 4\n')
    )
    arquivo.seek(0, 0)

    print(arquivo.read())
    print('lendo')
    arquivo.seek(0, 0)
    print(arquivo.readline(), end='')
    print(arquivo.readline().strip())
    print(arquivo.readline(), end='')
    print(arquivo.readline().strip())
    print('Readlines')
    for linha in arquivo.readlines():
        print(linha)

    
print('=' * 10)
with open(caminho_arquivo, 'r+') as arquivo:
    print(arquivo.read())