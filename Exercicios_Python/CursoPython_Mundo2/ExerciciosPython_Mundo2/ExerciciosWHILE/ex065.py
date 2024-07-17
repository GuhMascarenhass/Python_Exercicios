menor = maior = media = contador = 0
x = "S"
while x in 'Ss':
    numero = int(input("Digite um número: "))
    if contador == 0:
        menor = maior = numero
        contador += 1
    else:
        media += numero
        contador += 1
        if numero < menor:
            menor = numero
        elif numero > maior:
            maior = numero
    x = str(input("Deseja continuar? [S/N]")).strip().upper()[0]
print("A média aritmética foi de {}, seu maior e menor número foram respctivamente {} | {}".format(media/contador, menor, maior))

