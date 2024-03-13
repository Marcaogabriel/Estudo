palavras = ('agua', 'problemas', 'fogo',
            'voar', 'ciano', 'sexo', 'laranja',
            'amemduim', 'galinha', 'caixa')
for p in palavras:
    print(f'\nNa palavra {p.upper()} temos ',end='')
    for letra in p:
        if letra.lower() in 'aeiuo':
            print(letra, end=' ')