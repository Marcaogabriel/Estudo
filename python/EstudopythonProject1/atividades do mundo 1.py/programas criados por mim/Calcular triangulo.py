from time import sleep
print('-=' * 22)
print('Faça para descobrir Teste de python hipotenusa')
print('-=' * 22)
co1 = int(input('Qual o cateto oposto: '))
ca1 = int(input('Qual o cateto adjacente: '))
co = co1 ** 2
ca = ca1 ** 2
tr = co + ca
h = tr ** (1/2)
print(f'A hipotenusa é {h:.2f}')
