from math import hypot

ca = float(input('Qual o valor do cateto adjacente? '))
co = float(input('Qual o valor do cateto oposto? '))
a = hypot(co, ca)
print('A hipotenusa vai medir \033[36m{:.2f}\033[m'.format(a))