from random import randint

contador = 0

print("Disputa de par ou ímpar com o computador! "),
nome = str(input("Informe seu nome: ")).title().strip()

while True:

    print("-=" *5, f"Faça sua jogada, {nome}!", "-="*5)
    escolha = (int(input("1 - Ímpar\n2 - Par\n")))
    numero = int(input("Escolha seu número: "))

    if escolha == 1:
        print(f"Computador: Par X Ímpar :{nome}")
        pc = randint(0, 10)
        print(f"Computador: {pc} X {numero} :{nome} = {numero + pc}")

        if (numero + pc) % 2 == 0:
            print(f"{numero + pc} é par, Computador venceu!")
            break
        
        else:
            print(f"\n{numero + pc} é ímpar, {nome} venceu!\n")
            contador += 1
            print("\nVamos jogar novamente!\n")

    if escolha == 2:
        print(f"Computador: ímpar X Par :{nome}")
        pc = randint(0, 10)
        print(f"Computador: {pc} X {numero} :{nome} = {numero + pc}")

        if (numero + pc) % 2 == 0:
            print(f"\n{numero + pc} é par, {nome} venceu!")
            contador += 1
            print("\nVamos jogar novamente!\n")

        else:
            print(f"{numero + pc} é ímpar, computador venceu!")
            break

print(f"\n{nome} conquistou {contador} vitórias consecutivas! fim de jogo.")
    