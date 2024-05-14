contador = 0
soma = 0

while True:
    numero = float(input(("Informe um número (999 para interromper execução do programa): ")))

    if numero == 999:
        break

    contador += 1
    soma += numero
    
print(f"Foram digitados {contador} números e a soma entre eles resultou em {soma}")
        