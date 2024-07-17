a = int(input('Digite o valor de a: '))
b = int(input('Digite o valor de b: '))
c = int(input('Digite o valor de c: '))
if b - c < a < b + c and a - c < b < a + c and a - b < c < a + b:
    if a == b == c:
        print('Os valores dados correspondem há um triângulo equilátero')
    elif a == b and a != c or b == c and b != a or c == a and c != b:
        print('Os valores dados correspondem há um triângulo isóceles')
    else:
        print('Os valores dados correspondem há um triângulo escaleno')
else:
    print('Os valores dados não correspondem há um triângulo')
