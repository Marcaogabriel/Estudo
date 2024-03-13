import random

# Função para gerar um jogo aleatório da Mega Sena
def gerar_jogo_mega_sena():
    return sorted(random.sample(range(1, 31), 7))

# Função para comparar jogos com resultados antigos
def comparar_jogos(jogo_gerado, resultados_antigos):
    acertos = set(jogo_gerado).intersection(set(resultados_antigos))
    return len(acertos)

# Resultados antigos (exemplo)
resultados_antigos = [
    [1, 2, 8, 9, 14, 16, 29],
    [2, 10, 11, 13, 16, 19, 27],
    [7, 11, 17, 19, 25, 27, 28],
    [1, 9 ,13 ,25 ,26 ,27 ,29],
    [4, 6, 19, 22, 23, 24, 26],
    # Adicione mais resultados antigos conforme necessário
]

# Gerar um novo jogo
novo_jogo = gerar_jogo_mega_sena()
print(f"Novo jogo gerado: {novo_jogo}")

# Comparar com resultados antigos
for idx, resultado in enumerate(resultados_antigos):
    acertos = comparar_jogos(novo_jogo, resultado)
    print(f"Resultado anterior {idx+1}: {resultado}, Acertos: {acertos}")