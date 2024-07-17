maior = 0
menor = 0
for i in range(1, 6):
    pesos = float(input('Qual o peso da {}° pessoa? \nPeso:'.format(i)))
    if i == 1:
        menor = pesos
        maior = pesos
    else:
        if maior < pesos:
            maior = pesos
        if menor > pesos:
          menor = pesos

print('='*40)
print('O maior pesos lido foi de {}Kg .\nO menor peso lido foi {}Kg .'.format(maior, menor))
print('='*40)