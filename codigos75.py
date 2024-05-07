
from dataclasses import dataclass, field

@dataclass
class Pessoa:
    nome: str = field(default='MISSING', repr=False)
    sobrenome: str = 'Not sent'
    idade: int = 100
    enderecos: list[str]= field(default_factory=list)


if __name__ == '__main__':
    pessoa_1 = Pessoa()
    print(pessoa_1)