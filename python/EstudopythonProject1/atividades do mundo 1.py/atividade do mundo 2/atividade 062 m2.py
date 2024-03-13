print('GERADO DE PA')
print('-=' * 10)
p = int(input('Qual o primeiro termo: '))
r = int(input('Qual Teste de python razão: '))
t = p
c = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while c <= total:
        print('{} -> '.format(t), end='')
        t += r
        c += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer Teste de python mais? '))
print('Você finalizou vendo {} termos'.format(total))