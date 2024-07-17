from datetime import date
maior = ' '
nmaior = ' '

for i in range(0, 2):
    nomes = input('Nome:')
    idade = int(input('Ano de nascimento:'))
    nomes = nomes.title()
    n = date.today().year - idade
    if n >= 18:
        maior += nomes+'; '
    else:
        nmaior += nomes+'; '
print('Os que atingiram a maioridade foram:{}'.format(maior))
print('Os que não atingiram a maioridade foram:{}'.format(nmaior))
