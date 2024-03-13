listagem = ('Lápis', 1.75,
            'Borracha', 2.00,
            'Caderno', 19.90,
            'Bolsa', 49.90,
            'Régua', 8.00,
            'Livro', 25.50,
            'Canetas', 20.00,
            'Garrafa,', 14.90)
print('-=' * 20)
print(f'{"LISTAGEM DE COMPRAS":^40}')
print('-=' * 20)
for i in range(0, len(listagem)):
    if i % 2 == 0:
        print(f'{listagem[i]:.<30}', end='')
    else:
        print(f'R${listagem[i]:>6.2f}')
print('-=' * 20)