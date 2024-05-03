salario = float(input("Informe o salário do funcionário: R$"))
aumento = salario * 15/100
novosalario = salario + aumento
print("Salário base: R${:.2f}".format(salario))
print("Salário após o aumento de 15%: R${:.2f}".format(novosalario))
