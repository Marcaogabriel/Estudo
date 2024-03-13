from random import randint
from time import sleep

itens = ['Pedra', 'Papel', 'Tesoura']
computador = randint(0, 2)
print('''Vamos brincar!! Faça sua escolha
 [ 0 ] Pedra
 [ 1 ] Papel
 [ 2 ] Tesoura''')
jogador = int(input('Qual é Teste de python sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
print('-=' * 11)
print('computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
print('-=' * 11)
if computador == 0:
    if jogador == 0:
        print('\033[33mEMPATE\033[m')

    elif jogador == 1:
        print('\033[32mJOGADOR VENCE\033[m')

    elif jogador == 2:
        print('\033[31mCOMPUTADOR VENCEU\033[m')

    else:
        print('\033[31mJOGADA INVÁLIDA!\033[m')

elif computador == 1:
    if jogador == 0:
        print('\033[31mCOMPUTADOR VENCE\033[m')

    elif jogador == 1:
        print('\033[33mEMPATE\033[m')

    elif jogador == 2:
        print('\033[32mJOGADOR VENCE\033[m')

    else:
        print('\033[31mJOGADA INVÁLIDA!\033[m')

elif computador == 2:
    if jogador == 0:
        print('\033[32mJOGADOR VENCE\033[m')

    elif jogador == 1:
        print('\033[31mCOMPUTADOR VENCE\033[m')

    elif jogador == 2:
        print('\033[33mEMPATE\033[m')

    else:
        print('\033[31mJOGADA INVÁLIDA!\033[m')


# Pedra = 0
# Papel = 1
# Tesoura = 2