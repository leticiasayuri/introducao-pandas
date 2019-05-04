import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.DataFrame({'Aluno': ["Wilfred", "Abbie", "Harry", "Julia", "Carrie"],
                   'Faltas': [3, 4, 2, 1, 4],
                   'Prova': [2, 7, 5, 10, 6],
                   'Seminário': [8.5, 7.5, 9.0, 7.5, 8.0]})
print("DataFrame\n", df, "\n")

print("Tipos no DataFrame\n", df.dtypes, "\n")

print("Colunas\n", df.columns, "\n")

print("Valores da coluna Seminário\n", df["Seminário"], "\n")

print("Informações matemáticas\n", df.describe(), "\n")

# Ordenação de DataFrame
print("Ordenação pela coluna Seminário\n",
      df.sort_values(by="Seminário"), "\n")

# Seleção de valores pelo index
print("Selação de valores por índice (índice 3)\n", df.loc[3], "\n")

# Seleção de acordo com critérios condicionais
# Boolean Indexing

# Seleção das linhas em que o valor da coluna Seminário seja acima de 8.0
print("Seleção por critérios condicionais\nSeleção das linhas em que o valor da coluna Seminário seja acima de 8.0\n",
      df[df["Seminário"] > 8.0], "\n")

# Condições de múltiplas colunas (deve-se usar operadores bitwise)

# Seleção das linhas em que o valor da coluna Seminário seja acima de 8.0
# e o valor da coluna Prova não seja menor que 3
print("Seleção por critérios condicionais de múltiplas colunas\nSeleção das linhas em que o valor da coluna Seminário seja acima de 8.0 e o valor da coluna Prova não seja menor que 3\n",
      df[(df["Seminário"] > 8.0) & (df["Prova"] > 3)], "\n")
