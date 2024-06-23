import datetime
data_hoje = datetime.date.today()

def validar_data(data_texto):
    data_objeto = imput('insira data: ')
    """
    Converte a data no formato string para o formato datetime.date e valida se é a data de hoje.

    Args:
    data_texto: A data no formato string (por exemplo, "2024-06-23").

    Returns:
    True se a data for a data de hoje, False caso contrário.
    """
    try:
        data_objeto = datetime.datetime.strptime(data_texto, "%Y-%m-%d").date()
    except ValueError:
        return False

    return data_objeto == data_hoje
validar_data()
