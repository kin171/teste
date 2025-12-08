import tkinter as tk
from tkinter import messagebox, Toplevel
from tkinter import ttk
import csv
import os

class Formulario:
    def __init__(self, master):
        self.master = master
        self.master.title("Formulário OS")

        # Labels e Entrys
        self.os_label = tk.Label(master, text="OS:")
        self.os_label.grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.os_entry = tk.Entry(master)
        self.os_entry.grid(row=0, column=1, padx=5, pady=5)
        self.os_entry.bind('<Return>', lambda e: self.zona_entry.focus_set())

        self.zona_label = tk.Label(master, text="Zona:")
        self.zona_label.grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.zona_entry = tk.Entry(master)
        self.zona_entry.grid(row=1, column=1, padx=5, pady=5)
        self.zona_entry.bind('<Return>', lambda e: self.data_entry.focus_set())

        self.data_label = tk.Label(master, text="Data:")
        self.data_label.grid(row=2, column=0, padx=5, pady=5, sticky="e")
        self.data_entry = tk.Entry(master)
        self.data_entry.grid(row=2, column=1, padx=5, pady=5)
        self.data_entry.bind('<Return>', lambda e: self.operacao_entry.focus_set())

        self.operacao_label = tk.Label(master, text="Operação:")
        self.operacao_label.grid(row=3, column=0, padx=5, pady=5, sticky="e")
        self.operacao_entry = tk.Entry(master)
        self.operacao_entry.grid(row=3, column=1, padx=5, pady=5)
        self.operacao_entry.bind('<Return>', lambda e: self.salvar_button.focus_set())

        # Botões
        self.salvar_button = tk.Button(master, text="Salvar", command=self.salvar_dados)
        self.salvar_button.grid(row=4, column=0, padx=5, pady=10)

        self.visualizar_button = tk.Button(master, text="Visualizar Dados", command=self.abrir_janela_busca)
        self.visualizar_button.grid(row=4, column=1, padx=5, pady=10)

        self.fechar_button = tk.Button(master, text="Fechar", command=self.fechar_janela)
        self.fechar_button.grid(row=4, column=2, padx=5, pady=10)

    def salvar_dados(self):
        os_val = self.os_entry.get().strip()
        zona = self.zona_entry.get().strip()
        data = self.data_entry.get().strip()
        operacao = self.operacao_entry.get().strip()

        # Validação
        if not os_val:
            messagebox.showerror("Erro", "Por favor, preencha o campo OS")
            return
        if not zona:
            messagebox.showerror("Erro", "Por favor, preencha o campo Zona")
            return
        if not data:
            messagebox.showerror("Erro", "Por favor, preencha o campo Data")
            return
        if not operacao:
            messagebox.showerror("Erro", "Por favor, preencha o campo Operação")
            return

        arquivo = "dados_os.csv"
        campos = ['OS', 'Zona', 'Data', 'Operação']
        escrever_cabecalho = not os.path.exists(arquivo)
        try:
            with open(arquivo, mode='a', newline='', encoding='utf-8') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=campos)
                if escrever_cabecalho:
                    writer.writeheader()
                writer.writerow({'OS': os_val, 'Zona': zona, 'Data': data, 'Operação': operacao})
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao salvar os dados: {e}")
            return

        messagebox.showinfo("Sucesso", "Dados salvos com sucesso!")

        # Limpar campos
        self.os_entry.delete(0, tk.END)
        self.zona_entry.delete(0, tk.END)
        self.data_entry.delete(0, tk.END)
        self.operacao_entry.delete(0, tk.END)

        self.os_entry.focus_set()

    def abrir_janela_busca(self):
        if not os.path.exists("dados_os.csv"):
            messagebox.showinfo("Informação", "Nenhum dado salvo ainda.")
            return

        self.janela_busca = Toplevel(self.master)
        self.janela_busca.title("Buscar Dados")
        self.janela_busca.geometry("600x450")

        # Campos para busca
        frame_busca = tk.Frame(self.janela_busca)
        frame_busca.pack(padx=10, pady=10, fill='x')

        tk.Label(frame_busca, text="Buscar por OS:").grid(row=0, column=0, sticky='e', padx=5, pady=2)
        self.busca_os = tk.Entry(frame_busca)
        self.busca_os.grid(row=0, column=1, padx=5, pady=2)

        tk.Label(frame_busca, text="Buscar por Zona:").grid(row=1, column=0, sticky='e', padx=5, pady=2)
        self.busca_zona = tk.Entry(frame_busca)
        self.busca_zona.grid(row=1, column=1, padx=5, pady=2)

        tk.Label(frame_busca, text="Buscar por Data:").grid(row=2, column=0, sticky='e', padx=5, pady=2)
        self.busca_data = tk.Entry(frame_busca)
        self.busca_data.grid(row=2, column=1, padx=5, pady=2)

        tk.Label(frame_busca, text="Buscar por Operação:").grid(row=3, column=0, sticky='e', padx=5, pady=2)
        self.busca_operacao = tk.Entry(frame_busca)
        self.busca_operacao.grid(row=3, column=1, padx=5, pady=2)

        self.btn_buscar = tk.Button(frame_busca, text="Buscar", command=self.buscar_dados)
        self.btn_buscar.grid(row=4, column=0, columnspan=2, pady=10)

        # Treeview para mostrar resultados, com scrollbar
        frame_result = tk.Frame(self.janela_busca)
        frame_result.pack(padx=10, pady=5, fill='both', expand=True)

        columns = ("OS", "Zona", "Data", "Operação")
        self.tree = ttk.Treeview(frame_result, columns=columns, show='headings', selectmode='browse')
        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=120, anchor='center')
        self.tree.pack(side='left', fill='both', expand=True)

        scrollbar = ttk.Scrollbar(frame_result, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)
        scrollbar.pack(side='right', fill='y')

        # Botões apagar e fechar
        frame_botoes = tk.Frame(self.janela_busca)
        frame_botoes.pack(pady=5)

        self.btn_apagar = tk.Button(frame_botoes, text="Apagar Selecionado", command=self.apagar_registro)
        self.btn_apagar.pack(side='left', padx=5)

        self.btn_fechar_busca = tk.Button(frame_botoes, text="Fechar", command=self.janela_busca.destroy)
        self.btn_fechar_busca.pack(side='left', padx=5)

        # Carregar todos dados inicialmente
        self.carregar_todos_dados()

    def carregar_todos_dados(self):
        # Vai carregar todos dados sem filtro para facilitar apagar sem buscar antes
        self.tree.delete(*self.tree.get_children())
        try:
            with open("dados_os.csv", mode='r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    self.tree.insert('', 'end', values=(row['OS'], row['Zona'], row['Data'], row['Operação']))
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao ler o arquivo: {e}")

    def buscar_dados(self):
        os_busca = self.busca_os.get().strip().lower()
        zona_busca = self.busca_zona.get().strip().lower()
        data_busca = self.busca_data.get().strip().lower()
        operacao_busca = self.busca_operacao.get().strip().lower()

        self.tree.delete(*self.tree.get_children())

        try:
            with open("dados_os.csv", mode='r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                resultados = []
                for row in reader:
                    os_val = row['OS'].lower()
                    zona_val = row['Zona'].lower()
                    data_val = row['Data'].lower()
                    operacao_val = row['Operação'].lower()

                    # Checa se cada campo da busca está contido no respectivo valor, ou se vazio ignora
                    if (os_busca and os_busca not in os_val):
                        continue
                    if (zona_busca and zona_busca not in zona_val):
                        continue
                    if (data_busca and data_busca not in data_val):
                        continue
                    if (operacao_busca and operacao_busca not in operacao_val):
                        continue

                    resultados.append(row)

                if not resultados:
                    messagebox.showinfo("Busca", "Nenhum registro encontrado para os critérios de busca.")
                else:
                    for row in resultados:
                        self.tree.insert('', 'end', values=(row['OS'], row['Zona'], row['Data'], row['Operação']))

        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao ler o arquivo: {e}")

    def apagar_registro(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning("Aviso", "Selecione um registro para apagar.")
            return

        confirm = messagebox.askyesno("Confirmação", "Tem certeza que deseja apagar o registro selecionado?")
        if not confirm:
            return

        valores_selecionados = self.tree.item(selected_item)['values']
        os_del, zona_del, data_del, operacao_del = valores_selecionados

        # Ler todos registros e regravar, omitindo o selecionado
        try:
            registros = []
            with open("dados_os.csv", mode='r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    if (row['OS'] == os_del and row['Zona'] == zona_del and
                        row['Data'] == data_del and row['Operação'] == operacao_del):
                        continue
                    registros.append(row)

            with open("dados_os.csv", mode='w', newline='', encoding='utf-8') as f:
                campos = ['OS', 'Zona', 'Data', 'Operação']
                writer = csv.DictWriter(f, fieldnames=campos)
                writer.writeheader()
                writer.writerows(registros)

            messagebox.showinfo("Sucesso", "Registro apagado com sucesso!")
            self.tree.delete(selected_item)

        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao apagar o registro: {e}")

    def fechar_janela(self):
        self.master.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = Formulario(root)
    root.mainloop()
