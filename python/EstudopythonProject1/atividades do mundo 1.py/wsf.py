import random

Jogo = ['Cara', 'Coroa']
print(random.choice(Jogo))

sorteio = ['João', 'Kamila', 'Karla', 'Gomes', 'Marcos']
print(random.choice(sorteio))

print(random.randint(10,100))
#print(random.random()) # random -> valor 0.0 até 1.0
#print(random.uniform(4, 10)) # uniform -> valor decimal do minimo ao máximo
#print(random.randint(12, 55)) # randint -> Valor inteiro aleatorio do mínimo ao máximo

#cores = ['Verde', 'Vermelho', 'Azul']
#print(random.choice(cores)) # Choice -> Escolher umas das opções que tem na lista

#cartas_de_baralho = ['Carta 1', 'Carta 2', 'Carta 3', 'Carta 4', 'Carta 5']
#random.shuffle(cartas_de_baralho) # shuffle -> embaralha uma determinada lista
#print(cartas_de_baralho)
''