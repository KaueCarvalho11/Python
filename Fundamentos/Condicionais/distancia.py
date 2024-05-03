distancia = float(input("Informe a distância da viagem: km/h"))

if distancia <= 200:
    preco = distancia * 0.50
    print("Preço da passagem: R${:.2f}".format(preco))

else:
    preco = distancia * 0.45
    print("Preço da passagem: R${:.2f}".format(preco))
