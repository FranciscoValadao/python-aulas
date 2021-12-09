print ("*******************")
print ("Jogo de adivinhação")
print ("*******************")

total_tentativas= 3
numero_secreto = 42
rodada = 1

while(total_tentativas>0):
    print("tentativa", rodada, "de 3")
    rodada = rodada+1
    chute_inp = input("digite o seu número:")
    chute = int(chute_inp)
    print('voce digitou:',chute)
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
