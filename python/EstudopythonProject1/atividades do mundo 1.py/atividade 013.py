s = float(input('Diga um Salario: '))
a = s + (s * 20/100)
print('O salario que era \033[34m{}\033[m com 20% de aumento ficou \033[35m{}\033[m'.format(s, a))