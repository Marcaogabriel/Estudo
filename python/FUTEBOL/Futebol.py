import random
gols = 0

# Fazer um sistema de jogo
while True:
    time = random.randint(1,5)
    if time == 1:
        time = "Palmeiras"

    elif time == 2:
        time = "São Paulo"

    elif time == 3:
        time = "Fluminense"

    elif time == 4:
        time = "Botafogo"

    elif time == 5:
        time = "Flamengo"
    print(f'''O brasileirão série A hoje a tabela sera sport vs {time}''')
    print('''Deseja iniciar a partida? 
    [ 1 ] Sim
    [ 2 ] Não''')
    comecar = int(input('Escolha: '))

    if comecar == 1:
        while True:
            print(f'então vamos começar a partida entre sport vs {time}')
            golsdooutrotime = random.randint(0,4)
            chancesdegol = random.randint(1,6)
            if chancesdegol == 1:
                print('''Aos 47 minutos o sport tem a chance de fazer o gol qual local você ira bater?
                [ 1 ] No canto esquerdo
                [ 2 ] No canto direito
                [ 3 ] No ângulo direito
                [ 4 ] No ângulo esquerdo
                [ 5 ] No meio''')
                ondeseragol = random.randint(1,5)
                chutar = int(input('escolha onde chutar: '))
                if chutar == ondeseragol:
                    gols =+ 1
                    print(f'Goolllll e o sport marca o gol e o jogo está {gols} a {golsdooutrotime}')
                    if gols > golsdooutrotime:
                        print(f'E a partida encerra com a vitoria do Sport por {gols} a {golsdooutrotime}')
                        gols = 0
                        break

                    elif gols == golsdooutrotime:
                        print(f'E a partida encerra com o empate do Sport por {gols} a {golsdooutrotime}')
                        gols = 0
                        break

                    elif gols < golsdooutrotime:
                        print(f'E a partida encerra com a derrota do Sport por {gols} a {golsdooutrotime}')
                        gols = 0
                        break

                elif chutar != ondeseragol:
                    print(f'Não foi gol então o jogo continua {gols} a {golsdooutrotime}')

                    if gols > golsdooutrotime:
                        print(f'E a partida encerra com a vitoria do Sport por {gols} a {golsdooutrotime}')

                        break

                    elif gols == golsdooutrotime:
                        print(f'E a partida encerra com o empate do Sport por {gols} a {golsdooutrotime}')

                        break

                    elif gols < golsdooutrotime:
                        print(f'E a partida encerra com a derrota do Sport por {gols} a {golsdooutrotime}')
                        gols = 0
                        break
            if chancesdegol == 2:
                print('''Aos 30 minutos o sport tem a chance de fazer o gol qual local você ira bater?
                           [ 1 ] No canto esquerdo
                           [ 2 ] No canto direito
                           [ 3 ] No ângulo direito
                           [ 4 ] No ângulo esquerdo
                           [ 5 ] No meio''')
                ondeseragol = random.randint(1, 5)
                chutar = int(input('escolha onde chutar: '))

                if chutar == ondeseragol:
                    gols = + 1
                    print(f'Goolllll e o sport marca o gol e o jogo está {gols} a {golsdooutrotime}')
                    if gols > golsdooutrotime:
                        print(f'E a partida encerra com a vitoria do Sport por {gols} a {golsdooutrotime}')
                        gols = 0
                        break

                    elif gols == golsdooutrotime:
                        print(f'E a partida encerra com o empate do Sport por {gols} a {golsdooutrotime}')
                        gols = 0
                        break

                    elif gols < golsdooutrotime:
                        print(f'E a partida encerra com a derrota do Sport por {gols} a {golsdooutrotime}')
                        gols = 0
                        break

                elif chutar != ondeseragol:
                    print(f'Não foi gol então o jogo continua {gols} a {golsdooutrotime}')

                    if gols > golsdooutrotime:
                        print(f'E a partida encerra com a vitoria do Sport por {gols} a {golsdooutrotime}')
                        gols = 0
                        break

                    elif gols == golsdooutrotime:
                        print(f'E a partida encerra com o empate do Sport por {gols} a {golsdooutrotime}')
                        gols = 0
                        break

                    elif gols < golsdooutrotime:
                        print(f'E a partida encerra com a derrota do Sport por {gols} a {golsdooutrotime}')
                        gols = 0
                        break


    else:
        print()
