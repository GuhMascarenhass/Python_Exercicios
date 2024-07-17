n1 = int(input("Digite o primeiro valor: "))
n2 = int(input("Digite o segundo valor: "))
escolha = int(input("""  Escolha uma ação:
        \033[31m [1] Somar \033[m
        \033[32m [2] Multiplicar \033[m
        \033[33m [3] Maior \033[m
        \033[34m [4] Novos números   \033[m
        \033[35m [5] Sair do programa \033[m
         Escolha: """))

while escolha != int(5):

    if escolha == 1:
        resultado = n1 + n2
        print("O resultado da \033[31mSoma\033[m os valores é de: {}".format(resultado))
    elif escolha == 2:
        resultado = n1 * n2
        print("O resultado da \033[32mMultiplicação\033[m os valores é de: {}".format(resultado))
    elif escolha == 3:
        if n1 > n2:
            print("O \033[33mmaior\033[m dos dois valores é o {}".format(n1))
        elif n2 > n1:
            print("O \033[33mmaior\033[m dos dois valores é o {}".format(n2))
        else:
            print("Os \033[33mvalores\033[m são iguais.")
    elif escolha == 4:
        n1 = int(input("Digite o \033[34mprimeiro\033[m novo valor: "))
        n2 = int(input("Digite o \033[34msegundo\033[m novo valor: "))
        print("Os dois novos valores são \033[34m{}\033[m e \033[34m{}\033[m .".format(n1, n2))
    elif escolha < 0 or escolha > 5:
        print("Digite uma escolha válida!")
        escolha = int(input("""
        \033[31m [1] Somar \033[m
        \033[32m [2] Multiplicar \033[m
        \033[33m [3] Maior \033[m
        \033[34m [4] Novos números   \033[m
        \033[35m [5] Sair do programa \033[m
         Escolha: """))
    escolha = int(input("""  Deseja continuar?
        \033[31m [1] Somar \033[m
        \033[32m [2] Multiplicar \033[m
        \033[33m [3] Maior \033[m
        \033[34m [4] Novos números   \033[m
        \033[35m [5] Sair do programa \033[m
         Escolha: """))


