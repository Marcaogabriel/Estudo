palavras = ('agua', 'problemas', 'fogo',
            'voar', 'ciano', 'sexo', 'laranja',
            'amemduim', 'galinha', 'caixa')
for p in palavras:
    print(f'\nNa palavra {p.upper()} temos Soletrando: ',end='')
    for letra in p:
        if letra.lower() in 'abcdefghijklmnopqrstuvwxyz':
            print(letra, end=' ')