print("Progressão aritmética")

primeiro = int(input("Informe o primeiro termo da progressão aritmética: "))
razao = int(input("Informe a razão da progressão aritmética: "))
termo = primeiro
contador = 1

while contador <= 10:
    print(termo, end = " ")
    termo += razao
    contador += 1

continuar = True

while continuar == True:
    mais = int(input("\nQuantos mostrar quantos mais termos? "))

    if mais == 0:
        continuar = False

    else:
        contador = 1
        while contador <= mais:
            print(termo, end = " ")
            termo += razao
            contador += 1

print(f"Progressão finalizada.")