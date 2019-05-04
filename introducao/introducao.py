import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Series
notas = pd.Series([2, 7, 5, 10, 6])
print(notas.values)
print(notas.index)

notas = pd.Series([2, 7, 5, 10, 6], index=["Wilfred",
                                           "Abbie", "Harry", "Julia", "Carrie"])
print(notas)
print(notas["Julia"])

print("Média: ", notas.mean())
print("Desvio padrão: ", notas.std())

print(notas.describe())
