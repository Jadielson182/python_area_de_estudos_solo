class pessoa:
    def __init__(self,nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome


p1 = pessoa('Luiz', 'Otávio')
# p1.nome = 'Luiz'
# p1.sobrenome = 'Otávio'


p2 = pessoa('Maria', 'Joana')
# p2.nome = 'Maria'
# p2.sobrenome = 'Joana'


print(p1.nome)
print(p1.sobrenome)

print(p2.nome)
print(p2.sobrenome)