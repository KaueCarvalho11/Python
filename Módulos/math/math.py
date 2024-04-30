import math
a = int(input("Informe um número: "))
raiz = math.sqrt(a)
print("Raíz de {}:".format(a))
print("Raíz com duas casas decimais: {:.2f}".format(raiz))
print("Arredondada pra cima: {}".format(math.ceil(raiz)))
print("Arredondada pra baixo: {}".format(math.floor(raiz)))
