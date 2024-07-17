valorcasa = float(input('Qual o valor do imóvel ?\nR$'))
salaraio = float(input('Qual o seu salário ? \nR$'))
anos = int(input('Em quantos anos dejesa pagar ? \n'))
prestacao = valorcasa/(anos*12)
porcento = (salaraio*30)/100
if porcento <= prestacao:
    print('Seu empréstimo foi negado!')
else:
    print('Seu empréstimo foi aprovado e você irá pagar R${:.2f}'.format(prestacao))
    




