real = float(input("Informe o valor em dinheiro que você tem na sua carteira: R$"))
dolar = real / 5.12
print("Com R${:.2F} é possível comprar US${:.2F} ".format(real, dolar))