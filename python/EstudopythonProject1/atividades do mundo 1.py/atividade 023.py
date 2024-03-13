n = int(input('Escolha um número Teste de python ser analisado: '))
u = n // 1 % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10
dm = n // 10000 % 10
print('Analisando o número \033[35m{}\033[m'.format(n))
print('dezena de milhar: \033[36m{}\033[m'.format(dm))
print('milhar: \033[31m{}\033[m'.format(m))
print('Centena: \033[34m{}\033[m'.format(c))
print('Dezena: \033[33m{}\033[m'.format(d))
print('Unidade: \033[32m{}\033[m'.format(u))