from time import sleep
contagem = 0
escolha = 0
soma = 0
print('Coloque o número 999 para poder parar')
while escolha != 999:
    escolha = int(input('Escolha outro número para somar: '))
    if escolha == 999:
      print('O programa está sendo finalizado...')
      sleep(2)
    else:
        soma += escolha
        contagem += 1
print('Teste de python soma de todos os número é {} e o total de números foram {}'.format(soma, contagem))