import random

# Função para gerar um jogo aleatório da Mega Sena
def gerar_jogo_mega_sena():
    return sorted(random.sample(range(1, 25), 15))

# Função para comparar jogos com resultados antigos
def comparar_jogos(jogo_gerado, resultados_antigos):
    acertos = set(jogo_gerado).intersection(set(resultados_antigos))
    return len(acertos)

# Resultados antigos (exemplo)
resultados_antigos = [
    [2, 3, 5, 7, 8, 10, 13, 14, 15, 16, 17, 18, 19, 22, 25],
    [1, 6, 9, 10, 12, 14, 15, 16, 17, 18, 20, 21, 22, 23, 24],
    [1, 7, 9, 10, 11, 12, 13, 14, 17, 18, 19, 21, 23, 24, 25],
    [1, 2, 5, 7, 8, 9, 11, 13, 15, 16, 17, 18, 20, 23, 24],
    [2, 3, 5, 8, 9, 11, 14, 15, 16, 17, 18, 21, 22, 24, 25],
    # Adicione mais resultados antigos conforme necessário
]

# Gerar um novo jogo
novo_jogo = gerar_jogo_mega_sena()
print(f"Novo jogo gerado: {novo_jogo}")

# Comparar com resultados antigos
for idx, resultado in enumerate(resultados_antigos):
    acertos = comparar_jogos(novo_jogo, resultado)
    print(f"Resultado anterior {idx+1}: {resultado}, Acertos: {acertos}")