ano = int(input('Digite o ano: '))
bi = ano % 4
if bi == 0:
    print('O ano é Bissexto')
else:
    print('O ano não é Bissexto')
