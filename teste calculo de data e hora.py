import datetime

# Cria um objeto datetime para a data e hora atual
agora = datetime.datetime.now()

# Exibe a data e hora atuais no formato ISO 8601
print(f"Data e hora atuais: {agora:%Y-%m-%dT%H:%M:%S}")

# Cria um objeto datetime para uma data e hora específicas
data_hora_especifica = datetime.datetime(2023, 3, 8, 14, 30)

# Exibe a data e hora específicas no formato ISO 8601
print(f"Data e hora específicas: {data_hora_especifica:%Y-%m-%dT%H:%M:%S}")

# Adiciona 10 dias à data e hora específicas
nova_data_hora = data_hora_especifica + datetime.timedelta(days=10)

# Exibe a nova data e hora no formato ISO 8601
print(f"Nova data e hora após adicionar 10 dias: {nova_data_hora:%Y-%m-%dT%H:%M:%S}")


# Solicita ao usuário que insira o número de horas trabalhadas
horas_trabalhadas = float(input("Insira o número de horas trabalhadas: "))

# Solicita ao usuário que insira o valor da hora trabalhada
valor_hora = float(input("Insira o valor da hora trabalhada: "))

# Calcula o valor total a ser pago
valor_total = horas_trabalhadas * valor_hora

# Exibe o valor total a ser pago
print(f"Valor total a ser pago: R$ {valor_total:.2f}")


# Solicita ao usuário que insira o horário de entrada no formato HH:MM
horario_entrada = input("Insira o horário de entrada (HH:MM): ")

# Solicita ao usuário que insira o horário de saída no formato HH:MM
horario_saida = input("Insira o horário de saída (HH:MM): ")
horario_almoço = ('1:00')

# Converte os horários de entrada e saída para objetos datetime
entrada = datetime.datetime.strptime(horario_entrada, '%H:%M')
saida = datetime.datetime.strptime(horario_saida, '%H:%M')
horarioAlmoço= datetime.datetime.strptime(horario_almoço, '%H:%M')


# Calcula a diferença entre os horários de entrada e saída
diferenca = saida -horarioAlmoço - entrada 

# Converte a diferença para horas e minutos
horas = diferenca.seconds // 3600
minutos = (diferenca.seconds % 3600) // 60

# Exibe o número de horas e minutos trabalhados
print(f"Horas trabalhadas: {horas} horas e {minutos} minutos")


# Solicita ao usuário que insira o horário de entrada no formato HH:MM
#horario_entrada = input("Insira o horário de entrada (HH:MM): ")

# Solicita ao usuário que insira o horário de saída no formato HH:MM
#horario_saida = input("Insira o horário de saída (HH:MM): ")
#horarioAlmoço= datetime.datetime.strptime(horario_almoço, '%H:%M')

# Converte os horários de entrada e saída para objetos datetime
#entrada = datetime.datetime.strptime(horario_entrada, '%H:%M')
#saida = datetime.datetime.strptime(horario_saida, '%H:%M')

# Calcula a diferença entre os horários de entrada e saída, subtraindo o horário do almoço
#diferenca = saida - horarioAlmoço - entrada

# Converte a diferença para horas e minutos
#horas = diferenca.seconds // 3600
#minutos = (diferenca.seconds % 3600) // 60

# Exibe o número de horas e minutos trabalhados
#print(f"Horas trabalhadas: {horas} horas e {minutos} minutos")
