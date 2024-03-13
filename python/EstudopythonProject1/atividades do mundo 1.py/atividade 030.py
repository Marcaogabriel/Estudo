n = int(input('Diga um número: '))
r = n % 2
if r == 0:
    print('O número \033[32m{} é PAR\033[m'.format(n))
else:
    print('O número \033[31m{} é IMPAR'.format(n))