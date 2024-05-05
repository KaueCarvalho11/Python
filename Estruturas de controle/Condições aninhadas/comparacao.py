numero1 = int(input("Informe o valor do número 1: "))
numero2 = int(input("Informe o valor do número 2: "))

if numero1 > numero2:
    print("O {} é maior\nO {} é menor".format(numero1, numero2))

elif numero2 > numero1:
    print("O {} é maior\nO {} é menor".format(numero2, numero1))

else:
    print("Não existe valor maior, os dois são iguais")
