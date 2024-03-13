lista = []
mai = 0
men = 0
for cont in range(0, 5):
    print(f'Na posição {cont} vai estar o', end='')
    lista.append(int(input(' valor: ')))
    if cont == 0:
        mai = men = lista[cont]
    else:
        if lista[cont] > mai:
            mai = lista[cont]
        if lista[cont] < men:
            men = lista[cont]
print('-=' * 30)
print(f'Você digitou os valores {lista}')
print(f'O maior Valor foi {mai} nas posições ', end='')
for i, v in enumerate(lista):
    if v == mai:
        print(f'{i}...', end='')

print()
print(f'O menor Valor foi {men} nas posições ', end='')
for i, v in enumerate(lista):
    if v == men:
        print(f'{i}...', end='')
