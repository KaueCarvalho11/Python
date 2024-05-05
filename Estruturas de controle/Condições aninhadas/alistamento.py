from datetime import date

nasceu = int(input("Informe seu ano de nascimento: "))

idade = date.today().year - nasceu

print("Quem nasceu em {} tem {} anos em {}".format(nasceu, idade, date.today().year ))

if idade < 18:
    print("Você ainda vai se alistar no serviço militar.")
    tempo = 18 - idade
    print("Faltam {} ano(s) para seu alistamento!".format(tempo))

elif idade == 18:
    print("É hora de se alistar!")

else:
    print("Já passou o tempo do seu alistamento.")
    tempo = 18 - idade
    print("Passaram-se {} anos do seu alistamento!".format(abs(tempo)))

print("Procure a junta de serviço militar mais próxima do seu município.")
