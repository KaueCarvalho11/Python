a = int(input("Informe o valor de a: "))
b = int(input("Informe o valor de b: "))
soma = a + b
subtracao = a - b
multiplicacao = a * b
divisao = a / b
divisaoint = a // b
potencia = a ** b

print("\nSoma: {}, subtração: {}, multiplicação: {} ".format(soma, subtracao, multiplicacao), end = " ")
print("Divisão: {:.3f}, Divisão inteira: {}, potenciação: {} ".format(divisao, divisaoint, potencia))

# Não quebrar linha: end = " "
# Quebrar linha: \n