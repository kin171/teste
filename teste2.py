from datetime import datetime, pandas
import csv
'''
date = input ('digite a data: \n')
datahj = datetime.today()
datas = datetime.strftime(datahj, '%d/%m/%Y')
print ('\n', date)
print (datas)
if date != datas:
    print('data invalida')
else:
    print('data valida:')    
'''
def converter_hora(hora_str):
    """
    Converte string no formato HH:MM para objeto datetime.
    """
    try:
        return datetime.datetime.strptime(hora_str, "%H:%M")
    except ValueError:
        raise ValueError(f"Formato de hora inválido: {hora_str}")

def calcular_tempo_servico(data_str, hora_str, turno_str, frota_str):
    """
    Calcula o tempo de serviço em horas a partir de data, hora, turno e frota.

    Argumentos:
        data_str (str): Data no formato DD/MM/AAAA.
        hora_str (str): Hora no formato HH:MM.
        turno_str (str): Turno (maiusculo ou minusculo).
        frota_str (str): Frota (maiusculo ou minusculo).

    Retorno:
        float: Tempo de serviço em horas.
    """
    # Convertendo data e hora para objetos datetime
    data_obj = datetime.datetime.strptime(data_str, "%d/%m/%Y")
    hora_obj = converter_hora(hora_str)

    # Calculando data e hora de início do turno
    if turno_str.lower() == "a":
        hora_inicio_turno = datetime.datetime(year=data_obj.year, month=data_obj.month, day=data_obj.day, hour=5, minute=0)
    elif turno_str.lower() == "t":
        hora_inicio_turno = datetime.datetime(year=data_obj.year, month=data_obj.month, day=data_obj.day, hour=13, minute=0)
    else:
        raise ValueError(f"Turno inválido: {turno_str}")

    # Calculando tempo de serviço em segundos
    tempo_servico_segundos = (hora_obj - hora_inicio_turno).total_seconds()

    # Convertendo para horas e retornando
    return tempo_servico_segundos / 3600

def formatar_tempo_servico(tempo_servico_horas):
    """
    Formata o tempo de serviço em horas para string HH:MM:SS.
    """
    horas, minutos, segundos = int(tempo_servico_horas), int((tempo_servico_horas % 1) * 60), int(((tempo_servico_horas % 1) * 60 * 60) % 60)
    return f"{horas:02}:{minutos:02}:{segundos:02}"

# Abrindo o arquivo CSV
with open("saida.csv", "r") as arquivo_csv:
    leitor_csv = csv.reader(arquivo_csv)

    # Ignorando a primeira linha (cabeçalho)
    next(leitor_csv)

    # Processando cada linha do arquivo
    for linha in leitor_csv:
        try:
            data_str, hora_str, turno_str, frota_str = linha
            tempo_servico_horas = calcular_tempo_servico(data_str, hora_str, turno_str, frota_str)
            tempo_servico_formatado = formatar_tempo_servico(tempo_servico_horas)

            print(f"Data: {data_str}, Hora: {hora_str}, Turno: {turno_str}, Frota: {frota_str}, Tempo de Serviço: {tempo_servico_formatado}")
        except ValueError as erro:
            print(f"Erro na linha {linha}: {erro}")

