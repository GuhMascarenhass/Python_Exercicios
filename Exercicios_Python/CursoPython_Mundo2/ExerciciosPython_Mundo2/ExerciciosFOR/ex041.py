from datetime import date
nas = input('Em que ano você nasceu? ')
confg = str(nas.isalpha())
if confg == 'False':
    nascimento = int(nas)
    idade = date.today().year - nascimento
    if idade <= 9:
        print('Sua idade é de {}, e você entra na categoria Mirim'.format(idade))
    elif idade <= 14:
        print('Sua idade é de {}, e você entra na categoria Infantil'.format(idade))
    elif idade <= 19:
        print('Sua idade é de {}, e você entra na categoria Junior'.format(idade))
    elif idade <= 25:
        print('Sua idade é de {}, e você entra na categoria Sénior'.format(idade))
    elif idade > 25:
        print('Sua idade é de {}, e você entra na categoria Master'.format(idade))
else:
    print('Digite um ano válido!')
