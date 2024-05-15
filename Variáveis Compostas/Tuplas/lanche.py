lanche = "Hamburger", "Suco", "Pizza", "Pudin"
print(lanche)
print(lanche[1])
print(lanche[3])
print(lanche[-2])
print(lanche[1:3])
print(lanche[2:])
print(lanche[:2])
print(lanche[-2:])
print(lanche[-3:])

print(len(lanche))

for comida in lanche:
    print(f"Eu vou comer {comida}")

for contador in range(0, len(lanche)):
    print(f"Eu ja comi {lanche[contador]} na posição {contador}")

for posicao, comida in enumerate(lanche):
    print(f"Eu vou comer {comida} na posição {posicao}")

print(lanche)
print("\n",sorted(lanche))
