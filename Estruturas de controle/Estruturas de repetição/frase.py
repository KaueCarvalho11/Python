frase = str(input("Digite uma frase qualquer: ")).replace(" ", "").upper()

palindromo = True
for c in range (len(frase)):
    if frase [c] != frase [len(frase) -c-1]:
        palindromo = False
        break

if palindromo:
    print("A frase é um palíndromo.")

else:
    print("A frase não é um palíndromo.")
    