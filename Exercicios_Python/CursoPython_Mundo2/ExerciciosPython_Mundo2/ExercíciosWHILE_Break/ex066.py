contador = soma = 0
while True:
    numeros = int(input("Outro número [999 para finalizar]: "))
    if numeros == 999:
        break
    contador += 1
    soma += numeros
print(f"O resultado da soma foi de {soma:.2f} \nE você adicionou {contador:^20} números na conta!")
