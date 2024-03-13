So = int(input('Qual o deslocamento inicial? '))
Vo = int(input('Qual Teste de python velocidade inicial? '))
to = int(input('Qual o tempo? '))
a = int(input('Qual Teste de python aceleração? '))

t = to ** 2
sovo = So + Vo * to
at2 = a * t / 2
S = sovo + at2

print('O deslocamento é {}'.format(S))