import tkinter as tk

def adicionar_caractere(caractere):
    entrada.insert(tk.END, caractere)

def calcular():
    try:
        resultado = eval(entrada.get())
        entrada.delete(0, tk.END)
        entrada.insert(tk.END, str(resultado))
    except Exception:
        entrada.delete(0, tk.END)
        entrada.insert(tk.END, "Erro")

def limpar():
    entrada.delete(0, tk.END)

# Cria a janela da calculadora
janela = tk.Tk()
janela.title("Calculadora")

# Cria a entrada de texto
entrada = tk.Entry(janela, width=25)
entrada.grid(row=0, column=0, columnspan=4)

# Cria os botões numéricos e de operações
botoes = [
    ("7", 1, 0),
    ("8", 1, 1),
    ("9", 1, 2),
    ("/", 1, 3),
    ("4", 2, 0),
    ("5", 2, 1),
    ("6", 2, 2),
    ("*", 2, 3),
    ("1", 3, 0),
    ("2", 3, 1),
    ("3", 3, 2),
    ("-", 3, 3),
    ("0", 4, 0),
    (".", 4, 1),
    ("=", 4, 2),
    ("+", 4, 3)
]

for botao in botoes:
    texto, linha, coluna = botao
    tk.Button(janela, text=texto, width=5, command=lambda texto=texto: adicionar_caractere(texto)).grid(row=linha, column=coluna)

# Define a função de limpar a entrada
tk.Button(janela, text="Limpar", width=15, command=limpar).grid(row=5, column=0, columnspan=4)
calcular()
# Inicia o loop principal da janela
janela.mainloop()



