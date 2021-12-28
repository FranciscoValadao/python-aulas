import random

def jogar():
    print ("*******************")
    print ("Jogo de adivinhação")
    print ("*******************")

    total_tentativas= 6
    numero_secreto = random.randrange(1,100)
    rodada = 1

    while(total_tentativas>0):
        print("tentativa", rodada, "de 6")
        chute_inp = input("digite o seu número:")
        chute = int(chute_inp)
        print('voce digitou:',chute)
        if (0 < chute < 100):
            rodada = rodada + 1
            maior = (chute > numero_secreto)
            menor = (chute < numero_secreto)

            if numero_secreto == chute:
                print ("acertou")
                break
            else:
                if (maior):
                    print ("achou muito, otário")
                elif(menor):
                    print("achou pouco, otário")
            total_tentativas = total_tentativas -1
        else:
            print("**************************")
            print("o valor deve ser de 1 a 99")
            print("**************************")
    print("**************************")
    print("Fim de jogo")
    print("**************************")
if(__name__ == "__main__"):
    jogar()

