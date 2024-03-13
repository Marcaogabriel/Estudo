escolha = 1
contar = 0
soma = 0
resposta = ''
maior = 0
menor = 0
while resposta != 'N':
    escolha = int(input('Escolha um número: '))
    resposta = str(input('Deseja continuar? [S/N] ')).upper()
    soma += escolha
    contar += 1
    dividir = soma / contar
    if contar == 1:
        maior = escolha
        menor = escolha
    else:
        if escolha > maior:
            maior = escolha
        if escolha < menor:
            menor = escolha
print('A soma dos números é {} o total de números é {} já Teste de python sua média é {}'.format(soma, contar, dividir))
print('O maior número é {} e o menor é {}'.format(maior, menor))