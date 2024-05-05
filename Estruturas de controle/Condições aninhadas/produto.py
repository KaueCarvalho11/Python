produto = str(input("Informe o nome do produto: "))
preco = float(input("Informe o preço do produto: R$"))

print("Escolha a forma de pagamento: ")
escolha = int(input("1 - Á vista (dinheiro ou cheque, 10% de desconto)\n2 - Á vista no cartão (5% de desconto)\n3 - Parcelado (2x no cartão, preço normal)\n4 - Parcelado (3x ou mais no cartão, 20% de juros)\n"))

if escolha == 1:
    preco = preco - preco * 0.10
    print("Preço do produto {} á vista (dinheiro ou cheque) com 10% de desconto: R${:.2f}".format(produto, preco))

elif escolha == 2:
    preco = preco - preco * 0.05
    print("Preço do produto {} á vista (no cartão) com 5% de desconto: R${:.2f}".format(produto, preco))

elif escolha == 3:
    print("Preço do produto {} 2x no cartão (preço normal): R${:.2f}".format(produto, preco))
    parcela = preco / 2
    print("Sua compra será parcelada em 2x de R${:.2f}, sem juros adicionais.".format(parcela))

elif escolha == 4:
    preco = preco + preco * 0.20
    parcelas = int(input("Quantas parcelas? "))
    parcela = preco / parcelas

    print("Sua compra será parcelada em {}x de R${:.2f}".format(parcelas, parcela))
    print("Preço do produto {} parcelado ({}x no cartão) com 20% de juros: R${:.2f}".format(produto, parcelas, preco))

else:
    print("Opção inválida de pagamento!")
 