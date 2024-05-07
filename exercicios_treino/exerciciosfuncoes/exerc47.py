# Jogo de Craps. Faça um programa de implemente um jogo de Craps. O jogador lança um par de dados, 
# obtendo um valor entre 2 e 12. Se, na primeira jogada, você tirar 7 ou 11, você um "natural" e ganhou.
#  Se você tirar 2, 3 ou 12 na primeira jogada, isto é chamado de "craps" e você perdeu. Se, na primeira jogada,
#   você fez um 4, 5, 6, 8, 9 ou 10,este é seu "Ponto". Seu objetivo agora é continuar jogando os dados até tirar este número novamente.
#  Você perde, no entanto, se tirar um 7 antes de tirar este Ponto novamente.
import random
def jogar_dados():
    dado1 = random.randrange(1, 7)
    dado2 = random.randrange(1, 7)
    return dado1 + dado2


print('========VAMOS COMEÇAR O JOGO DO SCRAP========')    
ganhou = "Você ganhou, parabéns\n"
perdeu = "\n\n\t***** Craps! *****\n\nVocê perdeu!!!\tTente de novo\n"
ponto = "ponto\n"

while True:
    pontos = 0
    jogada = jogar_dados()
    if jogada == 7 or jogada == 11:
        print(jogada)
        print(ganhou)
        break
    if jogada == 2 or jogada == 3 or jogada == 12:
        print(jogada)
        print(perdeu)
        break
    else:
        print(jogada)
        pontos += jogada
        jogando = jogar_dados()
        if jogada == jogando:
            print(ganhou)
            break
        elif jogando == 7:
            print(perdeu)
            break



    
   

    


        




jogar_dados()