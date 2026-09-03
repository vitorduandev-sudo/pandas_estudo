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

# print(df.head())

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


''' df["nome"] df[["nome"]]
    Seleciona uma coluna ou mais
'''
print("Agora estou selecionando uma e duas tabelas:")
print()
# print(df["nome"])

# print(df[["nome", "Salario"]])





print("-----EXERCICIOS-----")

print("Quantidade de linhas:")
# para mostrar a quantidade de linhas utilizamos df.shape
print(f"existem {df.shape[0]} linhas ta tabela")

print()

print("Quantidade de Colunas: ")
# Para mostrar a quantidade de colunas podemos utilizar df.shape
print(f"Exitem {df.shape[1]} colunas na tabela")

print()

# print("Salario medio e idade media")
# # para calcular a media podemos utilizar a funcao mean()

# print(f"a media dos salrios é de {df["Salario"].mean()}")
# print(f"a media das idades é de {df["Idade"].mean()}")

# print("maior e menor salario")
# # para calcular os valores maximos e minimos podemos utilizar as funcoes max() e min()

# print(f"o maior salario foi de {df['Salario'].max()}")
# print(f"o menor salario foi de {df['Salario'].min()}")

print("-----FILTROS-----")

