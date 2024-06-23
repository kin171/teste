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
                validar_data_hoje()
        #return opcao_escolhida
            elif opcao_escolhida == 2:
                validar_hora()
        
          
            else:
                print('Opção inválida. Tente novamente.')
            
        except ValueError:
            print('Valor inválido. Digite um número inteiro (1 ou 2).')
            escolha()

    
     
def validar_data_hoje(dataentrada):  # sourcery skip: remove-unreachable-code
    dataentrada = input('Digite a data (dd/mm/aaaa): ')
    """
    Valida se a string representa a data de hoje no formato dd/mm/aaaa.

    Argumentos:
        data_str: A string que contém a data a ser validada.

    Retorno:
        True se a data for a data de hoje, False caso contrário.
    """
    
    try:
        data_obj = datetime.strptime(dataentrada, '%d/%m/%Y')
    except ValueError:
        print('DATA INVÁLIDA. FORMATO CORRETO: DD/MM/AAAA.')
    return dataentrada

    # Validação da data de hoje
    data_hoje = datetime.today()
if data_obj.day == data_hoje.day and data_obj.month == data_hoje.month and data_obj.year == data_hoje.year:
    
    else:
        print('A DATA INFORMADA NÃO É A DATA DE HOJE.')
    return False

# Exemplo de uso



if validar_data_hoje(dataentrada): # type: ignore
    print('Data válida: É a data de hoje!')
else:
    print('Data inválida.')


def validar_hora(hora_str):
    hora_str = input('Digite a hora (HH:MM): ')
    """
    Valida se a string representa uma hora no formato HH:MM.

    Argumentos:
    hora_str: A string que contém a hora a ser validada.

    Retorno:
    Objeto datetime representando a hora válida ou None se a hora for inválida.
    """
    try:
        hora_obj = datetime.strptime(hora_str, '%H:%M')
        return hora_obj
    except ValueError:
        print('FORMATO DE HORA INVÁLIDO. Use o formato HH:MM.')
    return None

# Exemplo de uso


if validar_hora(hora_str):
  print(f'Hora válida: {hora_str}')
else:
  print('Hora inválida.')
escolha()