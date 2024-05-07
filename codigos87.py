# C:\Users\jadie\Desktop\Curso python\python arquivos

import os

caminho  = os.path.join('\\Users','jadie', 'Desktop', 'Curso python', 'python arquivos' )
# print(os.path.exists(caminho))

for pasta in os.listdir(caminho):
    caminho_pasta = os.path.join(caminho, pasta) # quando cria uma variavel de caminho como agora no for e preciso adicionar o caminho completo
    print(pasta)
    if not os.path.isdir(caminho_pasta): # esse codigo e para caso tenha alguma pasta de sistema oculta que nao pode ser acessada
        continue
    for arquivo in os.listdir(caminho_pasta):
        print('   ', arquivo) # para ver a imagem e preciso juntar o caminho com o nome do arquivo