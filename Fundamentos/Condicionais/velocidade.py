velocidade = float(input("Informe a velocidade do carro: km/h"))

if velocidade > 80.0:
    print("Velocidade além do limite!")
    multa = (velocidade - 80) * 7
    print("Multado em R${:.2f}".format(multa))

else:
    print("Velocidade permitida!")
