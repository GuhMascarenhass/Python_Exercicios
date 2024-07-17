n1 = float(input('Digite a primeira nota:'))
n2 = float(input('Digite a segunda nota:'))
media = (n1 + n2) / 2
if media >= 7:
    print('A media do aluno foi {}, APROVADO!'.format(media))
elif media < 5:
    print('A média do aluno foi {}, REPR0VADO!'.format(media))
elif 5 <= media <= 6.9:
    print('A média do aluno foi {}, RECUPERAÇÃO!'.format(media))
