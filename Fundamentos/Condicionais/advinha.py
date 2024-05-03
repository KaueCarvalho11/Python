import random
import time

print("Computador está pensando em um número entre 0 e 5...")
pc = random.randint(0,5)
time.sleep(3)

usuario = int(input("Advinhe o número que o computador está pensando: "))
print("Número pensado pelo computador: {}\n Número escolhido: {}".format(pc, usuario))

if usuario == pc:
    print("Acertou!")

else:
    print("Errou!")
print("Fim de jogo")
