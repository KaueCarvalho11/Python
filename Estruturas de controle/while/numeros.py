continuar = "S"
media = 0
contador = 0
lista = []

while continuar == "S":
    numero = int(input("Digite um número inteiro: "))
    contador += 1
    media += numero
    lista.append(numero)
    continuar = str(input("Deseja continuar digitando valores? (S - Sim) ou (N - Não): ")).upper().strip()

    if continuar == "N":
        break

media = media/contador
print(f"\nVocê digitou {numero} números")
print("A média entre os valores digitados foi {:.2f}".format(media))
print(f"Maior valor informado: {max(lista)}\nMenor valor informado: {min(lista)}")
print("Fim da execução do programa")
