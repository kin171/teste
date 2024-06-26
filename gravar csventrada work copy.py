frotasLista = ["V1", "V2", "V3","B1","B2","PR"]
turnolista = ["A", "B", "C"]
 
import csv
from datetime import datetime

def definirFrota():
    frota = "-"
    while frota not in frotasLista:
        frota =  input('ex:  \n v1 para a van da vinhaça   \n v2 para a van da vinhaça 2 \n v3 para a van da vinhaça 3 \n b1 para a van da brigada 1 \n b2 para a van da brigada 2 \n pr para a van da preparo \n Qual a frota da van?: ')
        frota = frota.upper()
        if frota not in frotasLista:
            print('\n Frota inválida \n')
    return frota
    
def definirTurno():
    turno = "-"
    while turno not in turnolista:
        turno = input('\n Qual o tuno?: ')
        turno = turno.upper()
        if turno not in turnolista:
            print('\n Turno inválido \n')
    return turno

def calcularHoraExtra(jornada):
    horaNormal = timedelta(hours=7, minutes=20)
    if jornada >= horaNormal:
        horaextra = jornada - horaNormal
    else:
        horaextra = 0

    return horaextra

def formatarValoresString (frota, turno, datae, datas, jornada, horaextra):
    valores = str(frota) + ';' + str(turno) + ';' + str(datae) + ';'+ str(datas)+ ';' + str(jornada) + ';'+ str(horaextra)
    return valores



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
    
    while True:
        try:
            # Validando a data de entrada
            data_str = input("Digite a data no formato dd/mm/aaaa: ")
            data_obj = datetime.strptime(data_str,'%d/%m/%Y')         
            definirFrota()
            definirTurno()
            
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
                data_hora_completa = f"{data_formatada};{hora_entrada};{Turno};{definirFrota}"

                # Gravando dados no arquivo CSV
                with open("entrada.csv", "a", newline="") as arquivo_csv:
                    escritor_csv = csv.writer(arquivo_csv)
                    escritor_csv.writerow([data_hora_completa])
                    corrigir(encerrar = 'N')
                    print(f"Dados gravados com sucesso: {data_hora_completa}")

                break  # Interrompendo o loop while

            else:
                print("Data passada, entrada não permitida.")

        except ValueError as erro:
            print(f"Erro: {erro}")
        break    

def datasaida():
    
    while True:
        try:
            # Validando a data de entrada
            data_str = input("Digite a data no formato dd/mm/aaaa: ")
            data_obj = datetime.strptime(data_str,'%d/%m/%Y')         
            definirFrota()
            definirTurno()
            
            # Formatando data para string
            data_formatada = data_obj.strftime("%d/%m/%Y")

            # Validando se a data é igual à data atual
            data_hj = datetime.today()
            datahj = datetime.strftime(data_hj, '%d/%m/%Y')
            
            if datahj == data_str:
                hora_saida = input("Digite a hora de saida (HH:MM): ")

                # Validando formato da hora
                try:
                    hora_obj = datetime.strptime(hora_saida, "%H:%M")
                except ValueError:
                    raise ValueError("Formato de hora inválido!")

                # Formatando data e hora para string completa
                data_hora_completa = f"{data_formatada};{hora_saida};{turno};{frota}"
 
                # Gravando dados no arquivo CSV
                with open("saida.csv", "a", newline="") as arquivo_csv:
                    escritor_csv = csv.writer(arquivo_csv)
                    escritor_csv.writerow([data_hora_completa])

                print(f"Dados gravados com sucesso: {data_hora_completa}")
                break  # Interrompendo o loop while

            else:
                print("Data passada, entrada não permitida.")

        except ValueError as erro:
            print(f"Erro: {erro}")
        break            



def corrigir(encerrar):
    while  encerrar == 'N':

        # Inputs____________________________
        frota = definirFrota()
        turno = definirTurno()
        datae = DataEntrada() 
        datas = DataSaida()
        #____________________________________
        # Calculos___________________________
        jornada = calcularJornada(datae, datas)
        horaextra = calcularHoraExtra(jornada)
        #____________________________________
        #Valores Formatados_____________________
        valores = formatarValoresString(frota, turno, datae, datas, jornada, horaextra)
        print(valores)
        #_______________________________________

        confirma = input("\n Dados corretos?(s/n) ")
        confirma = confirma.upper()
        
        while confirma == "N":
            if confirma == "N":

                #TODO Corrigir validação de caso
                corrige = int(input("\n Qual dado quer alterar?\n 1 para Frota \n 2 para Turno \n 3 para Data e Hora Entrada \n 4 para Data e Hora Saida \n 0 para Continuar sem mais alterações: "))
                if corrige == 1:
                    frota = definirFrota()
                    continue
                elif corrige == 2:
                    turno = definirTurno()
                    continue
                elif corrige == 3:
                    datae = definirDataEntrada() 
                    continue
                elif corrige == 4:
                    datas = definirDataSaida()
                    continue

            jornada = calcularJornada(datae, datas)
            horaextra = calcularHoraExtra(jornada)
            
            valores = formatarValoresString(frota, turno, datae, datas, jornada, horaextra)
            print(valores)

            confirma = input("\n Dados corretos?(s/n) ")
            confirma = confirma.upper()

        encerrar = input('Deseja encerrar o programa? (s/n): ')
        encerrar = encerrar.upper()
    print ("Volte sempre!!")
escolha()