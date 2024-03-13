r1 = float(input('Diga o primeiro ângulo: '))
r2 = float(input('Diga o segundo ângulo: '))
r3 = float(input('Diga o terceiro ângulo: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os seguimentos acima PODEM FORMAR um triângulo ', end= '')
    if r1 == r2 == r3:
        print('EQUILATERO')
    elif r1 != r2 != r3 != r1:
        print('ESCALENO')
    else:
        print('ISÓSCELES')
else:
    print('Os ângulos acima NÃO PODM FORMAR um triângulo')