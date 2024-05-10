numero = 0
contador = 0
soma = 0

while numero != 999:
    numero = int(input("Informe um número inteiro: (999 para parar) "))
    if numero != 999:
        contador += 1
        soma += numero

    if numero == 999:
        break

print(f"\nForam digitados {contador} números e a soma deles resultou em {soma}")
print("\nFim da execução do programa")
