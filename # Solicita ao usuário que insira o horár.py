from datetime import datetime, timedelta
import os

import json


duracao = timedelta(hours = 1)  # Soma 1 horas


dataentrada = input('Data entrada e hora:')

datasaida = input('Data saida e hora:')


datae = datetime.strptime(dataentrada,('%d/%m/%Y %H:%M'))

datas = datetime.strptime(datasaida,('%d/%m/%Y %H:%M'))



diferenca = datas - datae
dif2 = diferenca - duracao 
dados = [datae, datas, dif2]
def salvar_informacoes(dados, arquivo):

    with open('jornada-agricola.txt', 'a') as arquivo:

        for linha in dados:

            arquivo.write(linha +'\n')
salvar_informacoes(dados, 'jornada-agricola.txt')


