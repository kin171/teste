import tkinter as tk
from tkinter import ttk
from datetime import datetime as dt
import csv
lista_codop = ['1 Irrigação','2 Fertirrigação','3 Aplic bioestimulante','4 Aplic inset','5 Aplic nematicida','6 Aplicação vinhaça','7 Lavagem de arrasto','8 Lavagem sistema','9 Limpeza em blocos','10 Limpeza rede principal','11 Montagem de válvulas','12 Chuva','13 Dry Off (preparação  dry off)','14 Enchimento reservatório','15 Falta de energia','16 Manutenção elétrica','17 Manutenção hidraulica (malha)','18 Manutenção mecanica','19 Solo úmido','99 sem irrigação']
lista_projetos = ['P1','P2','P3','P4','P5','P6','P7','P8','P9','P10','P11','P12','P13','P14','P15','P16']
lista_setor = ['S1','S2','S3','S4','S5']
lista_irrigação = []

janela = tk.Tk()

#Criação da função

def inserir_codigo():
    data = entry_data.get()
    #data = data.strftime("%d/%m/%Y")
    projeto = combobox_selecionar_tipo.get()
    setor = combobox_selecionar_tipo1.get()
    operacao = combobox_selecionar_tipo2.get()
    insumo = entry_insumo.get()
    insumo2 = entry_insumo1.get()
    insumo3 = entry_insumo3.get()
    insumo4 = entry_insumo4.get()
    insumo5 = entry_insumo5.get()
    insumo6 = entry_insumo6.get()
    insumo7 = entry_insumo7.get()
    insumo8 = entry_insumo8.get()
    hora_inicial = entry_horainicial.get()
    #hora_inicial = hora_inicial.strftime('%H:%M')
    hora_final = entry_horafinal.get()
    #hora_final = hora_final.strftime('%H:%M')
    
    lista_irrigação.append((data, projeto, setor, operacao, insumo, insumo2, insumo3, insumo4, insumo5, insumo6, insumo7, insumo8, hora_inicial, hora_final))
    with open('baseirrigacao.csv', 'a') as arquivo:
        linha = csv.writer(arquivo)
        linha.writerow(lista_irrigação)
    entry_data.delete(0, tk.END)
    combobox_selecionar_tipo.delete(0, tk.END)
    combobox_selecionar_tipo1.delete(0, tk.END)
    combobox_selecionar_tipo2.delete(0, tk.END)
    entry_insumo.delete(0, tk.END)
    entry_insumo3.delete(0, tk.END)
    entry_insumo3.delete(0, tk.END)
    entry_insumo4.delete(0, tk.END)
    entry_insumo5.delete(0, tk.END)
    entry_insumo6.delete(0, tk.END)
    entry_insumo7.delete(0, tk.END)
    entry_insumo8.delete(0, tk.END)
    entry_horainicial.delete(0, tk.END)
    entry_horafinal.delete(0, tk.END)
        
def limpar():
    entry_data.delete(0, tk.END)
    combobox_selecionar_tipo.delete(0, tk.END)
    combobox_selecionar_tipo1.delete(0, tk.END)
    combobox_selecionar_tipo2.delete(0, tk.END)
    entry_insumo.delete(0, tk.END)
    entry_insumo3.delete(0, tk.END)
    entry_insumo3.delete(0, tk.END)
    entry_insumo4.delete(0, tk.END)
    entry_insumo5.delete(0, tk.END)
    entry_insumo6.delete(0, tk.END)
    entry_insumo7.delete(0, tk.END)
    entry_insumo8.delete(0, tk.END)
    entry_horainicial.delete(0, tk.END)
    entry_horafinal.delete(0, tk.END)
    return 
def fechar():
    janela.destroy()




#Título da Janela

janela.title('INSERÇÃO DE BASE DE DADOS')

label_descricao = tk.Label(text="BASE DE DADOS")
label_descricao.grid(row=1, column=0,padx = 10, pady=10, sticky='nswe', columnspan =4 )

#entry_descricao = tk.Entry()

#entry_descricao1 = tk.label(text='projeto')
#entry_descricao.grid(row=2,column=0, padx=10, pady=10, sticky='nswe', columnspan = 2)
label_data =  tk.Label(text="DATA")
label_data.grid(row=2, column=0,padx = 10, pady=10, sticky='nswe', columnspan =2 )
entry_data =  tk.Entry()
entry_data.grid(row=2, column=2,padx = 10, pady=10, sticky='nswe', columnspan =2 )


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

label_insumo3 =  tk.Label(text="INSUMO 2")
label_insumo3.grid(row=8, column=0,padx = 10, pady=10, sticky='nswe', columnspan =2 )
entry_insumo3 =  tk.Entry()
entry_insumo3.grid(row=8, column=2,padx = 10, pady=10, sticky='nswe', columnspan =2 )

label_insumo4 =  tk.Label(text="INSUMO 3")
label_insumo4.grid(row=9, column=0,padx = 10, pady=10, sticky='nswe', columnspan =2 )
entry_insumo4 =  tk.Entry()
entry_insumo4.grid(row=9, column=2,padx = 10, pady=10, sticky='nswe', columnspan =2 )

label_insumo5 =  tk.Label(text="INSUMO 4")
label_insumo5.grid(row=10, column=0,padx = 10, pady=10, sticky='nswe', columnspan =2 )
entry_insumo5 =  tk.Entry()
entry_insumo5.grid(row=10, column=2,padx = 10, pady=10, sticky='nswe', columnspan =2 )

label_insumo6 =  tk.Label(text="INSUMO 5")
label_insumo6.grid(row=11, column=0,padx = 10, pady=10, sticky='nswe', columnspan =2 )
entry_insumo6 =  tk.Entry()
entry_insumo6.grid(row=11, column=2,padx = 10, pady=10, sticky='nswe', columnspan =2 )

label_insumo7 =  tk.Label(text="INSUMO 6")
label_insumo7.grid(row=12, column=0,padx = 10, pady=10, sticky='nswe', columnspan =2 )
entry_insumo7 =  tk.Entry()
entry_insumo7.grid(row=12, column=2,padx = 10, pady=10, sticky='nswe', columnspan =2 )

label_insumo8 =  tk.Label(text="INSUMO 7")
label_insumo8.grid(row=13, column=0,padx = 10, pady=10, sticky='nswe', columnspan =2 )
entry_insumo8 =  tk.Entry()
entry_insumo8.grid(row=13, column=2,padx = 10, pady=10, sticky='nswe', columnspan =2 )


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
