from time import sleep

a = int(input('Escolha um número: '))
b = int(input('Escolha outro número: '))
e = 1
while True:
    print('''ESCOLHA UMA OPÇÃO
    [ 1 ] SOMA
    [ 2 ] SUBTRAÇÃO
    [ 3 ] DIVISÃO
    [ 4 ] MULTIPLICAÇÃO
    [ 5 ] RAÍZ QUADRADA
    [ 6 ] FATORIAL
    [ 7 ] MENOR NÚMERO
    [ 8 ] MAIOR NÚMERO
    [ 9 ] NOVOS NÚMEROS
    [ 10 ] P.A
    [ 11 ] P.O
    [ 12 ] Equação do 2grau
    [ 0 ] SAIR DO PROGRAMA ''')
    e = int(input('Qual Teste de python sua escolha: '))
    # SOMA
    if e == 1:
       print('''QUAL OPÇÃO
       [ 1 ] {} + {}
       [ 2 ] {} + {}
       [ 3 ] {} + {}'''.format(a, b, a, a, b, b))
       e5 = int(input('Faça sua escolha: '))
       if e5 == 1:
           print('{} + {} = {}'.format(a, b, a + b))
       elif e5 == 2:
           print('{} + {} = {}'.format(a, a, a + a))
       elif e5 == 3:
           print('{} + {} = {}'.format(b, b, b + b))
       else:
           print('OPÇÃO INVALIDA')
       sleep(2)
    # SUBTRAÇÃO
    elif e == 2:
        print('''QUAL OPÇÃO
        [ 1 ] {} - {}
        [ 2 ] {} - {}
        [ 3 ] {} - {} 
        [ 4 ] {} - {}'''.format(a, b, b, a, a, a, b, b))
        e2 = int(input('Faça sua escolha: '))
        if e2 == 1:
            print('{} - {} = {}'.format(a, b, a - b))
        elif e2 == 2:
            print('{} - {} = {}'.format(b, a, b - a))
        elif e2 == 3:
            print('{} - {} = {}'.format(a, a, a - a))
        elif e2 == 4:
            print('{} - {} = {}'.format(b, b, b - b))
        else:
            print('OPÇÃO INVALIDA')
        sleep(2)
    # DIVISÃO
    elif e == 3:
        print('''QUAL OPÇÃO
                [ 1 ] {} / {}
                [ 2 ] {} / {}
                [ 3 ] {} / {} 
                [ 4 ] {} / {}'''.format(a, b, b, a, a, a, b, b))
        e3 = int(input('Faça sua escolha: '))
        if e3 == 1:
            print('{} / {} = {:.2f}'.format(a, b, a / b))
        elif e3 == 2:
            print('{} / {} = {:.2f}'.format(b, a, b / a))
        elif e3 == 3:
            print('{} / {} = {:.2f}'.format(a, a, a / a))
        elif e3 == 4:
            print('{} / {} = {:.2f}'.format(b, b, b / b))
        else:
            print('OPÇÃO INVALIDA')
        sleep(2)
    # MUTIPLICAÇÃO
    elif e == 4:
        print('''QUAL OPÇÃO:
        [ 1 ] {} x {}
        [ 2 ] {} x {}
        [ 3 ] {} x {}'''.format(a, b, a, a, b, b))
        e4 = int(input('Faça sua Escolha: '))
        if e4 == 1:
            print('{} x {} = {:.2f}'.format(a, a, a * a))
        elif e4 == 3:
            print('{} x {} = {:.2f}'.format(b, b, b * b))
        else:
            print('OPÇÃO INVALIDA')
        sleep(2)
    # RAÍZ QUADRADA
    elif e == 5:
        print('''QUAL OPÇÃO
        [ 1 ] √{}
        [ 2 ] √{}
        [ 3 ] Escolher um número para saber sua raiz'''.format(a, b))
        e0 = int(input('Faça sua escolha: '))
        if e0 == 1:
            print('√{} = {:.2f}'.format(a, a ** (1/2)))
        elif e0 == 2:
            print('√{} = {:.2f}'.format(b, b ** (1/2)))
        elif e0 == 3:
            t = int(input('Escolha o número que deseja fazer Teste de python raiz: '))
            print('√{} = {:.2f}'.format(t, t ** (1/2)))
        else:
            print('OPÇÃO INVALIDA')
        sleep(2)
    # Fatorial
    elif e == 6:
        print('''QUAL OPÇÃO
        [ 1 ] {}!
        [ 2 ] {}!
        [ 3 ] Escolha um número para fatorar'''.format(a, b))
        e1 = int(input('Faça sua escolha: '))
        if e1 == 1:
            c = a
            f1 = 1
            print('Calculando {}! = '.format(a), end='')
            while c > 0:
                print('{}'.format(c), end='')
                print(' tabela ' if c > 1 else ' = ', end='')
                f1 *= c
                c -= 1
            print('{}'.format(f1))
        elif e1 == 2:
            c = b
            f2 = 1
            print('Calculando {}! = '.format(b), end='')
            while c > 0:
                print('{}'.format(c), end='')
                print(' tabela ' if c > 1 else ' = ', end='')
                f2 *= c
                c -= 1
            print('{}'.format(f2))
        elif e1 == 3:
            g = int(input('Escolha o número para fatorar: '))
            c = g
            f3 = 1
            print('Calculando {}! = '.format(g), end='')
            while c > 0:
                print('{}'.format(c), end='')
                print(' tabela ' if c > 1 else ' = ', end='')
                f3 *= c
                c -= 1
            print('{}'.format(f3))
        else:
            print('OPÇÃO INVALIDA')
        sleep(2)
    #MENOR NÚMERO
    elif e == 7:
        if b < a:
            print('O menor número é o segundo que você escolheu que é: {}'.format(b))
        elif a < b:
            print('O menor número é o primeiro que você escolheu que é: {}'.format(a))
        else:
            print('Os números {} e {} são iguais'.format(a, b))
        sleep(2)
    # MAIOR NÚMERO
    elif e == 8:
        if b > a:
            print('O maior número é o segundo que você escolheu que é: {}'.format(b))

        elif a > b:
            print('O maior número é o primeiro que você escolheu que é: {}'.format(a))

        else:
            print('Os números {} e {} são iguais'.format(a, b))
        sleep(3)
    # NOVOS NÚMEROS
    elif e == 9:
        a = int(input('Escolha outro número: '))
        b = int(input('Escolha outro número: '))
        sleep(1)
    elif e == 10:
        while True:
            print('''QUAL OPÇÃO
                    [ 1 ] Razão
                    [ 2 ] Escolher termo para achar
                    [ 3 ] Não desejo continuar''')
            e9 = int(input('Faça sua escolha: '))
            if e9 == 1:
                primeirotermo = int(input('Digite o primeiro termo: '))
                termoadiante = int(input('Digite o termo adiante: '))
                razão = termoadiante - primeirotermo
                print(f'A razão é igual a {razão}')
            elif e9 == 2:
                pritermo = int(input('Qual o primeiro termo? '))
                qualter = int(input('Qual termo quer achar? '))
                razão1 = int(input('Qual a razão? '))
                sub = qualter - 1
                otermo = pritermo + sub * razão1
                print(otermo)

            elif e9 == 3:
                break

            else:
                print('OPÇÃO INVALIDA')
    #Equação o 2 grau
    elif e == 12:
        a = int(input('Digite o a: '))
        b = int(input('Digite o b: '))
        c = int(input('Digite o c: '))
        d2 = (b ** 2)
        d3 = a * c
        d4 = -4
        delta = d2 + (d4 * d3)
        print('Então se Teste de python for = {} b for {} e p for {} o delta sera {}'.format(a, b, c, delta))
        sleep(2)
        b1 = -b
        b2 = delta ** (1 / 2)
        b3 = 2 * a
        x1 = (b1 + b2) / b3
        x2 = (b1 - b2) / b3
        print('Então o bhaskara:')
        print('x1 = {:.2f}'.format(x1))
        print('x2 = {:.2f}'.format(x2))
    # SAIR DO PROGRAMA
    elif e == 0:
        print('Obrigado por utilizar o programa e volte sempre!!')
        break
    # NÚMERO DE 12 ACIMA
    else:
        print('OPÇÃO INVALIDA TENTE NOVAMENTE')