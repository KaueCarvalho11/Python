media = 0
velho = 0
homem = ""
mulheres = 0

for c in range (1, 5):
    print("\nCadastro:")
    nome = str(input("Informe o nome da {} pessoa: ".format(c)))

    idade = int(input("Informe a idade da pessoa: "))
    media += idade

    sexo = str(input("Informe o sexo da pessoa: (M - Masculino) e (F - Feminino): "))
    if sexo.upper() == "M" and idade > velho:
        velho = idade
        homem = nome

    if sexo.upper() == "F" and  idade < 20:
        mulheres += 1

print("\nA media de idade é: {}".format(media/4))
print("O homem mais velho se chama: {}".format(homem))
print("Quantidade de mulheres com menos de 20 anos: {}".format(mulheres))
