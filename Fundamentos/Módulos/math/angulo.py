import math
angulo = float(input("Informe um ângulo: "))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))
print(" Ângulo: {}\n Seno: {:.2f}\n Cosseno: {:.2f}\n Tangente: {:.2f}".format(angulo, seno, cosseno, tangente))
