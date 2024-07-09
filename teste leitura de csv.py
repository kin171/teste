import pandas as pd
'''
# Data específica para busca
data_busca = "26/06/2024"

# Lendo o arquivo CSV para um DataFrame
df = pd.read_csv("saida.csv")

# Filtrando o DataFrame por data
df_filtrado = df[df["data"] == data_busca]

# Verificando se o registro foi encontrado
if not df_filtrado.empty:
    # Acessando os dados do registro encontrado
    registro = df_filtrado.iloc[0]  # Assuming only one row matches the filter
    data = registro["data"]
    turno = registro["turno"]
    frota = registro["frota"]
    passageiros = registro["passageiros"]

    # Imprimindo as informações
    print(f"Data: {data}")
    print(f"Turno: {turno}")
    print(f"Frota: {frota}")
    print(f"Passageiros: {passageiros}")

    # Acessando outros dados (se necessário)
    # ...
else:
    print(f"Registro com data '{data_busca}' não encontrado.")
'''

''' 
# Lendo o arquivo CSV e armazenando em um DataFrame
df = pd.read_csv("saida.csv")

# Verificando o conteúdo do DataFrame
print(df)


dataprocura = input('qual data vc procura:')


# (Assumindo que 'df' é o DataFrame criado a partir do CSV)

# 1. Buscar pessoas em São Paulo:
pessoas_sp = df[df["data"].like("%{}%".format(dataprocura))]

print(pessoas_sp["data"])  # Exibe apenas a coluna 'Nome'


# 2. Acessar idade por nome:
nome = dataprocura()  # Altere para o nome desejado
idade_beatriz = df[df["data"] == nome]["turno"].values[0]
print(f"Idade de {nome}: {idade_beatriz}")

# 3. Obter cidades de pessoas com mais de 30 anos:
maiores_30 = df[df["Idade"] > 30]["Cidade"]
print(maiores_30)



# ... (Leitura do CSV e obtenção da data da busca como antes)

# Buscando a linha com a data especificada
linha_encontrada = df[df["data"] == dataprocura]

# Verificando se a data foi encontrada
if not linha_encontrada.empty:
    # Exibindo colunas específicas da linha encontrada
    print(linha_encontrada[["data", "outra_coluna", "outra_coluna2"]].to_string(index=False))
else:
    # ... (Mensagem de registro não encontrado)
    print ('nao achou ')

# Lendo o arquivo CSV e armazenando em um DataFrame
df = pd.read_csv("saida.csv")

# Obtendo a data da busca
dataprocura = input("Qual data você procura? ")

# Buscando a linha com a data especificada
linha_encontrada = df[df["data"] == dataprocura]

# Verificando se a data foi encontrada
if not linha_encontrada.empty:
    # Exibindo todas as informações da linha encontrada
    print(linha_encontrada.to_string(index=False))
else:
    print(f"Registro com data '{dataprocura}' não encontrado.")
'''