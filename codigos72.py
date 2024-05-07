
from dataclasses import dataclass

@dataclass
class Pessoa:
    nome: str
    sobrenome: str

    def __post_init__(self):
        self.nome_completo = f'{self.nome} {self.sobrenome}'

if __name__ == '__main__':
    pessoa_1 = Pessoa('Jadielson', 'Silva')
    print(pessoa_1)
    print(pessoa_1.nome_completo)