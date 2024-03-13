ano = int(input('Qual ano você quer analisar? '))
if ano % 4 == 0:
    print('O ano \033[36m{} é BISSEXTO\033[m'.format(ano))
else:
    print('O ano \033[31m{} NÃO é BISSEXTO'.format(ano))