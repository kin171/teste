import csv
from datetime import datetime

def dataentrada():
    while True:
        try:
            # Validando a data de entrada
            data_str = input("Digite a data no formato dd/mm/aaaa: ")
            data_obj = datetime.strptime(data_str,'%d/%m/%Y')         

            # Formatando data para string
            data_formatada = data_obj.strftime("%d/%m/%Y")

            # Validando se a data é igual à data atual
            data_hj = datetime.today()
            datahj = datetime.strftime(data_hj, '%d/%m/%Y')
            
            if datahj == data_str:
                print("Data atual, digite a hora de entrada:")
                hora_entrada = input("Digite a hora de entrada (HH:MM): ")

                # Validando formato da hora
                try:
                    hora_obj = datetime.strptime(hora_entrada, "%H:%M")
                except ValueError:
                    raise ValueError("Formato de hora inválido!")

                # Formatando data e hora para string completa
                data_hora_completa = f"{data_formatada};{hora_entrada};A;va"

                # Gravando dados no arquivo CSV
                with open("entrada.csv", "a", newline="") as arquivo_csv:
                    escritor_csv = csv.writer(arquivo_csv)
                    escritor_csv.writerow([data_hora_completa])

                print(f"Dados gravados com sucesso: {data_hora_completa}")
                break  # Interrompendo o loop while

            else:
                print("Data passada, entrada não permitida.")

        except ValueError as erro:
            print(f"Erro: {erro}")

dataentrada()
