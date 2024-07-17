cont = '1'
lista_valores = []
numero = int(input("Digite os valores:"))
while cont != '0':
    if numero in lista_valores:
        numero = int(input("Digite os valores:"))
    else:
        lista_valores.append(numero)
        numero = int(input("Digite os valores:"))
    cont = input("Dejesa continuar? (Aperte 0 para parar)")
lista_valores.sort()
print(lista_valores)
