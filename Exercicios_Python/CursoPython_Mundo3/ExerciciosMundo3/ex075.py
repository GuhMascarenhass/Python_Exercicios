i = int(input("Digite o primeiro valor: ")),\
    int(input("Digite o segundo valor:")), \
    int(input("Digite o terceiro valor:")),\
    int(input("Digite o quarto valor:"))
par = list()
for posicao, item in enumerate(i):
    # enumerate irá retornar a posição e o valor da tupla
    if item % 2 == 0:
        par.append(item)
try:
    tres = i.index(3)
except:
    tres = "inexistente"


print(f"O número 9 apareceu {i.count(9)} vezes, a primeira aparição do número 3 foi na posição {tres} e os pares "
      f"são {par} ")
