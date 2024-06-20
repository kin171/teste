from datetime import datetime, timedelta

dataInicial=input('data inicial?')
datafinal=input('data final?')
n1=float(input('digite um valor:'))
n2=float(input('digite um valor :'))
sub=datetime(datafinal)-datetime(dataInicial)
s= (n1 + n2)
print(f'o valor de {s} ')
print('A soma de ',n1, 'mais',n2, 'é igual a',s)
print(f'A soma entre {n1} {n2} é igual {s}')
print('a subtração das horas é',sub)
n1=float(input('digite um valor'))
n2=float(input('digite um valor '))
s= n1 * n2
print(f'o valor e {s}')

