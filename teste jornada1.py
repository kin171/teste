 from datetime import datetime, timedelta


# type: ignore
def escolha():
    """
    Apresenta um menu de opções e retorna a escolha do usuário.

    Retorno:
    Inteiro representando a opção escolhida (1 para data/hora de entrada ou 2 para data/hora de saída).
    """
    while True:
        try:
            opcao_escolhida = int(input('Escolha qual informação vai entrar: \n 1 para data e hora de entrada: \n 2 para data e hora de saída: \n'))
            if opcao_escolhida == 1:
                dataentrada()
        #return opcao_escolhida
            elif opcao_escolhida == 2:
                datasaida()
            else:
                print('Opção inválida. Tente novamente.')
            
        except ValueError:
            print('Valor inválido. Digite um número inteiro (1 ou 2).')
            escolha()


    
def dataentrada():
    while True:
        try:
            dataentrada = input('DIGITE A DATA ENTRADA: \n DD/MM/AAAA:')
            dataentradastr = datetime.strptime(dataentrada, '%d/%m/%Y')
            datahj = datetime.today()
            datahjstr = datetime.strftime(datahj, '%d/%m/%Y')
            if dataentrada != datahjstr:
                print ('Data invalida')            
                
            elif dataentrada == datahjstr:
                horaentrada = input('Digite a hora ENTRADA: HH:MM \n')
                horastr = datetime.strptime(horaentrada, '%H:%M')
                datahorastr = str(dataentradastr) + ' '+ str(horastr)
                dataentradastr = datetime.strptime(datahorastr, '%d/%m/%Y %H:%M')
                print(dataentradastr)
            else:
                print(dataentradastr)               
        except ValueError:
            print('pulou direto')
            
        

def datasaida():
    while True:
        try:
            datasaida = input('DIGITE A DATA SAIDA: \n DD/MM/AAAA:')
            datasaidastr = datetime.strptime(datasaida, '%d/%m/%Y')
            datahj = datetime.today()
            datahjstr = datetime.strftime(datahj, '%d/%m/%Y')
            if datasaida != datahjstr:
                print ('Data invalida') 
                          
                
            elif datasaida == datahjstr:
                horaentrada = input('Digite a hora SAIDA: HH:MM \n')
                horastr = datetime.strptime(horaentrada, '%H:%M')
                datahorastr = str(datasaidastr) + ' '+ str(horastr)
                datahorastr = datetime.strptime(datahorastr,'%d/%m/%Y %H:%M')
                print(datahorastr)
                break
            else:
                print(datahorastr)  
        except ValueError:
            print(' pulou aqui')
        
escolha()