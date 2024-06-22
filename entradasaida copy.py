from datetime import datetime, timedelta

# Inicialização de variavel
encerrar = 'N'


frotasLista = ["VA1", "VA2", "VA3", "VB1", "VB2","VB3", "VC1","VC2","VC3","BRA1","BRA2","BRA3","BRB1","BRB2","BRB3","PR1","PR2","PR3"]
turnolista = ["A", "B", "C"]
# Definição de funções

def salvarDados(frota, turno, datae, datas, jornada, horaextra):
    dado = str(frota) + ';' + str(turno) + ';' + str(datae) + ';'+ str(datas)+ ';' + str(jornada) + ';'+ str(horaextra) 
    # Substitua com seus valores reais
    with open('jornada_agricola.txt', 'a') as arquivo:
    # Escrevendo os dados no arquivo
        arquivo.write(dado + '\n')  # Adiciona quebra de linha no final

def definirFrota():
    frota = "-"
    while frota not in frotasLista:
        frota = input('ex:  \n va1 para a van da vinhaça \n va2 para a van da vinhaça \n va3 para a van da vinhaça  \n vb1 para a van da vinhaça  \n vb2 para a van da vinhaça  \nvb3 para a van da vinhaça  \n vc1 para a van da vinhaça \n vc2 para a van da vinhaça \n vc3 para a van da vinhaça  \n br1 para a van da brigada  \n br2 para a van da brigada \n br3 para a van da brigada  \n pr1 para a van da preparo \n pr1 para a van da preparo \n pr para a van da preparo \n Qual a frota da van?: ')
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
    datae = datetime.strptime(dataHoraStringEntrada,('%d/%m/%Y %H:%M'))
    return datae

def definirDataSaida():
    datasaida = input('\n Data saida: ')
    horaSaida = input('\n Hora saida: ')
    dataHoraString = str(datasaida) + " " + str(horaSaida) 
    datas = datetime.strptime(dataHoraString,('%d/%m/%Y %H:%M'))
    return datas

def calcularJornada(datae, datas):
    duracao = timedelta(hours = 1) # Soma 1 horas
    diferenca = datas - datae
    jornada = diferenca - duracao
    return jornada

def calcularHoraExtra(jornada):
    horaNormal = timedelta(hours=7, minutes=20)
    if jornada >= horaNormal:
        horaextra = jornada - horaNormal
    else:
        horaextra = 0

    return horaextra

def formatarValoresString (frota, turno, datae, datas, jornada, horaextra):
    valores = str(frota) + ';' + str(turno) + ';' + str(datae) + ';'+ str(datas)+ ';' + str(jornada) + ';'+ str(horaextra)
    return valores

# Main____________________________________________________
while  encerrar == 'N':

# Inputs____________________________
    frota = definirFrota()
    turno = definirTurno()
    datae = definirDataEntrada() 
    datas = definirDataSaida()
#____________________________________
# Calculos___________________________
    jornada = calcularJornada(datae, datas)
    horaextra = calcularHoraExtra(jornada)
#____________________________________
#Valores Formatados_____________________
    valores = formatarValoresString(frota, turno, datae, datas, jornada, horaextra)
    print(valores)
#_______________________________________

    confirma = input("\n Dados corretos?(s/n) ")
    confirma = confirma.upper()
    print(confirma)
    for confir in confirma:
        if confir == 'N':
            
            while confirma == "N":
                if confirma == "N":

                    #TODO Corrigir validação de caso
                    corrige = input("\n Qual dado quer alterar?\n 1 para Frota \n 2 para Turno \n 3 para Data e Hora Entrada \n 4 para Data e Hora Saida \n ")
                    if int(corrige) == 1:
                        frota = definirFrota()
                        confir = input("\n Dados corretos?(s/n) ")
                        confir = confir.upper()
                    #corrigir     
                    elif int(corrige) == 1:
                        confir = input("\n Dados corretos?(s/n) ")
                        confir = confir.upper()  
                        break
                    else :          
                        break
                elif int(corrige) == 2:
                    turno = definirTurno()
                    confir = input("\n Dados corretos?(s/n) ")
                    confir = confir.upper()
                    break
                elif int(corrige) == 3:
                    datae = definirDataEntrada()                        
                    confir = input("\n Dados corretos?(s/n) ")
                    confir = confir.upper()
                    break
                elif int(corrige) == 4:
                    datas = definirDataSaida()
                    confir = input("\n Dados corretos?(s/n) ")
                    confir = confir.upper()
                    break
                else:
                    break

        jornada = calcularJornada(datae, datas)
        horaextra = calcularHoraExtra(jornada)
        
        valores = formatarValoresString(frota, turno, datae, datas, jornada, horaextra)
        print(valores)

        confirma = input("\n Dados corretos?(s/n) ")
        confirma = confirma.upper()
        
    encerrar = input('Deseja encerrar o programa? (s/n): ')
    encerrar = encerrar.upper()
    print ("Volte sempre!!")