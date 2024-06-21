from datetime import datetime, timedelta

duracao = timedelta(hours = 1)  # Soma 1 horas
dataentrada = input('Data entrada e hora:')
datasaida = input('Data saida e hora:')
horanormal = ('7:20')
datae = datetime.strptime(dataentrada,('%d/%m/%Y %H:%M'))
datas = datetime.strptime(datasaida,('%d/%m/%Y %H:%M'))
dif1 = datetime.strptime(horanormal,('%H:%M')).time()
#hj = datetime.today()
#combined_datetime = datetime(year=hj.year, month=hj.month, day=hj.day,
hour=dif1.hour, minute=dif1.minute, second=0)

horaNormal = timedelta(hours=7, minutes=20)
diferenca = datas - datae
dif2 = diferenca - duracao 
print(dif2)
if dif2 >= horaNormal:
    dif3 = datas - combined_datetime
dado =str(datae)+ ' ;'+ str(datas)+ ';'+ str(dif2) + ';'+ str(dif3)  # Substitua com seus valores reais
with open('jornada_agricola.txt', 'a') as arquivo:
    # Escrevendo os dados no arquivo
    arquivo.write(dado + '\n')  # Adiciona quebra de linha no final




