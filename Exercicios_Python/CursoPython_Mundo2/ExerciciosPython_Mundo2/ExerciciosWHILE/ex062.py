p1 = int(input("Digite o primeiro termo da P.A: "))
r = int(input("Digite a razão da P.A: "))
x = 1
numerotermos = 10
cont = 11
print("Os termos da P.A são: ", end='')
while cont > x:
    resultado = p1 + (x - 1) * r
    print("{} » ".format(resultado), end='')
    x += 1
    if x == cont:
        print("Pausa")
        cont = int(input("\nDeseja adicionar mais termos na P.A? "))
        if cont != 0:
            cont = cont + 2
            p1 = resultado
            x = 1
            x += 1
            numerotermos += cont - 2
        else:
            print("O Número final de termos foram de {}.".format(numerotermos))
