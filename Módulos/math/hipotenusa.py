import math
print("Considere um triângulo retângulo")
oposto = float(input("Informe o comprimento do cateto oposto: "))
adjacente = float(input("Informe o comprimento d cateto adjacente: "))
hipotenusa = math.hypot(oposto, adjacente)
print(" Cateto oposto: {}\n Catedo adjacente: {}\n Hipotenusa: {:.2f}".format(oposto, adjacente, hipotenusa))
