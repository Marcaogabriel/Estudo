a = (int(input('Escolha um número: ')),
    int(input('Escolha outro número: ')),
    int(input('Escolha mais outro número: ')),
    int(input('Escolha o ultimo número: ')))
print(a)
print(f'O número 9 apareceu {a.count(9)} vezes')
if 3 in a:
    print(f'O número 3 está na posição {a.index(3)+1}')
else:
    print('O valor 3 não foi digitado')
print('OS valores pares digitados foram ', end='')
for n in a:
    if n % 2 == 0:
        print(n, end=' ')

