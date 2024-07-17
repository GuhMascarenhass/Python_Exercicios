n = int(input('Digite um número inteiro: '))
mult = 0
for cont in range(2, n):
    if n % cont == 0:
        print("Múltiplo de", cont)
        mult += 1
if mult == 0:
    print('O número {} é primo.'.format(n))
else:
    print('Tem', mult, 'múltiplos acima de 2 e abaixo de', n, end='.')
