import pandas as pd

# Passo 1 - Importar base de dados
tabela = pd.read_csv("ClientesBanco.csv", encoding="latin1")

# Passo 2 - Visualizar e tratar a base de dados
tabela = tabela.drop("CLIENTNUM", axis=1)
# Passo 3 - Ver a base de dados
# Passo 4 - construir uma analise para o motivo do cancelamento
# Geral - Identificar qual o motivo ou os principais motivos do clientes estarem cancelando o cartão de crédito

print(tabela)