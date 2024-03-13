l = []
lp = []
li = []
while True:
    a = int(input('Digite um valor para adicona-lo na lista: '))
    l.append(a)
    if a % 2 == 0:
        lp.append(a)
    if a % 2 == 1:
        li.append(a)
    r = ' '
    while r not in 'SN':
        r = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if r == 'N':
        break

l.sort()
print('-=' * 30)
print(f'Estes foram todos os números que você digitou {l}')
lp.sort()
print(f'Estes foram todos os números pares que você digitou {lp}')
li.sort()
print(f'Estes foram todos os números impares que você digitou {li}')
print('-=' * 30)