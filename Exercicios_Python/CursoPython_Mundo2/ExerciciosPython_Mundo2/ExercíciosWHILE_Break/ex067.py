while True:
    numero = int(input("Qual tabuada você quer ver hoje? "))
    if numero < 0:
        print('O número inserido é negativo, por isso a tabuaba foi encerrada.')
        break
    print(f'-'*40)
    for contador in range(1, 11):
        tabuada = numero * contador
        print(f'{contador} X {numero} = {tabuada}')
    print(f'-'*40)
print("FIM")
