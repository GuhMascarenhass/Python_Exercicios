numeros = int(input("Digite um número [999 para finalizar]: "))
contador = soma = 0
while True:
    contador += 1
    soma += numeros
    numeros = int(input("Outro número [999 para finalizar]: "))
    if numeros == 999:
       break
print(f"O resultado da soma foi de {soma:.2f} \nE você adicionou {contador:^20} números na conta!")
