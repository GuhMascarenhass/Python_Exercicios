n = int(input("Digite o número que ira calcular o fatorial: "))
cont = n
n1 = n
print("{}!={}".format(n, n), end='')
while cont != 1:
    cont -= 1
    n2 = n1 * cont
    n1 = n2
    print("*{}".format(cont), end='')
print("={}".format(n2))
