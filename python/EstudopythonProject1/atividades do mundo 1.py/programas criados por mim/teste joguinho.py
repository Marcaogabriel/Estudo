from random import choice
from time import sleep

a = int(input('\033[35mEscolha um número entre 1 e 5 veja se acerta\033[m: '))
b = int(input('\033[36mEscolha outro número para ver se acerta\033[m: '))
lista = [1, 2, 3, 4, 5]
resultado = choice(lista)
print('Espere estou escolhendo um número...')
sleep(3)
if a == resultado:
    print('\033[32mPARABENSS você acertou de primeira eu pensei no número {} e você tambem\033[m'.format(resultado))
elif b == resultado:
    print('\033[33mBOAAA não foi de primeira mas foi de segunda eu pensei no número {} e você tambem\033[m'.format(resultado))
else:
    print('\033[31mNossa como você é ruim eu lhe dei duas chances e vc errou eu pensei no número {} e vc no {} e no {}\033[m'.format(resultado, a, b))
    