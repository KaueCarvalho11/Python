from random import choice
from time import sleep

print("Jokenpô!\n")
nome = str(input("Informe seu nome: "))

print("-=" *5,"Faça sua jogada!", "-="*5)
escolha = int(input("Escolha uma opção:\n1 - Pedra\n2 - Papel\n3 - Tesoura\n"))

if escolha == 1:
    opcoes = ["Pedra", "Papel", "Tesoura"]
    pc = choice(opcoes)

    print("Hora do confronto!\nPedra, papel, teee...")
    sleep(3)
    print("SOURA!")

    print("{}: Pedra VS {} :Computador".format(nome, pc))

    if pc == "Pedra":
        print("Empate!")

    elif pc == "Papel":
        print("Computador venceu!")
    
    elif pc == "Tesoura":
        print("{} venceu!".format(nome))

elif escolha == 2:
    opcoes = ["Pedra", "Papel", "Tesoura"]
    pc = choice(opcoes)

    print("Hora do confronto!\nPedra, papel, teee...")
    sleep(3)
    print("SOURA!")

    print("{}: Papel VS {} :Computador".format(nome, pc))

    if pc == "Pedra":
        print("{} venceu!".format(nome))

    elif pc == "Papel":
        print("Empate!")

    elif pc == "Tesoura":
        print("Computador venceu! ")

elif escolha == 3:
    opcoes = ["Pedra", "Papel", "Tesoura"]
    pc = choice(opcoes)

    print("Hora do confronto!\nPedra, papel, teee...")
    sleep(3)
    print("SOURA!")

    print("{}: Tesoura VS {} :Computador".format(nome, pc))

    if pc == "Pedra":
        print("Computador venceu!")

    elif pc == "Papel":
        print("{} venceu!".format(nome))

    elif pc == "Tesoura":
        print("Empate!")

else:
    print("Opção inválida!")
    