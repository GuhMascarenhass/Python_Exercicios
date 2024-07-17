from time import sleep
import emoji
print('VAI COMEÇAR A CONTAGEM REGRESSIVA PARA OS FOGOS DE ARTIFÍCIO !!!')
print('LÁ VAI:')
for cr in range(10, 0, -1):
    print('\033[31m{}\033[m'.format(cr))
    sleep(1)
print(emoji.emojize(':collision: :fireworks: BOOOM :collision: :fireworks:'))
