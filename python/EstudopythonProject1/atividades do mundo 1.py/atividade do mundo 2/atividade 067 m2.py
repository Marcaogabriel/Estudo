e = 1
r = 1
while True:
    e = int(input('Escolha um número para aparecer sua tabuada: '))
    r = int(input('Ate quantos número você quer que Teste de python tabuada calcule? '))
    if e < 0:
        break
    else:
        for n in range(1, r+1):
            print(f'{e} x {n} = {e * n}')
