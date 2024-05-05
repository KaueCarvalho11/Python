nome = str(input("Informe seu nome: "))

if nome == "Kauê":
    print("Que belo nome! ")

elif nome == "Cleber" or nome == "Osmildo" or nome == "Antedeguemon":
    print("Esse nome me soa familiar")

elif nome in "Ana Claudia Jessica Juliana":
    print("Belo nome feminino   ")

else:
    print("Que nome comum!")

print("Tenha um bom dia, {}!".format(nome))
