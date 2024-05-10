valor1 = float(input("Informe o primeiro valor: "))
valor2 = float(input("Informe o segundo valor: "))
opcao = 0

while opcao != 5:

    print("\nRealize operações sobre os valores informados!\n")

    print("-=" * 5, "MENU", "-=" * 5)
    opcao = int(input("[1] Somar\n[2] Multiplicar\n[3] Maior\n[4]Novos números\n[5] Sair do programa\n"))

    if opcao == 1:
        print(f"\n{valor1} + {valor2} = {valor1 + valor2}")

    elif opcao == 2:
        print(f"\n{valor1} x {valor2} = {valor1 * valor2}")

    elif opcao == 3:
        lista = [valor1, valor2]
        print(f"\nMaior valor informado: {max(lista)}")

    elif opcao == 4:
        print("Informe novos valores:")
        valor1 = float(input("Informe o primeiro valor: "))
        valor2 = float(input("Informe o segundo valor: "))
        print(f"Valores atualizados para {valor1} e {valor2}")

    elif opcao == 5:
        print("Fim da execução do programa!")

    else: 
        print("Opção inválida, tente novamente!")
