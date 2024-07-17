nome = 'Mascarenhas'
print('\033[1;33;45mOlá, Mundo!')
print('\033[1;36;45mOlá, Mundo!\033[m')  # FOTO ANSI NA PASTA FOTOS PYTHON
# É possivel colacar essa formatação em uma matriz

print('Olá, Muito prazer em te conhecer, {}{}{}!!!'.format('\033[4;31m', nome, '\033[m'))
