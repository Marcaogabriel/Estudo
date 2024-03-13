a = int(input('Escolha um valor: '))
d = 5.08
ri = 2888.17
e = 5.21
d = a / d
ru = ri * a
eu = a / e
print(' Se você tiver R$ \033[32m{}\033[m você tera US$ \033[33m{:.2f}\033[m \n Se você tiver R$ \033[35m{}\033[m você tera Rp \033[34m{:.2f}\033[m \n Se você tiver R$ \033[36m{}\033[m você tera € \033[37m{:.2f}\033[m'.format(a, d, a, ru, a, eu))