from datetime import datetime
hora = datetime.now() 
horaentrada = input('Digite a hora: HH:MM \n')
horaentradastr = datetime.strptime(horaentrada, '%H:%M')
formathora = datetime.strftime(hora, ('%H:%M'))
if formathora == horaentrada:
    print (horaentradastr)
    print (horaentrada)
else:
    print ('hora invalida')

print(hora.strftime("%H:%M"))
