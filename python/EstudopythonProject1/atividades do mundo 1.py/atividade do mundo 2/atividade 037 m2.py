n = int(input('Escolha um número inteiro: '))
print('''Escolha para onde você quer converter
 [ 1 ] converter para BINÁRIO
 [ 2 ] converter para OCTAL
 [ 3 ] converter para HEXADECIMAL''')
opção = int(input('Sua opção: '))
if opção == 1:
    print('{} convertido para BINÁRIO é igual Teste de python {}'.format(n, bin(n) [2:] ))
elif opção == 2:
    print('{} convertiddo para OCTAL é igual Teste de python {}'.format(n, oct(n) [2:] ))
elif opção == 3:
    print('{} convertido para HEXADECIMAL é igual Teste de python {}'.format(n, hex(n) [2:] ))
else:
    print('Opção invalida tente novamente')
