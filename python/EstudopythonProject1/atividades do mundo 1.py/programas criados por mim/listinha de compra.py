listagem = (str(input('Qual o nome do produto: ')),
    int(input('Qual o Preço do produto R$')),
    str(input('Qual o nome do produto: ')),
    int(input('Qual o Preço do produto R$')),
    str(input('Qual o nome do produto: ')),
    int(input('Qual o Preço do produto R$')),
    str(input('Qual o nome do produto: ')),
    int(input('Qual o Preço do produto R$')),
    str(input('Qual o nome do produto: ')),
    int(input('Qual o Preço do produto R$')),
    str(input('Qual o nome do produto: ')),
    int(input('Qual o Preço do produto R$')),
    str(input('Qual o nome do produto: ')),
    int(input('Qual o Preço do produto R$')),
    str(input('Qual o nome do produto: ')),
    int(input('Qual o Preço do produto R$')),
    str(input('Qual o nome do produto: ')),
    int(input('Qual o Preço do produto R$')),
    str(input('Qual o nome do produto: ')),
    int(input('Qual o Preço do produto R$')))
print('_' * 43)
print(f'{" LISTAGEM DE COMPRAS":^40}')
print('_' * 43)
for i in range(0, len(listagem)):
    if i % 2 == 0:
        print(f'{listagem[i]:.<30}', end='')
    else:
        print(f'R${listagem[i]:>9.2f}')
print('_' * 43)


