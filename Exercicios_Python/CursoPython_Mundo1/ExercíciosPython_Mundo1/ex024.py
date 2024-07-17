nome = str(input('Nome completo: ').strip().title())
nome2 = nome.split()
print('O primeiro é {}'.format(nome2[0]))
print('O último nome é {}'.format(nome2[len(nome2) - 1]))
