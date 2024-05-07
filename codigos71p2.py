from dataclasses import dataclass

@dataclass
class Pessoa:
    nome: str 
    sobrenome: str

    @property
    def nome_completo(self):
        return f'{self.nome} {self.sobrenome}'

    @nome_completo.setter
    def nome_completo(self, valor):
        nome, *sobrenome = valor.split()
        sobrenome = ' '.join(sobrenome)
        self.nome = nome
        self.sobrenome = sobrenome


if __name__ == '__main__':
    pessoa_1 = Pessoa('Jadielson', 'Silva')
    print(pessoa_1)
    pessoa_1.nome_completo = 'Maria Helena da Silva'
    print(pessoa_1.nome_completo)
