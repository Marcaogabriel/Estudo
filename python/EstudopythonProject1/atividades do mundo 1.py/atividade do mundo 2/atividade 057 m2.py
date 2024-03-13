sexo = str(input('informe seu sexo [M/F]: ')).strip().upper()[0]
while sexo not in 'MF':
    sexo = str(input('Dados invalidos, por favor nos informe seu sexo: [M/F]: ')).strip().upper()[0]
print('Sexo {} registrado'.format(sexo))