dados = dict()
dados['nome'] = str(input('Nome: '))
dados['Media'] = int(input('Média: '))
if dados['Media'] > 6:
    print(f'O aluno {dados["nome"]} foi aprovado com média {dados["Media"]}')
else:
    print(f'O aluno {dados["nome"]} foi reprovado com média {dados["Media"]}')

