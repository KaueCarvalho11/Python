salario = float(input("Informe o salário do funcionário: R$"))

if salario > 1250:
    aumento = salario * 0.10
    novosalario = salario + aumento
    print("Salário R${:.2f} receberá um aumento de 10%, que equivale a {:.2f}".format(salario, aumento))
    print("Novo salário: R${:.2f}".format(novosalario))

else:
    aumento = salario * 0.15
    novosalario = salario + aumento
    print("Salário R${:.2f} receberá um aumento de 15%, que equivale a {:.2f}".format(salario, aumento))
    print("Novo salário: R${:.2f}".format(novosalario))
