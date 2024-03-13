
a = int(input('Escolha um número para fatorar: '))

c = a
f1 = 1
print(f'Calculando {a}! = ', end='')
while c > 0:
    print(f'{c}', end='')
    print(' x ' if c > 1 else ' = ', end='')
    f1 *= c
    c -= 1
print(f'{f1}')

print()
print()
idades = [15, 46, 75, 34, 23]
total = 0
for idade in idades:
    total += idade

print(f'Logo a soma de {idades} é -> {total}')

print()
print()

