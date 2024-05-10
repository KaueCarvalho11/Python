from time import sleep
from random import randint

computador = 0
usuario = 1
contador = 0

while computador != usuario:

    print("Computador está pensando em um número entre 0 e 10...")
    computador = randint(0, 10)
    sleep(3)

    usuario = int(input("Advinhe o valor que o computador pensou: "))
    contador += 1
    print("Número que o computador pensou: {}\nNúmero que você informou: {}".format(computador, usuario))

    if computador == usuario:
        print("\nAcertou! Fim de jogo")
        print("Você precisou de {} palpite(s)!".format(contador))

    else:
        print("\nTente novamente")
