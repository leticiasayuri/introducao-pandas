import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.DataFrame({'Aluno': ["Wilfred", "Abbie", "Harry", "Julia", "Carrie"],
                   'Faltas': [3, 4, 2, 1, 4],
                   'Prova': [2, 7, 5, 10, 6],
                   'Seminário': [8.5, 7.5, 9.0, 7.5, 8.0]})
print(df)

print(df.dtypes)

print(df.columns)

print(df["Seminário"])

print(df.describe())

# Ordenação de DataFrame
print(df.sort_values(by="Seminário"))

print(df)

# Seleção de valores pelo index
print(df.loc[3])

# Seleção de acordo com critérios condicionais
# Boolean Indexing

# Seleção das linhas em que o valor da coluna Seminário seja acima de 8.0
print(df[df["Seminário"] > 8.0])

# Condições de múltiplas colunas (deve-se usar operadores bitwise)

# Seleção das linhas em que o valor da coluna Seminário seja acima de 8.0 
# e o valor da coluna Prova não seja menor que 3
print(df[(df["Seminário"] > 8.0) & (df["Prova"] > 3)])
