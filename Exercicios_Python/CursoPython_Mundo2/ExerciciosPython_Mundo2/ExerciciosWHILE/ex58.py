from random import randrange
print('Óla eu sou o seu computador! Vamos jogar um jogo de adivinhação?')
print('Pensei em um número entre 0 a 10... Qual séra?')
numero = int(randrange(0, 10, 1))
tentativa = False
palpites = 0
vidas = 3
while not tentativa:
    escolha = int(input('Eu acho que é... '))
    palpites += 1
    vidas -= 1
    if escolha > numero:
        print('Vish o número é maior do que eu escolhi!')
    elif escolha < numero:
        print('Vish o número é menor do que eu escolhi!')
    else:
        tentativa = True
print("Parabéns, você acertou o número que eu escolhi em {} tentativas. O número era {}.".format(palpites, numero))
