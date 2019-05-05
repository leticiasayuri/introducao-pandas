import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def truncar(bairro):
    return bairro[:3]


df = pd.read_csv("introducao\dados.csv")
print('DataFrame criado a partir da leitura de dados.csv\n', df)

print("\nVisualização das 5 primeiras linhas do DataFrame\n", df.head())

print("\nVisualização das 10 primeiras linhas do DataFrame\n", df.head(n=10))

print("\nVisualização das 5 primeiras linhas do DataFrame\n", df.tail())

print("\nListar os valores únicos da coluna Bairro\n", df["bairro"].unique())

print("\nContagem dos valores de uma coluna (Bairro)\n",
      df["bairro"].value_counts())

print("\nNormalização dos valores contados da coluna Bairro\n",
      df["bairro"].value_counts(normalize=True))

# Com Pandas, podemos agrupar os dados com base em alguns critérios,
# o que pode ser útil para resolver os mais amplos problemas.
print("\nAgrupamento do DataFrame pelos valores da coluna Bairro, com informação das médias agrupadas pelos valores da coluna Bairros\n",
      df.groupby("bairro").mean())

print("\nListar os valores da coluna PM2 (do agrupamento) em ordem crescente\n",
      df.groupby("bairro").mean()["pm2"].sort_values())

print("\nDeixar os nomes dos bairros com apenas os três primeiros caracteres, aplicando uma função aos dados\n",
      df["bairro"].apply(truncar))

print("\nDeixar os nomes dos bairros com apenas os três primeiros caracteres, aplicando uma função lamda aos dados\n",
      df["bairro"].apply(lambda x: x[:3]))

# Tratamento de dados incompletos
df2 = df.head()
print("\nDataFrame de 5 linhas, criado a partir do DataFrame principal\n", df2)

df2 = df2.replace({"pm2": {12031.25: np.nan}})
print("\nTratamento de dados incompletos no DataFrame df2\n", df2)

print("\nRemoção de linhas ou colunas que possuam up.nan\n", df2.dropna())

print("\nPreenchimento de valores NaN com outro valor específico\n", df2.fillna(99))

print("\nIndicação de quais valores são NaN e quais não são\n", df2.isna())
