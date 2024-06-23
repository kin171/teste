from datetime import datetime, timedelta


escolha = input('Escolha qual informação vai entrar: \n 1 para data e hora de entrada: \n 2 para data e hora de saída: \n')
frotasLista = ["V1", "V2", "V3","B1","B2","PR",]
turnolista = ["A", "B", "C"]


def definirFrota():
    frota = "-"
    while frota not in frotasLista:
        frota = input('ex:  \n v1 para a van da vinhaça \n v2 para a van da vinhaça \n v3 para a van da vinhaça  \n b1 para a van da brigada 1  \n b2 para a van da brigada   \n pr para a van da preparo  \n Qual a frota da van?: ')
        frota = frota.upper()
        if frota not in frotasLista:
            print('\n Frota inválida \n')
    return frota
    
def definirTurno():
    turno = "-"
    while turno not in turnolista:
        turno = input('\n Qual o tuno?: ')
        turno = turno.upper()
        if turno not in turnolista:
            print('\n Turno inválido \n')
    return turno

def definirDataEntrada():
    dataentrada = input('\n Data entrada: ')
    horaEntrada = input('\n hora entrada: ')
    dataHoraStringEntrada = str(dataentrada) + " " + str(horaEntrada) 
    dataehora = datetime.strptime(dataHoraStringEntrada,('%d/%m/%Y %H:%M'))
    
    # ... (código para obter data e hora do usuário)
    
    try:
        dataehora = datetime.strptime(dataHoraStringEntrada, '%d/%m/%Y %H:%M')
    except ValueError:
        print('DATA OU HORA INVÁLIDA!')
        return None  # Retorna None se a data for inválida

    # ... (código para utilizar a data e hora válida)
         
    return datae

def definirDataSaida():
    datasaida = input('\n Data saida: ')
    horaSaida = input('\n Hora saida: ')
    dataHoraString = str(datasaida) + " " + str(horaSaida) 
    datas = datetime.strptime(dataHoraString,('%d/%m/%Y %H:%M'))
    return datas


frota = definirFrota()
turno = definirTurno()
datae = definirDataEntrada()
datas = definirDataSaida()

def escolhaInformacao():
    escolha = input('Escolha qual informação deseja alterar: \n'
                    '1. Data e hora de entrada\n'
                    '2. Data e hora de saída\n')

    while True:
        if escolha == '1':
            novaDataEntrada = definirDataEntrada()
            if novaDataEntrada:
                return novaDataEntrada, 'entrada'
            else:
                print('Falha ao obter data e hora de entrada válida.')
        elif escolha == '2':
            novaDataSaida = definirDataSaida()
            if novaDataSaida:
                return novaDataSaida, 'saida'
            else:
                print('Falha ao obter data e hora de saída válida.')
        else:
            print('Opção inválida. Tente novamente.')
            escolha = input('Escolha qual informação deseja alterar: \n'
                            '1. Data e hora de entrada\n'
                            '2. Data e hora de saída\n')
            
                    