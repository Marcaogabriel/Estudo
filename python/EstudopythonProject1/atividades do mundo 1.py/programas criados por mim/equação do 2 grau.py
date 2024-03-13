from time import sleep

a = int(input('Digite o Teste de python: '))
b = int(input('Digite o b: '))
c = int(input('Digite o c: '))

# Delta
d2 = (b ** 2)
d3 = a * c
d4 = -4
delta = d2 + (d4 * d3)
print('Então se Teste de python for = {} b for {} e p for {} o delta sera {}'.format(a, b, c, delta))
sleep(2)
#bhaskara

b1 = -b
b2 = delta ** (1/2)
b3 = 2 * a
x1 = (b1 + b2) / b3
x2 = (b1 - b2) / b3

print('Então o bhaskara:')
print('x1 = {:.2f}'.format(x1))
print('x2 = {:.2f}'.format(x2))