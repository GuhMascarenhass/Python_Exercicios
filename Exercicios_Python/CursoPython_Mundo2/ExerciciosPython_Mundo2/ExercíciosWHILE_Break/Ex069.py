contador = contador18 = contadorhomem = contadormulher = contadormulher20 = 0
while True:
    idade = int(input("IDADE: "))
    sexo = input("SEXO: ").title()
    escolha = input("Deseja continuar? (S/N)")

    if idade > 18:
         contador18+=1
    if sexo in "Mulher":
        contadormulher+=1
        if idade < 20:
            contadormulher20+=1
    if sexo in "Homem":
        contadorhomem+=1
    if escolha in "nN":
        break
print(f"A quantidade de cadastrados que possuem mais de 18 anos foi de: {contador18} pessoas")
print(f"Já a quantidade de Mulheres eram de {contadormulher} .")
print(f"Um total de {contadormulher20} mulheres tem menos de 20 anos.")
print(f"Já os cadastrados Homens foram de {contadorhomem}.")







