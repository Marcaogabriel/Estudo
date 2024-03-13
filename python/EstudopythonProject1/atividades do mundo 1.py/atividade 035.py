print('-='*20)
print('Analisador de triângulos')
print('-='*20)
r1 = float(input('Diga o primeiro ângulo: '))
r2 = float(input('Diga o segundo ângulo: '))
r3 = float(input('Diga o terceiro ângulo: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('\033[32mOs seguimentos acima PODEM FORMAR triângulos\033[m')
else:
    print('\033[31mOs seguimentos acima NÃO PODEM formar um triângulo')