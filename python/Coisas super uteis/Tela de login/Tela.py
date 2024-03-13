# from tkinter import *
#
# janela = Tk()
# janela.geometry("500x300")
#
# def clique(): # -> Definir a fnção do clique e dar uma utilidade
#     print("Fazer login")
#
# texto = Label(text="Fazer login")
# texto.pack(padx=10, pady=10) # -> Espaço de tudo para o texto
#2
# botao = Button(text="Login", command=clique())
# botao.pack(padx=10, pady=10)
#
# janela.mainloop()

import customtkinter

janela = customtkinter.CTk()
janela.geometry("500x300")

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")
def clique(): # -> Definir a fnção do clique e dar uma utilidade
   print("Fazer login")

texto = customtkinter.CTkLabel(janela, text="Fazer Login")
texto.pack(padx=10, pady=10)

email = customtkinter.CTkEntry(janela, placeholder_text="Seu e-mail")
email.pack(padx=10, pady=10)

senha = customtkinter.CTkEntry(janela, placeholder_text="Sua senha", show="*")
senha.pack(padx=10, pady=10)

checkbox = customtkinter.CTkCheckBox(janela, text="lembrar login", command=clique())
checkbox.pack(padx=10, pady=10)

botao = customtkinter.CTkButton(janela, text="Login", command=clique)
botao.pack(padx=10, pady=10)


janela.mainloop()

