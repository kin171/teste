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

def escolhainformação():
    escolha = '-'
    
    while escolhainformação not in escolha:
        if escolha == 1 :
            datae = definirDataEntrada()
            datae == ('%d/%m/%Y %H:%M')            
            print = ('Data ou hora invalida:')            
        elif escolha == 2:
            datas = definirDataSaida()
            datas == ('%d/%m/%Y %H:%M')
            print = ('Data ou hora invalida:')
            
                    