parte = dict()
gols = list()
totl = dict()
todos = 0
parte['nome'] = str(input('Nome do jogador: '))
partidas = int(input(f'Quantas partidas {parte["nome"]} jogou? '))
for e in range(0, partidas):
    a = int(input(f'Quantos gol {parte["nome"]} fez na {e + 1}º partida: '))
    gols.append(a)
    todos += a
    totl['total'] = todos
print('-=' * 24)
print(f'O jogador {parte["nome"]} jogou {partidas} partidas')
for e in range(0, partidas):
    print(f'=> Na partida {e + 1}, fez {gols[e]} gols')
print(f'Foi um total de {totl["total"]} gols')
print('-=' * 24)

