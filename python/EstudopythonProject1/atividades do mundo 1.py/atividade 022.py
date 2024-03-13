a = str(input('Digite seu nome: ')).strip()
print('Analisando seu nome...')
print('Seu nome em maiúsculas é \033[31m{}\033[m'.format(a.upper()))
print('Seu nome em minúsculas é \033[32m{}\033[m'.format(a.lower()))
print('Seu nome tem ao todo \033[33m{}\033[m letras'.format((len(a ) - a.count(' '))))
separa = a.split()
print('seu primeiro nome tem é \033[34m{}\033[m e ele tem \033[35m{}\033[m letras'.format(separa[0], len(separa[0])))

