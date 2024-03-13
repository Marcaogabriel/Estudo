import random
n1 = str(input('Diga o nome do primeiro aluno: '))
n2 = str(input('Diga o nome do segundo aluno: '))
n3 = str(input('Diga o nome do terceiro aluno: '))
n4 = str(input('Diga o nome do quarto aluno: '))
lista = [n1, n2, n3, n4]
escolhido = random.shuffle(lista)
print('A ordem de apresentação ficou')
print('\033[33m{}\033[m'.format(lista))