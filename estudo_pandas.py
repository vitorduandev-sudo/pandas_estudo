import pandas as pd
import numpy as np


#Verificar versão da biblioteca pandas
print(pd.__version__)


# Criação de um DataFrame para a manipulação dos dados
df = pd.read_csv("dataset_avicola_simulado.csv")

df = pd.DataFrame(df)

# print(df)

print("----------INICIO----------")

print()

print(df.head())

print()
print()



''' df.info()
    Mostra as informaçoes da tabela:
    * Quantidade de linhas
    * Nomes das colunas
    * Tipos dos dados
    * Valores Vazios
'''
print("Agora estou mostrando as informaçoes do DataSet:")
print()
print(df.info())

print()
print()


''' df.describe()
    Mostra a descrição da tabela
    * Media
    * Valor Minimo
    * Valor Maximo
    * quantidade
    * Desvio padrao
    * etc
''' 
print("Agora estou mostrando as descricoes das tabelas:")
print()
print(df.describe())

print()
print()


''' df.shape()
    Mostra a quantidade de linhas e colunas
    Saida:
    (x,y)
    x = Linhas
    y = colunas
'''
print("Agora estou mostrando a quantidade de linhas e colunas:")
print()
print(df.shape)

print()
print()


''' df.columns
    Mostra os nomes das colunas
'''
print("Agora estou mostrando os nomes das colunas:")
print()
print(df.columns)

print()
print()


''' df["temperatura_ar"] df[["temperatura_ar, amonia"]]
    Seleciona uma coluna ou mais
'''
print("Agora estou selecionando uma e duas tabelas:")
print()
print(df["temperatura_ar"])

print(df[["temperatura_ar", "amonia"]])





print("-----EXERCICIOS-----")

print("Quantidade de linhas:")
# para mostrar a quantidade de linhas utilizamos df.shape
print(f"existem {df.shape[0]} linhas ta tabela")

print()

print("Quantidade de Colunas: ")
# Para mostrar a quantidade de colunas podemos utilizar df.shape
print(f"Exitem {df.shape[1]} colunas na tabela")

print()

print("temperatura_ar media e amonia media")
# # para calcular a media podemos utilizar a funcao mean()

print(f"a media da temperatura do ar é de {df["temperatura_ar"].mean()}")
print(f"a media da amonia é de {df["amonia"].mean()}")

print()

print("maior e menor temperatura_ar")
# para calcular os valores maximos e minimos podemos utilizar as funcoes max() e min()

print(f"o maior temperatura_ar foi de {df['temperatura_ar'].max()}")
print(f"o menor temperatura_ar foi de {df['temperatura_ar'].min()}")

print("-----FILTROS-----")

print("todos registros que tiveram a temperatura_ar maior que 30")
print(df[df["temperatura_ar" ] > 30])

print()

print("todos registros que tiveram a amonia maior que 10")
print(df[df["amonia"] > 10])

print()

print("todos registros que tiveram a temperatura_ar menor que 25")
print(df[df["temperatura_ar"] < 25])

print()

print("todos registros que tiveram a amonia igual a 5")
print(df[df["amonia"] == 5])

print()

print("todos registros que tiveram a temperatura_ar maior ou igual a 30")
print(df[df["temperatura_ar"] >= 30])

print()

print("todos registros que tiveram a temperatura_ar maior que 30 E amonia > 10")
print(df[(df["temperatura_ar"] > 30) & (df["amonia"] > 10)])

print()

print("todos registros que tiveram a temperatura_ar menor que 25 E amonia menor que 5")
print(df[(df["temperatura_ar"] < 25) & (df["amonia"] < 5)])

print()

print("todos registros que tiveram a temperatura_ar maior que 35 OU amonia maior que 15")
print(df[(df["temperatura_ar"] > 35) | (df["amonia"] > 15)])

print()

print("todos registros que tiveram a temperatura_ar maior que 25 E temperatura_ar menor que 30")
print(df[(df["temperatura_ar"] > 25) & (df["temperatura_ar"] < 30)])

print()

print("Encontre todos os registros onde amonia maior que 10 e mostre a media desse registro")
print(f"a media desses registros é de: {df[df["amonia"] > 10] ["amonia"].mean():.2f}")

print()

print("Descubra a maior concentração de amonia somente quando: temperatura_ar for maior que 30")
print(f"a maior concentracao de amonia nesse intervalo foi de {df[df["temperatura_ar"] > 30] ["temperatura_ar"].max():.2f}")


print("------TREINAMENTO DIA 03/09/26")
print()

print("Mostre quanros registros existem no DataSet:")
print(f"Existem {df.shape[0]} registros no dataset")

print()

print("Calcule a média da coluna temperatura_ar:")
print(f"A media das temperaturas da coluna temperatura_ar é de {df["temperatura_ar"].mean():.2f}")

print()

print("Calcule a média da coluna amonia:")
print(f"A media na coluna amonia foi de {df['amonia'].mean()}")

print()

print("Descubra a maior temperatura registrada:")
print(f"A maior temperatura registrada foi de {df['temperatura_ar'].max()}")

print()

print("Descubra a menor temperatura registrada")
print(f"A menor temperatura registrada foi de {df['temperatura_ar'].min()}")

print()

print("Descubra a menor concentração de amônia registrada")
print(f"A menor concentração de amonia utilizada foi de {df['amonia'].min()}")

print("Mostre somente as colunas: timestamp, temperatura_ar, umidade_relativa")
print(df[["timestamp", "temperatura_ar", "umidade_relativa"]])

print()

print("Mostre somente: amonia, temperatura_globo_negro, itgu")
print(df[["amonia", "temperatura_globo_negro", "itgu"]])

print()

print("Descubra o tipo de dado (dtype) de cada coluna.")
print(df.dtypes)

print("Descubra quantos valores únicos existem na coluna timestamp")
print(f"existem {df["timestamp"].nunique()} valores unicos na coluna")

print()

print("Descubra se existem valores nulos em alguma das 7 colunas.")
print(df.isnull().sum())

print("Calcule a média de: temperatura_ar, umidade_relativa, amonia, temperatura_globo_negro, ponto_orvalho, itgu")
print(df[["temperatura_ar", "umidade_relativa", "amonia", "temperatura_globo_negro", "ponto_orvalho", "itgu"]].mean())

print()

print("Descubra a maior umidade relativa:")
print(f"A maior umidade relativa foi de {df["umidade_relativa"].max()}")

print()

print("Descubra a menor umidade relativa.")
print(f"A menor umidade relativa foi de {df["umidade_relativa"].min()}")

print()

print("Descubra a maior temperatura de globo negro.")
print(f"A maior temperatura do globo negro foi de {df["temperatura_globo_negro"].max()}")

print("Descubra o maior valor de ITGU.")
print(f"o maior valor do itgu foi de {df["itgu"].max()}")

print("Descubra o menor valor de ITGU.")
print(f"o menor valor do itgu foi de {df['itgu'].min()}")






