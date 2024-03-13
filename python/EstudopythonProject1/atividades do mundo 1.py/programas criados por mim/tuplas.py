lanche = 'Hamburger', 'suco', 'pizza', 'pudim', 'bolo',
for c in lanche:
    print(f'Eu vou comer {c}')

for c in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[c]}')

for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')

print(sorted(lanche))
print(lanche)