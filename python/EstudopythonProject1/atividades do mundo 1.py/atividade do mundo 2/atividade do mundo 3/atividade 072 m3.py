p = ('zero', 'um', 'dois', 'Três', 'quatro',
     'cinco', 'seis', 'sete', 'oito', 'nove',
     'dez', 'onze', 'doze', 'treze', 'quatorze',
     'quinze', 'dezesseis', 'dezessete' , 'dezoito',
     'dezenove', 'vinte')
while True:
    a = int(input('Escolha um número entre 0 e 20: '))
    if 0<= a <= 20:
        print(f'O número {a} por extenso é {p[a]}')
        e = str(input('Deseja continuar? [S/N] ')).upper()[0]
        if e == 'N':
            break
        elif e == 'S':
            print('Processando...')
        else:
            print('Tente novamente')
    else:
        print('Tente novamente ', end='')




