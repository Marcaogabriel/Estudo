lista = []
sm = 0
while True:
    lista.append(int(input('Digite um valor: ')))
    esco = ' '
    while esco not in 'SN':
        esco = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if esco == 'N':
        break

print(f'Você digitou um total de {len(lista)} números')
lista.sort(reverse=True)
print(f'A lista em ordem decrescente é {lista}')
if 5 in lista:
    print('foi encontrado o valor 5 na lista')
else:
    print('Não foi encontrado o valor 5 na lista')