while True:
    print('''GEOMETRIA ESPACIAL
    [ 1 ] Cubo
    [ 2 ] pirâmide
    [ 3 ] Cílindro
    [ 4 ] Cone
    [ 5 ] Paralelepipedo''')
    escolha = int(input('Escolha qual você quer fazer: '))
    if escolha == 1:
        aresta = float(input('Qual o valor da aresta: '))
        print('''Qual operação você deseja
        [ 1 ] Área total
        [ 2 ] Área do lado
        [ 3 ] Área da base
        [ 4 ] Volume   ''')
        escolha_cubo = int(input('Escolha: '))
        if escolha_cubo == 1:
            area_total = (aresta ** 2) * 6
            print(f'a área total é {area_total}cm²')

        elif escolha_cubo == 2:
            area_do_lado = (aresta ** 2) * 4
            print(f'a área lateral é {area_do_lado}cm²')

        elif escolha_cubo == 3:
            area_da_base = aresta ** 2
            print(f'A área da basa é {area_da_base}cm²')

        elif escolha_cubo == 4:
            Volume_cubo = aresta ** 3
            print(f'O volume do cubo é {Volume_cubo}cm³')

    elif