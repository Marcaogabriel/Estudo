testes = list()
dado = list()
totalmaior = totalmenor = 0
for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append((int(input('Idade: '))))
    testes.append(dado[:])
    dado.clear()
for p in testes:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade')
        totalmaior += 1
    else:
        print(f'{p[0]} é menor de idade')
        totalmenor += 1

print(f'Temos {totalmaior} maiores de idade e {totalmenor} menores de idade') 