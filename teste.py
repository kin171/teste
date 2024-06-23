from datetime import datetime, timedelta
def definirDataEntrada():
    data_valida = False
    while not data_valida:
        dataentrada = input('\n Data entrada: ')
        horaEntrada = input('\n Hora entrada: ')
        dataHoraStringEntrada = str(dataentrada) + " " + str(horaEntrada)

        try:
            dataehora = datetime.strptime(dataHoraStringEntrada, '%d/%m/%Y %H:%M')

            # Validação: Data no futuro
            if dataehora < datetime.today():
                print('DATA NO PASSADO. INFORME UMA DATA FUTURA.')
            elif dataehora.day != datetime.today().day:
                print('DIA DA ENTRADA DIFERENTE DO DIA DE HOJE.')
            else:
                data_valida = True  # Data válida, sai do loop
        except ValueError:
            print('DATA OU HORA INVÁLIDA! FORMATO CORRETO: DD/MM/AAAA HH:MM')

    return dataehora
def definirDataSaida():
    datasaida = input('\n Data saida: ')
    horaSaida = input('\n Hora saida: ')
    dataHoraString = str(datasaida) + " " + str(horaSaida) 

    try:
        datas = datetime.strptime(dataHoraString, '%d/%m/%Y %H:%M')
        # Validação: Data no futuro
        if datas < datetime.now():
            print('DATA NO PASSADO. INFORME UMA DATA FUTURA.')
            return None
        # Validação: Hora dentro do horário comercial
        elif datas.hour < 6 or datas.hour > 22:
            print('HORA FORA DO HORÁRIO COMERCIAL (6H-22H).')
            return None

    except ValueError:
        print('DATA OU HORA INVÁLIDA! FORMATO CORRETO: DD/MM/AAAA HH:MM')
        return None

    return datas
definirDataEntrada() 