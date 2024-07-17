contagem = "Zero", "Um", "Dois", "Três", "Quatro", "Cinco", "Seis", "Sete", "Oito", "Nove", "Dez", "Onze", "Doze","Treze", "Catorze", "Quinze", "Dezesseis", "Dezessete", "Dezoito", "Dezenove", "Vinte"
x = False
while x is False:
    try:
        n = int(input("Digite um número: "))
        if n < 0 or n > 20:
            print("Digite um número entre 0 e 20")
        if n <= 20:
            for pos, numeros in enumerate(contagem):
                if n == pos:
                    print(f"Você digitou o número {contagem[n]}.")
                    x = True
    except ValueError:
        print("O programa so aceita números!")



