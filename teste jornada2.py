from datetime import datetime, timedelta, csv


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
    corrige = 'N'
    entrada = '-'
    while datahora == ' ':
        try:    
            dataentrada = input('DIGITE A DATA DE ENTRADA: \n DD/MM/AAAA \n')
            datahj = datetime.today()
            datahjstr = datetime.strftime(datahj, '%d/%m/%Y')
            if dataentrada != datahjstr:
                print('DATA INVALIDA')
            elif dataentrada == datahjstr:
                horaentrada = input('DIGITE A HORA DE ENTRADA; \n HH:MM: \n')
                datahora1 = str(dataentrada)+' '+str(horaentrada)
                datahora = datetime.strptime(datahora1, '%d/%m/%Y %H:%M')
                
                with open("jornada-agricola.csv", "a") as arquivo_csv:
                    arquivo_csv.write(datahora,'\n')
                print(datahora)    

                
            else:
                print('data ou hora invalida')
        except ValueError:
            return False

escolha()                