print ("*******************")
print ("Jogo de adivinhação")
print ("*******************")

numero_secreto = 42
chute_inp = input("digite o seu número:")
chute = int(chute_inp)
print('voce digitou:',chute)
maior = (chute > numero_secreto)
menor = (chute < numero_secreto)

if numero_secreto == chute:
    print ("acertou")
else:
    if (maior):
        print ("achou muito, otário")
    elif(menor):
        print("achou pouco, otário")

