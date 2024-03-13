# Fazer uma calculadora
from tkinter import *
# Definir uma função

def barra():
    botao = Button(janela, text="☰", command=clique)
    botao.place(relx=0.01, rely=0.01, relwidth=0.23, relheight=0.1)
def caixadeescrever():
    Caixa = Entry(janela)
    Caixa.place(relx = 0.05, rely = 0.15, relwidth = 0.9, relheight=0.18)
def clique():
    Label(janela, text="")
# Inferior
def botao_inferior_trocar_sinal():
    botao = Button(janela, text="+/-", command=clique)
    botao.pack(padx=100, pady=100)
    botao.place(relx = 0.01, rely = 0.89, relwidth = 0.23, relheight=0.1)
    botao['height'] = 3
    botao['width'] = 10
    botao = Entry(janela)

def botao1_inferior_0():
    botao1 = Button(janela, text="0", command=clique)
    botao1.pack(padx=100, pady=100)
    botao1.place(relx = 0.26, rely = 0.89, relwidth = 0.23, relheight=0.1)
    botao1['height'] = 3
    botao1['width'] = 10
    botao1 = Entry(janela)

def botao2_inferior_virgula():
    botao2 = Button(janela, text=",", command=clique)
    botao2.pack(padx=100, pady=100)
    botao2.place(relx = 0.51, rely = 0.89, relwidth = 0.23, relheight=0.1)
    botao2['height'] = 3
    botao2['width'] = 10
    botao2 = Entry(janela)

def botao3_inferior_igual():
    botao3 = Button(janela, text="=", command=clique)
    botao3.pack(padx=100, pady=100)
    botao3.place(relx = 0.76, rely = 0.89, relwidth = 0.23, relheight=0.1)
    botao3['height'] = 3
    botao3['width'] = 10
    botao3 = Entry(janela)


# Coluna 1
def botao4_inferior_alto_1_coluna1():
    botao4 = Button(janela, text="1", command=clique)
    botao4.pack(padx=100, pady=100)
    botao4.place(relx = 0.01, rely = 0.78, relwidth = 0.23, relheight=0.1)
    botao4['height'] = 3
    botao4['width'] = 10
    botao4 = Entry(janela)


def botao5_medio_baixo_4_coluna1():
    botao5 = Button(janela, text="4", command=clique)
    botao5.pack(padx=100, pady=100)
    botao5.place(relx = 0.01, rely = 0.67, relwidth = 0.23, relheight=0.1)
    botao5['height'] = 3
    botao5['width'] = 10
    botao5 = Entry(janela)


def botao6_medio_7_coluna1():
    botao6 = Button(janela, text="7", command=clique)
    botao6.pack(padx=100, pady=100)
    botao6.place(relx = 0.01, rely = 0.56, relwidth = 0.23, relheight=0.1)
    botao6['height'] = 3
    botao6['width'] = 10
    botao6 = Entry(janela)


def botao7_medio_alto_fazer_divisao_1_pelo_numero_coluna1():
    botao7 = Button(janela, text="1/x", command=clique)
    botao7.pack(padx=100, pady=100)
    botao7.place(relx = 0.01, rely = 0.45, relwidth = 0.23, relheight=0.1)
    botao7['height'] = 3
    botao7['width'] = 10
    botao7 = Entry(janela)


def botao8_alto_porcentagem_coluna1():
    botao8 = Button(janela, text="%", command=clique)
    botao8.pack(padx=100, pady=100)
    botao8.place(relx = 0.01, rely = 0.34, relwidth = 0.23, relheight=0.1)
    botao8['height'] = 3
    botao8['width'] = 10
    botao8 = Entry(janela)

# Coluna 2

def botao9_inferior_alto_2_Coluna2():
    botao9 = Button(janela, text="2", command=clique)
    botao9.pack(padx=100, pady=100)
    botao9.place(relx = 0.26, rely = 0.78, relwidth = 0.23, relheight=0.1)
    botao9['height'] = 3
    botao9['width'] = 10
    botao9 = Entry(janela)

def botao10_medio_baixo_5_Coluna2():
    botao10 = Button(janela, text="5", command=clique)
    botao10.pack(padx=100, pady=100)
    botao10.place(relx = 0.26, rely = 0.67, relwidth = 0.23, relheight=0.1)
    botao10['height'] = 3
    botao10['width'] = 10
    botao10 = Entry(janela)

def botao11_medio_8_Coluna2():
    botao11 = Button(janela, text="8", command=clique)
    botao11.pack(padx=100, pady=100)
    botao11.place(relx = 0.26, rely = 0.56, relwidth = 0.23, relheight=0.1)
    botao11['height'] = 3
    botao11['width'] = 10
    botao11 = Entry(janela)

def botao12_medio_alto_elevar_Coluna2():
    botao12 = Button(janela, text="x²", command=clique)
    botao12.pack(padx=100, pady=100)
    botao12.place(relx = 0.26, rely = 0.45, relwidth = 0.23, relheight=0.1)
    botao12['height'] = 3
    botao12['width'] = 10
    botao12 = Entry(janela)

def botao13_alto_APAGAR_Coluna2():
    botao13 = Button(janela, text="0", command=clique)
    botao13.pack(padx=100, pady=100)
    botao13.place(relx = 0.26, rely = 0.34, relwidth = 0.23, relheight=0.1)
    botao13['height'] = 3
    botao13['width'] = 10
    botao13 = Entry(janela)

# Coluna 3

def botao14_inferior_alto_3_coluna3():
    botao14 = Button(janela, text="3", command=clique)
    botao14.pack(padx=100, pady=100)
    botao14.place(relx = 0.51, rely = 0.78, relwidth = 0.23, relheight=0.1)
    botao14['height'] = 3
    botao14['width'] = 10
    botao14 = Entry(janela)

def botao15_medio_baixo_6_coluna3():
    botao15 = Button(janela, text="6", command=clique)
    botao15.pack(padx=100, pady=100)
    botao15.place(relx = 0.51, rely = 0.67, relwidth = 0.23, relheight=0.1)
    botao15['height'] = 3
    botao15['width'] = 10
    botao15 = Entry(janela)

def botao16_medio_9_coluna3():
    botao16 = Button(janela, text="9", command=clique)
    botao16.pack(padx=100, pady=100)
    botao16.place(relx = 0.51, rely = 0.56, relwidth = 0.23, relheight=0.1)
    botao16['height'] = 3
    botao16['width'] = 10
    botao16 = Entry(janela)

def botao17_medio_alto_raiz_quadrada_coluna3():
    botao17 = Button(janela, text="√x", command=clique)
    botao17.pack(padx=100, pady=100)
    botao17.place(relx = 0.51, rely = 0.45, relwidth = 0.23, relheight=0.1)
    botao17['height'] = 3
    botao17['width'] = 10
    botao17 = Entry(janela)

def botao18_alto_Apagar_coluna3():
    botao18 = Button(janela, text="C", command=clique)
    botao18.pack(padx=100, pady=100)
    botao18.place(relx = 0.51, rely = 0.34, relwidth = 0.23, relheight=0.1)
    botao18['height'] = 3
    botao18['width'] = 10
    botao18 = Entry(janela)

# Coluna 4
def botao19_inferior_alto_soma_coluna4():
    botao19 = Button(janela, text="+", command=clique)
    botao19.pack(padx=100, pady=100)
    botao19.place(relx = 0.76, rely = 0.78, relwidth = 0.23, relheight=0.1)
    botao19['height'] = 3
    botao19['width'] = 10
    botao19 = Entry(janela)

def botao20_medio_baixo_subitracao():
    botao20 = Button(janela, text="-", command=clique)
    botao20.pack(padx=100, pady=100)
    botao20.place(relx = 0.76, rely = 0.67, relwidth = 0.23, relheight=0.1)
    botao20['height'] = 3
    botao20['width'] = 10
    botao20 = Entry(janela)

def botao21_medio_mutiplicacao():
    botao21 = Button(janela, text="x", command=clique)
    botao21.pack(padx=100, pady=100)
    botao21.place(relx = 0.76, rely = 0.56, relwidth = 0.23, relheight=0.1)
    botao21['height'] = 3
    botao21['width'] = 10
    botao21 = Entry(janela)

def botao22_medio_alto_divisao():
    botao22 = Button(janela, text="÷", command=clique)
    botao22.pack(padx=100, pady=100)
    botao22.place(relx = 0.76, rely = 0.45, relwidth = 0.23, relheight=0.1)
    botao22['height'] = 3
    botao22['width'] = 10
    botao22 = Entry(janela)

def botao23_alto_apagar():
    botao23 = Button(janela, text="Apagar", command=clique)
    botao23.pack(padx=100, pady=100)
    botao23.place(relx = 0.76, rely = 0.34, relwidth = 0.23, relheight=0.1)
    botao23['height'] = 3
    botao23['width'] = 10
    botao23 = Entry(janela)


# abir janela,
janela = Tk()
janela.title('Calculadora')
janela.geometry("320x480") # -> O primeiro é largura e o segundo é altura

# Comandos na calculadora
barra()
caixadeescrever()
botao_inferior_trocar_sinal()
botao1_inferior_0()
botao2_inferior_virgula()
botao3_inferior_igual()
botao4_inferior_alto_1_coluna1()
botao5_medio_baixo_4_coluna1()
botao6_medio_7_coluna1()
botao7_medio_alto_fazer_divisao_1_pelo_numero_coluna1()
botao8_alto_porcentagem_coluna1()
botao9_inferior_alto_2_Coluna2()
botao10_medio_baixo_5_Coluna2()
botao11_medio_8_Coluna2()
botao12_medio_alto_elevar_Coluna2()
botao13_alto_APAGAR_Coluna2()
botao14_inferior_alto_3_coluna3()
botao15_medio_baixo_6_coluna3()
botao16_medio_9_coluna3()
botao17_medio_alto_raiz_quadrada_coluna3()
botao18_alto_Apagar_coluna3()
botao19_inferior_alto_soma_coluna4()
botao20_medio_baixo_subitracao()
botao21_medio_mutiplicacao()
botao22_medio_alto_divisao()
botao23_alto_apagar()
janela.mainloop()