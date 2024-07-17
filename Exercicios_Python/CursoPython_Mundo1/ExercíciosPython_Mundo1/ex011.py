preco = float(input('Preço: '))
desconto = float(input('Desconto: '))

precodesc = preco-((preco * desconto)/100)
print('Preço final {}'.format(precodesc))