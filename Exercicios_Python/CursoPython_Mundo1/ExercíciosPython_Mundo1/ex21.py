cidade = str(input('Qual a sua cidade? '))
cidade = cidade.title().strip().split()
t = 'Santo' in cidade[0]
print(t)