from threading import Lock, Thread
from time import sleep

class Ingressos:
    def __init__(self, estoque:int):
        """Inicializando
        
        :param estoque: quantidade de ingressos em estoque
        """
        self.estoque = estoque
        self.Lock = Lock()


    def comprar(self, quantidade:int):
        """ 
        compra determinada quantidade de ingresso
        :param quantidade: A quantidade de ingressos que deseja comprar
        :return: Nada
        :rtype: None
        """
        self.Lock.acquire() # tranca o método
        if self.estoque < quantidade:
            print('Não temos ingressos suficientes')
            self.Lock.release()  #libera o método 
            return
        sleep(1)

        self.estoque -= quantidade
        print(f'Você comprou {quantidade} ingresso(s).'
              f'Ainda temos {self.estoque} em estoque')

        self.Lock.release()


if __name__ == '__main__':
    ingressos = Ingressos(10)

    # ingressos.comprar(1)
    # ingressos.comprar(1)
    # ingressos.comprar(1)
    for i in range(1, 20):
        # ingressos.comprar(i)
        t = Thread(target=ingressos.comprar, args=(i,))
        t.start()

    print(ingressos.estoque)





