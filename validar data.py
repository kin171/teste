
from datetime import date, datetime, timedelta
import time
import re
def definirDataEntrada():
    """
    This Python function defines an entry date and time, checks if it is today, and returns the combined
    datetime object.
    :return: The function `definirDataEntrada()` is returning the variable `datae`, which is a datetime
    object representing the date and time input by the user.
    """
    dataentrada = input('\n Data entrada: ')
    horaEntrada = input('\n hora entrada: ')
    dataHoraStringEntrada = str(dataentrada) + " " + str(horaEntrada)
    datae = datetime.strptime(dataHoraStringEntrada,('%d/%m/%Y %H:%M'))
    datahj = datetime.date.today()

    # Check if the date is today
    if datae.date() == datahj:
        print("A data informada é hoje!")
    else:
        print("A data informada não é hoje.")

    return datae
definirDataEntrada()
