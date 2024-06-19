from datetime import datetime, timedelta


duracao = timedelta(hours = 1)  # Soma 1 horas

dataentrada = input('Data entrada:')
datasaida = input('Data saida:')
horaalmoco=('1:00')
datae = datetime.strptime(dataentrada,('%H:%M'))
datas = datetime.strptime(datasaida,('%H:%M'))
horaAlmoco = datetime.strptime(horaalmoco,('%H:%M'))


data=(1900, 1, 1)
diferenca = datas - datae
dif1 = datas - horaAlmoco
dif2 = diferenca - duracao 
dif3 = datae - dif2


#total = ( dif3 - dif2)
#print("Diferença em dias:", dif2)
print('A jornada foi de {}'.format(dif2))
#print(diferenca)
#print(dif1)
#print(dif2)
#print(dif3)
#print(data)
#print(total)