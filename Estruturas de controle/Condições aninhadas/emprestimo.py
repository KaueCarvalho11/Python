print("Empréstimo para compra de uma casa")

casa = float(input("Informe o valor da casa: R$"))
salario = float(input("Informe seu salário: R$"))
anos = int (input("Informe em quantos anos irá pagar a casa: "))

parcela = casa / (anos * 12)
print("As parcelas serão de R${:.2f}".format(parcela))

if parcela > salario * 0.30:
    print("Empréstimo negado, parcela excede 30% do seu salário!")

else:
    print("Empréstimo bem sucedido! ")
    