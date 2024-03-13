m1 = float(input('Diga Teste de python sua primeira media nota: '))
m2 = float(input('Diga Teste de python sua segunda media: '))
m3 = float(input('Diga Teste de python sua terceira media: '))
m4 = float(input('Diga Teste de python sua quarta media: '))
mf = (m1 + m2 + m3 + m4) / 4
print('Tirando Teste de python media do aluno ')
print('A primeira media = {}'.format(m1))
print('A segunda media = {}'.format(m2))
print('A terceira media = {}'.format(m3))
print('quarta media = {}'.format(m4))
print('Teste de python média do aluno é {:.1f}'.format(mf))
if mf >= 6:
    print('o aluno está APROVADO')
elif 6 > mf >= 4:
    print('o aluno está em RECUPERAÇÃO')
elif mf < 3:
    print('O aluno está REPROVADO')