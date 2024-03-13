
import time

def tempo():
    time.sleep(2)
while True:
    print('CALCULADORA')
    print('''Qual operação você deseja? 
    [ 1 ] Soma +
    [ 2 ] Subtração -
    [ 3 ] Mutiplicação x
    [ 4 ] Divisão ÷
    [ 5 ] Elevar ao expoente x²
    [ 6 ] porcentagem %
    [ 7 ] Dividir 1 pelo número 1/x 
    [ 8 ] Alterar o sinal +/-
    [ 9 ] fazer a raiz pelo expoente √0
    ''')
    escolha = int(input('Escolha um dos números para operação: '))

    if escolha == 1:
        a = float(input('Escolha um número: '))
        b = float(input('Escolha outro número: '))
        soma = a + b
        print('calculando...')
        tempo()
        print(soma)

    elif escolha == 2:
        a = float(input('Escolha um número: '))
        b = float(input('Escolha outro número: '))
        subtracao = a - b
        print('calculando...')
        tempo()
        print(subtracao)

    elif escolha == 3:
        a = float(input('Escolha um número: '))
        b = float(input('Escolha outro número: '))
        multiplicacao = a * b
        print('calculando...')
        tempo()
        print(multiplicacao)

    elif escolha == 4:
        a = float(input('Escolha um número: '))
        b = float(input('Escolha outro número: '))
        divisao = a / b
        print('calculando...')
        tempo()
        print(divisao)

    elif escolha == 5:
        a = float(input('Escolha um número: '))
        b = float(input(f'Escolha o quanto você quer elevar {a}: '))
        expoente = a ** b
        print('calculando...')
        tempo()
        print(expoente)

    elif escolha == 6:
        a = float(input('Escolha um número: '))
        ba = float(input(f'Escolha por quantos porcento vc quer o número {a}: '))
        b = ba / 100
        porcentagem = a * b
        print('calculando...')
        tempo()
        print(porcentagem)

    elif escolha == 7:
        a = float(input('Escolha um número para dividir 1 por ele: '))
        umdividido = 1 / a
        print('calculando...')
        tempo()
        print(umdividido)

    elif escolha == 8:
        a = float(input('Escolha um número: '))
        b = float(input('Escolha outro número: '))
        mudarsinaldosdo_a = a * (-1)
        mudarsinaldosdo_b = b * (-1)
        print('calculando...')
        tempo()
        print(f'Mudando o sinal ficam {mudarsinaldosdo_a} e {mudarsinaldosdo_b}')

    elif escolha == 9:
        a = float(input('Escolha um número: '))
        b = float(input('Escolha um número para a raiz: '))
        raiz = a ** (1/b)
        print('calculando...')
        tempo()
        print(raiz)

    else:
        print('Você não escreveu escreveu nenhuma das operações que estavam')