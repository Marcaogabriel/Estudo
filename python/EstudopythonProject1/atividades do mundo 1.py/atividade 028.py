from random import randint
from time import sleep

nome = str(input('Diga seu nome: '))
print('-=-' * 30)
print('\033[33mOla {} vamos brincar escolha um número de 1 Teste de python 5 e tente Teste de python sorte de acertar\033[m'.format(nome))
print('-=-' * 30)
n = int(input('\033[35mEscolha um número\033[m: '))
e = randint(0, 5)
print('\033[34mEscolhendo um número...\033[m')
sleep(3)
if e == n:
    print('\033[32mParabens você venceu')
    print('Você venceu eu pensei no numero {} e você tambem\033[m'.format(e))
else:
    print('\033[31mVocê perdeu tente novamente')
    print('O número que escolhi foi {} e você escolheu {}'.format(e, n))