maioridade = 0
masculino = 0
feminino = 0

while True:
    print("\nSistema de cadastro")
    idade = int(input("Informe sua idade: "))
    sexo = str(input("Informe seu sexo: (M - Masculino) ou (F - Feminino): ")).strip().upper()
    escolha = str(input("Deseja continuar a cadastrar pessoas? (S - Sim) ou (N - Não): ")).strip().upper()

    if idade > 18:
        maioridade += 1

    if sexo == "M":
        masculino += 1

    if sexo == "F" and idade < 20:
        feminino += 1

    if escolha == "N":
        break


print(f"\n{maioridade} pessoas tem mais de 18 anos\n{masculino} pessoas são do sexo masculino")
print(f"{feminino} pessoas são do sexo feminino e tem menos de 20 anos")
