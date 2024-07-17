km = int(input('Km = '))
if km < 200:
    preco = km * 0.50
    print('Sua viajem foi menor que 200km, R${}'.format(preco))
else:
    preco = km * 0.45
    print('Sua viajem foi maior que 200km, R${}'.format(preco))
