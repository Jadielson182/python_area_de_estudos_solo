
class Classe:

    @staticmethod
    def funcao_que_esta_na_classe(*args, **kwargs):
        print('Oi', args, kwargs)

    
def funcao(*args, **kwargs):
    print('Oi', args, kwargs)


classe_1 = Classe()
classe_1.funcao_que_esta_na_classe(1, 2, 3)
funcao(1, 2, 3)
Classe.funcao_que_esta_na_classe(nomeado=15)
funcao(nomeado=15)


