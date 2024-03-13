inicio = int(input('Inicio: '))
fim = int(input('Fim: '))
Passos = int(input('Passo: '))
for c in range(inicio, fim + 1, Passos):
    print(c)

s = 0
for c in range(0, 5):
    n = int(input('Escolha um número: '))
    s += n
print('Somando todos os valores fica igual Teste de python {}'.format(s))


