from datetime import datetime

data = input("Digite a data no formato dd/mm/aaaa: ")
dats = datetime.strptime(data, "%d/%m/%Y") 
print (dats)
datahj = datetime.today()
datae = datetime.strftime(datahj,'%d/%m/%Y')
print (datae)


if data == datae:
    print("A data informada é hoje!")
else:
    print("A data informada não é hoje.")
   