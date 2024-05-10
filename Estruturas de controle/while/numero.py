numero = 1
par = 0
impar = 0

while numero != 0:
    numero = int(input("Informe um número: "))

    if numero % 2 == 0 and numero != 0:
        print("Número par")
        par += 1

    if numero % 2 != 0:
        print("Número ímpar")
        impar += 1

print("{} números pares e {} números ímpares: ".format(par, impar))
