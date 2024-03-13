while True:
    print('''QUAL ÁREA DESEJA?
    [ 1 ] triângulo
    [ 2 ] Quadrado
    [ 3 ] Retângulo
    [ 4 ] Trápezio
    [ 0 ] Sair do programa''')
    escolha = int(input('Qual área você deseja descobrir? '))
    if escolha == 1:
        base_triângulo = float(input('base: '))
        altura_triângulo = float(input('altura: '))
        area_triângulo = (base_triângulo * altura_triângulo) / 2
        print(f'Com a base {base_triângulo} e a altura {altura_triângulo} a área é {area_triângulo}')
    elif escolha == 2:
        lado_quadrado = float(input('Quanto vale um lado de um quadrado? '))
        area_quadrado = lado_quadrado ** 2
        print(f'Com o lado {lado_quadrado} a área é {area_quadrado}')
    elif escolha == 3:
        base_retângulo = float(input('base: '))
        altura_retângulo = float(input('altura: '))
        area_retângulo = base_retângulo * altura_retângulo
        print(f'Com a base {base_retângulo} e a altura {altura_retângulo} a área é {area_retângulo}')

    elif escolha == 4:
        base_maior = float(input('Base maior: '))
        base_menor = float(input('Base menor: '))
        Altura = float(input('Altura: '))
        Área_do_trápezio_parte_1 = (base_maior + base_menor) * Altura
        Área_do_trápezio = Área_do_trápezio_parte_1 / 2
        print(f'A área do trápezo é de {Área_do_trápezio}cm²')

    elif escolha == 0:
        break
    else:
        print('OPÇÃO INVALIDA, TENTE NOVAMENTE')