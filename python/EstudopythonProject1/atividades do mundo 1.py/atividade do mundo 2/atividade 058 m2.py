import random
r = random.randint(1, 10)
n = 1
c = 0
while n != r:
    n = int(input('Escolha um número: '))
    c += 1
    if n == r:
        print('Parabenss você acertou eu pensei no número {} e você precisou de {} tentativas'.format(r, c))

    else:
        if  n < r:
            print('Um pouco mais...')
        elif n > r:
            print('Um pouco menos...')

