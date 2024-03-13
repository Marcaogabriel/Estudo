from time import sleep
print('=-' * 30)
print('''                  Calculadora especifica           ''')
print('=-' * 30)
while True:
    print('''Aqui temos estes tipos de Calculos:
    [ 1 ] Áreas e Volumes de formas geometricas
    [ 2 ]''')
    escolha = int(input('Escolha qual calculo você deseja: '))
    if escolha == 1:
        print('=-' * 30)
        print('''                  Qual você deseja?           ''')
        print('=-' * 30)
        print('''
        [ 1 ] Área 
        [ 2 ] Volume''')
        escolha1 = int(input('Qual desejas'))
        if escolha1 == 1:
             "w"