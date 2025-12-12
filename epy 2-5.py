import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from datetime import datetime
import pandas as pd
import os
import openpyxl  # Para anexar ao Excel
from office365.runtime.auth.authentication_context import AuthenticationContext
from office365.sharepoint.client_context import ClientContext

# Simulação de dados de estoque (substitua por dados reais ou carregue de um arquivo/BD)
estoque_data = {
    'epi1_desc': {'preco': '10.00', 'estoque': '50', 'ult_ped': '01/01/2023'},
    'epi2_desc': {'preco': '15.00', 'estoque': '30', 'ult_ped': '02/01/2023'},
    'epi3_desc': {'preco': '20.00', 'estoque': '40', 'ult_ped': '03/01/2023'},
    'epi4_desc': {'preco': '25.00', 'estoque': '20', 'ult_ped': '04/01/2023'},
    'epi5_desc': {'preco': '30.00', 'estoque': '60', 'ult_ped': '05/01/2023'},
    'epi6_desc': {'preco': '35.00', 'estoque': '25', 'ult_ped': '06/01/2023'},
    'epi7_desc': {'preco': '40.00', 'estoque': '35', 'ult_ped': '07/01/2023'},
    'epi8_desc': {'preco': '45.00', 'estoque': '15', 'ult_ped': '08/01/2023'},
    'epi9_desc': {'preco': '50.00', 'estoque': '45', 'ult_ped': '09/01/2023'},
    'epi10_desc': {'preco': '55.00', 'estoque': '10', 'ult_ped': '10/01/2023'},
    'epi11_desc': {'preco': '60.00', 'estoque': '55', 'ult_ped': '11/01/2023'},
    'epi12_desc': {'preco': '65.00', 'estoque': '30', 'ult_ped': '12/01/2023'},
    'epi13_desc': {'preco': '70.00', 'estoque': '20', 'ult_ped': '13/01/2023'},
    'epi14_desc': {'preco': '75.00', 'estoque': '40', 'ult_ped': '14/01/2023'},
    'epi15_desc': {'preco': '80.00', 'estoque': '50', 'ult_ped': '15/01/2023'},
}

# Simulação de dados de funcionários (substitua por lookup real)
funcionarios_data = {
    '123': {'nome': 'João Silva', 'custo': 'Centro A'},
    '456': {'nome': 'Maria Santos', 'custo': 'Centro B'},
}

# Global dataframes
df_estoque = pd.DataFrame()
df_funcionarios = pd.DataFrame()
df_historico = pd.DataFrame()
hist_file_path = "historico_solicitacoes.xlsx"

class EPISolicitacaoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Solicitação de EPI")
        self.root.geometry("800x1000")

        # Header
        header_frame = tk.Frame(root, bg="#4a6d4d", height=50)
        header_frame.pack(fill=tk.X)
        tk.Label(header_frame, text="Solicitação de EPI", bg="#4a6d4d", fg="white", font=("Segoe UI", 16)).pack(pady=10)

        # Warning
        warning_label = tk.Label(root, text="O EPI QUE NÃO APARECER É POR QUE NÃO TEM EM ESTOQUE", bg="#ffffcc", fg="black", wraplength=700)
        warning_label.pack(pady=10, padx=20, fill=tk.X)

        # Form Frame
        form_frame = tk.Frame(root)
        form_frame.pack(pady=10, padx=20, fill=tk.BOTH, expand=True)

        # Data
        tk.Label(form_frame, text="DATA").grid(row=0, column=0, sticky="w", pady=5)
        self.data_entry = tk.Entry(form_frame, state="disabled")
        self.data_entry.insert(0, datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
        self.data_entry.grid(row=0, column=1, pady=5, sticky="ew")

        # CS
        tk.Label(form_frame, text="CS").grid(row=1, column=0, sticky="w", pady=5)
        self.cs_entry = tk.Entry(form_frame)
        self.cs_entry.grid(row=1, column=1, pady=5, sticky="ew")
        self.cs_entry.bind("<KeyRelease>", self.update_nome_custo)

        # Nome
        tk.Label(form_frame, text="Nome").grid(row=2, column=0, sticky="w", pady=5)
        self.nome_entry = tk.Entry(form_frame, state="disabled")
        self.nome_entry.grid(row=2, column=1, pady=5, sticky="ew")

        # Centro de Custo
        tk.Label(form_frame, text="Centro de Custo").grid(row=3, column=0, sticky="w", pady=5)
        self.custo_entry = tk.Entry(form_frame, state="disabled")
        self.custo_entry.grid(row=3, column=1, pady=5, sticky="ew")

        # EPI Sections
        self.epi_frames = []
        for i in range(1, 16):
            epi_frame = tk.LabelFrame(form_frame, text=f"EPI {i}", padx=10, pady=10)
            epi_frame.grid(row=3+i, column=0, columnspan=2, pady=5, sticky="ew")

            # Selecionar EPI
            tk.Label(epi_frame, text="Selecionar EPI").grid(row=0, column=0, sticky="w")
            epi_combo = ttk.Combobox(epi_frame, values=list(estoque_data.keys()), state="readonly")
            epi_combo.grid(row=0, column=1, pady=5, sticky="ew")
            epi_combo.bind("<<ComboboxSelected>>", lambda e, idx=i: self.update_epi_fields(idx))

            # Limpar button
            clear_btn = tk.Button(epi_frame, text="Limpar", command=lambda idx=i: self.clear_epi(idx))
            clear_btn.grid(row=0, column=2, padx=5)

            # Preço
            tk.Label(epi_frame, text="Preço").grid(row=1, column=0, sticky="w")
            preco_entry = tk.Entry(epi_frame, state="disabled")
            preco_entry.grid(row=1, column=1, pady=5, sticky="ew")

            # Estoque
            tk.Label(epi_frame, text="Estoque").grid(row=2, column=0, sticky="w")
            estoque_entry = tk.Entry(epi_frame, state="disabled")
            estoque_entry.grid(row=2, column=1, pady=5, sticky="ew")

            # Quantidade
            tk.Label(epi_frame, text="Quantidade").grid(row=3, column=0, sticky="w")
            qtd_combo = ttk.Combobox(epi_frame, values=["1", "2"], state="readonly")
            qtd_combo.current(0)
            qtd_combo.grid(row=3, column=1, pady=5, sticky="ew")

            # Último Pedido
            tk.Label(epi_frame, text="Último Pedido").grid(row=4, column=0, sticky="w")
            ult_ped_entry = tk.Entry(epi_frame, state="disabled")
            ult_ped_entry.grid(row=4, column=1, pady=5, sticky="ew")

            # Store references
            self.epi_frames.append({
                'combo': epi_combo,
                'preco': preco_entry,
                'estoque': estoque_entry,
                'qtd': qtd_combo,
                'ult_ped': ult_ped_entry
            })

        # Submit Button
        submit_btn = tk.Button(form_frame, text="Enviar", bg="#4a6d4d", fg="white", command=self.submit_form)
        submit_btn.grid(row=19, column=0, columnspan=2, pady=20, sticky="ew")

        # Configure grid weights
        form_frame.columnconfigure(1, weight=1)

    def update_nome_custo(self, event):
        cs = self.cs_entry.get()
        if cs in funcionarios_data:
            self.nome_entry.config(state="normal")
            self.nome_entry.delete(0, tk.END)
            self.nome_entry.insert(0, funcionarios_data[cs]['nome'])
            self.nome_entry.config(state="disabled")

            self.custo_entry.config(state="normal")
            self.custo_entry.delete(0, tk.END)
            self.custo_entry.insert(0, funcionarios_data[cs]['custo'])
            self.custo_entry.config(state="disabled")
        else:
            self.nome_entry.config(state="normal")
            self.nome_entry.delete(0, tk.END)
            self.nome_entry.config(state="disabled")

            self.custo_entry.config(state="normal")
            self.custo_entry.delete(0, tk.END)
            self.custo_entry.config(state="disabled")

    def update_epi_fields(self, idx):
        epi_frame = self.epi_frames[idx-1]
        selected = epi_frame['combo'].get()
        if selected in estoque_data:
            epi_frame['preco'].config(state="normal")
            epi_frame['preco'].delete(0, tk.END)
            epi_frame['preco'].insert(0, estoque_data[selected]['preco'])
            epi_frame['preco'].config(state="disabled")

            epi_frame['estoque'].config(state="normal")
            epi_frame['estoque'].delete(0, tk.END)
            epi_frame['estoque'].insert(0, estoque_data[selected]['estoque'])
            epi_frame['estoque'].config(state="disabled")

            epi_frame['ult_ped'].config(state="normal")
            epi_frame['ult_ped'].delete(0, tk.END)
            epi_frame['ult_ped'].insert(0, estoque_data[selected]['ult_ped'])
            epi_frame['ult_ped'].config(state="disabled")
        else:
            for field in ['preco', 'estoque', 'ult_ped']:
                epi_frame[field].config(state="normal")
                epi_frame[field].delete(0, tk.END)
                epi_frame[field].config(state="disabled")

    def clear_epi(self, idx):
        epi_frame = self.epi_frames[idx-1]
        epi_frame['combo'].set('')
        epi_frame['qtd'].current(0)
        for field in ['preco', 'estoque', 'ult_ped']:
            epi_frame[field].config(state="normal")
            epi_frame[field].delete(0, tk.END)
            epi_frame[field].config(state="disabled")

    def submit_form(self):
        # Aqui você pode adicionar lógica para salvar os dados
        messagebox.showinfo("Sucesso", "Solicitação enviada com sucesso!")
        # Reset form
        self.cs_entry.delete(0, tk.END)
        self.update_nome_custo(None)
        for epi_frame in self.epi_frames:
            epi_frame['combo'].set('')
            epi_frame['qtd'].current(0)
            for field in ['preco', 'estoque', 'ult_ped']:
                epi_frame[field].config(state="normal")
                epi_frame[field].delete(0, tk.END)
                epi_frame[field].config(state="disabled")

if __name__ == "__main__":
    root = tk.Tk()
    app = EPISolicitacaoApp(root)
    root.mainloop()
