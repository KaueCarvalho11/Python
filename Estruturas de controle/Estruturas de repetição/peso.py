lista = []

for c in range (1, 5 + 1):
    peso = float(input("Informe o peso da {}ª pessoa: ".format(c)))
    lista.append(peso)

print("Maior peso: {}kg".format(max(lista)))
print("Menor peso: {}kg".format(min(lista)))
