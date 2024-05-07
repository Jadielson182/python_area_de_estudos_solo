
from dataclasses import dataclass

@dataclass(init=False)
class Pessoa:
    nome: str
    sobrenome: str

    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome
        self.nome_completo = f'{self.nome} {self.sobrenome}'


if __name__ == '__main__':
    pessoa_1 = Pessoa('Jadielson', 'Silva')
    print(pessoa_1)
    print(pessoa_1.nome_completo)