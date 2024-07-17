for texto in range(1, 6):
    print(texto)  # mostra a variavel texto
    print('\033[33m-==\033[m' * 10)
    print('Fim')

for texto in range(6, 0, -1):
    print('\033[33m-\033[m' * 10)
    print(texto)
n1 = 11
n2 = 2
for texto in range(n1, n2, -2):
    print('\033[33m-=\033[m' * 10)
    print(texto)

st = ''
for texto in range(0, 5):
    n = str(input('Digite um texto:'))
    st = st + n + ','
print(st)
s = 0
for texto in range(0, 5):
    n = int(input('Digite um valor:'))
    s += n
print(s)
