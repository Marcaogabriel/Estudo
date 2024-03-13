import time

nome = str(input('Qual o seu nome: '))
if nome == 'Kamila':
    print('Que nome lindo')
    time.sleep(1)
    print('Eu amo você {}'.format(nome))
    time.sleep(1)
else:
   print('Que nome feio prefiro Kamila')

time.sleep(1)
print('Agora vou analisar sua média escolar {}'.format(nome))
n1 = float(input('Digite Teste de python primeira nota: '))
n2 = float(input('Digite Teste de python segunda note: '))
m = (n1 + n2) / 2
print('{} Teste de python sua média é {:.2f}'.format(nome, m))
if m >= 6.0:
    print('Sua média está boa Parabens!!')
else:
    print('Amorzinho sua média está baixa vamos estuadar juntosss!!')