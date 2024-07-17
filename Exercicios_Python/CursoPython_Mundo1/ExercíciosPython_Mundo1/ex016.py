from random import choice

nome = str(input('Nome do aluno: '))
nome2 = str(input('Nome do aluno: '))
nome3 = str(input('Nome do aluno: '))
nome4 = str(input('Nome do aluno: '))

nomes = [nome, nome2, nome3, nome4]

escolhido = choice(nomes)
print('O escolhido foi {}'.format(escolhido))