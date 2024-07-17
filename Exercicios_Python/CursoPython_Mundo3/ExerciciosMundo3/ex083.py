expressao = input("Digite a Expressão:")
abre = []
for posicao, letra in enumerate(expressao):
    if letra == "(":
        abre.append(letra)
    elif letra == ")":
        if len(abre) > 0:
            abre.pop()
        else:
            abre.append(letra)
            print(f"A um {abre} na posição errada!")
            break
if len(abre) != 0:
    print("expressão invalida")
else:
    print("Aceito")


