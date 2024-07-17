nome = input('Qual o seu nome ? ')
cores = {'vermelhosublinhado': '\033[4;31m',
         'brancobg': '\033[40m',
         'sublinhado': '\033[4m',
         'limpa': '\033[m'}
print('Prazer te conhecer {}{}{}. Seja bem-vindo(a) as aulas de Python'.format(cores['vermelhosublinhado'],nome,cores['limpa']))
