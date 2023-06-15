import random


def jogar():
    print("*********************************")
    print("Bem vindo ao Jogo de Adivinhacao!")
    print("*********************************")

    numero_secreto = random.randrange(1, 101)
    tentativas = 0
    pontos = 1000

    print("Escolha um nivel de dificuldade")
    nivel = int(input("[1]Facil [2]Medio [3]Dificil: "))

    if nivel == 1:
        tentativas = 20
    elif nivel == 2:
        tentativas = 10
    elif nivel > 3 or nivel < 1:
        print("Escolhe um nivel que existe po kkkk")
        tentativas = 0
    else:
        tentativas = 5

    for rodada in range(1, tentativas + 1):
        print("Tentativa {} de {}".format(rodada, tentativas))
        chute = int(input("Digite um numero: "))
        print("Você digitou ", chute)

        if chute < 1 or chute > 100:
            print("Voce deve digitar um numero entre 0 - 100!")
            continue

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if acertou:
            print("Voce acertou! O numero era {} e voce atingiu {} pontos ".format(numero_secreto, pontos))
            break
        else:
            print("Voce errou!")
            if maior:
                print("Seu chute foi maior que o numero secreto")
            elif menor:
                print("Seu chute foi menor que o numero secreto")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos

    print("Fim do jogo. O numero era {}".format(numero_secreto))


if __name__ == "__main__":
    jogar()
