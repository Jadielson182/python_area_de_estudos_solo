
caminho_arquivo = 'C:\\Users\\jadie\Documents\\arquivos python\\'
caminho_arquivo += 'aula_arquivo'

# arquivo = open(caminho_arquivo, 'w')
# arquivo.close()
with open(caminho_arquivo, 'w') as arquivo:
    print('Ola Mundo!')
    print('fechando aquivo')
