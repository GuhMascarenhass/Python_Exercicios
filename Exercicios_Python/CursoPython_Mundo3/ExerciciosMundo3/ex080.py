lista_valores = []
valor = int(input("Digite o número: "))
lista_valores.append(valor)
for x in range(0, 4):
    valor = int(input("Digite o número: "))
    tamanho = len(lista_valores)
    if valor >= lista_valores[-1]:
        lista_valores.append(valor)
        print("Adicionado ao final da lista")
    for index, dado in enumerate(lista_valores):
        if valor < dado:
            lista_valores.insert(index, valor)
            print(f"Adicionado ao indice {index}")
            break
print(lista_valores)