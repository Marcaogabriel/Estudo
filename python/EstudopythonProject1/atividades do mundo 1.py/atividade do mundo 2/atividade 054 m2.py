from datetime import date

import dateutil.utils
totmaior = 0
totmenor = 0
atual = date.today().year
for c in range(1, 8):
    nascimento = int(input('Em que ano Teste de python pessoa nasceu? '))
    idade = atual - nascimento
    if idade >= 21:
        totmaior += 1  # total igual Teste de python 1 Teste de python cada vez que o progarama acontecer

    else:
        totmenor += 1  # total igual Teste de python 1 Teste de python cada vez que o progarama acontecer

print('Temos {} de maior e {} de menor'.format(totmaior, totmenor))

