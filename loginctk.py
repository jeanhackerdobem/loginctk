import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

janela = customtkinter.CTk()
janela.geometry('200x260')

def clique():
    print("Logando...")


texto = customtkinter.CTkLabel(janela, text='Login')
texto.pack(padx=10, pady=10)


email = customtkinter.CTkEntry(janela, placeholder_text='Seu e-mail')
email.pack(padx=10, pady=10)

senha = customtkinter.CTkEntry(janela, placeholder_text='Sua senha', show='*')
senha.pack(padx=10, pady=10)

checkbox = customtkinter.CTkCheckBox(janela, text='Lembrar Login')
checkbox.pack(padx=10, pady=10)

botao = customtkinter.CTkButton(janela, text='Logar', command=clique)
botao.pack(padx=10, pady=10)

janela.mainloop()
