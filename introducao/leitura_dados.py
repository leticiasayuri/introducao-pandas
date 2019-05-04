import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("introducao\dados.csv")
print('DataFrame criado a partir da leitura de dados.csv\n', df)

print("\nVisualização das 5 primeiras linhas do DataFrame\n", df.head())

print("\nVisualização das 10 primeiras linhas do DataFrame\n", df.head(n=10))

print("\nVisualização das 5 primeiras linhas do DataFrame\n", df.tail())

print("\nListar os valores únicos da coluna Bairro\n", df["bairro"].unique())
