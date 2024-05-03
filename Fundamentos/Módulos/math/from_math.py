from math import sqrt, ceil, floor
a = int(input("Informe um número: "))
raiz = sqrt(a)
print("{}".format(a))
print("Raíz: {:.2f}".format(raiz))
print("Raíz arredondada pra cima: {}".format(ceil(raiz)))
print("Raíz arredondada para baixo: {}".format(floor(raiz)))
