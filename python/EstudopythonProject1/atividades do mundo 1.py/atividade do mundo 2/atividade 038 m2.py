from time import sleep

a = int(input('Escolha um número: '))
b = int(input('Escolha outro número: '))

print('Processando...')

sleep(2)
if a > b:
    print('O primeiro valor {} é maior que o Segundo número {}'.format(a, b))
elif b > a:
    print('O Segundo valor {} é maior que o primeiro valor {}'.format(b, a))
else:
    print('Os números {} e {} são iguais'.format(a, b))