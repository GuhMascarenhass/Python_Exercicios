p1 = int(input("Digite o primeiro termo da P.A: "))
r = int(input("Digite a razão da P.A: "))
decimo = 10
cont = 1
print("Os termos da P.A são: ", end='')
while cont > x:
    resultado = p1 + (decimo - 1) * r
    print("{} » ".format(resultado), end='')
    decimo -= 1
    if x == cont:
        cont = int(input("\nDeseja adicionar mais termos na P.A? "))
        cont = cont + 2
        p1 = resultado
        x = 1
        x += 1

print(" Pausa")

