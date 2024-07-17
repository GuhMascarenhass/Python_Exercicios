lista_valores = []
condicao = "1"
while condicao != "0":
    entrada = int(input("Digite o valor: "))
    lista_valores.append(entrada)
    condicao = input("Deseja continuar? [0 para NÃo / 1 para SIM] ")

decresente = lista_valores[:]
decresente.sort(reverse=True)
print("=-"*40)
print(f"Foram digitados {len(lista_valores)} valores.")
print(f"Lista em forma decrescente: {decresente}.")
try:
    print(f"O valor 5 está na posição: {lista_valores.index(5)}")
except ValueError:
    print("O valor 5 não se encontra na lista.")
print(f"-="*40)



