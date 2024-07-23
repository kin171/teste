'''
import tkinter as tk
from datetime import datetime  # For date validation

def validate_and_show_error(date_text, format_string='%d/%m/%Y'):
    """
    Validates the entered date and displays an error window if invalid.

    Args:
        date_text (str): The text to be validated.
        format_string (str, optional): The date format string. Defaults to '%Y-%m-%d'.
    """

    try:
        datetime.strptime(date_text, format_string)
    except ValueError:
        error_window = tk.Toplevel()
        error_window.title("Erro")
        error_label = tk.Label(error_window, text="FORMATO DE DATA ERRADA. POR FAVOR use DD/MM/AAAA.")
        error_label.pack()
        error_window.mainloop()  # Display the error window

def check_data_entry():
    """
    Gets the text from the entry widget, performs date validation,
    and either switches focus or displays an error window.
    """

    date_text = entry_data.get()
    validate_and_show_error(date_text)

# Create the main window
window = tk.Tk()
window.title("Data Entry")

# Label for "DATA"
label_data = tk.Label(text="DATA")
label_data.grid(row=2, column=0, padx=10, pady=10, sticky='nswe', columnspan=2)

# Entry widget for data
entry_data = tk.Entry()
entry_data.grid(row=2, column=2, padx=10, pady=10, sticky='nswe', columnspan=2)

# Button to trigger data entry check
check_button = tk.Button(window, text="Check Data", command=check_data_entry)
check_button.grid(row=4, column=2)

# Bind the check function to the <Return> (Enter) key press in the entry widget
# for real-time validation during typing
entry_data.bind("<Return>", lambda event: check_data_entry())

# Run the main event loop
window.mainloop()
'''
import tkinter as tk
from tkinter import messagebox
import regex as re

class FormValidator:
    def __init__(self, master):
        self.master = master
        self.master.title("Form Validator")
        
        # Create form fields
        self.name_label = tk.Label(master, text="Name:")
        self.name_label.grid(row=0, column=0)
        self.name_entry = tk.Entry(master)
        self.name_entry.grid(row=0, column=1)
        self.name_entry.bind('<Return>', lambda event: self.email_entry.focus_set() and validate_name(self))
        #self.name_entry.bind('<Return>', lambda event: self.email_entry.focus_set(), add='+') 
        self.email_label = tk.Label(master, text="Email:")
        self.email_label.grid(row=1, column=0)
        self.email_entry = tk.Entry(master)
        self.email_entry.grid(row=1, column=1)

        self.phone_label = tk.Label(master, text="Phone:")
        self.phone_label.grid(row=2, column=0)
        self.phone_entry = tk.Entry(master)
        self.phone_entry.grid(row=2, column=1)

        # Create submit button
        self.submit_button = tk.Button(master, text="Submit", command= self.validate_form(self))
        self.submit_button.grid(row=3, column=1)
def validate_name(self):
    name = self.name_entry.get()
    if not name:
            messagebox.showerror("Error", "Please enter your name")
    else:
            messagebox.showinfo("Success", "Form data processed successfully!")

    
    def validate_form(self):
        # Get form data
        name = self.name_entry.get()
        email = self.email_entry.get()
        phone = self.phone_entry.get()

        # Validate name
        if not name:
            messagebox.showerror("Error", "Please enter your name")
            return

        # Validate email
        email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(email_regex, email):
            messagebox.showerror("Error", "Please enter a valid email address")
            return

        # Validate phone
        phone_regex = r'^\d{11}$'
        if not re.match(phone_regex, phone):
            messagebox.showerror("Error", "Please enter a valid phone number")
            return

        # If all validations pass, process the form data
    

root = tk.Tk()
form_validator = FormValidator(root)
root.mainloop()