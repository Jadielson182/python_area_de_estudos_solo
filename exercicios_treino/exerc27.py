# Classe TV: Faça um programa que simule um televisor criando-o como um objeto.
# O usuário deve ser capaz de informar o número do canal e aumentar ou diminuir o volume. 
# Certifique-se de que o número do canal e o nível do volume permanecem dentro de faixas válidas.

class TV:
    def __init__(self, canal=0, volume=30):
        self.canal = canal
        self.volume = volume

    def selecionar_canal(self, canal):
        if canal > 0 and canal < 100:
            self.canal = canal
        else:
            print(f'Canal {canal} invalido')


    def aumentar_volume(self):
        if self.volume < 100:
            self.volume +=1

    def diminuir_volume(self):
        if self.volume > 0:
            self.volume -= 1

    
controle = TV()
controle.selecionar_canal(5)
controle.aumentar_volume()
controle.aumentar_volume()
controle.aumentar_volume()
controle.aumentar_volume()
controle.aumentar_volume()
controle.selecionar_canal(110)
print(f'\nCanal:', {controle.canal}, '\nVolume: ',{controle.volume})

    