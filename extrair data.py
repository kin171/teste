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
    #extrair_data(dats)
'''
def extrair_data(dats):
    
    data_hora_str = dats
# Expressão regular para extrair a data
    regex_data = r"(\d{4})-(\d{1,2})-(\d{1,2})"

# Extraindo a data
    match = re.search(regex_data, data_hora_str)

    if match:
    # Extraindo os grupos da expressão regular (ano, mês, dia)
        ano, mes, dia = match.groups()

    # Convertendo os grupos para strings e formatando a data
        data_formatada = f"{dia}/{mes}/{ano}"
        print(f"Data extraída: {data_formatada}")
    else:
        print("Não foi possível extrair a data da string.")
        
    extraiar_data(data_hora_str)  # noqa: F821


print(dats)
'''