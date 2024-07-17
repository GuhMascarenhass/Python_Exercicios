from random import randint
from time import sleep

print('=' * 20)
print('PAR OU ÍMPAR')
print('=' * 20)
vitoria = 0
while True:
    parouimpar = str(input('Você quer par ou ímpar? ')).strip().upper()
    if parouimpar == "PAR":
        numerom = randint(1, 10)
        print('Beleza, então eu escolho o Impar!')
        print('=' * 40)
        numerom = randint(1, 10)
        print('No 3 mostramos os números.')
        for c in range(1, 4):
            print(c)
            sleep(1)
        print('=' * 40)
        n = int(input('Seu número: '))
        resultado = n + numerom
        soma = (n + numerom) % 2
        print(f'O resultado foi {resultado}')
        print('=' * 40)
        if soma == 0:
            print('A não, você ganhou parabéns!')
            vitoria += 1
            print('=' * 40)
        else:
            print('Você perdeu. Boa sorte na próxima!')
            if vitoria == 0:
                print(f'Você ganhou {vitoria} vez.')
                print('=' * 40)
            else:
                print(f'Você ganhou {vitoria} vezes consecutivas.')
                print('=' * 40)
            break
    elif parouimpar == "IMPAR":
        print('Beleza, então eu sou o par!')
        print('='*40)
        numerom = randint(1, 10)
        print('No 3 mostramos os números.')
        for c in range(1, 4):
            print(c)
            sleep(1)
        print('=' * 40)
        n = int(input('Seu número: '))
        resultado = n + numerom
        soma = (n + numerom) % 2
        print(f'O resultado foi {resultado}')
        print('=' * 40)
        if soma != 0:
            print('A não, você ganhou parabéns!')
            vitoria += 1
            print('=' * 40)
        else:
            print('Você perdeu. Boa sorte na próxima!')
            if vitoria == 1:
                print(f'Você ganhou {vitoria} vez.')
                print('=' * 40)
            else:
                print(f'Você ganhou {vitoria} vezes consecutivas.')
                print('=' * 40)
            break
    else:
        print('Por favor escolha par ou ímpar')
        print(f'Você digitou: {parouimpar}')
print("fim")
