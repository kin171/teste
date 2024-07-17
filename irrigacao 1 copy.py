import tkinter as tk
from tkinter import ttk
from datetime import datetime as dt
import csv
lista_codop = ['1 Irrigação','2 Fertirrigação','3 Aplic bioestimulante','4 Aplic inset','5 Aplic nematicida','6 Aplicação vinhaça','7 Lavagem de arrasto','8 Lavagem sistema','9 Limpeza em blocos','10 Limpeza rede principal','11 Montagem de válvulas','12 Chuva','13 Dry Off (preparação  dry off)','14 Enchimento reservatório','15 Falta de energia','16 Manutenção elétrica','17 Manutenção hidraulica (malha)','18 Manutenção mecanica','19 Solo úmido','99 sem irrigação']
lista_projetos = ['P1','P2','P3','P4','P5','P6','P7','P8','P9','P10','P11','P12','P13','P14','P15','P16']
lista_setor = ['S1','S2','S3','S4','S5']


janela = tk.Tk()

#Criação da função

def inserir_codigo():
    data = entry_data.get()
    #if data != str('%H:%M'):
    #    print('Formato errado, digite novamente: ')    
    projeto = combobox_selecionar_tipo.get()
    setor = combobox_selecionar_tipo1.get()
    operacao = combobox_selecionar_tipo2.get()
    insumo = entry_insumo.get()
    insumo1 = entry_insumo1.get()
    insumo2 = entry_insumo2.get()
    insumo3 = entry_insumo3.get()
    insumo4 = entry_insumo4.get()
    insumo5 = entry_insumo5.get()
    insumo6 = entry_insumo6.get()
    insumo7 = entry_insumo7.get()
    hora_inicial = entry_horainicial.get()
    #hora_inicial = hora_inicial.strftime('%H:%M')
    hora_final = entry_horafinal.get()
    #hora_final = hora_final.strftime('%H:%M')
    #grava os arquivos
    with open('baseirrigacao.csv','a') as arquivo:
        writer = csv.writer(arquivo)
        #writer.writerow([data, projeto, setor, operacao, insumo, insumo1, insumo2, insumo3, insumo4, insumo5, insumo6, insumo7, hora_inicial, hora_final])
        arquivo.write(f'{data},{projeto},{setor},{operacao},{insumo},{insumo1},{insumo2},{insumo3},{insumo4},{insumo5}{insumo6},{insumo7},{hora_inicial},{hora_final} \n')
    #limpa os campos do formulario
    entry_data.delete(0, tk.END)
    combobox_selecionar_tipo.delete(0, tk.END)
    combobox_selecionar_tipo1.delete(0, tk.END)
    combobox_selecionar_tipo2.delete(0, tk.END)
    entry_insumo.delete(0, tk.END)
    entry_insumo1.delete(0, tk.END)
    entry_insumo2.delete(0, tk.END)
    entry_insumo3.delete(0, tk.END)
    entry_insumo4.delete(0, tk.END)
    entry_insumo5.delete(0, tk.END)
    entry_insumo6.delete(0, tk.END)
    entry_insumo7.delete(0, tk.END)
    entry_horainicial.delete(0, tk.END)
    entry_horafinal.delete(0, tk.END)
#botao de limpar        
def limpar():
    entry_data.delete(0, tk.END)
    combobox_selecionar_tipo.delete(0, tk.END)
    combobox_selecionar_tipo1.delete(0, tk.END)
    combobox_selecionar_tipo2.delete(0, tk.END)
    entry_insumo.delete(0, tk.END)
    entry_insumo1.delete(0, tk.END)
    entry_insumo2.delete(0, tk.END)
    entry_insumo3.delete(0, tk.END)
    entry_insumo4.delete(0, tk.END)
    entry_insumo5.delete(0, tk.END)
    entry_insumo6.delete(0, tk.END)
    entry_insumo7.delete(0, tk.END)
    entry_horainicial.delete(0, tk.END)
    entry_horafinal.delete(0, tk.END)
    return 
#botao fechar
def fechar():
    janela.destroy()




#Título da Janela

janela.title('INSERÇÃO DE BASE DE DADOS')
#botoes e campos
label_descricao = tk.Label(text="BASE DE DADOS")
label_descricao.grid(row=1, column=0,padx = 10, pady=10, sticky='nswe', columnspan =4 )



label_data =  tk.Label(text="DATA")
label_data.grid(row=2, column=0,padx = 10, pady=10, sticky='nswe', columnspan =2 )
entry_data =  tk.Entry()
entry_data.grid(row=2, column=2,padx = 10, pady=10, sticky='nswe', columnspan =2 )
#if data != str('%H:%M'):
#    print('Formato errado, digite novamente: ')

def validate_date(date_text):
    """
    Checks if the entered text is a valid date in the format YYYY-MM-DD.

    Args:
        date_text (str): The text to be validated.

    Returns:
        bool: True if the text is a valid date, False otherwise.
    """

    try:
        dt.strptime(date_text, '%d/%m/%Y')
        return True
    except ValueError:
        return False
    
def check_data_entry():
    """
    Gets the text from the entry widget and performs date validation.

    Displays an error message if the date is invalid.
    """

    date_text = entry_data.get()
    if not validate_date(date_text):
        error_label.config(text="Invalid date format. Please use YYYY-MM-DD.")
    else:
        error_label.config(text="")  # Clear error message if valid
'''
# Create the main window
window = tk.Tk()

# Label for "DATA"
label_data = tk.Label(window, text="DATA")
label_data.grid(row=2, column=0, padx=10, pady=10, sticky='nswe', columnspan=2)

# Entry widget for data
entry_data = tk.Entry(window)
entry_data.grid(row=2, column=2, padx=10, pady=10, sticky='nswe', columnspan=2)

# Error label for displaying validation messages
error_label = tk.Label(window, text="", fg="red")  # Red color for error messages
error_label.grid(row=3, column=0, columnspan=4, sticky='nsew')

# Button to trigger data entry check (optional, for manual validation)
# check_button = tk.Button(window, text="Check Data", command=check_data_entry)
# check_button.grid(row=4, column=2)

# Bind the check function to the <Return> (Enter) key press in the entry widget
# for real-time validation during typing
entry_data.bind("<Return>", lambda event: check_data_entry())

# Run the main event loop
window.mainloop()'''


label_projeto = tk.Label(text="PROJETO")
label_projeto.grid(row=3, column=0,padx = 10, pady=10, sticky='nswe', columnspan =2 )
combobox_selecionar_tipo = ttk.Combobox(values=lista_projetos)
combobox_selecionar_tipo.grid(row=3, column=2, padx = 10, pady=10, sticky='nswe', columnspan = 2)


label_tipo_unidade = tk.Label(text="SETOR")
label_tipo_unidade.grid(row=4, column=0,padx = 10, pady=10, sticky='nswe', columnspan =2 )
combobox_selecionar_tipo1 = ttk.Combobox(values=lista_setor)
combobox_selecionar_tipo1.grid(row=4, column=2, padx = 10, pady=10, sticky='nswe', columnspan = 2)

label_cod_operacao =  tk.Label(text='CODIGO OPERAÇÃO')
label_cod_operacao.grid(row=5, column=0,padx = 10, pady=10, sticky='nswe', columnspan =2 )
combobox_selecionar_tipo2 = ttk.Combobox(values=lista_codop)
combobox_selecionar_tipo2.grid(row=5, column=2, padx = 10, pady=10, sticky='nswe', columnspan = 2)

label_insumo =  tk.Label(text="INSUMO")
label_insumo.grid(row=6, column=0,padx = 10, pady=10, sticky='nswe', columnspan =2 )
entry_insumo =  tk.Entry()
entry_insumo.grid(row=6, column=2,padx = 10, pady=10, sticky='nswe', columnspan =2 )

label_insumo1 =  tk.Label(text="INSUMO 1")
label_insumo1.grid(row=7, column=0,padx = 10, pady=10, sticky='nswe', columnspan =2 )
entry_insumo1 =  tk.Entry()
entry_insumo1.grid(row=7, column=2,padx = 10, pady=10, sticky='nswe', columnspan =2 )

label_insumo2 =  tk.Label(text="INSUMO 2")
label_insumo2.grid(row=8, column=0,padx = 10, pady=10, sticky='nswe', columnspan =2 )
entry_insumo2 =  tk.Entry()
entry_insumo2.grid(row=8, column=2,padx = 10, pady=10, sticky='nswe', columnspan =2 )

label_insumo3 =  tk.Label(text="INSUMO 3")
label_insumo3.grid(row=9, column=0,padx = 10, pady=10, sticky='nswe', columnspan =2 )
entry_insumo3 =  tk.Entry()
entry_insumo3.grid(row=9, column=2,padx = 10, pady=10, sticky='nswe', columnspan =2 )

label_insumo4 =  tk.Label(text="INSUMO 4")
label_insumo4.grid(row=10, column=0,padx = 10, pady=10, sticky='nswe', columnspan =2 )
entry_insumo4 =  tk.Entry()
entry_insumo4.grid(row=10, column=2,padx = 10, pady=10, sticky='nswe', columnspan =2 )

label_insumo5 =  tk.Label(text="INSUMO 5")
label_insumo5.grid(row=11, column=0,padx = 10, pady=10, sticky='nswe', columnspan =2 )
entry_insumo5 =  tk.Entry()
entry_insumo5.grid(row=11, column=2,padx = 10, pady=10, sticky='nswe', columnspan =2 )

label_insumo6 =  tk.Label(text="INSUMO 6")
label_insumo6.grid(row=12, column=0,padx = 10, pady=10, sticky='nswe', columnspan =2 )
entry_insumo6 =  tk.Entry()
entry_insumo6.grid(row=12, column=2,padx = 10, pady=10, sticky='nswe', columnspan =2 )

label_insumo7 =  tk.Label(text="INSUMO 7")
label_insumo7.grid(row=13, column=0,padx = 10, pady=10, sticky='nswe', columnspan =2 )
entry_insumo7 =  tk.Entry()
entry_insumo7.grid(row=13, column=2,padx = 10, pady=10, sticky='nswe', columnspan =2 )


label_horainicial =  tk.Label(text="HORA INICIAL")
label_horainicial.grid(row=18, column=0,padx = 10, pady=10, sticky='nswe', columnspan =2 )
entry_horainicial =  tk.Entry()
entry_horainicial.grid(row=18, column=2,padx = 10, pady=10, sticky='nswe', columnspan =2 )

label_horafinal =  tk.Label(text="HORA FINAL")
label_horafinal.grid(row=19, column=0,padx = 10, pady=10, sticky='nswe', columnspan =2 )
entry_horafinal =  tk.Entry()
entry_horafinal.grid(row=19, column=2,padx = 10, pady=10, sticky='nswe', columnspan =2 )

botao_criar_codigo = tk.Button(text="REGISTRAR", command=inserir_codigo)
botao_criar_codigo.grid(row=20,column=0,padx = 10, pady=10,sticky='nswe', columnspan =2)

botao_criar_codigo = tk.Button(text="limpar", command=limpar)
botao_criar_codigo.grid(row=20,column=2,padx = 10, pady=10,sticky='nswe', columnspan =2)

botao_criar_codigo = tk.Button(text="fechar", command=fechar)
botao_criar_codigo.grid(row=20,column=4,padx = 10, pady=10,sticky='nswe', columnspan =2)

janela.mainloop()
