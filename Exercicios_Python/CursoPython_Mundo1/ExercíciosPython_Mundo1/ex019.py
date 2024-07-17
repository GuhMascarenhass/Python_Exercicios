nome = str(input('Nome: '))
upper = nome.upper()
lower = nome.lower()
sn = nome.split()
tamanhoSE = ''.join(sn)
print('O nome letras maiúsculas: {} \nNome minúsculo: {} \nTamanho sem espaços: {} \nNúmero de letras do primeiro nome: {}'
      .format(upper,lower,len(tamanhoSE), len(sn[0])))

