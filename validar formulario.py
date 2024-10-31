import tkinter as tk
from tkinter import messagebox

def fechar_janela():
    master.destroy()
def insumo_formulario(self):
        # Obter valores dos campos do formulário
        insumo = self.insumo_entry.get()
        #zona = self.zona_entry.get()
        #area = self.area_entry.get()


        # Validar campos do formulário
        if not insumo:
            messagebox.showerror("Erro", "Por favor, informe o insumo")
            return
        #if not zona:
        #    messagebox.showerror("Erro", "Por favor, informe a zona")
        #    return
        #if not area:
        #    messagebox.showerror("Erro", "Por favor, informe o area")
        #    return

class Formulario:
    def __init__(self, master):
        self.master = master
        self.master.title("Formulário de Exemplo")

        # Criar campos do formulário
        self.insumo_label = tk.Label(master, text="insumo:")
        self.insumo_label.grid(row=0, column=0)
        self.insumo_entry = tk.Entry(master)
        self.insumo_entry.grid(row=0, column=1)
        self.insumo_entry.bind('<Return>', lambda event: self.zona_entry.focus_set() and insumo_formulario(self))

        self.zona_label = tk.Label(master, text="zona:")
        self.zona_label.grid(row=1, column=0)
        self.zona_entry = tk.Entry(master)
        self.zona_entry.grid(row=1, column=1)
        self.zona_entry.bind('<Return>', lambda event: self.area_entry.focus_set())

        self.area_label = tk.Label(master, text="area:")
        self.area_label.grid(row=2, column=0)
        self.area_entry = tk.Entry(master)
        self.area_entry.grid(row=2, column=1)
        self.area_entry.bind('<Return>', lambda event: self.enviar_button.focus_set())

        # Criar botão de envio
        self.enviar_button = tk.Button(master, text="Enviar", command=self.enviar_formulario)
        self.enviar_button.grid(row=3, column=1)
        self.fechar_button = tk.Button(master, text="fechar", command=fechar_janela)
        self.fechar_button.grid(row=3, column=2)
    
    def enviar_formulario(self):
        insumo: self.insumo_entry.get()
        # Enviar formulário (por exemplo, para um banco de dados ou um servidor)
        print("Formulário enviado com sucesso!")
        print("insumo:", insumo)
        print("zona:", zona)
        print("area:", area)

root = tk.Tk()
form = Formulario(root)
root.mainloop()