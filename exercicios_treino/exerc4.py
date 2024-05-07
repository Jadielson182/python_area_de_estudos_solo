
# caminho_arquivo = 'exercicios_treino\\exerc4.txt'

# def criar_arquivo(txt):
#     with open(caminho_arquivo, 'w+', encoding='utf8') as arquivo:
#         arquivo.writelines(txt)
#     return arquivo
  
# def listar_arquivo(arquivos):
#     with open(caminho_arquivo, 'r+', encoding='utf8') as arquivo:
#         for  numero, item in enumerate(arquivos):
#             print(numero, item)
        





# criar_arquivo(('cavalo\n', 'Leão\n', 'macaco\n', 'galinha\n'))
# listar_arquivo(caminho_arquivo)


caminho_arquivo = 'exercicios_treino\\exerc4.txt'

    
        
        

with open(caminho_arquivo, 'w+', encoding='utf8') as arquivo:
    arquivo.writelines(('cavalo\n', 'Leão\n', 'macaco\n', 'galinha\n'))


with open(caminho_arquivo, 'r+', encoding='utf8') as arquivo:
    novo_arquivo = arquivo.read()

print(novo_arquivo)