from math import sqrt

a = float(input('Digite o valor de A: '))
b = float(input('Digite o valor de B: '))
c = float(input('Digite o valor de C: '))

if a == 0:
    a = sqrt(c * c + b * b)

elif b == 0:
    b = a * a - c * c

elif c == 0:
    c = sqrt(a * a + b * b)

if b < 0:
    b = b * (-1)
    b = sqrt(b)

if c < 0:
    c = c * (-1)
    c = sqrt(c)

if a < 0:
    a = a * (-1)
    a = sqrt(a)

print('A B C valem respectivamente {}, {}, {}'.format(a, b, c))
