from dataclasses import dataclass

@dataclass
class Pessoa:
    nome: str
    idade: int
    @property
    def nome_completo(self):
        return f'{self.nome} {self.idade}'

    @nome_completo.setter
    def nome_completo(self, valor):
        self.nome = nome
        self.idade  = idade

if __name__ == '__main__':
    pessoa_1 = Pessoa('Jadielson', 35)
    print(pessoa_1.nome_completo)


