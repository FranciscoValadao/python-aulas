import random


def jogar():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")
    print("TEMA 1: CARROS")
    print("TEMA 2: FRUTAS")

    tema = input("Selecione o tema (1) OU (2): ")

    if tema == "1":
        print("selecionou CARROS")
        arquivo = open("carros.txt", "r")
        palavras = []

        for linha in arquivo:
            linha = linha.strip()
            palavras.append(linha)

        arquivo.close()
    else:
        print("selecionou FRUTAS")
        arquivo = open("frutas.txt", "r")
        palavras = []

        for linha in arquivo:
            linha = linha.strip()
            palavras.append(linha)

        arquivo.close()

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()
    tamanho = len(palavra_secreta)
    letras_acertadas = ["_" for letra in palavra_secreta]
    erros = 0

    print("A palavra possui", tamanho, "letras")

    enforcou = False
    acertou = False

    while not enforcou and not acertou:

        chute = input("Qual letra? ")
        chute = chute.strip().upper()

        if chute in palavra_secreta:
            index = 0

            for letra in palavra_secreta:
                if chute.upper() == letra.upper():
                    letras_acertadas[index] = letra
                index += 1
                if "_" not in letras_acertadas:
                    acertou = 1
                    print("deu bom!")

        else:
            erros += 1
            if erros == 6:
                enforcou = 1
                print("deu ruim")

        print(letras_acertadas)

    print("Fim do jogo")


if __name__ == "__main__":
    jogar()
