media = 0
maior = 0
menosdevinte = 0
iden = ''
igual = ''
nmulheres = 0
teste = bool
for i in range(1, 5):
    nome = str(input('Digite o nome da {}° pessoa: '.format(i)))
    idade = int(input('Digite a idade da {}° pessoa: '.format(i)))
    sexo = str(input('Digite o sexo da {}° pessosa: '.format(i)))
    media += idade
    nome, sexo = nome.strip().title(), sexo.strip().title()
    print(sexo)
    if sexo == 'Homem':
        if maior < idade:
            maior = idade
            iden = nome
        if maior == idade:

            igual += nome + ', '

    if sexo == 'Mulher':
        if idade < 20:
            menosdevinte += 1
            nmulheres += 1
    elif sexo != 'Homem' or 'Mulher' or 'mulher' or 'homem':
        teste = bool(True)
    print('=' * 60)

print('A média de idade do grupo é de {} anos.'.format(media / 4))
if not teste:
    print('Digite um sexo valido!')

if igual != '':
    print('Há homens com idades iguais, {}'.format(igual))
else:
    print('O Homem mais velho é o {}'.format(iden))
if nmulheres != 0:
    print('Há {} mulher(s) com menos de vinte anos.'.format(menosdevinte))




