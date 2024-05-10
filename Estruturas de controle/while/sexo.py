sexo = ""

while sexo != "F" and sexo != "M":
    sexo = str(input("Informe seu sexo: (M - Masculino) ou (F - Feminino): ")).upper().strip()

    if sexo != "F" and sexo != "M":
        print("Dados inválidos, tente novamente ")

    else:
        print("Sexo {} registrado, fim da execução do programa.".format(sexo))
    