reta1 = float(input("Informe o cumprimento do primeiro segmento: "))
reta2 = float(input("Informe o cumprimento do segundo segmento: "))
reta3 = float(input("Informe o cumprimento do terceiro segmento: "))

if reta1 + reta2 > reta3 and reta1 + reta3 > reta2 and reta2 + reta3 > reta1:
    print("É possível formar um triângulo!")

else:
    print("Não é possível formar um triângulo!")
    