l = ('palmeiras', 'Internacional','Flamengo','Fluminense',
     'Corinthians','Athletico-PR','Atlético-MG','América-MG',
     'Goiás','Santos','Bragantino','Botafogo','São Paulo',
     'Ceará','Fortaleza','Coritiba','Cuiabá','Avaí','Atletico-GO',
     'Juventude')
print('-=' * 30)
print(f'Lista de times: {l}')
print('-=' * 30)
print(f'Do primeiro até o quinto colocado: {l[:5]}')
print('-=' * 30)
print(f'Do decimo sexto até o último colocado: {l[-4:]}')
print('-=' * 30)
print(f'Em ordem alfabetica: {(sorted(l))}')
print('-=' * 30)
print(f'O time Santos está no {l.index("Santos")+1}º lugar')
print('-=' * 30)