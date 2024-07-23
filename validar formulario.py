

import tkinter as tk
from tkinter import messagebox
import re

class FormValidator:
    def __init__(self, master):
        self.master = master
        self.master.title("Form Validator")

        # Create form fields
        self.data_label = tk.Label(master, text="Data (dd/mm/yyyy):")
        self.data_label.grid(row=0, column=0)
        self.data_entry = tk.Entry(master)
        self.data_entry.grid(row=0, column=1)
        self.data_entry.bind('<Return>', lambda event: self.insumo_entry.focus_set() and validar_data(self))


        self.insumo_label = tk.Label(master, text="Insumo:")
        self.insumo_label.grid(row=1, column=0)
        self.insumo_entry = tk.Entry(master)
        self.insumo_entry.grid(row=1, column=1)

        self.area_aplicada_label = tk.Label(master, text="Área Aplicada (m²):")
        self.area_aplicada_label.grid(row=2, column=0)
        self.area_aplicada_entry = tk.Entry(master)
        self.area_aplicada_entry.grid(row=2, column=1)

        self.area_total_label = tk.Label(master, text="Área Total (m²):")
        self.area_total_label.grid(row=3, column=0)
        self.area_total_entry = tk.Entry(master)
        self.area_total_entry.grid(row=3, column=1)

        # Create submit button
        self.submit_button = tk.Button(master, text="Submit", command=self.validar_data)
        self.submit_button.grid(row=4, column=1)
    def validar_data(self):
        data = self.data_entry.get()
        # Validate data
        data_regex = r'^\d{2}/\d{2}/\d{4}$'
        if not re.match(data_regex, data):
            messagebox.showerror("Error", "Please enter a valid date (dd/mm/yyyy)")
    
    
    def validate_form(self):
        # Get form data
        data = self.data_entry.get()
        insumo = self.insumo_entry.get()
        area_aplicada = self.area_aplicada_entry.get()
        area_total = self.area_total_entry.get()

        # Validate data
        data_regex = r'^\d{2}/\d{2}/\d{4}$'
        if not re.match(data_regex, data):
            messagebox.showerror("Error", "Please enter a valid date (dd/mm/yyyy)")
            return

        # Validate insumo
        if not insumo:
            messagebox.showerror("Error", "Please enter the insumo")
            return

        # Validate area aplicada
        try:
            area_aplicada_float = float(area_aplicada)
            if area_aplicada_float <= 0:
                messagebox.showerror("Error", "Please enter a valid area aplicada (greater than 0)")
                return
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid area aplicada (number)")
            return

        # Validate area total
        try:
            area_total_float = float(area_total)
            if area_total_float <= 0:
                messagebox.showerror("Error", "Please enter a valid area total (greater than 0)")
                return
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid area total (number)")
            return

# If all validations pass, process the form data
#messagebox.showinfo("Success", "Form data processed successfully!")

root = tk.Tk()
#form_validator = FormValidator(root)
#root.mainloop()