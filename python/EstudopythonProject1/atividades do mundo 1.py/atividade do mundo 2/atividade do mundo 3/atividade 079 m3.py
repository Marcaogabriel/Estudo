listinha = list()
while True:
    n = int(input('Digite um valor: '))
    if n not in listinha:
        listinha.append(n)
        print('Valor adicionado')
    else:
        print('Valor duplicado não adiciona')

    r = str(input('Deseja continuar? [S/N] '))
    if r in 'Nn':
        break
print('-=' * 30)
listinha.sort()
print(f'Você digitou os valores {listinha}')