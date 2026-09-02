import pandas as pd
import numpy as np


#Verificar versão da biblioteca pandas
print(pd.__version__)


# Criação de um DataFrame para a manipulação dos dados
dados = {
    "nome": ["Duan", "Vanthuir", "Alex", "Icaro", "Taylon", "Axl", "Ertow","Rafael","Amanda", "Marcio"],

    "Idade": [17,50,30,33,29,22,45,26,19,70],

    "Cidade": ["São Bento do Una", "Garanhuns", "Lajedo", "Lajedo", "São Bento do Una", "São Bento do Una", "Caruaru", "São Bento do Una", "São Bento do Una", "São Bento do Una" ],

    "Profissao": ["Estudante", "Professor", "Professor", "Professor", "Professor", "Estudante", "Professor", "Estudante", "Professor", "Professor"],

    "Salario": [200,5000,4000,3733,8333,8388,3863,9000,38363,8282]
}


df = pd.DataFrame(dados)

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


''' df["nome"] df[["nome", "salario"]]
    Seleciona uma coluna ou mais
'''
print("Agora estou selecionando uma e duas tabelas:")
print()
print(df["nome"])

print(df[["nome", "Salario"]])





print("-----EXERCICIOS-----")

print("Quantidade de linhas:")
# para mostrar a quantidade de linhas utilizamos df.shape
print(f"existem {df.shape[0]} linhas ta tabela")

print()

print("Quantidade de Colunas: ")
# Para mostrar a quantidade de colunas podemos utilizar df.shape
print(f"Exitem {df.shape[1]} colunas na tabela")

print()

print("Salario medio e idade media")
# para calcular a media podemos utilizar a funcao mean()

print(f"a media dos salrios é de {df["Salario"].mean()}")
print(f"a media das idades é de {df["Idade"].mean()}")

print("maior e menor salario")
# para calcular os valores maximos e minimos podemos utilizar as funcoes max() e min()

print(f"o maior salario foi de {df['Salario'].max()}")
print(f"o menor salario foi de {df['Salario'].min()}")

print("-----FILTROS-----")




# aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa