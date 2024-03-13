import requests
from tkinter import *

# PEGAR COTAÇÃO
def pegar_cotacoes():
    requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")

    requisicao_dic = requisicao.json()

    cotacao_dolar = requisicao_dic['USDBRL']['bid']
    cotacao_euro = requisicao_dic['EURBRL']['bid']
    cotacao_btc = requisicao_dic['BTCBRL']['bid']

# Esse texto vai ser igual a cotações para aparecer na janela
    texto = f'''
    Dólar: {cotacao_dolar}
    Euro: {cotacao_euro}
    BTC: {cotacao_btc}'''

    texto_cotacoes["text"] = texto


# passo 1 criar sua janela principal

janela = Tk()

# passo 1.1 fazer titulo da janela

janela.title("Cotação das Moedas")

# passo 1.2 fazer parte escrita da janela

texto_orientacao = Label(janela, text="Clique no botão para ver as cotações das moedas")

# Posição 1.2.1 dos textos column = Coluna  row = Linha OPICIONAL

texto_orientacao.grid(column=0, row=0, padx=15, pady=15 )

# passo 1.3 Colocando botão e organizando ele

botao = Button(janela, text="Buscar cotações Dólar/Euro/BTC", command=pegar_cotacoes)
botao.grid(column=0, row=1)

# passo 1.4 quando clicar no botão saber a ação

texto_cotacoes = Label(janela, text="")
texto_cotacoes.grid(column=0, row=2)



# Manter a Janela aberta até vc querer fechar
janela.mainloop()

#janela.geometry("")Dentro é só colocar quanto por quanto quer o tamanho da imagem Ex: 300x300