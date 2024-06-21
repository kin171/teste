a = "Caio"
b = 10
c = 5.05

bS=str(b)
cS=str(c)

dados = (a + ";" + bS + ";" + cS)
dadosS = str(dados)

#print(dados)

with open ("TesteArquivo.txt", "a") as arquivo:
    arquivo.write(dadosS, '\n')