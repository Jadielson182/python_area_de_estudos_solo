from pathlib import Path

caminho_projeto = Path()
# print(caminho_projeto.absolute())

caminho_arquivo = Path(__file__)
# print(caminho_arquivo)

# print(caminho_arquivo.parent.parent)

ideias = caminho_arquivo.parent / 'ideias'
# print(ideias / 'arquivo.txt')

# print(Path.home())

arquivo = Path.home() / 'Desktop' / 'arquivo_txt'

# arquivo.touch()
# print(arquivo)
# arquivo.write_text('Olá Mundo.') # esse comando se repetido so salva o ultima string 
# print(arquivo.read_text())
# # arquivo.unlink()

caminho_arquivo = Path.home() / 'Desktop' / 'arquivo_txt'

with caminho_arquivo.open('a+') as file:
    file.write('Uma linha\n')
    file.write('Outra linha\n')

print(caminho_arquivo.read_text())



