n = 0
while n == 0:
    sexo = str(input('Digite M para Mulher e H para Homem: ')).upper()[0].strip()
    print(sexo)
    if sexo != 'M' and sexo != 'H':
        print('Digite um sexo válido!')
    else:
        n += 1
print('Fim')

sexo2 = str(input('Informe seu sexo: [M/F] ')).strip().upper()[0]
while sexo2 not in 'MmFf':
    sexo2 = str(input('Digite um sexo válido: ')).strip().upper()[0]
print('Sexo {} registrado com sucesso!!'.format(sexo2))


