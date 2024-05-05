numero = int(input("Informe um número inteiro: "))

print("Escolha uma base de conversão para o número {}.".format(numero))
escolha = int (input(("1 - Binário\n2 - Octal\n3 - Hexadecimal:\n\n")))

if escolha == 1:
    print("\n{} em binário: {}".format(numero, bin(numero)[2:]))

elif escolha == 2:
    print("\n{} em octal: {}".format(numero, oct(numero)[2:]))

elif escolha == 3:
    print("\n{} em hexadecimal: {}".format(numero, hex(numero)[2:]))

else:
    print("Opção inválida")
