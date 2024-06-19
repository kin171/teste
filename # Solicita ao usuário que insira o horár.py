import datetime

# Solicita ao usuário que insira o horário de entrada no formato HH:MM
horario_entrada = input("Insira o horário de entrada (HH:MM): ")

# Solicita ao usuário que insira o horário de saída no formato HH:MM
horario_saida = input("Insira o horário de saída (HH:MM): ")
horario_almoco= ('1:00')
horarioAlmoço= datetime.datetime.strptime(horario_almoco, '%H:%M')

# Converte os horários de entrada e saída para objetos datetime
entrada = datetime.datetime.strptime(horario_entrada, '%H:%M')
saida = datetime.datetime.strptime(horario_saida, '%H:%M')

# Calcula a diferença entre os horários de entrada e saída, subtraindo o horário do almoço
from datetime import datetime

# Cria uma data
data = datetime.date(1900, 1, 1)

# Cria uma hora
#hora = datetime.time(14, 30)

diferenca = saida - entrada
# Combina a data e a hora
data_e_hora = datetime.combine(data, diferenca)

# Exibe a data e hora combinadas
print(data_e_hora)


#diferencaFormat = datetime.date.strftime(diferenca,'%H:%M')
#diferencaAlmoco = diferenca - horarioAlmoço
#dif2=datetime.datetime.strptime(diferenca, '%H:%M')
#dif1=diferenca- entrada
print(entrada)
print(saida)
print(diferenca)
# Converte a diferença para horas e minutos
#horas = dif1.seconds // 3600
#minutos = (dif1.seconds % 3600) // 60

# Exibe o número de horas e minutos trabalhados
#print(f"Horas trabalhadas: {horas} horas e {minutos} minutos")
