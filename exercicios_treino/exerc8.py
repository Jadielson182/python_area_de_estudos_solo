# Crie uma classe Baralho que represente um baralho de cartas. 
#Adicione métodos para embaralhar o baralho e distribuir cartas para jogadores.

import random

class Baralho:
    def __init__(self):
        self.cartas = ['Valete (J)', 'Dama (Q)', 'Rei (K)', '8 Copas (♥)', ' 8 Espadas (♠)', ' 8 Ouros (♦)', 'AS Paus (♣)',
        'AS Espadas (♠)','Coringa', '8 paus (♣)']
        self.mao_jogador1 = None
        self.mao_jogador2 = None
        

    def embaralhar(self):
        random.shuffle(self.cartas)
        return self.cartas
        

    def distribuir_cartas(self, numero_cartas):
        random.choices
        self.mao_jogador1 = random.sample(self.cartas, numero_cartas)
        self.mao_jogador2 = random.sample(self.cartas, numero_cartas)
        return (f'Mão de Jadielson {self.mao_jogador1}\n'
                f'Mao de Luiz {self.mao_jogador2}')

    def __repr__(self):
        class_name = type(self).__name__
        attr = f'{self.cartas!r} {self.mao_jogador1!r} {self.mao_jogador2!r}'
        return f'{class_name} {attr}'

# Exemplo de uso:
baralho = Baralho()
baralho.embaralhar()
mao_jogador1 = baralho.distribuir_cartas(5)
# mao_jogador2 = baralho.distribuir_cartas(5)
print(mao_jogador1)
# print(mao_jogador2)
# print(baralho.cartas)