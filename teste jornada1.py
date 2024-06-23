from datetime import datetime, timedelta




def validar_data_hoje(data_str):
    """
    Valida se a string representa a data de hoje no formato dd/mm/aaaa.

    Argumentos:
        data_str: A string que contém a data a ser validada.

    Retorno:
        True se a data for a data de hoje, False caso contrário.
    """
    try:
        data_obj = datetime.strptime(data_str, '%d/%m/%Y')
    except ValueError:
        print('DATA INVÁLIDA. FORMATO CORRETO: DD/MM/AAAA.')
        return False

    # Validação da data de hoje
    data_hoje = datetime.today()
    if data_obj.day == data_hoje.day and data_obj.month == data_hoje.month and data_obj.year == data_hoje.year:
        return True
    else:
        print('A DATA INFORMADA NÃO É A DATA DE HOJE.')
        return False

# Exemplo de uso
 data_str = input('Digite a data (dd/mm/aaaa): ')
hora_str = input('Digite a hora (HH:MM): ')

if validar_data_hoje(data_str):
    print('Data válida: É a data de hoje!')
else:
    print('Data inválida.')


def validar_hora(hora_str):
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
