soma = 0
cont = 0
for c in range(1, 7):
    a = int(input('Escolha um número: '))
    if a % 2 == 0:
        soma += a
        cont += 1
print('A soma dos números pares {} é {}'.format(cont, soma))