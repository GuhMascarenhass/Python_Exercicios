numeros = int(input("Digite um número [999 para finalizar]: "))
x = True
contador = soma = 0
while x:
    contador += 1
    soma += numeros
    numeros = int(input("Outro número [999 para finalizar]: "))
    if numeros == 999:
        x = False
print("O resultado da soma foi de {} \nE você adicionou {} números na conta!".format(soma, contador))
