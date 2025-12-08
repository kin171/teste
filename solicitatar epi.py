import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import pandas as pd
from datetime import datetime
import os

# Função para carregar dados do Excel
def carregar_dados():
    global df_estoque, df_funcionarios
    try:
        # Selecionar arquivo de estoque
        estoque_file = filedialog.askopenfilename(title="Selecione o arquivo de Estoque", filetypes=[("Excel files", "*.xlsx")])
        if not estoque_file:
            return
        df_estoque = pd.read_excel(estoque_file)
        
        # Selecionar arquivo de funcionários
        func_file = filedialog.askopenfilename(title="Selecione o arquivo de Funcionários", filetypes=[("Excel files", "*.xlsx")])
        if not func_file:
            return
        df_funcionarios = pd.read_excel(func_file)
        
        messagebox.showinfo("Sucesso", "Dados carregados com sucesso!")
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao carregar dados: {str(e)}")

# Função para preencher nome e centro de custo baseado no CS
def preencher_nome_custo(event=None):
    cs = cs_entry.get()
    if cs and cs.isdigit():
        cs = int(cs)
        func = df_funcionarios[df_funcionarios['Title'] == cs]
        if not func.empty:
            nome_entry.config(state='normal')
            nome_entry.delete(0, tk.END)
            nome_entry.insert(0, func['NOME'].values[0])
            nome_entry.config(state='disabled')
            
            custo_entry.config(state='normal')
            custo_entry.delete(0, tk.END)
            custo_entry.insert(0, func['Custo'].values[0])
            custo_entry.config(state='disabled')
        else:
            nome_entry.config(state='normal')
            nome_entry.delete(0, tk.END)
            nome_entry.config(state='disabled')
            custo_entry.config(state='normal')
            custo_entry.delete(0, tk.END)
            custo_entry.config(state='disabled')
    else:
        nome_entry.config(state='normal')
        nome_entry.delete(0, tk.END)
        nome_entry.config(state='disabled')
        custo_entry.config(state='normal')
        custo_entry.delete(0, tk.END)
        custo_entry.config(state='disabled')

# Função para atualizar preço e estoque baseado na seleção de EPI
def atualizar_preco_estoque(epi_combo, preco_entry, estoque_entry):
    selected = epi_combo.get()
    if selected:
        item = df_estoque[df_estoque['Descrição_APP'] == selected]
        if not item.empty:
            preco_entry.config(state='normal')
            preco_entry.delete(0, tk.END)
            preco_entry.insert(0, item['Preco'].values[0])
            preco_entry.config(state='disabled')
            
            estoque_entry.config(state='normal')
            estoque_entry.delete(0, tk.END)
            estoque_entry.insert(0, item['Estoque'].values[0])
            estoque_entry.config(state='disabled')
        else:
            preco_entry.config(state='normal')
            preco_entry.delete(0, tk.END)
            preco_entry.config(state='disabled')
            estoque_entry.config(state='normal')
            estoque_entry.delete(0, tk.END)
            estoque_entry.config(state='disabled')

# Função para limpar seleção de EPI
def limpar_epi(epi_combo, qtd_combo):
    epi_combo.set('')
    qtd_combo.set('')

# Função para enviar solicitação
def enviar_solicitacao():
    cs = cs_entry.get()
    nome = nome_entry.get()
    custo = custo_entry.get()
    data = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    
    # Coletar EPIs selecionados
    epis = []
    for i in range(1, 6):  # Limitando a 5 EPIs para simplicidade
        epi = globals()[f'epi{i}_combo'].get()
        qtd = globals()[f'qtd{i}_combo'].get()
        preco = globals()[f'preco{i}_entry'].get()
        estoque = globals()[f'estoque{i}_entry'].get()
        if epi and qtd:
            epis.append({
                'EPI': epi,
                'Quantidade': qtd,
                'Preco': preco,
                'Estoque': estoque
            })
    
    if not cs or not epis:
        messagebox.showerror("Erro", "Preencha pelo menos CS e selecione um EPI com quantidade.")
        return
    
    # Salvar em Excel
    saida_file = filedialog.asksaveasfilename(title="Salvar Solicitação", defaultextension=".xlsx", filetypes=[("Excel files", "*.xlsx")])
    if not saida_file:
        return
    
    dados = {
        'CS': [cs],
        'Nome': [nome],
        'Centro de Custo': [custo],
        'Data': [data]
    }
    for epi in epis:
        dados[f"EPI_{epi['EPI']}"] = [epi['EPI']]
        dados[f"Qtd_{epi['EPI']}"] = [epi['Quantidade']]
        dados[f"Preco_{epi['EPI']}"] = [epi['Preco']]
        dados[f"Estoque_{epi['EPI']}"] = [epi['Estoque']]
    
    df_saida = pd.DataFrame(dados)
    df_saida.to_excel(saida_file, index=False)
    
    messagebox.showinfo("Sucesso", "Solicitação enviada com sucesso!")
    
    # Limpar formulário
    cs_entry.delete(0, tk.END)
    preencher_nome_custo()
    for i in range(1, 6):
        limpar_epi(globals()[f'epi{i}_combo'], globals()[f'qtd{i}_combo'])
        atualizar_preco_estoque(globals()[f'epi{i}_combo'], globals()[f'preco{i}_entry'], globals()[f'estoque{i}_entry'])

# Criar janela principal
root = tk.Tk()
root.title("Solicitação de EPI")
root.geometry("800x600")

# Menu para carregar dados
menubar = tk.Menu(root)
filemenu = tk.Menu(menubar, tearoff=0)
filemenu.add_command(label="Carregar Dados", command=carregar_dados)
menubar.add_cascade(label="Arquivo", menu=filemenu)
root.config(menu=menubar)

# Frame principal
frame = ttk.Frame(root, padding="10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# CS
ttk.Label(frame, text="CS:").grid(row=0, column=0, sticky=tk.W)
cs_entry = ttk.Entry(frame)
cs_entry.grid(row=0, column=1, sticky=(tk.W, tk.E))
cs_entry.bind("<KeyRelease>", preencher_nome_custo)

# Nome
ttk.Label(frame, text="Nome:").grid(row=1, column=0, sticky=tk.W)
nome_entry = ttk.Entry(frame, state='disabled')
nome_entry.grid(row=1, column=1, sticky=(tk.W, tk.E))

# Centro de Custo
ttk.Label(frame, text="Centro de Custo:").grid(row=2, column=0, sticky=tk.W)
custo_entry = ttk.Entry(frame, state='disabled')
custo_entry.grid(row=2, column=1, sticky=(tk.W, tk.E))

# Data (auto)
ttk.Label(frame, text="Data:").grid(row=3, column=0, sticky=tk.W)
data_label = ttk.Label(frame, text=datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
data_label.grid(row=3, column=1, sticky=tk.W)

# EPIs (limitando a 5 para exemplo)
for i in range(1, 6):
    ttk.Label(frame, text=f"EPI {i}:").grid(row=4+i-1, column=0, sticky=tk.W)
    globals()[f'epi{i}_combo'] = ttk.Combobox(frame, state='readonly')
    globals()[f'epi{i}_combo'].grid(row=4+i-1, column=1, sticky=(tk.W, tk.E))
    globals()[f'epi{i}_combo'].bind("<<ComboboxSelected>>", lambda e, i=i: atualizar_preco_estoque(globals()[f'epi{i}_combo'], globals()[f'preco{i}_entry'], globals()[f'estoque{i}_entry']))
    
    ttk.Label(frame, text="Preço:").grid(row=4+i-1, column=2, sticky=tk.W)
    globals()[f'preco{i}_entry'] = ttk.Entry(frame, state='disabled')
    globals()[f'preco{i}_entry'].grid(row=4+i-1, column=3, sticky=(tk.W, tk.E))
    
    ttk.Label(frame, text="Estoque:").grid(row=4+i-1, column=4, sticky=tk.W)
    globals()[f'estoque{i}_entry'] = ttk.Entry(frame, state='disabled')
    globals()[f'estoque{i}_entry'].grid(row=4+i-1, column=5, sticky=(tk.W, tk.E))
    
    ttk.Label(frame, text="Quantidade:").grid(row=4+i-1, column=6, sticky=tk.W)
    globals()[f'qtd{i}_combo'] = ttk.Combobox(frame, values=["1", "2"], state='readonly')
    globals()[f'qtd{i}_combo'].grid(row=4+i-1, column=7, sticky=(tk.W, tk.E))
    
    ttk.Button(frame, text="Limpar", command=lambda i=i: limpar_epi(globals()[f'epi{i}_combo'], globals()[f'qtd{i}_combo'])).grid(row=4+i-1, column=8)

# Botão Enviar
ttk.Button(frame, text="Enviar", command=enviar_solicitacao).grid(row=10, column=0, columnspan=9, pady=10)

# Inicializar variáveis globais
df_estoque = pd.DataFrame()
df_funcionarios = pd.DataFrame()

root.mainloop()
