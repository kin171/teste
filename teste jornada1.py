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
    dataentrada = input('DIGITE A DATA: \n DD/MM/AAAA:')
    dataentradastr = datetime.strptime(dataentrada, '%d/%m/%Y')
    datahj = datetime.today()
    datahjstr = datetime.strftime(datahj, '%d/%m/%Y')
    if dataentrada != datahjstr:
        print: ('Data invalida')        
        dataentrada()
    else:
        horaentrada = input('Digite a hora: HH:MM \n')
        horastr = datetime.strptime(horaentrada, '%H:%M')
        datahorastr = dataentradastr + ' '+ horastr
        print(datahorastr)
        return datahorastr 
       
        

def datasaida():
    print('deu certo ate aqui!!!!')
escolha()
        
     