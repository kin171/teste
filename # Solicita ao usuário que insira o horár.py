from datetime import datetime, timedelta
from os import write


duracao = timedelta(hours = 1)  # Soma 1 horas

dataentrada = input('Data entrada e hora:')
datasaida = input('Data saida e hora:')
horaalmoco=('1:00')
datae = datetime.strptime(dataentrada,('%d/%m/%Y %H:%M'))
datas = datetime.strptime(datasaida,('%d/%m/%Y %H:%M'))
horaAlmoco = datetime.strptime(horaalmoco,('%H:%M'))

diferenca = datas - datae
#dif1 = datas - horaAlmoco
dif2 = diferenca - duracao 
#dif3 = datae - dif2
open ('jornada agricola.txt', 'a')

dados = [datae, datas, diferenca]
def salvar_informacoes(dados, jornada agricola):
 # """
 # Função para salvar dados em um arquivo de texto.

  #Args:
     # dados: Uma lista de dados a serem salvos.
     # nome_arquivo: O nome do arquivo para salvar os dados.
  #"""
  with open('jornada agricola.txt', "a") as arquivo:
    for dado in dados:
      arquivo.write(dado + "\n")

# Exemplo de uso
#dados = ["Dado 1", "Dado 2", "Dado 3"]
salvar_informacoes(dados, "jornada agricola.txt")

#for dado in dados:
    #arquivo.write(dado + '\n')
jornada agricola.close()


#total = ( dif3 - dif2)
#print("Diferença em dias:", dif2)
print('A jornada foi de {}'.format(dif2))
#print(diferenca)
#print(dif1)
#print(dif2)
#print(dif3)
#print(data)
#print(total)import datetime
print (datae)
print (datas)