from random import randint
escolhas = randint(1, 10), randint(1, 10), randint(0, 10), randint(0, 10), randint(0, 10)
print(f'Os valores sorteados foram: ', end='')
for n in escolhas:
    print(f'{n} ', end='')
print(f'\nO maior valor sorteado foi {max(escolhas)}')
print(f'O menor número sorteado foi {min(escolhas)}')