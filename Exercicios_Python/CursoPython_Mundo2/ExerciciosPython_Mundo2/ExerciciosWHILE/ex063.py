print("Sequêcia de Fibonacci")
print("Agora eu preciso saber quantos termos ela vai ter. ")
s = int(input("Ela terá: "))
t0 = 0
t1 = 1
n = 0
while n != s:
    t1 = t0 + t1
    print("{}".format(t0), end='-')
    print("{}".format(t1), end=' ')
    t0 = t1 + t0
    n += 1
print("Fim")
