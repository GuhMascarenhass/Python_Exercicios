print("Sequêcia de Fibonacci")
print("Agora eu preciso saber quantos termos ela vai ter. ")
s = int(input("Ela terá: "))
t0 = 0
t1 = 1
n = 2
print("{}-{}-".format(t0, t1), end='')
while n != s:
    n += 1
    t3 = t0 + t1
    print("{}".format(t3), end='-')
    t0 = t1
    t1 = t3
print("Fim")
