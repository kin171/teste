from datetime import datetime, timedelta
<<<<<<< HEAD
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
def salvar(dados, arquivo):
    with open('jornada_agricola.txt', 'a') as arquivo:
        dados_json = json.dumps(dados)
        arquivo.write(dados_json + '\n')  # Adiciona quebra de linha no final    
        salvar(dados, 'jornada_agricola.txt')
=======

duracao = timedelta(hours = 1)  # Soma 1 horas
dataentrada = input('Data entrada e hora:')
datasaida = input('Data saida e hora:')
horanormal = ('7:20')
datae = datetime.strptime(dataentrada,('%d/%m/%Y %H:%M'))
datas = datetime.strptime(datasaida,('%d/%m/%Y %H:%M'))

horaNormal = timedelta(hours=7, minutes=20)
diferenca = datas - datae
jornada = diferenca - duracao 
print(jornada)
if jornada >= horaNormal:
    dif3 = jornada - horaNormal

dado =str(datae) + ';'+ str(datas)+ ';' + str(jornada) + ';'+ str(dif3)  # Substitua com seus valores reais
with open('jornada_agricola.txt', 'a') as arquivo:
    # Escrevendo os dados no arquivo
    arquivo.write(dado + '\n')  # Adiciona quebra de linha no final


>>>>>>> 9722029137d0a25e17c84ad8dd67c1ee779200ae


