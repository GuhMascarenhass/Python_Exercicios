nome = input('Qual o seu nome? ')
print('Prazer em te conhecer')
print('{:-^20} !'.format(''))  # Dentro da chaves tem varias funçoes que podem ser feitas para a formataçao
v1 = int(input('Digite um valor: '))
v2 = int(input('Digite outro valor: '))
s = v1 + v2
sub = v1 - v2
m = v1 * v2
d = v1 / v2
di = v1 // v2
e = v1 ** v2
r = v1 % v2
# o end= e o que eu vou querer no final da string, ela n vai quebrar automatica
print('Soma é {}\nSubtração é {}\nProduto é {}'.format(s, sub, m), end='\n===')
print('Divisão é {:.3f}\nPotência é {}\nDivisão inteira é {}\nResto é {}'.format(d, e, di, r))
