v = float(input('Qual é velocidade atual do carro? '))
if v > 80:
    print('\033[31mMULTADO! você passou o limite premitido que é 80 km/h')
    m = (v - 80)* 7
    print('Você devera pagar uma multa de R${:.2f}\033[m!'.format(m))
else:
    print('\033[34mtenha um bom dia e dirija com segurança')