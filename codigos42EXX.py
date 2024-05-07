class Carro:
    def __init__(self, nome):
        self.nome = nome
        self._fabricante = None
        self._motor = None


    @property
    def fabricante(self):
        return self._fabricante

    @fabricante.setter
    def fabricante(self, fabricante):
        self._fabricante = fabricante
  
    
    @property
    def motor(self):
        return self._motor

    @motor.setter
    def motor(self, motor):
        self._motor = motor


class Fabricante:
    def __init__(self,nome):
        self.nome = nome



class Motor:
    def __init__(self, nome):
        self.nome = nome


chevete = Carro('Chevete')
fusca = Carro('Fusca')
ferrari = Carro('Ferrari')
caminhao = Carro('Caminhão')
toro = Carro('Toro')

motor_1_0 = Motor('Motor 1.0')
motor_1_4 = Motor('Motor 1.4')
motor_1_6 = Motor('Motor 1.6')
motor_1_8 = Motor('Motor 1.8')
motor_2_0 = Motor('Motor 2.0')

ferrari_fabrica = Fabricante('Ferrari')
chevrolet = Fabricante('Chevrolet')
volkwagen = Fabricante('Volkswagen')
ford = Fabricante('Ford')
fiat = Fabricante('Fiat')

chevete.fabricante = chevrolet
chevete.motor = motor_1_4
print(f'{chevete.nome} fabricado pela {chevete.fabricante.nome} com {chevete.motor.nome}')
print()
fusca.fabricante = volkwagen
fusca.motor = motor_1_6
print(f'{fusca.nome} fabricado pela {fusca.fabricante.nome} com {fusca.motor.nome}')
print()
ferrari.fabricante = ferrari_fabrica
ferrari.motor = motor_2_0
print(f'{ferrari.nome} fabricado pela {ferrari.fabricante.nome} com {ferrari.motor.nome}.')
print()
caminhao.fabricante = ford
caminhao.motor = motor_1_8
print(f'{caminhao.nome}  fabricado pela {caminhao.fabricante.nome} com {caminhao.motor.nome}.')
print()
toro.fabricante = fiat
toro.motor = motor_1_0
print(f'{toro.nome} fabricado pela {toro.fabricante.nome} com {toro.motor.nome}.')
print()

