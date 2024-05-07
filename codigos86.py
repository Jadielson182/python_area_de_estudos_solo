import os

caminho = os.path.join('/home/users', 'Desktop', 'Curso', 'arquivo.txt')
print(caminho)

diretorio, arquivo = os.path.split(caminho)
nome_caminho, extensao_arquivo = os.path.splitext(caminho)
# print(nome_caminho, extensao_arquivo)
# print(os.path.exists('C:/Users/jadie/Desktop/pyton area de  estudos solo'))
# print(os.path.abspath('.'))
print(os.path.basename(caminho))
print(os.path.basename(diretorio))
# print(os.path.dirname(caminho))

