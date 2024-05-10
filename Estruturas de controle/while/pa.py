print("Progressão aritmética! ")

primeiro = int (input("Informe o primeiro termo da progressão aritmética: "))
razao = int(input("Informe a razão da progressão aritmética: "))
termo = primeiro
contador = 1


while contador <= 10:
    print(termo)
    termo += razao
    contador += 1 

print("Fim da progressão aritmética.")
