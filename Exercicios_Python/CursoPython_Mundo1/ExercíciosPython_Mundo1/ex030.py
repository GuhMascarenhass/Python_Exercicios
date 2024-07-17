v1 = int(input('Valor: '))
v2 = int(input('Valor: '))
v3 = int(input('Valor: '))

if v1 > v2 > v3:
    print('O maior valor é {} e o menor é {} '.format(v1, v3))

elif v1 > v3 > v2:
    print('O maior valor é {} e o menor é {} '.format(v1, v2))

if v2 > v3 > v1:
    print('O maior valor é {} e o menor é {} '.format(v2, v1))

elif v2 > v1 > v3:
    print('O maior valor é {} e o menor é {} '.format(v2, v3))

if v3 > v2 > v1:
    print('O maior valor é {} e o menor é {} '.format(v3, v1))

elif v3 > v1 > v2:
    print('O maior valor é {} e o menor é {} '.format(v3, v2))





