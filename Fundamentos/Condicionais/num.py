numero1 = float(input("Informe um número: "))
numero2 = float(input("Informe outro número: "))
numero3 = float(input("Informe mais um número: "))

menor = min(numero1, numero2, numero3)
maior = max(numero1, numero2, numero3)

print("O maior número é {}\nO menor número é {}".format(maior, menor))
