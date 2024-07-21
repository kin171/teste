import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from datetime import datetime as dt
import regex as re
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

'''def validate_and_show_error(date_text, format_string='%d/%m/%Y'):
    if not format_string:
        messagebox.showerror('ERRO' , 'FAVOR INSERIR A DATA NO FORMATO DD/MM/AAAA')
    else:
        return
def check_data_entry():
   
    Gets the text from the entry widget, performs date validation,
    and either switches focus or displays an error window.
    

    date_text = entry_data.get()
    validate_and_show_error(date_text)
'''
#entry_data.bind('<esc>', lambda event: janela.destroy())
#entry_data.bind("<Return>", lambda event:  check_data_entry())



#Título da Janela

janela.title('CADASTRO DE BOLETINS PARA BAIXA')
#botoes e campos
label_descricao = tk.Label(text="BASE DE DADOS")
label_descricao.grid(row=1, column=0,padx = 10, pady=10, sticky='nswe', columnspan =4 )



label_data =  tk.Label(text="DATA")
label_data.grid(row=2, column=0,padx = 10, pady=10, sticky='nswe', columnspan =2 )
entry_data =  tk.Entry()
entry_data.grid(row=2, column=2,padx = 10, pady=10, sticky='nswe', columnspan =2 )

data = entry_data.get()
def validar_data(data):
    datavali = dt.strftime('%d/%m/%Y')
    if data != datavali:
        messagebox.showerror("Erro", "por favor entre com a data")
        return
    

#entry_data.bind('<Return>', lambda event: combobox_selecionar_tipo.focus_set() and validar_data(data))
entry_data.bind('<return>', validar_data(data))
entry_data.bind('<return>', lambda event:combobox_selecionar_tipo.focus_set,add='+')
label_projeto = tk.Label(text="RESERVA")
label_projeto.grid(row=3, column=0,padx = 10, pady=10, sticky='nswe', columnspan =2 )
combobox_selecionar_tipo = ttk.Combobox(values=lista_projetos)
combobox_selecionar_tipo.grid(row=3, column=2, padx = 10, pady=10, sticky='nswe', columnspan = 2)

combobox_selecionar_tipo.bind("<Return>", lambda event: combobox_selecionar_tipo1.focus_set())

label_tipo_unidade = tk.Label(text="ZONA")
label_tipo_unidade.grid(row=4, column=0,padx = 10, pady=10, sticky='nswe', columnspan =2 )
combobox_selecionar_tipo1 = ttk.Combobox(values=lista_setor)
combobox_selecionar_tipo1.grid(row=4, column=2, padx = 10, pady=10, sticky='nswe', columnspan = 2)

combobox_selecionar_tipo1.bind("<Return>", lambda event: combobox_selecionar_tipo2.focus_set())

label_cod_operacao =  tk.Label(text='PRODUTO')
label_cod_operacao.grid(row=5, column=0,padx = 10, pady=10, sticky='nswe', columnspan =2 )
combobox_selecionar_tipo2 = ttk.Combobox(values=lista_codop)
combobox_selecionar_tipo2.grid(row=5, column=2, padx = 10, pady=10, sticky='nswe', columnspan = 2)

combobox_selecionar_tipo2.bind("<Return>", lambda event: entry_insumo.focus_set())

label_insumo =  tk.Label(text="COD PRODUTO")
label_insumo.grid(row=6, column=0,padx = 10, pady=10, sticky='nswe', columnspan =2 )
entry_insumo = tk.Entry()
entry_insumo.grid(row=6, column=2,padx = 10, pady=10, sticky='nswe', columnspan =2 )


entry_insumo.bind("<Return>", lambda event: entry_insumo1.focus_set())

label_insumo1 =  tk.Label(text="AREA")
label_insumo1.grid(row=7, column=0,padx = 10, pady=10, sticky='nswe', columnspan =2 )
entry_insumo1 =  tk.Entry()
entry_insumo1.grid(row=7, column=2,padx = 10, pady=10, sticky='nswe', columnspan =2 )
'''
label_insumo2 =  tk.Label(text="CENTRO DE CUSTO")
label_insumo2.grid(row=8, column=0,padx = 10, pady=10, sticky='nswe', columnspan =2 )
entry_insumo2 =  tk.Entry()
entry_insumo2.grid(row=8, column=2,padx = 10, pady=10, sticky='nswe', columnspan =2 )

label_insumo3 =  tk.Label(text="QUANTIDADE")
label_insumo3.grid(row=9, column=0,padx = 10, pady=10, sticky='nswe', columnspan =2 )
entry_insumo3 =  tk.Entry()
entry_insumo3.grid(row=9, column=2,padx = 10, pady=10, sticky='nswe', columnspan =2 )

label_insumo4 =  tk.Label(text="SOLICITANTE")
label_insumo4.grid(row=10, column=0,padx = 10, pady=10, sticky='nswe', columnspan =2 )
entry_insumo4 =  tk.Entry()
entry_insumo4.grid(row=10, column=2,padx = 10, pady=10, sticky='nswe', columnspan =2 )

label_insumo5 =  tk.Label(text="STATUS")
label_insumo5.grid(row=11, column=0,padx = 10, pady=10, sticky='nswe', columnspan =2 )
entry_insumo5 =  tk.Entry()
entry_insumo5.grid(row=11, column=2,padx = 10, pady=10, sticky='nswe', columnspan =2 )
'''


entry_insumo1.bind("<Return>", lambda event: entry_insumo6.focus_set())

label_insumo6 =  tk.Label(text="MES")
label_insumo6.grid(row=12, column=0,padx = 10, pady=10, sticky='nswe', columnspan =2 )
entry_insumo6 =  tk.Entry()
entry_insumo6.grid(row=12, column=2,padx = 10, pady=10, sticky='nswe', columnspan =2 )


entry_insumo6.bind("<Return>", lambda event: entry_insumo7.focus_set())

label_insumo7 =  tk.Label(text="INSUMO 7")
label_insumo7.grid(row=13, column=0,padx = 10, pady=10, sticky='nswe', columnspan =2 )
entry_insumo7 =  tk.Entry()
entry_insumo7.grid(row=13, column=2,padx = 10, pady=10, sticky='nswe', columnspan =2 )


entry_insumo7.bind("<Return>", lambda event: entry_horainicial.focus_set())

label_horainicial =  tk.Label(text="HORA INICIAL")
label_horainicial.grid(row=18, column=0,padx = 10, pady=10, sticky='nswe', columnspan =2 )
entry_horainicial =  tk.Entry()
entry_horainicial.grid(row=18, column=2,padx = 10, pady=10, sticky='nswe', columnspan =2 )


entry_horainicial.bind("<Return>", lambda event: entry_horafinal.focus_set())

label_horafinal =  tk.Label(text="HORA FINAL")
label_horafinal.grid(row=19, column=0,padx = 10, pady=10, sticky='nswe', columnspan =2 )
entry_horafinal =  tk.Entry()
entry_horafinal.grid(row=19, column=2,padx = 10, pady=10, sticky='nswe', columnspan =2 )

entry_horafinal.bind("<Return>", lambda event: botao_criar_codigo.focus_set())

botao_criar_codigo = tk.Button(text="REGISTRAR", command=inserir_codigo)
botao_criar_codigo.grid(row=20,column=0,padx = 10, pady=10,sticky='nswe', columnspan =2)

botao_criar_codigo1 = tk.Button(text="LIMPAR", command=limpar)
botao_criar_codigo1.grid(row=20,column=2,padx = 10, pady=10,sticky='nswe', columnspan =2)

botao_criar_codigo2 = tk.Button(text="FECHAR", command=fechar)
botao_criar_codigo2.grid(row=20,column=4,padx = 10, pady=10,sticky='nswe', columnspan =2)

janela.mainloop()
