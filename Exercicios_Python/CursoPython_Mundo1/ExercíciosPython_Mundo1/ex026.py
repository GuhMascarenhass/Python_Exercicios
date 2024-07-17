v = int(input('Velocidade do carro: '))
if v> 80:
    valor= (v - 80) * 7
    print('Você foi multado em R${}.'.format(valor))
else:
    print('Você não foi multado.')