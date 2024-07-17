# jeito 1
for n in range(3, 10, 3):
    n2 = n + n
    print(n)
print('A soma dos números ímpares múltiplos de 3 é : {}'.format(n2))
#  jeito 2

for n in range(1, 501):
    n1 = n % 3
    if n1 == 0:
        n2 = n + n
print('A soma dos números ímpares múltiplos de 3 é : {}'.format(n2))
