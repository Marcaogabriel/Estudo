b = float(input('altura da parede: '))
h = float(input('altura da parede: '))
a = b * h
t = a / 2
print('Em uma parede de dimensão \033[32m{}\033[m tabela \033[33m{}\033[m Teste de python sua área é \033[34m{:.2f}\033[m \n logo para pintar Teste de python parede precisará de \033[35m{:.2f}\033[m l de tinta'.format(b, h, a, t))