

class Carro:

    def __init__(self,nome):
        self.nome = nome
        self._motor = None
        self._fabricante = None



    @property
    def motor_do_carro(self):
        return self._motor


    @motor_do_carro.setter
    def motor_do_carro(self,motor):
        self._motor = motor

        

    @property
    def fabricante(self):
        return self._fabricante

    
    @fabricante.setter
    def fabricante(self, fabricante):
        self._fabricante = fabricante


class Motor:

    def __init__(self, nome):
        self.nome = nome


class Fabricante:

    def __init__(self, nome):
        self.nome = nome


fiat_palio = Carro('Palio')
fusca = Carro('Fusca')
caminhao = Carro('Caminhao')
chevete = Carro('Chevete')

fiat = Fabricante('Fabricante fiat')
mercedes = Fabricante('Fabricante Mercedes')
ferrari = Fabricante('Fabricante Ferrari')

motor_v8 = Motor('Motor V8')
motor_v12 = Motor('Motor V12')
motor_v10 = Motor('Motor V10')

fiat_palio.fabricante = fiat
fiat_palio.equipar_motor = motor_v8
print(fiat_palio.nome,fiat_palio.fabricante.nome, fiat_palio.equipar_motor.nome)


fusca.fabricante = ferrari
fusca.equipar_motor = motor_v12
print(fusca.nome, fusca.fabricante.nome, fusca.equipar_motor.nome)




caminhao.fabricante = mercedes
caminhao.equipar_motor =  motor_v10
print(caminhao.nome, caminhao.fabricante.nome, caminhao.equipar_motor.nome)

chevete.fabricante = ferrari
chevete.equipar_motor = motor_v8
print(chevete.nome,chevete.fabricante.nome, chevete.equipar_motor.nome)




