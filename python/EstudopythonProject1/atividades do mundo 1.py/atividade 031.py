d = float(input('Qual Teste de python distância: '))
if d <= 200:
    p = 0.50 * d
    print('O preço da passagem é R${:.2f}'.format(p))
else:
    p1 = 0.45 * d
    print('O valor Teste de python pagar da passagem é R${:.2f}'.format(p1))