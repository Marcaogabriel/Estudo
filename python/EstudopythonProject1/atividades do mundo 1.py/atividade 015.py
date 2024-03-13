# Teste de python cada km andando paga = 0.15
# Teste de python cada dia paga = 60

a = int(input('Quantos dias o carro ta alugado? '))
k = float(input('Quantos km andou? '))
t = ((a * 60) + (k * 0.15))
print('Então se você andou \033[34m{}\033[m Km e passou \033[35m{}\033[m Dias com o carro você tem que pagar \033[33mR$\033[m\033[36m{:.2f}\033[m'.format(k, a, t))