from math import trunc

n = float(input('Digite um número: '))
print('O número \033[32m{}\033[m sem suas casa decimais fica \033[35m{}\033[m'.format(n, trunc(n)))


