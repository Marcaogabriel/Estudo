from random import choice

n1 = str(input('Diga o nome do primeiro aluno: '))
n2 = str(input('Diga o nome do segundo aluno: '))
n3 = str(input('Diga o nome do terceiro aluno: '))
n4 = str(input('Diga o nome do quarto aluno: '))
lista = [n1, n2, n3, n4]
escolhido = choice(lista)
print('o aluno escolhido foi \033[37m{}\033[m'.format(escolhido))