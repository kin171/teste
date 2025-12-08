import tkinter as tk
from tkinter import messagebox
import re

def verificar_dados():
    nome = entry_nome.get()
    email = entry_email.get()
    

    if not nome:
        messagebox.showerror("Erro", "O nome não pode estar vazio.")
        return

    if not verificar_email(email):
        messagebox.showerror("Erro", "O e-mail inserido não é válido.")
        return

    salvar_dados(nome, email)
    messagebox.showinfo("Sucesso", "Dados verificados e salvos com sucesso!")
    limpar_dados()  # Limpa os dados após salvar

def verificar_email(email):
    # Usando uma expressão regular simples para verificar o formato do e-mail
    regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(regex, email) is not None

def salvar_dados(nome, email):
    with open("dados.txt", "a") as arquivo:
        arquivo.write(f"Nome: {nome}, E-mail: {email}\n")

def limpar_dados():
    entry_nome.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    entry_nome.focus_set()  # Focar novamente no campo Nome

def fechar_formulario():
    janela.destroy()  # Fecha a janela

def proximo_campo(event):
    # Muda o foco para o próximo campo ou verifica os dados se Enter for pressionado no último campo
    if event.widget == entry_nome:
        entry_email.focus_set()
    elif event.widget == entry_email:
        verificar_dados()  # Verifica os dados ao pressionar Enter no último campo

# Criar a janela principal
janela = tk.Tk()
janela.title("Formulário de Verificação de Dados")

# Criar os rótulos e entradas usando grid
label_nome = tk.Label(janela, text="Nome:")
label_nome.grid(row=0, column=0, padx=10, pady=5)

entry_nome = tk.Entry(janela)
entry_nome.grid(row=0, column=1, padx=5, pady=5)
entry_nome.bind("<Return>", proximo_campo)  # Bind Enter para o campo Nome

label_email = tk.Label(janela, text="E-mail:")
label_email.grid(row=1, column=0, padx=5, pady=5)

entry_email = tk.Entry(janela)
entry_email.grid(row=1, column=1, padx=5, pady=5)
entry_email.bind("<Return>", proximo_campo)  # Bind Enter para o campo E-mail

# Criar o botão de verificação
botao_verificar = tk.Button(janela, text="Salvar ", command=verificar_dados)
botao_verificar.grid(row=2, column=0, columnspan=2, pady=5)

# Criar o botão de limpar
botao_limpar = tk.Button(janela, text="Limpar Dados", command=limpar_dados)
botao_limpar.grid(row=2, column=2, columnspan=2, pady=5)

# Criar o botão de fechar
botao_fechar = tk.Button(janela, text="Fechar", command=fechar_formulario)
botao_fechar.grid(row=2, column=4, columnspan=2, pady=5)

# Iniciar o loop principal da interface gráfica
janela.mainloop()