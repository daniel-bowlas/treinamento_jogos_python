def jogar():
    print('*********************************')
    print("Bem vindo ao Jogo de Forca!")
    print("*********************************")

    palavra_secreta = "jaca".upper()
    letra_acertadas = ["_" for letra in palavra_secreta]

    enforcou = False
    acertou = False
    errou = 0

    while not enforcou and not acertou:

        chute = input("Qual letra? ")
        chute = chute.strip().upper()

        if chute in palavra_secreta:
            index = 0
            for letra in palavra_secreta:
                if chute == letra:
                    letra_acertadas[index] = letra
                index = index + 1
        else:
            errou += 1
            print("Ops, você errou! Faltam {} tentativas.".format(6 - errou))

        enforcou = errou == 6
        acertou = "_" not in letra_acertadas

        print(letra_acertadas)

    if acertou:
        print("Você ganhou!")
    else:
        print("Você foi enforcado!")
    print("Fim de jogo")


if __name__ == "__main__":
    jogar()
