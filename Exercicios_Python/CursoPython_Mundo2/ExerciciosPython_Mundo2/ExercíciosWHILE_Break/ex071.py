saque = int(input("Valor a sacar R$ "))
cinquenta = saque // 50
saquec = (saque - (50 * cinquenta))
vinte =  saquec // 20
saquev = (saquec-(20 * vinte))
dez = saquev // 10
saqued = (saquev-(10 * dez))
um = saqued // 1
print(f"Irão sair {cinquenta} nota(s) de R$50, {vinte} nota(s) de R$20, {dez} nota(s) de R$10 e {um} nota(s) de R$1 ")
