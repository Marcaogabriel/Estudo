from datetime import date

at = date.today().year
ano = int(input('Digite seu ano de nascimento: '))
a = at - ano
print('Uma pessoa que nasceu em {} tem {} anos em {}'.format(ano, a, at))
if a < 18:
    f = 18 - a
    an = at + f
    print('Relaxa ainda falta {} anos para você se alistar'.format(f))
    print('Seu alistamento sera no ano {}'.format(an))
elif a == 18:
    print('Opa esta na hora de se alistar entre no site do exercito')
elif a > 18:
    s = a - 18
    ano = at - s
    print('Opa amigão você já passou do tempo de se alistar Teste de python {} anos'.format(s))
    print('Seu alistamento era para ser em {}'.format(ano))