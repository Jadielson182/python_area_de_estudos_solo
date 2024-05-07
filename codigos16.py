caminho_arquivo = 'arquivo_txt'

with open(caminho_arquivo, 'w+', encoding='utf-8')as arquivo:
    arquivo.write('atenção aqui\n')
    arquivo.write('atençao la\n')
    arquivo.writelines(
        ('atenção se foi\n', 'atenção ainda não foi')
    )
