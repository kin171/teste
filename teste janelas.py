
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
