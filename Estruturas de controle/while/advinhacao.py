from random import randint
from time import sleep

computador = randint(0, 10)

print("Sou seu computador... acabei de pensar em um número entre 0 e 10")
print("Será que você consegue advinhar?")
acertou = False
palpite = 0

while acertou == False:
    jogador = int(input("Qual é o seu palpite? "))
    palpite += 1

    if jogador == computador:
        acertou = True

    else:
        if jogador < computador:
            print("Mais...")

        elif jogador > computador:
            print("Menos...")

if palpite == 1:
    print(f"UAU! parabéns! você acertou com apenas {palpite} tentativa, de primeira!")

elif palpite <= 5:
    print(f"Parabéns! você acertou com apenas {palpite} tentativas, você é bom nisso!")

elif palpite > 5 and palpite < 10:
    print(f"Parabéns! você acertou com {palpite} tentativas, nem demorou tanto assim!")

elif palpite > 10:
    print(f"Parabéns! você acertou com {palpite} tentativas, mais sorte da próxima vez")
