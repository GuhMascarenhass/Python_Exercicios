total = quantidade = aux =  0
nomeBarato = ""
print('-='*20)
print("CARRINHO DE COMPRAS")
print('-='*20)

while True:
    nome = input("Digite o nome do produto: ")
    preco = int(input("Digite o preço R$ "))
    total += preco
    if preco >= 1000:
        quantidade =+ 1
    if  aux < preco :
        nomeBarato = nome
    escolha = input("Quer continuar? [S/N] ")
    if escolha in "Nn":
        print(f"CUSTO TOTAL: {total}")
        print(f"ACIMA DE R$ 1000: {quantidade}")
        print(f"MAIS BARATO: {nomeBarato}")
        print("Fim da execução")
        break
    while escolha not in "sSnN":
            print("Digite uma opção valida!!!")
            escolha = input("Quer continuar? [S/N] ")
