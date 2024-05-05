condicao = False

reta1 = float(input("Informe o comprimento do primeiro segmento: "))
reta2 = float(input("Informe o comprimento do segundo segmento: "))
reta3 = float(input("Informe o comprimento do terceiro segmento: "))

if reta1 + reta2 > reta3 and reta1 + reta3 > reta2 and reta2 + reta3 > reta1:
    condicao = True
    print("É possível formar um triângulo!")

if condicao == True:
    if reta1 == reta2 == reta3:
        print("Triângulo equilátero, pois, todos os lados são iguais.")
    
    elif reta1 == reta2 or reta1 == reta3 or reta2 == reta3:
        print("Triângulo isósceles, pois, dois lados são iguais.")
    
    else:
        print("Triângulo escaleno, pois, todos os lados são diferentes")

else:
    print("Não é possível formar um triângulo")
 