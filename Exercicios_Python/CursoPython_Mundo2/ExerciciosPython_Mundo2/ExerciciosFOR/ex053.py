text = str(input('Digite a frase:'))
text = text.split()
text = ''.join(text)
if str(text) == str(text)[::-1]:
    print(str(text)[::-1])

