a = int(input("Informe um valor: "))
dobro = a * 2
triplo = a * 3
raiz_quadrada = a**(1/2)

print("O dobro de {} é {}".format(a, dobro))
print("O tríplo de {} é {}".format(a, triplo))
print("A raíz quadrada de {} é {:.2f}".format(a, raiz_quadrada))
print("Raíz quadrada cálculada com a função 'pow': {}".format(pow(a, (1/2))))
