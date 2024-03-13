totma18 = tot18 = totmn18 = toth = totma20 = tot20 = totm20 = totf = totfma20 = totf20 = totfm20 = 0
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    if sexo == 'M':
        toth += 1
    if sexo == 'M' and idade > 20:
        totma20 += 1
    if sexo == 'M' and idade == 20:
        tot20 += 1
    if sexo == 'M' and idade < 20:
        totm20 += 1
    if sexo == 'F':
        totf += 1
    if sexo == 'F' and idade > 20:
        totfma20 += 1
    if sexo == 'F' and idade == 20:
        totf20 += 1
    if sexo == 'F' and idade < 20:
        totfm20 += 1
    if idade > 18:
        totma18 += 1
    if idade == 18:
        tot18 += 1
    if idade < 18:
        totmn18 += 1

    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if resposta == 'N':
        break

print(f'O total de homens é {toth}')
print(f'O total de homens com mais de 20 anos é {totma20}')
print(f'O total de homens com 20 anos é {tot20}')
print(f'O total de homens com menos de 20 anos é {totm20}')
print(f'O total de mulheres é {totf}')
print(f'O total de mulheres com mais de 20 anos é {totfma20}')
print(f'O total de mulheres com 20 anos é {totf20}')
print(f'O total de mulheres com menos de 20 anos é {totfm20}')
print(f'O total de Pessoas com mais de 18 anos é {totma18}')
print(f'O total de Pessoas com 18 anos é {tot18}')
print(f'O total de pessoas com menos de 18 anos é {totmn18}')
