produtos = [
    {"nome": "Ipad", "preço": 12000, "Quantidade" :500},
    {"nome": "Iphone", "preço": 8000, "Quantidade" :1000},
    {"nome": "Airpod", "preço": 3000, "Quantidade" :800},
    {"nome": "AppleWatch", "preço": 4000, "Quantidade" :300},
    {"nome": "MacBook", "preço": 15000, "Quantidade" :300},
]

import pandas as pd

tabela = pd.DataFrame(produtos)
tabela["Faturamento"] = (tabela["preço"] * tabela["Quantidade"])


# CRIAR GRÁFICOS
import matplotlib.pyplot as plt

# Dados escritos
dados = tabela["nome"]
valores = tabela["Faturamento"]

# Criação do gráfico de barras
plt.bar(dados, valores)

# Adicionando rótulos
plt.xlabel('Dados')
plt.ylabel('Valores')
plt.title('Gráfico de Faturamento')

# Exibindo o gráfico
plt.show()
print(tabela)
