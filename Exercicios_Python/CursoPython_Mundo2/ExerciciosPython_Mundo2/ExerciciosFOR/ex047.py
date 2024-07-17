#  jeito 1
print('Os números pares entre 1 e 50 são:')
for n in range(2, 51, 2):
    print(n, end=' ')
print('.')
#  jeito 2
n2 = ''
for n in range(1, 51):
    n1 = str(n % 2)
    if n1 == '0':
        n2 = n2 + str(n) + '; '
print('\nOs números pares entre 1 e 50 são os seguintes: {}'.format(n2))
