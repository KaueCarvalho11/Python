soma = 0
caro = 0
produtos = []

while True:
    print("\nFaça suas compras!")
    nome = str(input("Informe o nome do produto: ")).title().strip()

    preco = float(input("Informe o preço do produto: R$"))
    soma += preco
    produtos.append((preco, nome))

    escolha = str(input("Deseja continuar as compras? (S - Sim) ou (N - Não): ")).upper().strip()
    
    if preco > 1000:
        caro += 1

    if escolha == "N":
        break

barato = min(produtos)

print(f"\nO total gastro na compra foi R${soma:.2f}\n{caro} produtos custam mais de R$1000.00")
print(f"O produto mais barato foi {barato[1]} que custa R${barato[0]:.2f}")
