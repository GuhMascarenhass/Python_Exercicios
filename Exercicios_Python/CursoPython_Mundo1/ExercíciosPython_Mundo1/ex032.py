a = int(input('Digite o valor de a: '))
b = int(input('Digite o valor de b: '))
c = int(input('Digite o valor de c: '))

if b - c < a < b + c and a - c  < b < a + c and a - b  < c < a + b:
    print('Os valores dados correspondem há um triângulo')
else:
    print('Os valores dados não correspondem há um triângulo')

