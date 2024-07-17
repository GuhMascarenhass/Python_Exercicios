numeros = []
par = []
impar = []
condicao = "1"
while condicao != "0":
    entrada = int(input("Digite o valor: "))
    numeros.append(entrada)
    condicao = input("Deseja continuar? [0 para NÃO / 1 para SIM] ")
for valor in numeros:
    if valor % 2 == 0:
        par.append(valor)
    else:
        impar.append(valor)

print("-="*40)
print(f"Valores digitados: {numeros}")
print(f"Os pares são: {par}")
print(f"Os impares são: {impar}")
print("-="*40)
