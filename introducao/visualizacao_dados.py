import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df = pd.read_csv("introducao\dados.csv")

histograma1 = df["preco"].plot.hist()
plt.savefig("introducao\histograma_1.pdf")
plt.close()

histograma2 = df["preco"].plot.hist(bins=30, edgecolor="black")
plt.savefig("introducao\histograma_2.pdf")
plt.close()

# Gráfico de barras verticais
contagem1 = df["bairro"].value_counts().plot.bar()
plt.savefig("introducao\contagem_1.pdf")
plt.close()

# Gráfico de barras horizontais
contagem2 = df["bairro"].value_counts().plot.barh()
plt.savefig("introducao\contagem_2.pdf")
plt.close()
