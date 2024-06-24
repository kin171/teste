from datetime import datetime
date = input ('digite a data: \n')
datahj = datetime.today()
datas = datetime.strftime(datahj, '%d/%m/%Y')
print ('\n', date)
print (datas)
if date != datas:
    print('data invalida')
else:
    print('data valida:')    
