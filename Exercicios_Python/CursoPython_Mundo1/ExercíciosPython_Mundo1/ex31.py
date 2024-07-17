salario = float(input('Digite o salário: '))

if salario>=1250.00:
    aumento = salario + (salario * 10 /100)
    print('O salário com o aumento ficaria em {}'.format(aumento))
else:
    aumento = salario + (salario * 15 /100)
    print('O salário com o aumento ficaria em {}'.format(aumento))
