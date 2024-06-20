from datetime import datetime, timedelta
import os

import json


duracao = timedelta(hours = 1)  # Soma 1 horas


dataentrada = input('Data entrada e hora:')

datasaida = input('Data saida e hora:')
horaEntrada = '7:20'

datae = datetime.strptime(dataentrada,('%d/%m/%Y %H:%M'))

datas = datetime.strptime(datasaida,('%d/%m/%Y %H:%M'))
dif1 = datetime.strptime(horaEntrada,('%d/%m/%Y %H:%M'))


diferenca = datas - datae
dif2 = diferenca - duracao 
if dif2 >= dif1:
    dif3 = datas - dif1
dado =str(datae)+ ' ;'+ str(datas)+ ';'+ str(dif2) + ';'+ str(dif3)  # Substitua com seus valores reais
with open('jornada_agricola.txt', 'a') as arquivo:
    # Escrevendo os dados no arquivo
    arquivo.write(dado + '\n')  # Adiciona quebra de linha no final




