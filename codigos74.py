
from dataclasses import asdict, astuple, dataclass

@dataclass
class Pessoa:
    nome: str
    sobrenome: str


if __name__ == '__main__':
    pessoa_1 = Pessoa('jadielson', 'Silva')
    print(pessoa_1)
    print(asdict(pessoa_1))
    print(astuple(pessoa_1))
    print(asdict(pessoa_1).values())
    print(asdict(pessoa_1).keys())
    print(asdict(pessoa_1).items())
    print(astuple(pessoa_1)[0])

  

