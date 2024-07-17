cores = {'txtazul': '\033[34m',
         'txtlimpa': '\033[m',
         'txtverde': '\033[32m',
         'txtbranco': '\033[97m',
         'txtvermelho': '\033[31m'
         }
numero = int(input('Digite um número inteiro qualquer: '))
opcao = int(input('[ 1 ] para {}binario{};\n[ 2 ] para {}octal{};\n[ 3 ] para {}hexadecimal;{}\n'.format(cores['txtazul'], cores['txtlimpa'], cores['txtverde'], cores['txtlimpa'], cores['txtbranco'], cores['txtlimpa'])))

if opcao == 1:

    print('Opção "1" escolhida.')
    print('-'*30)
    print(numero, 'em \033[34mbinário \033[m corresponde a {0:b}'.format(numero))

elif opcao == 2:
    print('Opção "2" escolhida.')
    print('-'*30)
    print(numero, 'em \033[32moctagonal\033[m corresponde a {0:o}'.format(numero))

elif opcao == 3:
    print('Opção "3" escolhida.')
    print('='*30)
    print(numero, 'em \033[97mhexadecimal\033[m corresponde a {0:x}'.format(numero))

else:
    print(cores['txtvermelho'], 'Escolha uma opção valida!')

# eu usei para transformar dentro das chaves do format, aqui um site com as transformaçoes
# https://www.delftstack.com/pt/howto/python/python-int-to-binary/
