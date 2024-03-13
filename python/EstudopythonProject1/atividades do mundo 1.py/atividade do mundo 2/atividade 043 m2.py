peso = float(input('Qual o seu peso? (KG) '))
altura = float(input('Qual é sua altura? (m) '))
imc = peso / (altura ** 2)
print('O imc dessa pessoa é {:.1f}'.format(imc))
if imc < 18.5:
    print('Você está abaixo do PESO NORMAL')
elif 18.5 <= imc < 25:
    print('Você está na faixa do PESO NORMAL')
elif 25 <= imc < 30:
    print('Você está em SOBREPESO')
elif 30 <= imc < 40:
    print('Você está em OBESIDADE')
elif imc >= 40:
    print('Você está em OBESIDADE MÓRBIDA, CUIDADO')