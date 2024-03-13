from datetime import date

atual = date.today().year
a = int(input('Qual o ano que o atleta nasceu: '))
s = atual - a
print('O atleta tem {} anos'.format(s))

if s <= 9:
    print('CLASSIFICAÇÃO: MIRIM'.format(s))
elif s <= 14:
    print('CLASSIFICAÇÃO: INFANTIL'.format(s))
elif s <= 19:
    print('CLASSIFICAÇÃO: JUNIOR'.format(s))
elif s <= 25:
    print('CLASSIFICAÇÃO: SÊNIOR'.format(s))

else:
    print('CLASSIFICAÇÃO: MASTER'.format(s))

