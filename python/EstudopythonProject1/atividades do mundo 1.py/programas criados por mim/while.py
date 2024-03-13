import emoji
from time import sleep

n = 1
while n != 7:
    n = int(input('Qual o número favorito de kamila? '))
    if n == 7:
        print('Parabensss você acerttou o número favorito da 🐇')
    else:
        print('Você errou tente novamente')
        sleep(1)

r = 'S'
while r == 'S':
    n = int(input('Escolha um número: '))
    r = str(input('Quer continuar [S/N] ')).upper()
print('acabo')