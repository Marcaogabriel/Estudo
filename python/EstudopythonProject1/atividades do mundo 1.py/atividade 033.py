from time import sleep

a = int(input('Escolha um número: '))
b = int(input('Escolha outro número: '))
c = int(input('Escolha mais um número: '))
# Verificando o menor
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
# Verificando o maior
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('O maior número é \033[32m{}\033[m'.format(maior))
print('O menor número é \033[31m{}\033[m'.format(menor))
sleep(3)
print('A média entre \033[32m{}\033[m e \033[31m{}\033[m é igual Teste de python...'.format(maior, menor))
m = (maior + menor) / 2
sleep(2)
print('A média entre esses dois números é \033[33m{:.2f}'.format(m))