import tkinter as tk
from tkinter import messagebox
from datetime import datetime, timedelta

def calcular_jornada():
    try:
        entrada = entry_entrada.get()
        saida = entry_saida.get()
        
        # Convertendo as entradas de string para datetime
        hora_entrada = datetime.strptime(entrada, "%H:%M")
        hora_saida = datetime.strptime(saida, "%H:%M")
        
        # Verificando se a hora de saída é maior que a hora de entrada
        if hora_saida <= hora_entrada:
            messagebox.showerror("Erro", "A hora de saída deve ser maior que a hora de entrada.")
            return
        
        # Calculando a jornada e descontando 1 hora
        jornada = (hora_saida - hora_entrada - timedelta(hours=1)).seconds / 3600  # Convertendo para horas
        label_jornada_resultado.config(text=f"Jornada: {jornada:.2f} horas")
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira o horário no formato HH:MM.")

def salvar_dados():
    data = entry_data.get()
    frota = entry_frota.get()
    entrada = entry_entrada.get()
    saida = entry_saida.get()
    
    if not frota or not entrada or not saida or not data:
        messagebox.showerror("Erro", "Todos os campos devem ser preenchidos.")
        return

    with open("dados.txt", "a") as arquivo:
        arquivo.write(f"Data: {data}, Frota: {frota}, Entrada: {entrada}, Saída: {saida}\n")
    
    messagebox.showinfo("Sucesso", "Dados salvos com sucesso!")
    limpar_dados()  # Limpa os dados após salvar

def limpar_dados():
    entry_data.delete(0, tk.END)
    entry_frota.delete(0, tk.END)
    entry_entrada.delete(0, tk.END)
    entry_saida.delete(0, tk.END)
    label_jornada_resultado.config(text="Jornada: ")

def fechar_formulario():
    janela.destroy()  # Fecha a janela

# Criar a janela principal
janela = tk.Tk()
janela.title("Formulário de Cálculo de Jornada")

# Criar os rótulos e entradas usando grid
label_data = tk.Label(janela, text="Data (DD/MM/AAAA):")
label_data.grid(row=0, column=0, padx=10, pady=5)

entry_data = tk.Entry(janela)
entry_data.grid(row=0, column=1, padx=5, pady=5)

label_frota = tk.Label(janela, text="Frota:")
label_frota.grid(row=1, column=0, padx=10, pady=5)

entry_frota = tk.Entry(janela)
entry_frota.grid(row=1, column=1, padx=5, pady=5)

label_entrada = tk.Label(janela, text="Entrada (HH:MM):")
label_entrada.grid(row=2, column=0, padx=5, pady=5)

entry_entrada = tk.Entry(janela)
entry_entrada.grid(row=2, column=1, padx=5, pady=5)

label_saida = tk.Label(janela, text="Saída (HH:MM):")
label_saida.grid(row=3, column=0, padx=5, pady=5)

entry_saida = tk.Entry(janela)
entry_saida.grid(row=3, column=1, padx=5, pady=5)

# Rótulo para mostrar o resultado da jornada
label_jornada_resultado = tk.Label(janela, text="Jornada: ")
label_jornada_resultado.grid(row=5, columnspan=2)

# Botão para calcular a jornada
botao_calcular = tk.Button(janela, text="Calcular Jornada", command=calcular_jornada)
botao_calcular.grid(row=4, columnspan=2, pady=5)

# Botão para salvar os dados
botao_salvar = tk.Button(janela, text="Salvar Dados", command=salvar_dados)
botao_salvar.grid(row=6, columnspan=2, pady=5)

# Botão para limpar os dados
botao_limpar = tk.Button(janela, text="Limpar Dados", command=limpar_dados)
botao_limpar.grid(row=7, columnspan=2, pady=5)

# Botão para fechar o formulário
botao_fechar = tk.Button(janela, text="Fechar", command=fechar_formulario)
botao_fechar.grid(row=7, columnspan=2, pady=5)