from time import sleep


def linha():
    print('=-' * 30)



total = 0
carrinho = list()
listinha = list()
mt = 0
a = 0
titulo = 'BEM VINDOS A CIDADEZINHA'
nomedaloja1 = 'BEM VINDO AO MERCADO MARCÃO'
nomedaloja2 = 'LOJAS KAMILA'
# Parte da tela Inicial
while True:
    linha()
    print(titulo.center(55))
    linha()
    print('''Em qual Loja deseja entrar?
    [ 1 ] LOJAS MARCÃO 
    [ 2 ] LOJAS KAMILA ''')
    escolha0 = int(input('Escolha o local: '))
# Parte Do Marcão
    if escolha0 == 1:
        while True:
            linha()
            print(nomedaloja1.center(55))
            linha()
            print('''Qual Área Você deseja entrar:
                        [ 1 ] Corredor 1
                        [ 2 ] Corredor 2
                        [ 3 ] Corredor 3
                        [ 4 ] Corredor 4
                        [ 5 ] Corredor 5
                        [ 6 ] Corredor 6
                        [ 7 ] Padaria
                        [ 8 ] Açougue
                        [ 88 ] Ver na lista o valor das coisas que está no carrinho
                        [ 99 ] Ver o carrinho e o valor total da compra
                        [ 0 ] Finalizar compras''')
            escolha = int(input('Digite em qual prateleira você deseja entrar: '))
            linha()
            if escolha == 1:
                while True:
                    print('''No corredor 1 tem
                    [ 1 ] Prateleira de grãos 
                    [ 2 ] Prateleira de miojo
                    [ 3 ] Prateleira de chá
                    [ 4 ] Prateleira de café
                    [ 5 ] Prateleira de temperos
                    [ 88 ] Ver na lista o valor das coisas que está no carrinho
                    [ 99 ] Ver o carrinho e o valor total da compra
                    [ 0 ] Sair do corredor''')
                    escolha1 = int(input('Qual Prateleira você vai ver? '))
                    sleep(0.3)
                    if escolha1 == 1:
                            print('''Prateleira de grãos
                            [ 1 ] 10R$ 1kg Feijão 
                            [ 2 ] 10R$ 1kg Arroz
                            [ 3 ] 10R$ 1kg Flocão
                            [ 4 ] 4.50R$ milho de pipoca
                            [ 5 ] 2R$ Pipoca de micro-ondas
                            [ 6 ] 5R$ Macarrão
                            [ 7 ] 7R$ Macarrão prego
                            [ 8 ] 13R$ Massa de Lasanha
                            [ 88 ] Ver na lista o valor das coisas que está no carrinho
                            [ 99 ] Ver o carrinho e o valor total da compra
                            [ 0 ] Sair da Prateleira
                            ''')
                            while True:
                                escolha11 = int(input('Oque você ira colocar no carrinho? '))
                                if escolha11 == 1:
                                    print(f'Você adicionou 1Kg de Feijão ao seu carrinho' )
                                    carrinho.append(f'1Kg de Feijão' )
                                    listinha.append(f'1Kg de Feijão\Preço 10R$')
                                    total += 10
                                elif escolha11 == 2:
                                    print('Você adicionou 1 Kg de Arroz ao seu carrinho')
                                    carrinho.append('1Kg de Arroz')
                                    listinha.append('1kg de Arroz\Preço 10R$')
                                    total += 10
                                elif escolha11 == 3:
                                    print('Você adicionou 1 Kg de Flocão ao seu carrinho')
                                    carrinho.append('1Kg de Flocão')
                                    listinha.append('1kg de Flocão\Preço 10R$')
                                    total += 10
                                elif escolha11 == 4:
                                    print('Você adicionou Milho de pipoca ao seu carrinho')
                                    carrinho.append('Milho de Pipoca')
                                    listinha.append('Milho de Pipoca\Preço 4.50R$')
                                    total += 4.50
                                elif escolha11 == 5:
                                    print('Você adicionou Pipoca de micro-ondas ao seu carrinho')
                                    carrinho.append('Pipoca de micro-ondas')
                                    listinha.append('Pipoca de micro-ondas\Preço 2R$')
                                    total += 2
                                elif escolha11 == 6:
                                    print('Você adicionou Macarrão ao seu carrinho')
                                    carrinho.append('Macarrão')
                                    listinha.append('Macarrão\Preço 5R$')
                                    total += 5
                                elif escolha11 == 7:
                                    print('Você adicionou Macarrão prego ao seu carrinho')
                                    carrinho.append('Macarrão prego')
                                    listinha.append('Macarrão prego\Preço 7R$')
                                    total += 7
                                elif escolha11 == 8:
                                    print('Você adicionou Massa de Lasanha prego ao seu carrinho')
                                    carrinho.append('Massa de Lasanha')
                                    listinha.append('Massa de Lasanha\Preço 10R$')
                                    total += 10
                                elif escolha11 == 88:
                                    linha()
                                    print('Aqui está a Listinha dos preços dos itens que você tem')
                                    listinha.sort()
                                    for l in listinha:
                                        print(l)
                                        sleep(0.5)
                                    linha()
                                elif escolha11 == 99:
                                    print('Aqui está seu carrinho')
                                    linha()
                                    sleep(1)
                                    for c in carrinho:
                                        print(c)
                                        sleep(0.5)
                                    linha()
                                    print(f'O preço total é {total:.2f}R$')
                                    linha()
                                elif escolha11 == 0:
                                    break
                                else:
                                    print('\033[31mOPÇÃO INVALIDA\033[m, TENTE NOVAMENTE')
                    elif escolha1 == 2:
                        print('''Prateleira de Miojo
                         [ 1 ] 1.25R$ Miojo sabor galinha caipira
                         [ 2 ] 1.25R$ Miojo sabor carne
                         [ 3 ] 1.25R$ Miojo sabor goreng Indomie
                         [ 4 ] 1.25R$ Miojo sabor galinha caipira picante
                         [ 5 ] 1.25R$ Miojo sabor  Costela
                         [ 6 ] 4.00R$ Cup Noodles sabor Legumes
                         [ 7 ] 4.00R$ Cup Noodles sabor Frutos do Mar
                         [ 8 ] 4.00R$ Cup Noodles sabor Bolonhesa
                         [ 9 ] 4.00R$ Cup Noodles sabor Yakissoba
                         [ 10 ] 4.00R$ Cup Noodles sabor Curry
                         [ 88 ] Ver na lista o valor das coisas que está no carrinho
                         [ 99 ] Ver o carrinho e o valor total da compra
                         [ 0 ] Sair da Prateleira''')
                        while True:
                            escolha12 = int(input('Oque você ira colocar no carrinho? '))
                            if escolha12 == 1:
                                print('Você adicionou Miojo sabor galinha caipira no carrinho')
                                carrinho.append('Miojo sabor galinha caipira')
                                listinha.append('Miojo sabor galinha caipira\Preço 1.25R$')
                                total += 1.25
                            elif escolha12 == 2:
                                print('Você adicionou Miojo sabor carne no carrinho')
                                carrinho.append('Miojo sabor carne')
                                listinha.append('Miojo sabor carne\Preço 1.25R$')
                                total += 1.25
                            elif escolha12 == 3:
                                print('Você adicionou Miojo sabor goreng Indomie no carrinho')
                                carrinho.append('Miojo sabor goreng Indomie')
                                listinha.append('Miojo sabor goreng Indomie\Preço 1.25R$')
                                total += 1.25
                            elif escolha12 == 4:
                                print('Você adicionou iojo sabor galinha caipira picante no carrinho')
                                carrinho.append('Miojo sabor galinha caipira picante')
                                listinha.append('Miojo sabor galinha caipira picante\Preço 1.25R$')
                                total += 1.25
                            elif escolha12 == 5:
                                print('Você adicionou Miojo sabor Costela no carrinho')
                                carrinho.append('Miojo sabor  Costela')
                                listinha.append('Miojo sabor  Costela\Preço 1.25R$')
                                total += 1.25
                            elif escolha12 == 6:
                                print('Você adicionouCup Noodles sabor Legumes no carrinho')
                                carrinho.append('Cup Noodles sabor Legumes')
                                listinha.append('MCup Noodles sabor Legumes\Preço 4R$')
                                total += 4
                            elif escolha12 == 7:
                                print('Você adicionou Cup Noodles sabor Frutos do Mar no carrinho')
                                carrinho.append('Cup Noodles sabor Frutos do Mar')
                                listinha.append('Cup Noodles sabor Frutos do Mar\Preço 4R$')
                                total += 4
                            elif escolha12 == 8:
                                print('Você adicionou Cup Noodles sabor Bolonhesa no carrinho')
                                carrinho.append('Cup Noodles sabor Bolonhesa')
                                listinha.append('Cup Noodles sabor Bolonhesa\Preço 4R$')
                                total += 4
                            elif escolha12 == 9:
                                print('Você adicionou Cup Noodles sabor Yakissoba no carrinho')
                                carrinho.append('Cup Noodles sabor Yakissoba')
                                listinha.append('Cup Noodles sabor Yakissoba\Preço 4R$')
                                total += 4
                            elif escolha12 == 10:
                                print('Você adicionou Cup Noodles sabor Curry no carrinho')
                                carrinho.append('Cup Noodles sabor Curry')
                                listinha.append('Cup Noodles sabor Curry\Preço 4R$')
                                total += 4
                            elif escolha12 == 88:
                                linha()
                                print('Aqui está a Listinha dos preços dos itens que você tem')
                                listinha.sort()
                                for l in listinha:
                                    print(l)
                                    sleep(0.5)
                                linha()
                            elif escolha12 == 99:
                                print('Aqui está seu carrinho')
                                linha()
                                sleep(1)
                                for c in carrinho:
                                    print(c)
                                    sleep(0.5)
                                linha()
                                print(f'O preço total é {total:.2f}R$')
                                linha()
                            elif escolha12 == 0:
                                break
                            else:
                                print('\033[31mOPÇÃO INVALIDA\033[m, TENTE NOVAMENTE')

                    elif escolha1 == 3:
                        print('''Prateleira de chá
                        [ 1 ] 7.00 R$ Caixinha de chá de boldo
                        [ 2 ] 7.00 R$ Caixinha de chá de camomila                    
                        [ 3 ] 7.00 R$ Caixinha de chá de capim-cidreira
                        [ 4 ] 7.00 R$ Caixinha de chá verde 
                        [ 5 ] 7.00 R$ Caixinha de chá de hibisco
                        [ 6 ] 7.00 R$ Caixinha de chá de hortelã
                        [ 7 ] 7.00 R$ Caixinha de chá de erva doce
                        [ 8 ] 7.00 R$ Caixinha de chá de erva cidreira
                        [ 9 ] 7.00 R$ Caixinha de chá de alecrim
                        [ 10 ] 7.00 R$ Caixinha de chá de Mate
                        [ 88 ] Ver na lista o valor das coisas que está no carrinho
                        [ 99 ] Ver o carrinho e o valor total da compra
                        [ 0 ] Sair da Prateleira''')
                        escolha13 = int(input('Escolha oque vai levar: '))
                        if escolha13 == 1:
                            print('Você adicionou Caixinha de chá de boldo no carrinho')
                            carrinho.append('Caixinha de chá de boldo')
                            listinha.append('Caixinha de chá de boldo\Preço 7.00R$')
                            total += 1.25
                        elif escolha13 == 2:
                            print('Você adicionou Miojo sabor carne no carrinho')
                            carrinho.append('Miojo sabor carne')
                            listinha.append('Miojo sabor carne\Preço 1.25R$')
                            total += 1.25
                        elif escolha13 == 3:
                            print('Você adicionou Miojo sabor goreng Indomie no carrinho')
                            carrinho.append('Miojo sabor goreng Indomie')
                            listinha.append('Miojo sabor goreng Indomie\Preço 1.25R$')
                            total += 1.25
                        elif escolha13 == 4:
                            print('Você adicionou iojo sabor galinha caipira picante no carrinho')
                            carrinho.append('Miojo sabor galinha caipira picante')
                            listinha.append('Miojo sabor galinha caipira picante\Preço 1.25R$')
                            total += 1.25
                        elif escolha13 == 5:
                            print('Você adicionou Miojo sabor Costela no carrinho')
                            carrinho.append('Miojo sabor  Costela')
                            listinha.append('Miojo sabor  Costela\Preço 1.25R$')
                            total += 1.25
                        elif escolha13 == 6:
                            print('Você adicionouCup Noodles sabor Legumes no carrinho')
                            carrinho.append('Cup Noodles sabor Legumes')
                            listinha.append('MCup Noodles sabor Legumes\Preço 4R$')
                            total += 4
                        elif escolha13 == 7:
                            print('Você adicionou Cup Noodles sabor Frutos do Mar no carrinho')
                            carrinho.append('Cup Noodles sabor Frutos do Mar')
                            listinha.append('Cup Noodles sabor Frutos do Mar\Preço 4R$')
                            total += 4
                        elif escolha13 == 8:
                            print('Você adicionou Cup Noodles sabor Bolonhesa no carrinho')
                            carrinho.append('Cup Noodles sabor Bolonhesa')
                            listinha.append('Cup Noodles sabor Bolonhesa\Preço 4R$')
                            total += 4
                        elif escolha13 == 9:
                            print('Você adicionou Cup Noodles sabor Yakissoba no carrinho')
                            carrinho.append('Cup Noodles sabor Yakissoba')
                            listinha.append('Cup Noodles sabor Yakissoba\Preço 4R$')
                            total += 4
                        elif escolha13 == 10:
                            print('Você adicionou Cup Noodles sabor Curry no carrinho')
                            carrinho.append('Cup Noodles sabor Curry')
                            listinha.append('Cup Noodles sabor Curry\Preço 4R$')
                            total += 4
                        elif escolha13 == 88:
                            linha()
                            print('Aqui está a Listinha dos preços dos itens que você tem')
                            listinha.sort()
                            for l in listinha:
                                print(l)
                                sleep(0.5)
                            linha()
                        elif escolha13 == 99:
                            print('Aqui está seu carrinho')
                            linha()
                            sleep(1)
                            for c in carrinho:
                                print(c)
                                sleep(0.5)
                            linha()
                            print(f'O preço total é {total:.2f}R$')
                            linha()
                        elif escolha13 == 0:
                            break
                        else:
                            print('\033[31mOPÇÃO INVALIDA\033[m, TENTE NOVAMENTE')
                    elif escolha1 == 4:
                        print()
                    elif escolha1 == 5:
                        print()
                    elif escolha1 == 88:
                        linha()
                        print('Aqui está a Listinha dos preços dos itens que você tem')
                        for l in listinha:
                            print(l)
                            sleep(0.5)
                        linha()
                    elif escolha1 == 99:
                        print('Aqui está seu carrinho')
                        linha()
                        sleep(1)
                        for c in carrinho:
                            print(c)
                            sleep(0.5)
                        linha()
                        print(f'O preço total é {total}R$')
                        linha()

                    elif escolha1 == 0:
                        break
                    else:
                        print('\033[31mOPÇÃO INVALIDA\033[m, TENTE NOVAMENTE')

            elif escolha == 2:
                    print('''No corredor 2 tem
                    [ 1 ] Prateleira de Biscoitos
                    [ 2 ] Prateleira de Salgadinho 
                    [ 3 ] Prateleira de ''')
            elif escolha == 3:
                    print()
            elif escolha == 4:
                    print()
            elif escolha == 5:
                print()
            elif escolha == 6:
                print()
            elif escolha == 7:
                print()
            elif escolha == 8:
                print()
            elif escolha == 88:
                linha()
                print('Aqui está a Listinha dos preços dos itens que você tem')
                for l in listinha:
                    print(l)
                    sleep(0.5)
                linha()
            elif escolha == 99:
                print('Aqui está seu carrinho')
                linha()
                sleep(1)
                for c in carrinho:
                    print(c)
                    sleep(0.5)
                linha()
                print(f'O preço total é {total}R$')
                linha()
            elif escolha == 0:
                print('Aqui está seu carrinho')
                linha()
                sleep(1)
                for c in carrinho:
                    print(c)
                    sleep(0.5)
                linha()
                print(f'O preço total é {total}R$')
                break
            else:
                print('\033[31mOPÇÃO INVALIDA\033[m, TENTE NOVAMENTE')
# Parte de Kamila
    elif escolha0 == 2:
        print()
