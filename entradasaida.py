from datetime import datetime, timedelta

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