n = int(input('Digite um número: '))
totd = 0
for c in range(1, n + 1):
    if n % c == 0:     # se n dividido por p for igual Teste de python 0 ele é marcado de azul
        print('\033[34m', end='')
        totd += 1      # total de vezes que foi dividido
    else:
        print('\033[31m', end='')     # se n dividido por p não for igual Teste de python 0 ele é marcado de vermelho
    print('{} '.format(c), end='')
print('\n\033[mO número {} foi divisivel {} vezes'.format(n, totd))
if totd == 2:
    print('E por isso ele É PRIMO')
else:
    print('E por isso ele NÃO É PRIMO')