casa = float(input('Qual o valor da casa? '))
salario = float(input('Qual o salario? '))
anos = int(input('Em quantos anos você vai pagar: '))
prestação = casa / (anos * 12)
minimo = salario * 30/100
print('Para pagar uma casa de R${:.2f} em {} anos'.format(casa, anos, end =''))
print('A prestação sera de R${:.2f}'.format(prestação))
if prestação <= minimo:
    print('O Empréstimo pode ser concedido')
else:
    print('Empréstimo negado')
