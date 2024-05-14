print("Caixa eletrônico!")
valor = int(input("Informe o valor que deseja sacar: R$"))

total = valor
cedulas = [50, 20, 10, 1]

for cedula in cedulas:
    quantidade = total // cedula
    total %= cedula

    if quantidade > 0:
        print(f"{quantidade} cédula(s) de R${cedula:.2f}")

print("Dinheiro sacado com sucesso!")
