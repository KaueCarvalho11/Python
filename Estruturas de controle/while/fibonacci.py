print("Sequência de fibonacci")

fibonacci = int(input("Quantos elementos da sequência de fibonacci deseja ver? "))
contador = 1
primeiro = 0
segundo = 1  

while contador <= fibonacci:
    print(primeiro)
    proximo = primeiro + segundo
    primeiro = segundo
    segundo = proximo
    contador +=  1
