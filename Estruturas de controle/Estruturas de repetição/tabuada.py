numero = int(input("Informe um número: "))

for c in range (1, 11):
    soma = numero * c
    print("{} X {:2} = {} ".format(numero, c, soma))
