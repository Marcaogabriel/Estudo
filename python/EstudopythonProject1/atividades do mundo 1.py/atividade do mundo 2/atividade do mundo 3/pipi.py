a = []
b = a
for c in range(0, 5):
    a.append(int(input('Digite um valor: ')))
print(f'Lista A: {a}')
print(f'Lista B: {b}')


#d = (int(input('Digite um Valor: ')),
#int(input('Digite um Valor: ')),
#int(input('Digite um Valor: ')))

c = [1, 2, 3, 4, 5]
g = c[:]
g[2] = 8
print(f'TABELA {c}')
print(f'TABELA {g}')