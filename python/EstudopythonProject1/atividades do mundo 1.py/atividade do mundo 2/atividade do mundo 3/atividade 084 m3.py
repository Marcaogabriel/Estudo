temp = []
prin = []
maior = menor = 0
while True:
    temp.append(str(input('Nome: ')))
    temp.append(int(input('Peso: ')))
    if len(prin) == 0:
        maior = menor = temp[1]
    else:
        if temp[1] > maior:
            maior = temp[1]
        if temp[1] < menor:
            menor = temp[1]
    prin.append(temp[:])
    temp.clear()
    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if resposta == 'N':
        break
print('-=-' * 40)
print(f'O total de pessoas cadastradas foram {len(prin)}')
print(f'O maior peso foi {maior}Kg Peso de', end='')
for p in prin:
    if p[1] == maior:
        print(f'{p[0]}' , end=' ')
print()
print(f'O menor peso foi de {menor}Kg Peso de ', end=' ')
for p in prin:
    if p[1] == menor:
        print(f'{p[0]}', end='')
print()








