from datetime import date

maioridade = 0
menoridade = 0

for c in range (1, 8):
    ano = int(input("Informe um ano de nascimento: "))
    idade = date.today().year - ano
    
    if idade >= 21:
        maioridade +=1

    else:
        menoridade +=1

print("{} pessoas atingiram a maioridade\n{} pessoas ainda são de menor ".format(maioridade, menoridade))
