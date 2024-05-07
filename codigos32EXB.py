from codigos32EX import CAMINHO_DO_ARQUIVO, Pessoa, fazendo_dump
import json

# fazendo_dump()
with open(CAMINHO_DO_ARQUIVO, 'r', encoding='utf8') as arquivos:
    pessoas = json.load(arquivos)
    
    pessoa_1 = Pessoa(**pessoas[0])
    pessoa_2 = Pessoa(**pessoas[1])
    pessoa_3 = Pessoa(**pessoas[2])
    pessoa_4 = Pessoa(**pessoas[3])

cadastro = [pessoa_1.__dict__, pessoa_2.__dict__, pessoa_3.__dict__, pessoa_4.__dict__,]
# print(cadastro)
print()
if __name__ == '__main__':
    print('O codigo32EXB e o __main__')
    fazendo_dump()
if __name__ != '__main__':
    print('codigo32EXB e o __main__')
    