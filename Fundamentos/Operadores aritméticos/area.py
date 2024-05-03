largura = float(input("Informe a largura da parede: "))
altura = float(input("Informe a altura da parede: "))
area =  largura * altura
tinta = area / 2
print("Sua parede tem a dimensão de {}x{}".format(largura, altura))
print("Área {}m²".format(area))
print("Quantidade de tinta necessária para pinta-la: {}l ".format(tinta))
