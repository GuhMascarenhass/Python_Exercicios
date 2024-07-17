import random
numeros = list()
numerosdois = random.randint(1, 10), random.randint(1, 10), random.randint(1, 10), random.randint(1, 10), random.randint(1, 10)
for i in range(0, 5):
    numeros.append(random.randint(0, 10))
numeros = tuple(numeros)
x =sorted(numeros)
print(f"Maior: {x[1]} , Menor: {x[4]}/ {min(numerosdois)}  ,{max(numerosdois)}")
print(numeros)
print(numerosdois)