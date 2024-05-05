from math import pow

print("Cálculo de índice de massa corporal (IMC)")

peso = float(input("Informe seu peso: "))
altura = float(input("Informe sua altura: "))
imc = peso / pow(altura, 2)

print("Seu IMC é de {:.1f}".format(imc))

if imc < 18.5:
    print("Abaixo do peso.")

elif imc >= 18.5 and imc < 25:
    print("Peso ideal.")

elif imc >= 25 and imc < 30:
    print("Sobrepeso.")

elif imc >= 30 and imc < 40:
    print("Obesidade.")

else:
    print("Obesidade mórbida")  
