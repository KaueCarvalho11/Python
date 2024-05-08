print("Progressão aritmética! ")

primeiro = int(input("Informe o primeiro termo da progressão aritmética: "))
razao = int(input("Informe a razão da progressão aritmética: "))

for c in range (10):
    termo = primeiro + c * razao
    print(termo)
