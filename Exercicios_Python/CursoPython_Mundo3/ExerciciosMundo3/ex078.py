lista_valores = list()
posicao_menor = []
posicao_maior = []
for vezes in range(0, 5):
    lista_valores.append(int(input("Digite os valores: ")))

menor = lista_valores[0]
maior = lista_valores[0]
for value in lista_valores:
    if value <= menor:
        menor = value

    if value >= maior:
        maior = value

for indice, valor in enumerate(lista_valores):
    if valor == menor:
        posicao_menor.append(indice)
    elif valor == maior:
        posicao_maior.append(indice)

print(f"Menor {menor} nas posições: {posicao_menor}")
print(f"Maior {maior} nas posições: {posicao_maior}")