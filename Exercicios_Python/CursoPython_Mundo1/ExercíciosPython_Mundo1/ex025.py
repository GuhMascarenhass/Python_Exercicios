import random

numero = int(input('Digite um número entre 0 e 5: '))
random = random.randint(0, 5)

if random==numero:
    print('Você acertou, o número era: {}'.format(random))
else:
    print('Você errou, o número era: {}'.format(random))

print("Você acertou, o número era: {}" if random == numero else 'Você errou, o número era: {}'.format(random))  # forma reduzida, apenas 1 if else.
