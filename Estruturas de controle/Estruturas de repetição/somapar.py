soma = 0
contador = 0

for c in range(1, 7):
    numero = int(input("Informe o {}º valor inteiro: ".format(c)))
    if numero % 2 == 0:
        soma += numero
        contador = contador + 1

print("Você informou {} números pares e a soma deles resultou em {}".format(contador, soma))
