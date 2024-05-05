nota1 = float(input("Informe a primeira nota do aluno: "))
nota2 = float(input("Informe a segunda nota do aluno: "))
media = (nota1 + nota2) / 2

if media < 5.0:
    print("Sua média foi {:.1f}, REPROVADO!".format(media))

elif media >= 5.0 and media < 7.0:
    print("Sua média foi {:.1f}, RECUPERAÇÃO!".format(media))

else:
    print("Sua média foi {:.1f}, APROVADO!".format(media))
    