import os

caminho_arquivo = 'C:\\Users\\jadie\\Documents\\arquivos python\\'
caminho_arquivo += 'arquivo_1.txt'

novo_caminho = 'C:\\Users\\jadie\\Documents\\arquivos python\\interna\\'
novo_caminho += 'aruivo_2.txt'

with open(caminho_arquivo, 'w+', encoding='utf8') as arquivo:
    arquivo.write('Atenção pessoal\n')
    arquivo.writelines(
        ('python e django\n', 'javascript\n', 'Html 5 e css3\n')
    )

# os.unlink(caminho_arquivo)
# os.remove(caminho_arquivo)
os.rename(caminho_arquivo, novo_caminho)