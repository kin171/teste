import json

import pandas as pd 
'''
with open('jornada-agricola.csv', 'r') as arquivo:
    dados=json.load(arquivo)
    print(dados)    
'''
import csv

# Abrindo o arquivo CSV
with open("saida.csv", "r") as arquivo_csv:
    leitor_csv = csv.reader(arquivo_csv)

    # Definindo os índices das colunas de interesse
    indice_frota = 0  # Assuming 'Nome' is in the first column
    indice_turno = 1  # Assuming 'Idade' is in the second column

    # Lendo as linhas e acessando colunas específicas
    for linha in leitor_csv:
        nome = linha[indice_frota]
        idade = linha[indice_turno]
        print(f"Nome: {nome}, Idade: {idade}")
     