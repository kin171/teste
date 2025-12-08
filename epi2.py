import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import pandas as pd
from datetime import datetime
import os
import openpyxl  # Para anexar ao Excel

# Função para carregar dados do Excel (local ou SharePoint)
def carregar_dados():
    global df_estoque, df_funcionarios, df_historico, hist_file_path
    try:
        # Opção para carregar de SharePoint ou local
        sharepoint = messagebox.askyesno("Carregar de SharePoint", "Deseja carregar arquivos do SharePoint? (Caso contrário, selecione arquivos locais)")
        if sharepoint:
            # Placeholder: Integração com SharePoint requer bibliotecas como office365-rest-python-client
            messagebox.showerror("Erro", "Integração com SharePoint não implementada. Use arquivos locais.")
            return
        
        # Carregar localmente
        estoque_file = filedialog.askopenfilename(title="Selecione o arquivo de Estoque", filetypes=[("Excel files", "*.xlsx")])
        if not estoque_file:
            return
        df_estoque = pd.read_excel(estoque_file)
        
        func_file = filedialog.askopenfilename(title="Selecione o arquivo de Funcionários", filetypes=[("Excel files", "*.xlsx")])
        if not func_file:
            return
        df_funcionarios = pd.read_excel(func_file)
        
        hist_file = filedialog.askopenfilename(title="Selecione o arquivo de Histórico de Solicitações (EPI)", filetypes=[("Excel files", "*.xlsx")])
        hist_file_path = "historico_solicitacoes.xlsx"
        if hist_file:
            df_historico = pd.read_excel(hist_file)
            hist_file_path = hist_file
        else:
            if os.path.exists(hist_file_path):
                df_historico = pd.read_excel(hist_file_path)
            else:
                df_historico = pd.DataFrame(columns=['CS', 'Nome', 'Centro de Custo', 'Data', 'EPI', 'Quantidade', 'Preco', 'Estoque'])
        
        # Verificar colunas essenciais
        required_cols_estoque = ['Descrição_APP', 'Preco', 'Estoque']
        if not all(col in df_estoque.columns for col in required_cols_estoque):
            messagebox.showerror("Erro", f"Arquivo de Estoque deve ter colunas: {required_cols_estoque}")
            return
        
        required_cols_func = ['Title', 'NOME', 'Custo']
        if not all(col in df_funcionarios.columns for col in required_cols_func):
            messagebox.showerror("Erro", f"Arquivo de Funcionários deve ter colunas: {required_cols_func}")
            return
        
        # Preencher comboboxes
        epi_values = df_estoque['Descrição_APP'].tolist()
        for i in range(1, 16):
            globals()[f'epi{i}_combo']['values'] = epi_values
        
        messagebox.showinfo("Sucesso", "Dados carregados com sucesso!")
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao carregar dados: {str(e)}")

# Função para filtrar EPIs
def filtrar_epis(event, epi_combo):
    typed = epi_combo.get()
    if typed == '':
        epi_combo['values'] = df_estoque['Descrição_APP'].tolist()
    else:
        filtered = [epi for epi in df_estoque['Descrição_APP'].tolist() if typed.lower() in epi.lower()]
        epi_combo['values'] = filtered

# Função para preencher nome e centro de custo
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

# Função para atualizar preço, estoque e última vez
def atualizar_preco_estoque(epi_combo, preco_entry, estoque_entry, ultima_entry):
    selected = epi_combo.get()
    cs = cs_entry.get()
    if selected and cs:
        item = df_estoque[df_estoque['Descrição_APP'] == selected]
        if not item.empty:
            preco_entry.config(state='normal')
            preco_entry.delete(0, tk.END)
            preco_entry.insert(0, str(item['Preco'].values[0]))  # Converter para string
            preco_entry.config(state='disabled')
            
            estoque_entry.config(state='normal')
            estoque_entry.delete(0, tk.END)
            estoque_entry.insert(0, str(item['Estoque'].values[0]))
            estoque_entry.config(state='disabled')
            
            # Buscar última vez no histórico
            if not df_historico.empty:
                hist = df_historico[(df_historico['CS'].astype(str) == str(cs)) & (df_historico['EPI'].str.strip().str.lower() == selected.strip().lower())]
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
            # Limpar se EPI não encontrado
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
        # Limpar se CS ou EPI vazio
        preco_entry.config(state='normal')
        preco_entry.delete(0, tk.END)
        preco_entry.config(state='disabled')
        estoque_entry.config(state='normal')
        estoque_entry.delete(0, tk.END)
        estoque_entry.config(state='disabled')
        ultima_entry.config(state='normal')
        ultima_entry.delete(0, tk.END)
        ultima_entry.config(state='disabled')

# Função para limpar EPI
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
    cs = cs_entry.get()
    nome = nome_entry.get()
    custo = custo_entry.get()
    data = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    
    epis = []
    for i in range(1, 16):
        epi = globals()[f'epi{i}_combo'].get()
        qtd = globals()[f'qtd{i}_combo'].get()
        preco = globals()[f'preco{i}_entry'].get()
        estoque = globals()[f'estoque{i}_entry'].get()
        if epi and qtd:
            epis.append({
                'EPI': epi,
                'Quantidade': int(qtd),  # Converter para int
                'Preco': float(preco) if preco else 0.0,  # Converter para float
                'Estoque': int(estoque) if estoque else 0  # Converter para int
            })
    
    if not cs or not epis:
        messagebox.showerror("Erro", "Preencha pelo menos CS e selecione um EPI com quantidade.")
        return
    
    # Salvar no arquivo de histórico usando openpyxl
    try:
        if os.path.exists(hist_file_path):
            wb = openpyxl.load_workbook(hist_file_path)
            ws = wb.active
            for epi in epis:
                ws.append([int(cs), nome, custo, data, epi['EPI'], epi['Quantidade'], epi['Preco'], epi['Estoque']])
            wb.save(hist_file_path)
        else:
            wb = openpyxl.Workbook()
            ws = wb.active
            ws.append(['CS', 'Nome', 'Centro de Custo', 'Data', 'EPI', 'Quantidade', 'Preco', 'Estoque'])
            for epi in epis:
                ws.append([int(cs), nome, custo, data, epi['EPI'], epi['Quantidade'], epi['Preco'], epi['Estoque']])
            wb.save(hist_file_path)
        
        # Recarregar df_historico
        df_historico = pd.read_excel(hist_file_path)
        
        messagebox.showinfo("Sucesso", f"Solicitação enviada e histórico atualizado em {hist_file_path}!")
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao salvar o arquivo: {str(e)}")
    
    # Limpar formulário
    cs_entry.delete(0, tk.END)
    preencher_nome_custo()
    for i in range(1, 16):
        limpar_epi(globals()[f'epi{i}_combo'], globals()[f'qtd{i}_combo'], globals()[f'preco{i}_entry'], globals()[f'estoque{i}_entry'], globals()[f'ultima{i}_entry'])

# Criar janela principal
root = tk.Tk()
root.title("Solicitação de EPI")
root.geometry("1600x1200")

# Menu
menubar = tk.Menu(root)
filemenu = tk.Menu(menubar, tearoff=0)
filemenu.add_command(label="Carregar Dados", command=carregar_dados)
menubar.add_cascade(label="Arquivo", menu=filemenu)
root.config(menu=menubar)

# Frame com scrollbar
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

# Campos
ttk.Label(scrollable_frame, text="CS:").grid(row=0, column=0, sticky=tk.W)
cs_entry = ttk.Entry(scrollable_frame)
cs_entry.grid(row=0, column=1, sticky=(tk.W, tk.E))
cs_entry.bind("<KeyRelease>", preencher_nome_custo)

ttk.Label(scrollable_frame, text="Nome:").grid(row=1, column=0, sticky=tk.W)
nome_entry = ttk.Entry(scrollable_frame, state='disabled')
nome_entry.grid(row=1, column=1, sticky=(tk.W, tk.E))

ttk.Label(scrollable_frame, text="Centro de Custo:").grid(row=2, column=0, sticky=tk.W)
custo_entry = ttk.Entry(scrollable_frame, state='disabled')
custo_entry.grid(row=2, column=1, sticky=(tk.W, tk.E))

ttk.Label(scrollable_frame, text="Data:").grid(row=3, column=0, sticky=tk.W)
data_label = ttk.Label(scrollable_frame, text=datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
data_label.grid(row=3, column=1, sticky=tk.W)

for i in range(1, 16):
    ttk.Label(scrollable_frame, text=f"EPI {i}:").grid(row=4+i-1, column=0, sticky=tk.W)
    globals()[f'epi{i}_combo'] = ttk.Combobox(scrollable_frame, state='normal', width=60)
    globals()[f'epi{i}_combo'].grid(row=4+i-1, column=1, sticky=(tk.W, tk.E))
    globals()[f'epi{i}_combo'].bind("<KeyRelease>", lambda e, i=i: filtrar_epis(e, globals()[f'epi{i}_combo']))
    globals()[f'epi{i}_combo'].bind("<<ComboboxSelected>>", lambda e, i=i: atualizar_preco_estoque(globals()[f'epi{i}_combo'], globals()[f'preco{i}_entry'], globals()[f'estoque{i}_entry'], globals()[f'ultima{i}_entry']))
    
    ttk.Label(scrollable_frame, text="Preço:").grid(row=4+i-1, column=2, sticky=tk.W)
    globals()[f'preco{i}_entry'] = ttk.Entry(scrollable_frame, state='disabled', width=15)
    globals()[f'preco{i}_entry'].grid(row=4+i-1, column=3, sticky=(tk.W, tk.E))
    
    ttk.Label(scrollable_frame, text="Estoque:").grid(row=4+i-1, column=4, sticky=tk.W)
    globals()[f'estoque{i}_entry'] = ttk.Entry(scrollable_frame, state='disabled', width=15)
    globals()[f'estoque{i}_entry'].grid(row=4+i-1, column=5, sticky=(tk.W, tk.E))
    
    ttk.Label(scrollable_frame, text="Última vez:").grid(row=4+i-1, column=6, sticky=tk.W)
    globals()[f'ultima{i}_entry'] = ttk.Entry(scrollable_frame, state='disabled', width=20)
    globals()[f'ultima{i}_entry'].grid(row=4+i-1, column=7, sticky=(tk.W, tk.E))
    
    ttk.Label(scrollable_frame, text="Quantidade:").grid(row=4+i-1, column=8, sticky=tk.W)
    globals()[f'qtd{i}_combo'] = ttk.Combobox(scrollable_frame, values=["1", "2"], state='readonly', width=10)
    globals()[f'qtd{i}_combo'].grid(row=4+i-1, column=9, sticky=(tk.W, tk.E))
    
    ttk.Button(scrollable_frame, text="Limpar", command=lambda i=i: limpar_epi(globals()[f'epi{i}_combo'], globals()[f'qtd{i}_combo'], globals()[f'preco{i}_entry'], globals()[f'estoque{i}_entry'], globals()[f'ultima{i}_entry'])).grid(row=4+i-1, column=10)

ttk.Button(scrollable_frame, text="Enviar", command=enviar_solicitacao).grid(row=20, column=0, columnspan=11, pady=10)

# Inicializar
df_estoque = pd.DataFrame()
df_funcionarios = pd.DataFrame()
df_historico = pd.DataFrame()
hist_file_path = "historico_solicitacoes.xlsx"

root.mainloop()
