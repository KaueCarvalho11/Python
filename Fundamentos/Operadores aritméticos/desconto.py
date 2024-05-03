produto = input("Digite o nome de um produto: ")
preco = float(input("Informe o preço do produto {}: R$".format(produto)))
desconto = preco * 5/100
novopreco = preco - desconto
print("Valor do produto {} após o desconto de 5%: R{:.2f}".format(produto, novopreco))