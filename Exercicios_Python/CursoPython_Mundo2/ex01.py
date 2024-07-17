cores = {'azul': '\033[34m',
         'sublinhado': '\033[4m',
         'limpa': '\033[m'}
nome = str(input('{}{}Qual é o seu nome ?{}'.format(cores['azul'], cores['sublinhado'], cores['limpa'])).title().strip())
n2 = nome.split()
if n2[0] == 'Gustavo':
    print('Que nome bonito!')
elif n2[0] in 'Maria Rosana Joana Jéssica':
    print('Que nome legal!')
print('Está gostando do curso de Python', nome, '?')
