n = str(input('Qual seu nome? ')).strip()
print('Seu nome tem Paz? \033[32m{}\033[m'.format('paz' in n.lower()))