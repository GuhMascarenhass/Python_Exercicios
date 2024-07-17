p1 = float(input('Digite o primeiro termo da P.A: '))
rasao = float(input('Digite a rasão: '))
print('Os termos desse P.A são:', end='')
for p in range(1, 11):
    r = p1 + (p - 1) * rasao
    print('{}'.format(r), end=' → ')
print('Acabou.')

#  jeito 2

p1 = int(input('Digite o primeiro termo da P.A: '))
rasao = int(input('Digite a rasão: '))
decimo = p1 + (11 - 1) * rasao
print('Os termos desse P.A são:', end='')
for p in range(p1, decimo, rasao):
    print('{}'.format(p), end=' → ')
print('Acabou.')
