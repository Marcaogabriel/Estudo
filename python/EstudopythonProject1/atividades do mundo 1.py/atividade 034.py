s = float(input('Escolha um salario: '))
if s > 1250.00:
    a = s + (s * 10/100)
    print('já que seu salario era \033[34m{:.2f}\033[m você recebe \033[32m10%\033[m de aumento ficou R$\033[34m{:.2f}\033[m'.format(s, a))
else:
    a2 = s + (s * 15/100)
    print('Já que seu salario era \033[32m{:.2f}\033[m você recebera aumento de \033[35m15%\033[m ficando com R$\033[36m{:.2f}\033[m'.format(s, a2))