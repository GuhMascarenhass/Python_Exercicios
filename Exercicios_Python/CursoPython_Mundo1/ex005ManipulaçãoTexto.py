# Fatiamento de string
t = 'Gustavo Mascarenhas dos santos'
print(t[3])  # Aqui ele printa a string no posiçao 3 contando do 0 configiração[inicio, fim, tempo]
print(t[3:17])  # print na posição 3 até a 17 terminando de contar no 17
print(t[3:17:3])  # Nesse é saltando de 2 em dois
print(t[:5])  # omitindo o começo da string ele começa desde o inicio
print(t[15:])  # omitindo o final, ele começa na 15 e vai até o final da string
print(t[9::3])  # começa na 9 e vai ate o final pulando 3 em 3
print(t[::-1])  # aqui irá printar a frase ao contrario
# manipulação
print(len(t))  # tamanho da string
print(t.count('os', 0, 30))  # conta quantos 'o' tem na frase, ja aplicando o fatiamento
print(t.find('asdhg'))  # acha na string a posição que começa tal palavra
print('dos' in t)  # confere se em t tem a palavra 'dos'
print("""A teoria e o modelo científico e cosmológico mais aceito sobre a origem do universo é a chamada “Teoria do 
Big Bang”. 

Nele, ocorreu uma inflação em que o espaço se expandio originando o que hoje chamamos de  espaço e tempo. 

Alguns cientistas o consideram infinito e apontam para a existência de outros universos.""")  # Aspas triplas fazem o
# texto ir na formatação que os espaços tiverem
# Há tambem a possibilidade de juntar comandos em seguencia .upper().find()

# Trasformação

print(t.replace('texto', 'fui'))  # troca a texto por fui
print(t.upper())  # coloca a string em maiusculo
print(t.lower())  # coloca a string em minuscula
print(t.capitalize())  # joga a string inteira em minuscula e coloca a primeira letra em maiusculo
print(t.title())  # analiza a string e coloca cada palavra com a primeira letra maiuscula
print(t.strip())  # remove os espaços inuteis da frase: ___gustavo_ -> gustavo
print(t.rstrip())  # strip removendo somente o lado direito right
print(t.lstrip())  # strip removendo somente o lado esquerdo left

# Divisão
print(t.split())  # vai dividir minha string conforme os espaços nela
print(t.split('.', maxsplit=0))  # vai dividir a string conforme os parametros dados, : '.' etc...
#  Junção
t2 = t.split()
print(t2[3][4])  # t2[]mostra a palavra []letra
print('-'.join(t2))  # O .join() adiciona um caractere nos entre as palavras que foram splitadas
