contador = 1

while True:
    numero = int(input("Informe o número que deseja ver a tabuada: (Número negativo para interromper a execução): "))

    if numero < 0:
        break

    while contador <= 10:
        resultado = numero * contador
        print(f"{numero} X {contador} = {resultado}")
        contador +=1

    contador = 1
  
print("Fim da execução do programa")
    