soma = contar = menor = cont = maior = 0
barato = 0
caro = 0
print('-=' * 20)
print('     LOJÃO MARCÃO SUPER DESCONTÃO')
print('-=' * 20)
while True:
    produto = str(input('Qual o nome do produto: '))
    preço = float(input('Qual o valor do produto: R$'))
    soma += preço
    cont += 1
    if preço > 1000:
        contar += 1
    if cont == 1 or preço < menor:
        menor = preço
        barato = produto
    if cont == 1 or preço > maior:
        maior = preço
        caro = produto
    quer = ' '
    while quer not in 'SN':
        quer = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if quer == 'N':
        break
print(f'O valor total da compra é R${soma:.2f}')
print(f'Tem no total {contar} produtos maior que R$1000.00')
print(f'O produto mais barato foi a {barato} e custa R${menor}')
print(f'O produto mais caro foi o {caro} e custa R${maior}')