km = float(input("Quantos quilômetros foram percorridos com o carro? "))
dias = int(input("Por quantos dias o carro foi alugado? "))
diaria = dias * 60
quilometragem = km * 15/100
total = diaria + quilometragem
print("Valor a ser pago: R${:.2f}".format(total))
