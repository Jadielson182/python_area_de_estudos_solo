from dataclasses import dataclass

@dataclass
class Pessoa:
    nome: str
    sobrenome: str
    idade: int

if __name__ == '__main__':
    pessoa_1 = Pessoa('jadielson', 'Silva', 35)
    print(pessoa_1)

    pessoa_2 = Pessoa('jadielson', 'Silva', 35)
    print(pessoa_1 == pessoa_2)
