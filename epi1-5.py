import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import pandas as pd
from datetime import datetime
import os

# Variáveis globais para DataFrames
df_estoque = pd.DataFrame()
df_funcionarios = pd.DataFrame()
df_historico = pd.DataFrame()
historico_file = None  # Arquivo de histórico carregado

# Listas para widgets de EPI
epi_combos = []
preco_entries = []
estoque_entries = []
ultima_entries = []
qtd_combos = []

# Função para carregar dados do Excel
def carregar_dados():
    global df_estoque, df_funcionarios, df_historico, historico_file
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

        # Selecionar arquivo de histórico (opcional, mas recomendado)
        hist_file = filedialog.askopenfilename(title="Selecione o arquivo de Histórico de Solicitações (opcional)", filetypes=[("Excel files", "*.xlsx")])
        if hist_file:
            df_historico = pd.read_excel(hist_file)
            historico_file = hist_file
        else:
            df_historico = pd.DataFrame(columns=['CS', 'EPI', 'Data'])  # DataFrame vazio se não carregado
            historico_file = None

        # Preencher comboboxes de EPI com os dados carregados
        epi_values = df_estoque['Descrição_APP'].tolist() if 'Descrição_APP' in df_estoque.columns else []
        for combo in epi_combos:
            combo['values'] = epi_values

        messagebox.showinfo("Sucesso", "Dados carregados com sucesso!")
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao carregar dados: {str(e)}")

# Função para filtrar EPIs baseado no texto digitado em tempo real
def filtrar_epis(event, epi_combo):
    typed = epi_combo.get()
    if typed == '':
        epi_combo['values'] = df_estoque['Descrição_APP'].tolist() if 'Descrição_APP' in df_estoque.columns else []
    else:
        filtered = [epi for epi in df_estoque['Descrição_APP'].tolist() if typed.lower() in epi.lower()]
        epi_combo['values'] = filtered
    # Removido: abertura automática do dropdown para não interromper a digitação

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

# Função para atualizar preço, estoque e última vez baseado na seleção de EPI
def atualizar_preco_estoque(epi_combo, preco_entry, estoque_entry, ultima_entry):
    selected = epi_combo.get()
    cs = cs_entry.get()
    if selected and cs:
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
            
            # Buscar última vez no histórico (case-insensitive)
            if not df_historico.empty:
                hist = df_historico[(df_historico['CS'].astype(str).str.lower() == cs.lower()) & (df_historico['EPI'].str.lower() == selected.lower())]
                if not hist.empty:
                    ultima_data = hist['Data'].max()
                    ultima_entry.config(state='normal')
                    ultima_entry.delete(0, tk.END)
                    ultima_entry.insert(0, ultima_data)
                    ultima_entry.config(state='disabled')
                else:
                    ultima_entry.config(state='normal')
                    ultima_entry.delete(0, tk.END)
                    ultima_entry.insert(0, "Nunca solicitado")
                    ultima_entry.config(state='disabled')
            else:
                ultima_entry.config(state='normal')
                ultima_entry.delete(0, tk.END)
                ultima_entry.insert(0, "Histórico não carregado")
                ultima_entry.config(state='disabled')
        else:
            preco_entry.config(state='normal')
            preco_entry.delete(0, tk.END)
            preco_entry.config(state='disabled')
            estoque_entry.config(state='normal')
            estoque_entry.delete(0, tk.END)
            estoque_entry.config(state='disabled')
            ultima_entry.config(state='normal')
            ultima_entry.delete(0, tk.END)
            ultima_entry.config(state='disabled')
    else:
        preco_entry.config(state='normal')
        preco_entry.delete(0, tk.END)
        preco_entry.config(state='disabled')
        estoque_entry.config(state='normal')
        estoque_entry.delete(0, tk.END)
        estoque_entry.config(state='disabled')
        ultima_entry.config(state='normal')
        ultima_entry.delete(0, tk.END)
        ultima_entry.config(state='disabled')

# Função para limpar seleção de EPI
def limpar_epi(epi_combo, qtd_combo, preco_entry, estoque_entry, ultima_entry):
    epi_combo.set('')
    qtd_combo.set('')
    preco_entry.config(state='normal')
    preco_entry.delete(0, tk.END)
    preco_entry.config(state='disabled')
    estoque_entry.config(state='normal')
    estoque_entry.delete(0, tk.END)
    estoque_entry.config(state='disabled')
    ultima_entry.config(state='normal')
    ultima_entry.delete(0, tk.END)
    ultima_entry.config(state='disabled')

# Função para enviar solicitação
def enviar_solicitacao():
    global historico_file, df_historico  # Declarar globais no início da função
    cs = cs_entry.get()
    nome = nome_entry.get()
    custo = custo_entry.get()
    data = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    # Validações básicas
    if not cs:
        messagebox.showerror("Erro", "Preencha o CS.")
        return
    if not cs.isdigit() or int(cs) <= 0:
        messagebox.showerror("Erro", "CS deve ser um número positivo.")
        return

    # Coletar EPIs selecionados
    epis = []
    for idx in range(len(epi_combos)):
        epi = epi_combos[idx].get()
        qtd = qtd_combos[idx].get()
        preco = preco_entries[idx].get()
        estoque = estoque_entries[idx].get()
        if epi and qtd:
            epis.append({
                'EPI': epi,
                'Quantidade': qtd,
                'Preco': preco,
                'Estoque': estoque
            })

    if not epis:
        messagebox.showerror("Erro", "Selecione pelo menos um EPI com quantidade.")
        return

    # Salvar solicitação no arquivo de histórico (adicionando linhas)
    try:
        # Criar DataFrame em formato longo (uma linha por EPI)
        linhas = []
        for epi in epis:
            linhas.append({
                'CS': cs,
                'Nome': nome,
                'Centro de Custo': custo,
                'Data': data,
                'EPI': epi['EPI'],
                'Quantidade': epi['Quantidade'],
                'Preco': epi['Preco'],
                'Estoque': epi['Estoque']
            })

        df_nova_solicitacao = pd.DataFrame(linhas)

        # Se já existe arquivo de histórico carregado, adicionar as novas linhas
        if historico_file and os.path.exists(historico_file):
            # Carregar o histórico existente
            df_historico_existente = pd.read_excel(historico_file)
            # Adicionar as novas solicitações
            df_historico_atualizado = pd.concat([df_historico_existente, df_nova_solicitacao], ignore_index=True)
            # Salvar de volta no arquivo de histórico
            df_historico_atualizado.to_excel(historico_file, index=False)
            messagebox.showinfo("Sucesso", f"Solicitação adicionada ao histórico: {historico_file}")
        else:
            # Se não há histórico carregado, criar novo arquivo de histórico
            novo_historico_file = filedialog.asksaveasfilename(title="Criar Arquivo de Histórico", defaultextension=".xlsx", filetypes=[("Excel files", "*.xlsx")])
            if not novo_historico_file:
                messagebox.showwarning("Aviso", "Salvamento cancelado pelo usuário.")
                return
            df_nova_solicitacao.to_excel(novo_historico_file, index=False)
            # Atualizar variável global
            historico_file = novo_historico_file
            df_historico = df_nova_solicitacao
            messagebox.showinfo("Sucesso", f"Novo arquivo de histórico criado: {novo_historico_file}")

    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao salvar solicitação: {str(e)}")

    # Limpar formulário
    cs_entry.delete(0, tk.END)
    preencher_nome_custo()
    for idx in range(len(epi_combos)):
        limpar_epi(epi_combos[idx], qtd_combos[idx], preco_entries[idx], estoque_entries[idx], ultima_entries[idx])
        atualizar_preco_estoque(epi_combos[idx], preco_entries[idx], estoque_entries[idx], ultima_entries[idx])

# Criar janela principal
root = tk.Tk()
root.title("Solicitação de EPI")
root.geometry("1600x1200")  # Ajustado para 15 EPIs

# Menu para carregar dados
menubar = tk.Menu(root)
filemenu = tk.Menu(menubar, tearoff=0)
filemenu.add_command(label="Carregar Dados", command=carregar_dados)
menubar.add_cascade(label="Arquivo", menu=filemenu)
root.config(menu=menubar)

# Frame principal com scrollbar
canvas = tk.Canvas(root)
scrollbar = ttk.Scrollbar(root, orient="vertical", command=canvas.yview)
scrollable_frame = ttk.Frame(canvas)

scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(
        scrollregion=canvas.bbox("all")
    )
)

canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)

canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

# CS
ttk.Label(scrollable_frame, text="CS:").grid(row=0, column=0, sticky=tk.W)
cs_entry = ttk.Entry(scrollable_frame)
cs_entry.grid(row=0, column=1, sticky=(tk.W, tk.E))
cs_entry.bind("<KeyRelease>", preencher_nome_custo)

# Nome
ttk.Label(scrollable_frame, text="Nome:").grid(row=1, column=0, sticky=tk.W)
nome_entry = ttk.Entry(scrollable_frame, state='disabled')
nome_entry.grid(row=1, column=1, sticky=(tk.W, tk.E))

# Centro de Custo
ttk.Label(scrollable_frame, text="Centro de Custo:").grid(row=2, column=0, sticky=tk.W)
custo_entry = ttk.Entry(scrollable_frame, state='disabled')
custo_entry.grid(row=2, column=1, sticky=(tk.W, tk.E))

# Data (auto)
ttk.Label(scrollable_frame, text="Data:").grid(row=3, column=0, sticky=tk.W)
data_label = ttk.Label(scrollable_frame, text=datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
data_label.grid(row=3, column=1, sticky=tk.W)

# EPIs (15)
for i in range(15):  # 15 EPIs
    ttk.Label(scrollable_frame, text=f"EPI {i+1}:").grid(row=4+i, column=0, sticky=tk.W)
    epi_combo = ttk.Combobox(scrollable_frame, state='normal', width=60)
    epi_combo.grid(row=4+i, column=1, sticky=(tk.W, tk.E))
    epi_combo.bind("<KeyRelease>", lambda e, combo=epi_combo: filtrar_epis(e, combo))
    epi_combo.bind("<<ComboboxSelected>>", lambda e, idx=i: atualizar_preco_estoque(epi_combos[idx], preco_entries[idx], estoque_entries[idx], ultima_entries[idx]))
    epi_combos.append(epi_combo)
    
    ttk.Label(scrollable_frame, text="Preço:").grid(row=4+i, column=2, sticky=tk.W)
    preco_entry = ttk.Entry(scrollable_frame, state='disabled', width=15)
    preco_entry.grid(row=4+i, column=3, sticky=(tk.W, tk.E))
    preco_entries.append(preco_entry)
    
    ttk.Label(scrollable_frame, text="Estoque:").grid(row=4+i, column=4, sticky=tk.W)
    estoque_entry = ttk.Entry(scrollable_frame, state='disabled', width=15)
    estoque_entry.grid(row=4+i, column=5, sticky=(tk.W, tk.E))
    estoque_entries.append(estoque_entry)
    
    ttk.Label(scrollable_frame, text="Última vez:").grid(row=4+i, column=6, sticky=tk.W)
    ultima_entry = ttk.Entry(scrollable_frame, state='disabled', width=20)
    ultima_entry.grid(row=4+i, column=7, sticky=(tk.W, tk.E))
    ultima_entries.append(ultima_entry)
    
    ttk.Label(scrollable_frame, text="Quantidade:").grid(row=4+i, column=8, sticky=tk.W)
    qtd_combo = ttk.Combobox(scrollable_frame, values=["1", "2"], state='readonly', width=10)
    qtd_combo.grid(row=4+i, column=9, sticky=(tk.W, tk.E))
    qtd_combos.append(qtd_combo)
    
    ttk.Button(scrollable_frame, text="Limpar", command=lambda idx=i: limpar_epi(epi_combos[idx], qtd_combos[idx], preco_entries[idx], estoque_entries[idx], ultima_entries[idx])).grid(row=4+i, column=10)

# Botão Enviar
ttk.Button(scrollable_frame, text="Enviar", command=enviar_solicitacao).grid(row=20, column=0, columnspan=11, pady=10)

# Inicializar variáveis globais
df_estoque = pd.DataFrame()
df_funcionarios = pd.DataFrame()
df_historico = pd.DataFrame()

root.mainloop()