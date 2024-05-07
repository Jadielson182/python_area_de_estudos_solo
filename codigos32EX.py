import json

CAMINHO_DO_ARQUIVO = 'codigos32EX.json'


class Pessoa:
    def __init__(self, nome, idade, sexo):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo

pessoa_1 = Pessoa('Jadielson', 35, 'M')
pessoa_2 = Pessoa('Maria', 34, 'F' )
pessoa_3 = Pessoa('Carlos', 27, 'M')
pessoa_4 = Pessoa('sushi', 19, 'F')
cadastro = [pessoa_1.__dict__, pessoa_2.__dict__, pessoa_3.__dict__, pessoa_4.__dict__]

def fazendo_dump():
    with open(CAMINHO_DO_ARQUIVO, 'w+', encoding='utf8') as arquivo:
        print('Fazendo Dump')
        json.dump(cadastro,arquivo, indent=2,ensure_ascii=False)

# print(__name__)

if __name__ != '__main__':
    print('codigo32EX  não e o __main__')
    # fazendo_dump()
if __name__ == '__main__':
    print('O codigo32EX e o main')
    fazendo_dump()

# with open(CAMINHO_DO_ARQUIVO, 'r', encoding='utf8') as arquivo:
#     novo_arquivos = json.load(arquivo)
#     print(novo_arquivos)
# print(Pessoa)
