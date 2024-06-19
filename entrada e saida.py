from datetime import datetime, timedelta

dataentrada = input('Data entrada:')
datasaida = input('Data saida:')
horaalmoco=('1:00')
datae = datetime.strptime(dataentrada,('%H:%M'))
datas = datetime.strptime(datasaida,('%H:%M'))
horaAlmoco = datetime.strptime(horaalmoco,('%H:%M'))


data=(1900, 1, 1)
diferenca = datas - datae
dif1 = datas - horaAlmoco
dif2 = datae - horaAlmoco 
dif3 = dif1 - dif2

total = ( dif3 - dif2)

print("Diferença em dias:", diferenca)
print(f'A jornada foi de {total}')
print(diferenca)
print(dif1)
print(dif2)
print(dif3)
print(data)
print(total)