from random import randint
from time import sleep
from operator import itemgetter
jogo = { 'jogador1': randint(1, 6),
         'jogador2': randint(1, 6),
         'jogador3': randint(1, 6),
         'jogador4': randint(1, 6)}
rank = dict
rank = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print('-=' * 15)
print('Ranking')
for i, v in enumerate(rank):
    print(f'{i+1} lugar: {v[0]} com {v[1]}')
    sleep(1)
print('-=' * 15)