from datetime import date

sexo = str(input('Qual o seu sexo? ').title().strip())
if sexo == 'Homem':
    nas = input('Em que ano você nasceu? ')
    confg = str(nas.isalpha())
    if confg == 'False':
        nascimento = int(nas)
        alistamento = date.today().year - nascimento
        if 18 > alistamento:
            print('ENTRO1')
            print('Você não tem idade para se alistar!')
            print('Falta(m) {} ano(s) para o alistamento.'.format(18 - alistamento))
        elif 18 < alistamento < 45:
            print('ENTRO2')
            print('Você precisa se alistar ao exército brasileiro!')
            print('Já se passaram {} ano(s) do prazo!'.format(alistamento - 18))
        elif alistamento > 45:
            print('ENTRO3')
            print('Você já passou da idade limite para o alistamento.')
        elif alistamento == 18:
            print('ENTRO4')
            print('Você está na idade de se alistar!')
            print('Vá a uma junta militar ou acesse o site https://alistamento.eb.mil.br')
    else:
        print('Digite um ano válido!')

elif sexo == 'Mulher':
    print('Você não precisa fazer o alistamento obrigatório.')

else:
    print('Digite seu sexo biologico!')
