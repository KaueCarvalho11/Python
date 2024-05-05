from datetime import date

ano = int(input("Informe o ano de nascimento do atleta: "))
idade = date.today().year - ano

print("O atleta tem {} anos".format(idade))

if idade <= 9:
    print("Atleta da categoria mirim!")

elif idade > 9 and idade <= 14:     
    print("Atleta da categoria infantil!")

elif idade > 14 and idade <= 19:
    print("Atleta da categoria junior!")

elif idade > 19 and idade <= 25:
    print("Atleta da categoria sênior!")

else:
    print("Atleta da categoria master!")
    