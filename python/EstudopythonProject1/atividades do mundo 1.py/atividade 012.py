a = float(input('Diga o preço do produto: '))
p = a - (a * 10/100)
print('o produto que era \033[31m{:.2f}\033[m com 10% de desconto ficou \033[32m{:.2f}\033[m'.format(a, p))