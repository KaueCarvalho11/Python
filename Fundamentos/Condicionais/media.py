nota1 = float(input("Informe a primeira nota: "))
nota2 = float(input("Informe a segunda nota: "))
media = (nota1 + nota2) / 2

print("Média: {:.1f}".format(media))

if media >= 7.0:
    print("Aprovado!")
    
else:
    print("Reprovado!")
print("Até próximo ano! ")
