from datetime import datetime, timedelta

# Inicialização de variavel
encerrar = 'n'
frotasLista = ["VA1", "VA2", "VA3","VB1","VB2","VB3","VC1","VC2","VC3","BR1","BR2","BR3","PR1","PR2","PR3"]
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
        frota = input('ex:  \n va para a van da vinhaça   \n vb para a van da vinhaça 2 \n vc para a van da vinhaça 3 \n br1 para a van da brigada 1 \n br2 para a van da brigada 2 \n pr1 para a van da preparo \n Qual a frota da van?')
        frota = frota.upper()
        if frota not in frotasLista:
            print('Frota inválida')
        else :
            def definirTurno():
                turno = "-"
                while turno not in turnolista:
                    turno = input('Qual o tuno?')
                    turno = turno.upper()
                if turno not in turnolista:
                    print('Turno inválido')
                return turno
  
    return frota


while  encerrar == 'n':
    duracao = timedelta(hours = 1)  # Soma 1 horas
    definirFrota()
    
    #turno = input('Qual o tuno?')
    #turno = turno.upper()
    #dataentrada = input('Data entrada e hora:')
    #datasaida = input('Data saida e hora:')
    #datae = datetime.strptime(dataentrada,('%d/%m/%Y %H:%M'))
    #datas = datetime.strptime(datasaida,('%d/%m/%Y %H:%M'))

    #horaNormal = timedelta(hours=7, minutes=20)
    #diferenca = datas - datae
    #jornada = diferenca - duracao 
    #print(jornada)
    #if jornada >= horaNormal:
        #horaextra = jornada - horaNormal
    #else:
        #horaextra = 0

    encerrar = input('Deseja encerrar o programa? (s/n): ')
    print ("TIXAU, BOCA NO PAU!!!!!")